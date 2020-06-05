from flask import Flask, jsonify, request, make_response, render_template, url_for
from apps import utils
from apps import scheduler
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)


limiter = Limiter(
    app,
    key_func=get_remote_address,
    application_limits=["100 per hour"]
)


@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
            jsonify(error=f"Rate limit exceeded {e.description}")
            , 429
    )


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")



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

