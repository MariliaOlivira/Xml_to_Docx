class Product:
  def __init__(self, prodNode, nameSpace) -> None:
    self.description = prodNode.find('prod/xProd', nameSpace).text
    self.price       = prodNode.find('prod/vUnTrib', nameSpace).text
    self.quantity    = prodNode.find('prod/qTrib', nameSpace).text
    self.unity       = prodNode.find('prod/uTrib', nameSpace).text

  def getProduct(self) -> dict:
    return {'name': self.description, 
            'price': float(self.price), 
            'quant': float(self.quantity), 
            'unity': self.unity}