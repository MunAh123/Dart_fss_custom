import requests
from bs4 import BeautifulSoup as bs

# request for data
def request_get(url: str, params: dict = None, timeout: int = 120, stream: bool = False):
    return requests.get(url=url, params=params, timeout=timeout, stream=stream)


class CorpList(object):
    def __init__(self):
        self.__corp_bs = []
        self._load()
        self.api_key = "f93aa72ed8104217931e191505590ee5b2c9b91e"


    def download_corp_list(self):
        # not in use currently
        corp_url = "https://opendart.fss.or.kr/api/corpCode.xml"
        url = '{}?crtfc_key={}'.format(corp_url, self.api_key)
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
        found_bs = self.__corp_bs.find("stock_code", text= stock_code)
        if found_bs == None:
            return False
        else:
            return_bs = found_bs.parent
        return return_bs

    def get_stock_code_list_api(self):
        list_final = []
        codes = self.__corp_bs.find_all("stock_code")
        for code in codes:
            if code.get_text() != " ":
                code_text = code.get_text()
                list_final.append(code_text)
        # print(list_final)
        # print(len(list_final))
        return list_final

    def get_stock_code_list_web(self):
        url = '{}?method=download&searchType=13'.format('http://kind.krx.co.kr/corpgeneral/corpList.do')
        list_final = []
        url = '{}&marketType={}'.format(url, "allMkt")
        resp = request_get(url=url, timeout=120)
        soup = bs(resp.text, 'html.parser')
        rows = soup.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 0:
                crp_nm = cols[0].text.strip()
                crp_cd = cols[1].text.strip()
                crp_ctp = cols[2].text.strip()
                crp_prod = cols[3].text.strip()
                crp_info = {'crp_cd': crp_cd, 'crp_nm': crp_nm, 'crp_ctp': crp_ctp, 'crp_prod': crp_prod}
                list_final.append(crp_cd)
        # print(list_final)
        # print(len(list_final))
        return list_final



if __name__ == '__main__':
    #from api
    a = CorpList()
    a._load()
    # b = a.find_by_stock_code(309900).find("corp_code").get_text()
    # print(b)
    c = a.get_stock_code_list_web()
    print(c)
