class Register:
  def __init__(self,action,loc,subloc,origin):
    self.action = str(action)
    self.loc = str(loc)
    self.subloc = str(subloc)
    self.origin = str(origin)
    self.opcode = str(str(action)+str(loc)+str(subloc)+str(origin))
    
  def register(self):
    return 0

  def postStream(self):
    print(self.origin + self.action + " to register at " + self.subloc + " within "+ self.subloc)



