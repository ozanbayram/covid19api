from flask import Flask, jsonify, request
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


@app.route('/countries/all', methods=['GET'])
def all_countries():
    return jsonify(utils.read_json("country_data"))


@app.route('/countries', methods=['GET'])
def one_country():
    countries_data = utils.read_json("country_data")
    query_parameters = request.args
    id = query_parameters.get('id')
    continent = query_parameters.get('continent')
    name = query_parameters.get('name')
    if id:
        country = [country for country in countries_data[1:] if country["Id"] == str(id)]
        return jsonify(country)
    if continent:
        country = [country for country in countries_data[1:] if country["InContinent"] == continent]
        return jsonify(country)
    if name:
        country = [country for country in countries_data[1:] if country["Country"] == name]
        return jsonify(country)


@app.route('/continents', methods=['GET'])
def all_regions():
    regions_data = utils.read_json("region_data")
    return jsonify(regions_data)


@app.route('/continent/<int:continent_id>', methods=['GET'])
def one_region(region_id):
    regions_data = utils.read_json("region_data")
    region = [region for region in regions_data[1:] if region["Id"] == region_id]
    return jsonify(region)


# @app.route('/all', methods=['GET'])
# def all_data():
#     total_data = utils.read_json("total_data")
#     countries_data = utils.read_json("countries_data")
#     regions_data = utils.read_json("regions_data")
#     return jsonify(regions_data, total_data, countries_data)


if __name__ == '__main__':
    app.run(debug=True)
