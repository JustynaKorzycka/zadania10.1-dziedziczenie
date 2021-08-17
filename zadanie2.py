class Vehicle: 
  def __init__(self, max_speed_, number_):
    self.max_speed = max_speed_
    self.number = number_
    self.type_of_vehicle = None
    self.depot = None

  def __str__(self):
    if self.type_of_vehicle == 'Bus':
      return f'Autobus nr {self.number} max prędkość {self.max_speed}km/h zużycie paliwa w miesiącu: {self.fuel_consumption} litrów'
    elif self.type_of_vehicle == 'Tram':
      return f'Tramwaj nr {self.number} max prędkość {self.max_speed} ma: {self.wagon_number} wagonów'

class Bus(Vehicle):
  def __init__(self, max_speed_, number_, fuel_consumption_):
    super().__init__(max_speed_, number_)
    self.fuel_consumption = fuel_consumption_
    self.type_of_vehicle = 'Bus'
  
class Tram(Vehicle):
  def __init__(self, max_speed_, number_, wagon_number_):
    super().__init__(max_speed_, number_)
    self.wagon_number =  wagon_number_
    self.type_of_vehicle = 'Tram'
    
class Depot:
  def __init__(self, name_, type_):
    self.name = name_
    self.type_of_depot = type_
    self.vehicle_list = []

  def __str__(self):
    if self.type_of_depot == 'bus-depot':
      return (f'Zajezdnia {self.name} {self.type_of_depot} fuel-consumtion per month: {self.fuel_amount}')
      
    elif self.type_of_depot == 'tram-depot':
      return (f'Zajezdnia {self.name} {self.type_of_depot} all wagons: {self.wagons_amount}') 
  
class BusDepot(Depot):
  def __init__(self, name):
    super().__init__(name, 'bus-depot')
    self.fuel_amount = 0
  
  def count_fuel_amount(self):
    self.fuel_amount += self.vehicle_list[len(self.vehicle_list)-1].fuel_consumption 

class TramDepot(Depot):
  def __init__(self, name):
    super().__init__(name, 'tram-depot')
    self.wagons_amount = 0

  def count_wagons_amount(self):
    self.wagons_amount += self.vehicle_list[len(self.vehicle_list)-1].wagon_number 

class PublicTransportPanel:

  def add_vehicle_to_depot(self, vehicle, depot):
    depot.vehicle_list.append(vehicle)
    vehicle.depot = depot
    if isinstance(vehicle, Bus):
      depot.count_fuel_amount()
    if isinstance(vehicle, Tram):
      depot.count_wagons_amount()
  
  def print_depot(self, depot):
    print(depot)

def main():
  public_transport = PublicTransportPanel()
  bus1 = Bus(80,500, 1000 )
  tram1 = Tram(120, 4, 100)

  bus2 = Bus(80,144,99 )
  tram2 = Tram(120, 24, 1)

  depot_bus = BusDepot('nowa huta')
  depot_tram = TramDepot('podgórze')

  public_transport.add_vehicle_to_depot(bus1, depot_bus)
  public_transport.add_vehicle_to_depot(bus2, depot_bus)
  public_transport.add_vehicle_to_depot(tram1, depot_tram)
  public_transport.add_vehicle_to_depot(tram2, depot_tram)

  public_transport.print_depot(depot_bus)
  public_transport.print_depot(depot_tram)

if __name__ == '__main__':
  main()