from Constants import *
from Temp_constants import *

from info.Enterprise.School import School
from info.Product import Product
from info.Enterprise.Concurrent import Concurrent

import pandas as pd
import xml.etree.ElementTree as xml

import docx

fileName = "teste.docx"

# doc = docx.Document(f'{DIR}/recibo.docx')
doc = docx.Document(DICT_P_P['samel'])


# arq = xml.parse(PATH)
# root = arq.getroot()

# emit = root.find(EMITENT_XPATH, NAMESPACE)
# dest = root.find(DESTINATION_XPATH, NAMESPACE)
# prodList = root.findall(PRODUCT_LIST_XPATH, NAMESPACE)

# df = pd.DataFrame
# lis = list()

# for product in prodList:
#   p = Product(product, NAMESPACE).getProduct()
#   lis.append(p)

# info  = Concurrent(emit, NAMESPACE).getEnterpriseInfo()
# info2 = School(dest, NAMESPACE).getEnterpriseInfo()

# print(df([info]).set_index('name'), end='\n\n')
# print(df([info2]).set_index('name'))
