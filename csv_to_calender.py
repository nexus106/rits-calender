import os
from dotenv import load_dotenv
import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

# Google Calendar API認証情報のパス
credentials_path = "credentials_service.json"

# Google Calendar APIのバージョンとカレンダーID
calendar_id = os.environ["calender_id"]
service = build(
    "calendar",
    "v3",
    credentials=service_account.Credentials.from_service_account_file(credentials_path),
)

# CSVファイルのパス
csv_path = "gakubu-copy.csv"

with open(csv_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = f'{row["年"]}-{row["月"].zfill(2)}-{row["日"].zfill(2)}'
        event_summary = row["行事"]
        event_description = "学年暦"

        event = {
            "summary": event_summary,
            "description": event_description,
            # 終日の予定なので時間指定はしない
            "start": {
                "date": date,
                "timeZone": "Asia/Tokyo",
            },
            "end": {
                "date": date,
                "timeZone": "Asia/Tokyo",
            },
            # 終日
            "transparency": "transparent",
        }

        service.events().insert(calendarId=calendar_id, body=event).execute()
