class Enterprise:
  def __init__(self, enterpriseNode, nameSpace) -> None:
    self.name = enterpriseNode.find('xNome',nameSpace).text
    self.cnpj = enterpriseNode.find('CNPJ',nameSpace).text
  
  def getEnterpriseInfo(self):
    return {
      'name': self.name,
      'cnpj': self.cnpj
    }