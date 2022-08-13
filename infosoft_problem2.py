# Problem 2 - Fuel Station Design


class FuelStation:
    def __init__(self, diesel, petrol, electric):
        self.diesel: int = diesel
        self.petrol: int = petrol
        self.electric: int = electric
        self.diesel_count = self.diesel
        self.petrol_count = self.petrol
        self.electric_count = self.electric

    def fuel_vehicle(self, fuel_type: str) -> bool:

        if fuel_type == 'diesel':
            if self.diesel == 0:
                return False
            elif self.diesel > 0:
                self.diesel = self.diesel - 1
                return True
            else:
                return False

        elif fuel_type == 'petrol':
            if self.petrol == 0:
                return False
            elif self.petrol > 0:
                self.petrol = self.petrol - 1
                return True
            else:
                return False

        elif fuel_type == 'electric':
            if self.electric == 0:
                return False
            elif self.electric > 0:
                self.electric = self.electric - 1
                return True
            else:
                return False
        else:
            return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        if fuel_type == 'diesel':
            self.diesel = self.diesel + 1
            if self.diesel <= self.diesel_count:
                return True
            else:
                return False

        elif fuel_type == 'petrol':
            self.petrol = self.petrol + 1
            if self.petrol <= self.petrol_count:
                return True
            else:
                return False

        elif fuel_type == 'electric':
            self.electric = self.electric + 1
            if self.electric <= self.electric_count:
                return True
            else:
                return False

        else:
            return False


fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("petrol"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))
