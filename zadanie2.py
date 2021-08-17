class Vehicle: 
  def __init__(self, max_speed_, number_):
    self.max_speed = max_speed_
    self.number = number_



class Bus(Vehicle):
  def __init__(self, max_speed_, number_, fuel_consumption_):
    super().__init__(max_speed_, number_)
    self.fuel_consumption = fuel_consumption_
  
  

  def __str__(self):
    return f'Autobus nr {self.number} max prędkość {self.max_speed}km/h zużycie paliwa w miesiącu: {self.fuel_consumption} litrów'
  
class Tram(Vehicle):
  def __init__(self, max_speed_, number_, wagon_number_):
    super().__init__(max_speed_, number_)
    self. wagon_number =  wagon_number_

  def __str__(self):
    return f'Tramwaj nr {self.number} max prędkość {self.max_speed} ma: {self.wagon_number} wagonów'

class depot:
  def __init__(self, name_, type_):
    self.name = name_
    self.type_of_depot = type_
    self.vehicle = []
  
  def __str__(self):
    return f'Zajezdnia {self.name}  '
  


  


def main():
  bus1 = Bus(80,500, 120 )
  print(bus1)

if __name__ == '__main__':
  main()