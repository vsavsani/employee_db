class Employee():
  
  def __init__(self, number, name, mobile, landline):
    self.number = number
    self.name = name
    self.mobile = mobile
    self.landline = landline
 
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

