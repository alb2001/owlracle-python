import requests


class OwlracleAPI:
    def __init__(self, api_key=None, version="v4", network="eth", useragent="API-Wrapper/0.1"):
        self.url = f"https://api.owlracle.info/{version}"
        self._api_key = api_key
        self.network = network
        self._useragent = useragent

    def get_gas_fee_estimation(self, blocks=None, percentile=None, accept=None, feeinusd=None, eip1559=None, reportwei=None, calcfrom=None):
        endpoint = f"/{self.network}/gas"
        response = requests.get(self.url + endpoint, params={"apikey": self._api_key,
                                                             "blocks": blocks,
                                                             "percentile": percentile,
                                                             "accept": accept,
                                                             "feeinusd": feeinusd,
                                                             "eip1559": eip1559,
                                                             "reportwei": reportwei,
                                                             "calcfrom": calcfrom})
        
        return response.json()
    
    def get_gas_history(self, from_=None, to=None, candles=None, page=None, timeframe=None, tokenprice=None, txfee=None):
        endpoint = f"/{self.network}/history"
        response = requests.get(self.url + endpoint, params={"apikey": self._api_key,
                                                             "from": from_,
                                                             "to": to,
                                                             "candles": candles,
                                                             "page": page,
                                                             "timeframe": timeframe,
                                                             "tokenprice": tokenprice,
                                                             "txfee": txfee})
        
        return response.json()
    
    def get_api_key_information(self, api_key=None):
        if api_key == None:
            api_key = self._api_key

        endpoint = f"/keys/{api_key}"
        response = requests.get(self.url + endpoint)
        return response.json()
    
    def get_api_key_credit_recharge_history(self, api_key=None):
        if api_key == None:
            api_key = self._api_key

        endpoint = f"/credit/{api_key}"
        response = requests.get(self.url + endpoint)
        return response.json()
    
    def get_api_key_usage_log(self, api_key=None, fromtime=None, totime=None, limit=None):
        if api_key == None:
            api_key = self._api_key
        
        endpoint = f"/logs/{api_key}"
        response = requests.get(self.url + endpoint, params={"fromtime": fromtime,
                                                             "totime": totime,
                                                             "limit": limit})
        
        return response.json()
    
    def get_rpc_endpoint(self):
        url = self.url
        url = url.rsplit("/", 1)[0]
        endpoint = "/rpc"
        response = requests.get(url + endpoint)
        return response.json()