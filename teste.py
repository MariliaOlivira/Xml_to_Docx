import xml.etree.ElementTree as xml
from Product import Product
import pandas as pd


PATH = "/home/francisco/Desktop/planilhas_escolas/xml_pdf_nfe/teste.xml"
NAMESPACE = {'':'http://www.portalfiscal.inf.br/nfe'}

arq = xml.parse(PATH)
root = arq.getroot()

prodList = root.findall('NFe/infNFe/det', NAMESPACE)

for product in prodList:
  p = Product(product, NAMESPACE)
  print(p.getProduct())
