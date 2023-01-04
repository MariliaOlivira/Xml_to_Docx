class Address:
  def __init__(self, addressNode, nameSpace) -> None:
    self.street     = addressNode.find('xLgr',nameSpace).text
    self.num        = addressNode.find('nro',nameSpace).text
    self.city       = addressNode.find('xMun',nameSpace).text
    self.state      = addressNode.find('UF',nameSpace).text
    self.cep        = addressNode.find('CEP',nameSpace).text

  def getAddress(self) -> str:
    return f'{self.street} {self.num} {self.city} {self.state} CEP: {self.cep}'
