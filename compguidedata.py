import requests
from bs4 import BeautifulSoup

class GetData(object):
    def __init__(self):
        self.urlbase1 = "https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A"
        self.urlbase2 = "&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN="
        self.sample_code = "005930"

    def create_data(self, code: str = False):
        temp_code = code
        if not temp_code:
            temp_code = self.sample_code
        url = self.urlbase1 + temp_code + self.urlbase2

        open_url = requests.get(url)
        soup = BeautifulSoup(open_url.text, 'html.parser')

        tbody = soup('table', {'class': "us_table_ty1 table-hb thbg_g h_fix zigbg_no"})[0].find_all('tr')
        for row in tbody:
            cols = row.findChildren(recursive=False)
            print(cols)
            cols = [ele.text.strip() for ele in cols]

            print(cols)


if __name__ == '__main__':
    test = GetData()
    test.create_data()
