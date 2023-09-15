class Address:

  def __init__(self, new_street, new_suburb, new_postcode):
    self.__street = new_street

    self.__suburb = new_suburb

    self.__postcode = new_postcode

  def __str__(self):
    return f"Street: {self.__street} , Suburb: {self.__suburb}, Postcode: {self.__postcode}"
