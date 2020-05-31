import requests
from bs4 import BeautifulSoup
from apps import utils


class Parser:

    r = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(r.content, "html.parser", from_encoding='utf-8')

    def __init__(self):
        self.country_data = []
        self.region_data = []
        self.total_data = []
        self.main()

    def get_country(self):
        keys = [
            "Id", "Country", "TotalCase", "NewCase", "TotalDeath", "NewDeath",
            "TotalRecovered", "ActiveCase", "SeriousCase", "TotalCasePer1M",
            "TotalDeathPer1M", "TotalTests", "TestPer1M", "Population", "InContinent",
                ]
        tr_list = self.soup.find("tbody").find_all("tr", {"style": ""})
        #for index, tr in enumerate(tr_list):
        for tr in tr_list:
            values = []
            try:
                if tr["class"] == ['total_row_world']:
                    continue
            except KeyError:
                pass
                #values.append(index)

            for value in tr.find_all("td"):
                value = value.text.strip(" +").strip()
                if value == "":
                    value = "0"
                values.append(value)
            country = dict(zip(keys, values))
            self.country_data.append(country)

    def get_region(self):
        region_tr = self.soup.find_all("tbody")[1].find_all("tr")
        for index, tr in enumerate(region_tr[:-1]):
            Id = index
            Region = tr.find_all('td')[-1].text.strip(" +").strip()
            TotalCase = tr.find_all('td')[2].text.strip(" +").strip()
            NewCase = tr.find_all('td')[3].text.strip(" +").strip()
            if not NewCase: NewCase = "0"
            TotalDeath = tr.find_all('td')[4].text.strip(" +").strip()
            NewDeath =tr.find_all('td')[5].text.strip(" +").strip()
            if not NewDeath: NewDeath = "0"
            TotalRecovered =tr.find_all('td')[6].text.strip(" +").strip()
            ActiveCase = tr.find_all('td')[7].text.strip(" +").strip()
            if not ActiveCase: ActiveCase = "0"
            SeriousCase = tr.find_all('td')[8].text.strip(" +").strip()
            if not ActiveCase: ActiveCase = "0"
            self.region_data.append({
                "Region": Region,
                "TotalCase": TotalCase,
                "NewCase": NewCase,
                "TotalDeath": TotalDeath,
                "NewDeath": NewDeath,
                "TotalRecovered": TotalRecovered,
                "ActiveCase": ActiveCase,
                "SeriousCase": SeriousCase,
                "Id": Id
            })

    def get_total(self):
        tr = self.soup.find_all("tbody")[2].find("tr").find_all("td")
        Region = "World"
        TotalCase = tr[1].text.strip(" +").strip()
        NewCase = tr[2].text.strip(" +").strip()
        if not NewCase:NewCase = "0"
        TotalDeath = tr[3].text.strip(" +").strip()
        NewDeath =tr[4].text.strip(" +").strip()
        if not NewDeath: NewDeath = "0"
        TotalRecovered = tr[5].text.strip(" +").strip()
        ActiveCase = tr[6].text.strip(" +").strip()
        if not ActiveCase: ActiveCase = "0"
        SeriousCase = tr[7].text.strip(" +").strip()
        if not ActiveCase: ActiveCase = "0"
        self.total_data.append(
            {
                "Region": Region,
                "TotalCase": TotalCase,
                "NewCase": NewCase,
                "TotalDeath": TotalDeath,
                "NewDeath": NewDeath,
                "TotalRecovered": TotalRecovered,
                "ActiveCase": ActiveCase,
                "SeriousCase": SeriousCase
            }
        )

    def main(self):
        self.country_data.append({"LastUpdate": utils.current_time()})
        self.region_data.append({"LastUpdate": utils.current_time()})
        self.total_data.append({"LastUpdate": utils.current_time()})
        self.get_total()
        self.get_country()
        self.get_region()
