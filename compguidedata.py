import requests
from bs4 import BeautifulSoup

class GetData(object):
    def __init__(self):
        self.urlbase1 = "https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A"
        self.urlbase2 = "&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN="
        self.sample_code = "005930"
        self.soup = ""

    def create_soup(self, code: str = False):
        temp_code = code
        if not temp_code:
            temp_code = self.sample_code
        url = self.urlbase1 + temp_code + self.urlbase2

        open_url = requests.get(url)
        soup = BeautifulSoup(open_url.text, 'html.parser')
        self.soup = soup
        return soup

    def create_data_top1(self):
        tbody = self.soup('div', {'class': "corp_group2"})[0].find_all('dl')
        clean_table = []
        counter = 0
        for row in tbody:
            cols = row.findChildren(recursive=False)
            cols = [ele.text.strip() for ele in cols]

            # print(cols)
            if counter == 0:
                clean_table.append(["per", cols[1]])
            elif counter == 2:
                clean_table.append(["12Mper", cols[1]])
            elif counter == 4:
                clean_table.append(["업종per", cols[1]])
            elif counter == 6:
                clean_table.append(["pbr", cols[1]])
            elif counter == 8:
                clean_table.append(["배당수익률", cols[1]])

            counter += 1
        return clean_table

    def create_data_t1(self):
        tbody = self.soup('table', {'class': "us_table_ty1 table-hb thbg_g h_fix zigbg_no"})[0].find_all('tr')
        counter = 0
        clean_table = []
        for row in tbody:
            cols = row.findChildren(recursive=False)
            cols = [ele.text.strip() for ele in cols]

            # print(cols)
            if counter == 0 or counter == 1 or counter == 2:
                clean_table.append([cols[0], cols[1]])
                clean_table.append([cols[2], cols[3]])
            elif counter == 3:
                clean_table.append(["시가총액상장예정", cols[1]])
                clean_table.append([cols[2], cols[3]])
            elif counter == 4:
                clean_table.append(["시가총액보통주", cols[1]])
                clean_table.append([cols[2], cols[3]])
            elif counter == 6:
                clean_table.append(["발행주식수보통주/우선주", cols[1]])
                clean_table.append(["유동주식수보통주", cols[3]])
            counter += 1
        return clean_table


if __name__ == '__main__':
    test = GetData()
    test.create_soup("009150")
    b = test.create_data_t1()
    print(b)
    a = test.create_data_top1()
    print(a)