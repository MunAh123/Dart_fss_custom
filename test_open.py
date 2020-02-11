# import pandas as pd
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import webbrowser
#
# #STEP 2
# auth_key="f93aa72ed8104217931e191505590ee5b2c9b91e" #authority key
# company_code="024110" #company code
# start_date="1990101"
#
# #STEP 3
# corp_url = "https://opendart.fss.or.kr/api/corpCode.xml"
# url = '{}?crtfc_key={}'.format(corp_url, auth_key)
# print(url)
#
# #STEP 4
# resultXML=urlopen(url)  #this is for response of XML
# print(resultXML)
# result=resultXML.read() #Using read method
# print(result)
#
# #STEP 5
# xmlsoup=BeautifulSoup(result,'html.parser')

import xml.dom.minidom
doc = xml.dom.minidom.parse("corpCode.xml")
print(doc.nodeName)

