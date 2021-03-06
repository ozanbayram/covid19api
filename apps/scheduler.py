from apscheduler.schedulers.background import BackgroundScheduler
from apps.parser import Parser
from apps import utils


def update_data():
    parser = Parser()
    utils.create_json(parser.continents_data, "continents_data")
    utils.create_json(parser.total_data, "total_data")
    utils.create_json(parser.countries_data, "countries_data")


update_data()
sched = BackgroundScheduler(daemon=True)
sched.add_job(update_data, 'interval', seconds=3600)
sched.start()