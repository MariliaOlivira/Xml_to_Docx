class Product:
  def __init__(self, prodNode, nameSpace) -> None:
    self.description = prodNode.find('prod/xProd', nameSpace).text
    self.price       = prodNode.find('prod/vUnTrib', nameSpace).text
    self.quantity    = prodNode.find('prod/qTrib', nameSpace).text
    self.unity       = prodNode.find('prod/uTrib', nameSpace).text

  def getProduct(self) -> dict:
    price = float(self.price)
    quant = float(self.quantity)
    return {'name': self.description,
            'unity': self.unity,
            'price': price, 
            'quant': quant,
            'total': price*quant}
