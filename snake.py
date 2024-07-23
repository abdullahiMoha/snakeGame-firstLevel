from turtle import Turtle

# these for class Snake, they unchangeable variables
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    A class to represent a snake in a snake game.

    Attributes
    ----------
    DEFAULT_SNAKE_SEGMENTS : int
        The default number of segments the snake starts with.
    DEFAULT_POSITION : int
        The default starting position of the snake on the game screen.
    snake : list
        A list of Turtle objects representing the segments of the snake.
    head : Turtle
        A reference to the head segment of the snake for movement control.

    Methods
    -------
    create_snake():
        Initializes the snake with a default number of segments at default positions.

    add_segment(position):
        Adds a new segment to the snake at the specified position.
        Parameters:
            position (tuple): The (x, y) position to place the new segment.

    extend():
        Extends the snake by adding a new segment at the position of the last segment.

    move():
        Moves the snake forward by moving each segment to the position of the segment in front of it.

    up():
        Changes the direction of the snake's head to up if it's not currently moving down.

    down():
        Changes the direction of the snake's head to down if it's not currently moving up.

    right():
        Changes the direction of the snake's head to right if it's not currently moving left.

    left():
        Changes the direction of the snake's head to left if it's not currently moving right.
    """

    def __init__(self):
        """
        Initializes a new Snake instance.

        Sets up the default number of snake segments and position, creates the initial snake,
        and identifies the head of the snake for movement control.
        """
        self.DEFAULT_SNAKE_SEGMENTS = 3
        self.DEFAULT_POSITION = 20
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """
        Initializes the snake with default segments.

        This method uses a predefined set of starting positions to add segments to the snake,
        effectively creating it on the game screen.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        This for Adding new segments to the snake
        It has one parameter which is type of tuple when passing to it,
        it also sets what ever needed for that segment
        """
        trl = Turtle("square")
        trl.color("white")
        trl.penup()
        trl.goto(position)
        self.snake.append(trl)

    def rest_snake(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        """ Extends the snake by adding new segments to the snake, calling this method add_segment()"""
        self.add_segment(self.snake[-1].position())

    def move(self):
        """ Moves the snake forward or backward directions """
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
