class Stock:
  def __init__(self, name, symbol, previous_closing_price, current_price):
    self.__name = name
    self.__symbol = symbol
    self.__previous_closing_price = previous_closing_price
    self.__current_price = current_price
    
  def get_name(self):
    return self.__name
  
  def get_symbol(self):
    return self.__symbol
  
  def get_previous_closing_price(self):
    return self.__previous_closing_price
  
  def get_current_price(self):
    return self.__current_price

  def set_previous_closing_price(self, previous_closing_price):
    self.__previous_closing_price = previous_closing_price
    
  def set_current_price(self, current_price):
    self.__current_price = current_price

  def get_change_percent(self):
    difference = self.__current_price - self.__previous_closing_price
    percentage = (difference / self.__previous_closing_price) * 100
    return percentage
    
  def __str__(self):
    details = f"Name: {self.__name}"
    details += f"\nSymbol: {self.__symbol}"
    details += f"\nPrevious Closing Price: {self.__previous_closing_price}"
    details += f"\nCurrent Price: {self.__current_price}"
    details += f"\nPrice Change Percentage: {self.get_change_percent()}%"
    return details
