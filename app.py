from flask import Flask, jsonify
import json
import scheduler


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    with open("data/total_data.json", "r") as js:
        total_data = json.load(js)
        return total_data[0]["LastUpdate"]

    # with open("data/time.json", "r") as js:
    #     time = json.load(js)
    #     return time["time"]

@app.route('/total', methods=['GET'])
def total():
    with open("data/total_data.json", "r") as js:
        total_data = json.load(js)
    return jsonify(total_data)


@app.route('/country', methods=['GET'])
def all_countries():
    with open("data/country_data.json", "r") as js:
        countries_data = json.load(js)
    return jsonify(countries_data)


@app.route('/country/<int:country_id>', methods=['GET'])
def one_country(country_id):
    with open("data/country_data.json", "r") as js:
        countries_data = json.load(js)
    country = [country for country in countries_data[1:] if country["Id"] == str(country_id)]
    return jsonify(country)


@app.route('/region', methods=['GET'])
def all_regions():
    with open("data/region_data.json", "r") as js:
        regions_data = json.load(js)
    return jsonify(regions_data)


@app.route('/region/<int:region_id>', methods=['GET'])
def one_region(region_id):
    with open("data/region_data.json", "r") as js:
        regions_data = json.load(js)
    region = [region for region in regions_data[1:] if region["Id"] == region_id]
    return jsonify(region)


@app.route('/all', methods=['GET'])
def all_data():
    with open("data/total_data.json", "r") as js:
        total_data = json.load(js)
    with open("data/country_data.json", "r") as js:
        countries_data = json.load(js)
    with open("data/region_data.json", "r") as js:
        regions_data = json.load(js)
    return jsonify(regions_data, total_data, countries_data)


if __name__ == '__main__':
    app.run(debug=True)








# parser = Parser()
# total_data = parser.total_data
# countries_data = parser.country_data
# regions_data = parser.region_data
