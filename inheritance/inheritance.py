class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def show_details(self):
        print('i am a vehicle')
        print('mileage of vehicle is ',self.mileage)
        print('cost of vehicle is ',self.cost)

v1=Vehicle(500,500)
v1.show_details()
class Car(Vehicle):
    def show_car(self):
        print("i am a car")
c1=Car(260,290)
c1.show_details()
c1.show_car()