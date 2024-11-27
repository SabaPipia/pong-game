from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.speed('fastest')
        if pos == 'L':
            self.starting_x = -350
        elif pos == 'R':
            self.starting_x = 350
        else:
            self.reset()

        self.set_position(self.starting_x,0)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
    
    def set_position(self, x, y):
        self.goto(x,y)
    
    def up(self):
        y_cor = self.ycor() + 50
        self.goto(self.starting_x, y_cor)
    
    def down(self):
        y_cor = self.ycor() - 50
        self.goto(self.starting_x, y_cor)
    
