from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    """
    The mani class of snake's Scoreboard.
    It has 3 functions(), and they are as follows
    update_scoreboard() which updates thw scoreboard count
    """

    def __init__(self):
        """"It makes score-board to appear"""
        super().__init__()
        self.score = 0
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """This method update the score of the game"""
        self.clear()
        self.write(f"Score: {self.score}  Highest Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        """This method increased the score of the gamer/user"""
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        """
        This method resets the score of the gamer/user to the highest if its score is greater than the
        highest score
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
