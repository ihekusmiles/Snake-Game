from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 17, 'bold')

# This class will create the scoreboard which will be stored in a data.txt file
# The data.txt file will be created automatically if not already found.
# Additionally, this class will update the scoreboard and reset it as the game loops.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 270)
        self.color("white")
        self.hideturtle()
        self.check_text_file()
        self.update_scoreboard()

    def check_text_file(self):
        try:
            with open("data.txt") as data:
                self.highscore = int(data.read())
        except FileNotFoundError:
            with open("data.txt", mode="w") as data:
                data.write("0")
        finally:
            with open("data.txt") as data:
                self.highscore = int(data.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
