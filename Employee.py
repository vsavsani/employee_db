class Employee():
  
  def __init__(self, number, name, mobile1, mobile2, landline1, landline2):
    self.number = number
    self.name = name
    self.mobile = [None]*2
    self.mobile[0] = mobile1
    self.mobile[1] = mobile2
    self.landline = [None]*2
    self.landline[0] = landline1
    self.landline[1] = landline2
 
  def set_number(self, number):
    self.number = number
  def set_name(self, name):
    self.name = name
  def set_mobile (self, mobile):
    self.mobile = mobile
  def set_landline (self, landline):
    self.landline = landline

  def get_number(self):
    return self.number
  def get_name(self):
    return self.name
  def get_mobile(self):
    return self.mobile
  def get_landline(self):
    return self.landline
  def __str__(self):
    return "Name: " +self.name+ "\nID Number: "+self.number+"\nMobileNo: "+self.mobile+"\nLandline: "+self.landline

