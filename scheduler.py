from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from Parser import Parser
import utils

# count = 0
# def sensor():
#     global count
#     sched.print_jobs()
#     print('Count: ' , count)
#     count += 1

def update_data():
    parser = Parser()
    utils.create_json(parser.region_data, "region_data")
    utils.create_json(parser.total_data, "total_data")
    utils.create_json(parser.country_data, "country_data")
    # 60utils.create_json({"time":utils.current_time()},"time")


update_data()
sched = BackgroundScheduler(daemon=True)
sched.add_job(update_data,'interval', seconds=3600)
sched.start()