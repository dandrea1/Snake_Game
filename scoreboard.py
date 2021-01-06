from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 265)
        self.color('white')
        self.write(f"Score: {self.score}", align=ALIGNMENT,font = FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)
