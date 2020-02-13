import requests
from bs4 import BeautifulSoup as bs

# request for data
def request_get(url: str, params: dict = None, timeout: int = 120, stream: bool = False):
    return requests.get(url=url, params=params, timeout=timeout, stream=stream)


class CorpList(object):
    def __init__(self):
        self.__corp_bs = []
        self._load()

    def download_corp_list(self):
        # not in use currently
        api_key = "f93aa72ed8104217931e191505590ee5b2c9b91e"
        corp_url = "https://opendart.fss.or.kr/api/corpCode.xml"
        url = '{}?crtfc_key={}'.format(corp_url, api_key)
        print(url)
        resp = request_get(url=url, timeout=120)
        return resp

    def _load(self):
        # load beautifulsoup from the xml file
        # open the xml file with utf8 encoding
        infile = open("corpCode.xml", "r", encoding="utf8")
        # read the file
        contents = infile.read()
        # parse it with bs
        self.__corp_bs = bs(contents, "xml")

    def corp_bs(self):
        if len(self.__corp_bs) == 0:
            self._load()
        return self.__corp_bs

    def find_by_name(self, query: str):
        found_bs = self.__corp_bs.find("corp_name", text = query)
        if found_bs == None:
            return False
        else:
            return_bs = found_bs.parent
        return return_bs

    def find_by_stock_code(self, stock_code: str):
        found_bs = self.__corp_bs.find("stock_code", text=query)
        if found_bs == None:
            return False
        else:
            return_bs = found_bs.parent
        return return_bs

