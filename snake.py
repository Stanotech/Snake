from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_creation()
        self.direction = "right"



    def snake_creation(self):
        for x in range(3):
            seg = Turtle()
            seg.penup()
            seg.shape("square")
            seg.color("white")
            seg.turtlesize(1)
            seg.setpos(x * 21, 0)
            self.segments.append(seg)

    def move(self, grow):

        if not grow:
            for seg in range(0, len(self.segments) - 1, 1):
                self.segments[seg].setpos(self.segments[seg + 1].xcor(), self.segments[seg + 1].ycor())

        if grow:        # adding one segment before head
            seg = Turtle()
            seg.penup()
            seg.shape("square")
            seg.color("white")
            seg.turtlesize(1)
            seg.setpos(self.segments[len(self.segments) - 1].xcor(), self.segments[len(self.segments) - 1].ycor())
            self.segments.insert(len(self.segments) - 1, seg)


        if self.direction == "up":
            old_y = self.segments[len(self.segments) - 1].ycor()
            self.segments[len(self.segments) - 1].sety(old_y + 21)
        if self.direction == "down":
            old_y = self.segments[len(self.segments) - 1].ycor()
            self.segments[len(self.segments) - 1].sety(old_y - 21)
        if self.direction == "right":
            old_x = self.segments[len(self.segments) - 1].xcor()
            self.segments[len(self.segments) - 1].setx(old_x + 21)
        if self.direction == "left":
            old_x = self.segments[len(self.segments) - 1].xcor()
            self.segments[len(self.segments) - 1].setx(old_x - 21)