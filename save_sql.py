from .corp import CorpList
from .compguidedata import GetData
from .sqlite import SqlDB

class SaveData(object):
    def __init__(self):
        self.corp = CorpList()
        self.compdata = GetData()
        self.sqlite = SqlDB()

    def save_all(self):
        corp_list = self.corp.get_stock_code_list_web()
        counter = 0
        for code in corp_list:
            counter += 1
            print(code)
        print(counter)


if __name__ == '__main__':
    a = SaveData()
    a.save_all()
