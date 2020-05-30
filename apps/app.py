from flask import Flask, jsonify
from apps import utils
from apps import scheduler

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    total_data = utils.read_json("total_data")
    return total_data[0]["LastUpdate"]


@app.route('/total', methods=['GET'])
def total():
    return jsonify(utils.read_json("total_data"))


@app.route('/country', methods=['GET'])
def all_countries():
    return jsonify(utils.read_json("country_data"))


@app.route('/country/<int:country_id>', methods=['GET'])
def one_country(country_id):
    countries_data = utils.read_json("country_data")
    country = [country for country in countries_data[1:] if country["Id"] == str(country_id)]
    return jsonify(country)


@app.route('/region', methods=['GET'])
def all_regions():
    regions_data = utils.read_json("region_data")
    return jsonify(regions_data)


@app.route('/region/<int:region_id>', methods=['GET'])
def one_region(region_id):

    regions_data = utils.read_json("regions_data")
    region = [region for region in regions_data[1:] if region["Id"] == region_id]
    return jsonify(region)


@app.route('/all', methods=['GET'])
def all_data():
    total_data = utils.read_json("total_data")
    countries_data = utils.read_json("countries_data")
    regions_data = utils.read_json("regions_data")
    return jsonify(regions_data, total_data, countries_data)


if __name__ == '__main__':
    app.run(debug=True)
