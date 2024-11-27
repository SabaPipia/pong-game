from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed('slowest')
        self.penup()
        self.x_move = 10
        self.y_move = 10        
    
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def refresh(self):
        self.goto(0,0)
        self.x_move = 10

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.speed_up()
        self.x_move *= -1

    def speed_up(self):
        self.x_move = self.x_move * 0.2 + self.x_move
    
    

