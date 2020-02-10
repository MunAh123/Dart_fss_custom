import requests
from bs4 import BeautifulSoup

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

def get_corp_list():
    corp_list = []
    corp_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
    url = '{}?method=download&searchType=13'.format(corp_url)
    resp = request_get(url=url, timeout=120)
    soup = BeautifulSoup(resp.text, 'html.parser')
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
# get_corp_list()

_SEARCH_URL_ = "https://opendart.fss.or.kr/api/"
api_key = "f93aa72ed8104217931e191505590ee5b2c9b91e"

url = _SEARCH_URL_ + "company.json"
print(url)
params = dict(
    crtfc_key=api_key,
    corp_code = "00828497"
)
resp = request_get(url=url, params=params)
print(resp)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)