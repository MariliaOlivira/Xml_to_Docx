from Constants import *
from info.Enterprise.School import School
from info.Product import Product
from info.Enterprise.Concurrent import Concurrent


import pandas as pd
import xml.etree.ElementTree as xml

arq = xml.parse(PATH)
root = arq.getroot()

emit = root.find('NFe/infNFe/emit', NAMESPACE)
dest = root.find('NFe/infNFe/dest', NAMESPACE)
prodList = root.findall('NFe/infNFe/det', NAMESPACE)

df = pd.DataFrame
lis = list()

for product in prodList:
  p = Product(product, NAMESPACE).getProduct()
  lis.append(p)

info  = Concurrent(emit, NAMESPACE).getEnterpriseInfo()
info2 = School(dest, NAMESPACE).getEnterpriseInfo()

print(df([info]).set_index('name'), end='\n\n')
print(df([info2]).set_index('name'))
