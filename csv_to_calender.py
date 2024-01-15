import os
from dotenv import dotenv_values
import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# load_dotenv()
env_config = dotenv_values(".env")


# Google Calendar API認証情報のパス
credentials_path = "credentials_service.json"

# Google Calendar APIのバージョンとカレンダーID
# calendar_id = os.environ["calender_id"]
service = build(
    "calendar",
    "v3",
    credentials=service_account.Credentials.from_service_account_file(credentials_path),
)

# CSVファイルのパス
dir_path = "."
file_files = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
]
# 現在のディレクトリから全てのファイル名のリストを作成
csv_files = [f for f in file_files if ".csv" in f]
csv_files_replace = [f.replace(".csv", "") for f in csv_files]
# 全てのファイル名のリストから拡張子を除いたcsvファイル名のみのリストを作成
print(csv_files_replace)


# すべてのcsvファイルの予定をカレンダーに登録
for f in csv_files_replace:
    print(f)
    with open(f+".csv", newline="", encoding="utf-8") as csvfile:
        try:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date = f'{row["年"]}-{row["月"].zfill(2)}-{row["日"].zfill(2)}'
                event_summary = row["行事"]
                if f == "gakubu":
                    event_description = "学部_学年暦"
                if f == "daigakuin_bunkei":
                    event_description = "大学院文系_学年暦"
                if f == "daigakuin_rikei":
                    event_description = "大学院理系_学年暦"
                if f == "daigakuin_quarter":
                    event_description = "大学院クオーター制_学年暦"
                if f == "daigakuin_houmu":
                    event_description = "大学院法務研究科_学年暦"
                if f == "gakubu-copy":
                    event_description = "テスト"

                # APIにデータを渡すための整形

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
                calendar_id = env_config[f]
                service.events().insert(calendarId=calendar_id, body=event).execute()
        except Exception as e:
            print("file open error")
            print(e)
