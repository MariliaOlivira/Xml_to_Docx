import xml.etree.ElementTree as xml
from Product import Product
from Enterprise import Enterprise
import pandas as pd

PATH = "/home/francisco/Desktop/planilhas_escolas/xml_pdf_nfe/teste.xml"
NAMESPACE = {'':'http://www.portalfiscal.inf.br/nfe'}

arq = xml.parse(PATH)
root = arq.getroot()

prodList = root.findall('NFe/infNFe/det', NAMESPACE)
emit = root.find('NFe/infNFe/emit', NAMESPACE)
dest = root.find('NFe/infNFe/dest', NAMESPACE)

df = pd.DataFrame
lis = list()

for product in prodList:
  p = Product(product, NAMESPACE).getProduct()
  lis.append(p)

print(df(lis).set_index('name'), end='\n\n')

info = Enterprise(emit, NAMESPACE).getEnterpriseInfo()
info2 = Enterprise(dest, NAMESPACE).getEnterpriseInfo()

print(df([info]).set_index('name'), end='\n\n')
print(df([info2]).set_index('name'))
