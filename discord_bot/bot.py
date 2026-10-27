import os
from datetime import datetime, timedelta, timezone
from .schedule import run_for_today

DAY_MAP = {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4}


def main():
    jst = timezone(timedelta(hours=9))
    now = datetime.now(jst)

    cron = os.environ.get("SCHEDULE_CRON", "")
    day = cron.split()[-1] if cron else ""

    # 定期実行はcronの曜日、手動実行は現在の曜日
    weekday = DAY_MAP[day] if day in DAY_MAP else now.weekday()

    print(f"[INFO] JST now = {now.isoformat()}, cron='{cron}', weekday={weekday}")
    run_for_today(weekday)
    print("[INFO] Finished sending messages")


if __name__ == "__main__":
    main()
