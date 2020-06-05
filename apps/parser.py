import requests
from bs4 import BeautifulSoup
from apps import utils


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}


class Parser:

    r = requests.get('https://www.worldometers.info/coronavirus/',headers=headers)
    soup = BeautifulSoup(r.content, "html.parser", from_encoding='utf-8')

    def __init__(self):
        self.countries_data = []
        self.continents_data = []
        self.total_data = []
        self.main()

    def get_country(self):
        keys = [
            "Id", "Country", "TotalCase", "NewCase", "TotalDeath", "NewDeath",
            "TotalRecovered", "ActiveCase", "SeriousCase", "TotalCasePer1M",
            "TotalDeathPer1M", "TotalTests", "TestPer1M", "Population", "InContinent",
                ]
        tr_list = self.soup.find("tbody").find_all("tr", {"style": ""})
        for tr in tr_list:
            values = []
            try:
                if tr["class"] == ['total_row_world']:
                    continue
            except KeyError:
                pass

            for idx, value in enumerate(tr.find_all("td")):
                if idx == 7:  # fixed wrong pair in dict
                    continue
                value = value.text.strip(" +").strip()
                if value == "":
                    value = "0"
                values.append(value)
            country = dict(zip(keys, values))
            self.countries_data.append(country)

    def get_continent(self):
        continent_tr = self.soup.find_all("tbody")[1].find_all("tr")
        for index, tr in enumerate(continent_tr[:-1]):
            idx = index
            continent = tr.find_all('td')[-4].text.strip(" +").strip()
            total_case = tr.find_all('td')[2].text.strip(" +").strip()
            new_case = tr.find_all('td')[3].text.strip(" +").strip()
            if not new_case: new_case = "0"
            total_death = tr.find_all('td')[4].text.strip(" +").strip()
            new_death =tr.find_all('td')[5].text.strip(" +").strip()
            if not new_death: new_death = "0"
            total_recovered =tr.find_all('td')[6].text.strip(" +").strip()
            active_case = tr.find_all('td')[8].text.strip(" +").strip()
            if not active_case: active_case = "0"
            serious_case = tr.find_all('td')[7].text.strip(" +").strip()
            if not active_case: active_case = "0"
            self.continents_data.append({
                "Continent": continent,
                "TotalCase": total_case,
                "NewCase": new_case,
                "TotalDeath": total_death,
                "NewDeath": new_death,
                "TotalRecovered": total_recovered,
                "ActiveCase": active_case,
                "SeriousCase": serious_case,
                "Id": idx
            })

    def get_total(self):
        tr = self.soup.find_all("tbody")[2].find("tr").find_all("td")
        region = "World"
        total_case = tr[1].text.strip(" +").strip()
        new_case = tr[2].text.strip(" +").strip()
        if not new_case:new_case = "0"
        total_death = tr[3].text.strip(" +").strip()
        new_death =tr[4].text.strip(" +").strip()
        if not new_death: new_death = "0"
        total_recovered = tr[5].text.strip(" +").strip()
        active_case = tr[6].text.strip(" +").strip()
        if not active_case: active_case = "0"
        serious_case = tr[9].text.strip(" +").strip()
        if not active_case: active_case = "0"
        self.total_data.append(
            {
                "Region": region,
                "TotalCase": total_case,
                "NewCase": new_case,
                "TotalDeath": total_death,
                "NewDeath": new_death,
                "TotalRecovered": total_recovered,
                "ActiveCase": active_case,
                "SeriousCase": serious_case
            }
        )

    def main(self):
        self.countries_data.append({"LastUpdate": utils.current_time()})
        self.continents_data.append({"LastUpdate": utils.current_time()})
        self.total_data.append({"LastUpdate": utils.current_time()})
        self.get_total()
        self.get_country()
        self.get_continent()