import requests

# https://opendart.fss.or.kr/api/"type".json

# 공시정보 = list
# 기업개황 = company
# 공시 서류 원본 = document
# 고유번호 = corpCode


class LoadApi(object):
    def __init__(self):
        self.auth_key="f93aa72ed8104217931e191505590ee5b2c9b91e" #authority key

    def get_url(self):
        # search type
        print("what tye:")
        type_s = input()

        # company code
        corp_code = False
        print("company code:")
        corp_code = input()
        if corp_code:
            # temporary code for testing
            corp_code = "00293886"

        # company name

        # start date
        bgn_de = False
        print("begin date:")
        bgn_de = input()

        # end date
        end_de = False
        print("end date:")
        end_de = input()

        # bsns_year
        bsns_year = False
        print("사업연도")
        bsns_year = input()

        # pblntf_ty 상세유형
        pblntf_ty = False
        print("상세유형")
        pblntf_ty = input()

        #rcept_no
        rcept_no = False
        print("rcept_no:")
        rcept_no = input()

        # reprt_code
        reprt_code = False
        print("1:1분기\n2:반기\n3:3분기\n4:사업")
        result = input()
        if result == "1":
            reprt_code = "11013"
        elif result == "2":
            reprt_code = "11012"
        elif result == "3":
            reprt_code = "11014"
        elif result == "4":
            reprt_code = "11011"



        # make url
        url = "https://opendart.fss.or.kr/api/"+type_s+".xml?crtfc_key=" + self.auth_key
        if corp_code:
            url += "&corp_code=" + corp_code
        if bgn_de:
            url += "&bgn_de=" + bgn_de
        if end_de:
            url += "&end_de=" + end_de
        if bsns_year:
            url += "&bsns_year=" + bsns_year
        if pblntf_ty:
            url += "&pblntf_ty=" + pblntf_ty
        if rcept_no:
            url += "&rcept_no=" + rcept_no
        if reprt_code:
            url += "&reprt_code=" + reprt_code
        print(url)
        return url

    def response_url(self):
        url = self.get_url()
        response = requests.get(url)
        print(response.json())

