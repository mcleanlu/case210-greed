import random
from game.casting.actor import Actor
from game.casting.gems import Gem
from game.casting.rocks import Rock
from game.casting.cast import Cast
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 24
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
GEM_AMOUNT = 20
ROCK_AMOUNT = 40

def main():
    
    # create the cast
    cast = Cast()
    
    # create the points
    points = Actor()
    points.set_text("")
    points.set_font_size(FONT_SIZE)
    points.set_color(WHITE)
    points.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("points", points)
    
    # create the robot
    x = int(MAX_X / 2)
    y = 570
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robot", robot)

    #create the gems
    for n in range(GEM_AMOUNT):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        gems = Gem()
        gems.set_text('*')
        gems.set_font_size(FONT_SIZE)
        gems.set_color(Color(0,255,0))
        gems.set_position(position)
        cast.add_actor("gems", gems)
    
    #create the rocks
    for n in range(ROCK_AMOUNT):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        rocks = Rock()
        rocks.set_text('o')
        rocks.set_font_size(FONT_SIZE)
        rocks.set_color(Color(255,0,0))
        rocks.set_position(position)
        cast.add_actor("rocks", rocks)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()