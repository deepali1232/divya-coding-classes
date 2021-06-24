class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def show_vehicle_details(self):
        print('i am a vehicle')
        print('mileage of vehicle is ',self.mileage)
        print('cost of vehicle is ',self.cost)
v1=Vehicle(300,500)

class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp

    def show_car_details(self):
        print('no of tyres in a car',self.tyres)
        print('hp of car',self.hp)
        print('i am a car')

c1=Car(100,1000000,4,999)
c1.show_vehicle_details()
c1.show_car_details()

