from Dart_fss_custom.corp import CorpList
from Dart_fss_custom.compguidedata import GetData
from Dart_fss_custom.sqlite import SqlDB
from bs4 import BeautifulSoup as bs
import urllib
import re

class SaveData(object):
    def __init__(self):
        self.corp = CorpList()
        self.compdata = GetData()
        self.sqlite = SqlDB()
        self.corp_list = []

    def get_corp_list(self):
        self.corp_list = self.corp.get_stock_code_list_web()

    def save_web(self):
        """
        save everything from scratch for all company in kor. the assumption is that there will not already exist a data
        :return:
        """
        if len(self.corp_list) == 0:
            self.get_corp_list()
        self.sqlite.table_main()
        for code in self.corp_list:
            self.compdata.create_soup(code)
            temp_compdetail = self.compdata.create_data_top1()
            temp_row_data = (code, "a", temp_compdetail[0][1], temp_compdetail[1][1], temp_compdetail[2][1], temp_compdetail[3][1], temp_compdetail[4][1])
            print(temp_row_data)
            self.sqlite.insert_row(temp_row_data)

    def open_api(self, corp_code: str = "00356370", bsns_year: str = "2018", reprt_code: str = "11011", fs_div: str = "OFS"):
        """
        create a bs soup with the wanted company
        :param corp_code: corp code to identify
        :param bsns_year: what year
        :param reprt_code: which report
        :param fs_div: what type of report
        :return: soup for the xml
        """
        base_url = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.xml?crtfc_key={}&corp_code={}&bsns_year={}&reprt_code={}&fs_div={}".format(
            self.corp.api_key,  corp_code, bsns_year, reprt_code, fs_div
        )
        resp = urllib.request.urlopen(base_url)
        # data = resp.read()
        # text = data.decode("utf-8")
        soup = bs(resp, "xml")
        return soup

    def save_api(self):
        """
        save the api into sqlite
        :return:
        """
        # the list of company with stock code
        if len(self.corp_list) == 0:
            print("loading")
            self.get_corp_list()
        print("done")
        self.corp._load()
        #create the table format
        self.sqlite.table_main()

        print(len(self.corp_list))
        counter = 0
        for stock_code in self.corp_list:
            print(counter)
            counter+= 1
            print(stock_code)
            corp_code = self.corp.find_by_stock_code(stock_code).find("corp_code").get_text()
            print(corp_code)

            # get the soup using the api
            soup = self.open_api(corp_code= corp_code, fs_div= "OFS")
            # check if the api was recieved properly
            if soup.find("status").get_text() != "000":
                print("error" + soup.find("message").get_text())
                # break to break out of the current loop, continue to go to next iteration, pass will pass on and do
                # nothing mainly used to keep if empty
                continue
            # soup to get the 기 and re to extract the integer from it
            corp_age = re.search('\d+', soup.find("thstrm_nm").get_text()).group()

            for list_soup in soup.select("list"):
                temp_row_data = self.create_row_api(list_soup, stock_code, "OFS", corp_age)
                print(temp_row_data)
                self.sqlite.insert_row(temp_row_data)

    def create_row_api(self,list_soup, stock_code, fs_div, corp_age):
        """
        create a appropriate row data taking the remainging years on the report.
        :param stock_code: stock code to go in the row
        :param fs_div: type of report to go in the row
        :param corp_age: age of the corp
        :return: row data
        """
        # when there is 2 left get rid of the prev year 2
        if corp_age == "2":
            temp_row_data = (
                stock_code,
                fs_div,
                list_soup.find("rcept_no").get_text(),
                list_soup.find("reprt_code").get_text(),
                list_soup.find("bsns_year").get_text(),
                list_soup.find("corp_code").get_text(),
                list_soup.find("sj_div").get_text(),
                list_soup.find("sj_nm").get_text(),
                list_soup.find("account_id").get_text(),
                list_soup.find("account_nm").get_text(),
                list_soup.find("account_detail").get_text(),
                list_soup.find("thstrm_nm").get_text(),
                list_soup.find("thstrm_amount").get_text(),
                list_soup.find("frmtrm_nm").get_text(),
                list_soup.find("frmtrm_amount").get_text(),
                "-",
                "-",
                list_soup.find("ord").get_text()
            )
        # get rid of the prev year 1 and 2
        elif corp_age == "1":
            temp_row_data = (
                stock_code,
                fs_div,
                list_soup.find("rcept_no").get_text(),
                list_soup.find("reprt_code").get_text(),
                list_soup.find("bsns_year").get_text(),
                list_soup.find("corp_code").get_text(),
                list_soup.find("sj_div").get_text(),
                list_soup.find("sj_nm").get_text(),
                list_soup.find("account_id").get_text(),
                list_soup.find("account_nm").get_text(),
                list_soup.find("account_detail").get_text(),
                list_soup.find("thstrm_nm").get_text(),
                list_soup.find("thstrm_amount").get_text(),
                "-",
                "-",
                "_",
                "-",
                list_soup.find("ord").get_text()
            )
        # contain all data, no need to exclude
        else:
            temp_row_data = (
                stock_code,
                fs_div,
                list_soup.find("rcept_no").get_text(),
                list_soup.find("reprt_code").get_text(),
                list_soup.find("bsns_year").get_text(),
                list_soup.find("corp_code").get_text(),
                list_soup.find("sj_div").get_text(),
                list_soup.find("sj_nm").get_text(),
                list_soup.find("account_id").get_text(),
                list_soup.find("account_nm").get_text(),
                list_soup.find("account_detail").get_text(),
                list_soup.find("thstrm_nm").get_text(),
                list_soup.find("thstrm_amount").get_text(),
                list_soup.find("frmtrm_nm").get_text(),
                list_soup.find("frmtrm_amount").get_text(),
                list_soup.find("bfefrmtrm_nm").get_text(),
                list_soup.find("bfefrmtrm_amount").get_text(),
                list_soup.find("ord").get_text()
            )

        return temp_row_data


    def update_all_needed(self):
        print("to be made")


if __name__ == '__main__':
    a = SaveData()
    a.save_api()
    print("done")
