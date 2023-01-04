from info.Address import Address
from Constants import NAMESPACE

class Enterprise:
  def __init__(self, enterpriseNode, addressTagName, nameSpace) -> None:
    addressNode = enterpriseNode.find(addressTagName, nameSpace)
    address = Address(addressNode, NAMESPACE)

    self.name    = enterpriseNode.find('xNome', nameSpace).text
    self.cnpj    = enterpriseNode.find('CNPJ', nameSpace).text
    self.address = address.getAddress()
  
  def getEnterpriseInfo(self):
    return {
      'name'    : self.name,
      'cnpj'    : self.cnpj,
      'address' : self.address
    }
