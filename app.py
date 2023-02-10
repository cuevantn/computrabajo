from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, time
import csv

from main import update_data
from constants import DATA_PATH

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data")
async def get_data():
    with open("data.csv", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

scheduler = BackgroundScheduler()
scheduler.add_job(update_data, 'interval', days=1, start_date=datetime.combine(datetime.today(), time(hour=5, minute=0)))
scheduler.start()