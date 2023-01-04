from info.Enterprise.Enterprise import Enterprise

class Concurrent(Enterprise):
  def __init__(self, enterpriseNode, nameSpace) -> None:
    super().__init__(enterpriseNode, 'enderEmit', nameSpace)
    self.inscription = enterpriseNode.find('IE', nameSpace).text

  def getEnterpriseInfo(self):
    info = super().getEnterpriseInfo()
    info['inscription'] = self.inscription

    return info
