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
    return jsonify(utils.read_json("countries_data"))


@app.route('/countries', methods=['GET'])
def one_country():
    countries_data = utils.read_json("countries_data")
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


@app.route('/continents/all', methods=['GET'])
def all_continents():
    continents_data = utils.read_json("continents_data")
    return jsonify(continents_data)


@app.route('/continents', methods=['GET'])
def one_continent():
    continents_data = utils.read_json("continents_data")
    query_parameters = request.args
    name = query_parameters.get('name')
    id = query_parameters.get('id')
    if name:
        continent = [continent for continent in continents_data[1:] if continent["Continent"] == name]
        return jsonify(continent)
    if id:
        continent = [continent for continent in continents_data[1:] if continent["Id"] == int(id)]
        return jsonify(continent)

if __name__ == '__main__':
    app.run(debug=True)















# @app.route('/all', methods=['GET'])
# def all_data():
#     total_data = utils.read_json("total_data")
#     countries_data = utils.read_json("countries_data")
#     regions_data = utils.read_json("regions_data")
#     return jsonify(regions_data, total_data, countries_data)