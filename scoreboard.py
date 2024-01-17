from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update()
    def update(self):
        self.write(f"Score:{self.score}",align="center",font=("Courier,24,bold"))  
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over!Score{self.score}",align="center",font=("Courier,24,bold"))
    def reset(self):    
        if self.score>self.high_score:
            self.high_score=self.scores
        self.score=0
        self.update()
    def clearscr(self):
        self.score = 0

    def increaseScore(self):
        self.score+=1
        self.clear()
        self.update()