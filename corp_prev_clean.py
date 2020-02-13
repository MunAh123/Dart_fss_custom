import requests
from bs4 import BeautifulSoup as bs

# request for data
def request_get(url: str, params: dict = None, timeout: int = 120, stream: bool = False):
    return requests.get(url=url, params=params, timeout=timeout, stream=stream)


class Corp(object):
    _SEARCH_URL_ = "https://opendart.fss.or.kr/api/"

    def __init__(self, corp_code: str, lazy_loading: bool = True, **kwargs):
        self.corp_code = corp_cd
        self.corp_name = kwargs.get("corp_nm")
        self.corp_ctp = kwargs.get('corp_ctp')
        self.corp_prod = kwargs.get('corp_prod')

        self._info = None
        if lazy_loading is False:
            self.load()

    def load(self):
        # import in original
        api_key = "f93aa72ed8104217931e191505590ee5b2c9b91e"

        url = self._SEARCH_URL_+"company.json"
        params = dict(
            crtfc_key = api_key,
            corp_code = self.corp_cd
        )
        resp = request_get(url=url, params=params)


class corp_list(object):
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
        infile = open("corpCode.xml", "r", encoding="utf8")
        contents = infile.read()
        self.__corp_bs = bs(contents, "xml")

    def corp_bs(self):
        if len(self.__corp_bs) == 0:
            self._load()
        return self.__corp_bs

    def find_by_name(self, query: str):
        found_bs = self.__corp_bs.find("corp_name", text = query)
        return_bs = found_bs.parent
        return return_bs

    def find_by_stock_code(self, stock_code: str):
        found_bs = self.__corp_bs.find("stock_code", text=query)
        return_bs = found_bs.parent
        return return_bs

def get_corp_list():
    corp_list = []
    api_key = "f93aa72ed8104217931e191505590ee5b2c9b91e"
    corp_url = "https://opendart.fss.or.kr/api/corpCode.xml"
    url = '{}?crtfc_key={}'.format(corp_url, api_key)
    print(url)
    resp = request_get(url=url, timeout=120)
    print(resp)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)
    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 0:
            corp_name = cols[0].text.strip()
            corp_code = cols[1].text.strip()
            corp_ctp = cols[2].text.strip()
            corp_prod = cols[3].text.strip()
            crp_info = {'crp_cd': corp_code, 'crp_nm': corp_name, 'crp_ctp': corp_ctp, 'crp_prod': corp_prod}
            print(crp_info)


####################################
# tests
get_corp_list()

# _SEARCH_URL_ = "https://opendart.fss.or.kr/api/"
# api_key = "f93aa72ed8104217931e191505590ee5b2c9b91e"
#
# url = _SEARCH_URL_ + "company.json"
# print(url)
# params = dict(
#     crtfc_key=api_key,
#     corp_code = "00828497"
# )
# resp = request_get(url=url, params=params)
# print(resp)
# soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

