import turtle
import time

def main():
    s = turtle.Screen()
    launcher = Launcher()

    s.onkeypress(launcher.turn_left, "Left")
    s.onkeypress(launcher.turn_right, "Right")
    s.onkeypress(launcher.launch, "space")
    s.listen()

    s.mainloop()


class Launcher:
    def __init__(self):
        self.speed_x = 1
        self.speed_y = 1
        self.x = 0
        self.y = 0
        self.g = 9.81
        self.t = turtle.Turtle()
        self.t.shapesize(10)
        self.t.pensize(5)

    def turn_left(self):
        self.t.left(1)

    def turn_right(self):  
        self.t.right(1)

    def launch(self):
        self.move_projectile()

    def move_projectile(self):
        while True:
            # vy2 = voy2 - 2g(y - y0)
            self.x += self.speed_x
            self.y += self.speed_y
            self.t.goto(self.x, self.x)
            self.speed_y -= self.g


if __name__ == "__main__":
    main()