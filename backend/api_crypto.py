import os
import requests


class API_cryptocurrency:
    def __init__(self, api_key: str) -> None:
        self.url = "https://pro-api.coinmarketcap.com"
        self.headers = {
            "X-CMC_PRO_API_KEY": api_key 
        }

    def api_get_top_cryptocurrencies(self, limit = 100) -> list:
        "вернет список криптовалют"
        route = "/v1/cryptocurrency/map"
        data = {
            "limit": limit,
            "sort": "cmc_rank"
        }
        res = requests.get(self.url + route, headers=self.headers, params=data)
        self.list_top_cryptocurrency = res.json()["data"]

        return self.list_top_cryptocurrency 
    
    def api_get_info_cryptocurrency(self, id) -> dict:
        "вернет инфо по 1 криптовалюте"
        id = str(id)
        route = "/v2/cryptocurrency/quotes/latest"
        res = requests.get(self.url + route, headers=self.headers, params={"id":id})
        print(res.text)
        return res.json()["data"][id]
        

if __name__ == "__main__":
    print(os.environ.get("API_key"))
    api = API_cryptocurrency(os.environ.get("API_key"))
    print(api.api_get_info_cryptocurrency(1))