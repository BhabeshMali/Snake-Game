from turtle import Turtle

class Score(Turtle) :
    def __init__(self) :
        super().__init__()
        self.value = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        #self.write(
        self.update_score()
    def update_score(self) :
        self.write(f"Score: {self.value} ", align = "center", font = ("Arial",15,"normal"))
    def game_over(self) :
        self.goto(0,0)
        self.write("Game Over", align = "center", font = ("Arial",20,"normal"))
    def score_inc(self) :
        self.value +=1
        self.clear()
        self.update_score()
        