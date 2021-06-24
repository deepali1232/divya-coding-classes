class Parent1:
    def assign_str1(self,str1):
        self.str1=str1

    def show_str1(self):
        print(self.str1)


class Parent2:
    def assign_str2(self,str2):
        self.str2=str2
    def show_str2(self):
        print(self.str2)


class Derived(Parent1,Parent2):
    def assign_str3(self,str3):
        self.str3=str3
    def show_str3(self):
        print(self.str3)
d1=Derived()
d1.assign_str1('i am string 1')
d1.assign_str2('i am string 2')
d1.assign_str3('i am string 3')
d1.show_str1()
d1.show_str2()
d1.show_str3()
