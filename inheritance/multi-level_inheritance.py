class Parent:
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
class Child(Parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        print(self.age)
class Grandchild(Child):
    def assign_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        print(self.gender)
gc=Grandchild()
gc.assign_name('divya')
gc.assign_age(24)
gc.assign_gender('female')
gc.show_name()
gc.show_age()
gc.show_gender()