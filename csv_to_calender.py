import os
from dotenv import load_dotenv
import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

# Google Calendar API認証情報のパス
credentials_path = 'credentials_service.json'

# Google Calendar APIのバージョンとカレンダーID
calendar_id = os.environ['calender_id']
service = build('calendar', 'v3', credentials=service_account.Credentials.from_service_account_file(credentials_path))

# CSVファイルのパス
csv_path = 'gakubu-copy.csv'

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = f'2023-{row["月"].zfill(2)}-{row["日"].zfill(2)}'
        event_summary = row["行事"]
        event_description = "学年暦"
        # event_description = f'曜日: {row["曜"]}'

        event = {
            'summary': event_summary,
            'description': event_description,
            'start': {
                'dateTime': f'{date}T00:00:00',
                'timeZone': 'Asia/Tokyo',
            },
            'end': {
                'dateTime': f'{date}T23:59:59',
                'timeZone': 'Asia/Tokyo',
            },
        }

        service.events().insert(calendarId=calendar_id, body=event).execute()
