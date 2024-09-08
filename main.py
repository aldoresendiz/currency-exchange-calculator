"""
    The following is an example of using Classes in Python.
    A 'Class' is a special 'template' that implements the functionality for
    a tool we want to instantiate every time we need to perform a certain operation
    and we do not want to implment in our code.
    The cool thing about a class is that the user (usually a developer) does not need
    to know how it works but what it does and what it does does it well without any issues
    instead of them having to write code for a simple task like in this case implement a
    currency exchange utility in their application. All the developer needs to do is
    declare the class (instantiate) and use it accordingly by manipulating the object created.
"""


class Currency:

  currencies =  {'CHF': 0.842935, #swiss franc 
                 'CAD': 1.36, #canadian dollar
                 'GBP': 0.76, #british pound
                 'JPY': 142.31, #japanese yen
                 'EUR': 0.90, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def __str__(self):
    return f"{round(self.value,2)} {self.unit}"

  def __repr__(self):
    return f"{round(self.value,2)} {self.unit}"

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
      
  def __add__(self, other):
    """
      Defines the '+' operator.
      If other is a Currency object the currency values 
      are added and the result will be the unit of 
      self. If other is an int or a float, other will
      be treated as a USD value. 
    """
    if type(other) == int or type(other) == float:
      x = (other * Currency.currencies[self.unit])
    else:
      x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
    return Currency(x + self.value, self.unit)


  def __iadd__(self, other):
    """
      Similar to __add__
    """
    return Currency.__add__(self,other)

  def __radd__(self, other):
    res = self + other
    if self.unit != "USD":
      res.changeTo("USD")
    return res

  def __sub__(self, other):
    """
      Defines the '+' operator.
      If other is a Currency object the currency values 
      are subtracted and the result will be the unit of 
      self. If other is an int or a float, other will
      be treated as a USD value. 
    """
    if type(other) == int or type(other) == float:
      x = (other * Currency.currencies[self.unit])
    else:
      x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
    return Currency(self.value - x, self.unit)


  def __isub__(self, other):
    """
      Similar to __sub__
    """
    return Currency.__sub__(self,other)

  def __rsub__(self, other):
    res = other - self.value
    res = Currency(res,self.unit)
    if self.unit != "USD":
      res.changeTo("USD")
    return res

'''
Now defining our class above we simply have to 'call' it
'''
v1 = Currency(22.42, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
