from Dart_fss_custom.corp import CorpList
from Dart_fss_custom.compguidedata import GetData
from Dart_fss_custom.sqlite import SqlDB

class SaveData(object):
    def __init__(self):
        self.corp = CorpList()
        self.compdata = GetData()
        self.sqlite = SqlDB()
        self.corp_list = []

    def get_corp_list(self):
        self.corp_list = self.corp.get_stock_code_list_web()

    def save_all_start(self):
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

    def update_all_needed(self):
        print("to be made")



if __name__ == '__main__':
    a = SaveData()
    a.save_all_start()
