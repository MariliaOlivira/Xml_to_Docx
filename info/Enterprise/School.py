from info.Enterprise.Enterprise import Enterprise

class School(Enterprise):
  def __init__(self, enterpriseNode, nameSpace) -> None:
    super().__init__(enterpriseNode, 'enderDest', nameSpace)
