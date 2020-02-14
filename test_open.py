# from Dart_fss_custom.corp import CorpList
#
#
# corp_list = CorpList()
# test1 = corp_list.find_by_name("삼성전자")
# print(test1)
# test2 = corp_list.find_by_name("asa")
# print(test2)

# 20200213000090

# from Dart_fss_custom.index import LoadApi
#
# load_api = LoadApi()
# load_api.response_url()


from xbrl import XBRLParser, GAAP, GAAPSerializer
xbrl_parser = XBRLParser()
xbrl = xbrl_parser.parse("20190401004781_ifrs/00126380_2011-04-30.xbrl")

if __name__ == '__main__':
    print("a")
