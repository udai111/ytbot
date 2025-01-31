from celery import Celery
import os
from db import SessionLocal
from models import YouTubeAccount
from youtube_uploader import setup_browser, login_youtube, upload_video
from utils import enable_tor_proxy

app = Celery(
    'youtube_bot',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

app.conf.update(
    result_expires=3600,
    worker_concurrency=int(os.getenv("CELERY_CONCURRENCY", 4)),
    task_serializer='json',
    accept_content=['json']
)

@app.task
def upload_task(account_id, video_path, title="Random Title", description="Random Desc"):
    db = SessionLocal()
    account = db.query(YouTubeAccount).filter_by(id=account_id).first()
    db.close()

    if not account or not account.is_active:
        return f"Account {account_id} not active or does not exist."

    # Enable Tor for each upload
    enable_tor_proxy()
    driver = setup_browser(headless=True)
    try:
        login_youtube(driver, account.email, account.password)
        upload_video(driver, video_path, title, description)
        driver.quit()
        return f"Uploaded {video_path} with {account.email}"
    except Exception as e:
        driver.quit()
        return f"Failed to upload: {e}"
