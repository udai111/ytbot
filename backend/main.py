import schedule
import time
import random
import os

from celery_app import upload_task
from db import SessionLocal
from models import YouTubeAccount

def schedule_uploads():
    db = SessionLocal()
    accounts = db.query(YouTubeAccount).filter_by(is_active=True).all()
    db.close()

    videos = [v for v in os.listdir("videos") if v.endswith(".mp4")]
    random.shuffle(videos)

    # Dispatch tasks to Celery
    for account in accounts:
        if not videos:
            break
        video = videos.pop()
        video_path = os.path.join("videos", video)
        upload_task.delay(account.id, video_path, "Auto Title", "Auto Description")

# Example: run every 2 hours
schedule.every(2).hours.do(schedule_uploads)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(30)
