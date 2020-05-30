from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from Parser import Parser
import utils

def update_data():
    parser = Parser()
    utils.create_json(parser.region_data, "region_data")
    utils.create_json(parser.total_data, "total_data")
    utils.create_json(parser.country_data, "country_data")

update_data()
sched = BackgroundScheduler(daemon=True)
sched.add_job(update_data,'interval', seconds=3600)
sched.start()