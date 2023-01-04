from Product import Product
from Enterprise import Enterprise

import pandas as pd
import xml.etree.ElementTree as xml

from Constants import *

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

print(df(lis).set_index('name'), end='\n\n')

info  = Enterprise(emit, NAMESPACE).getEnterpriseInfo()
info2 = Enterprise(dest, NAMESPACE).getEnterpriseInfo()

print(df([info]).set_index('name'), end='\n\n')
print(df([info2]).set_index('name'))
