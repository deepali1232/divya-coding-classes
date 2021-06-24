class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        print(self.color)
    def show_cost(self):
        print(self.cost)
    def make_calls(self):
        print('making calls')
    def play_games(self):
        print('play games')

p1=Phone()
p1.set_color('red')
p1.set_cost(20000)
p1.show_color()
p1.show_cost()

p1.make_calls()
p1.play_games()