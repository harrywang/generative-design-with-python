from p5 import *


def setup():
    size(720, 720)  # size of the canvas
    #no_cursor()  # no_cursor raise NotImplementedError

    color_mode('HSB', 160, 100, 100)  # use hsb with max values for h, s, b
    rect_mode('CENTER')
    no_stroke()  # disables drawing the stroke (outline)


def draw():
    background(mouse_y/2, 100, 100)  # values for H, S, B
    fill(360 - mouse_y/2, 100, 100)  # sets the color used to fill shapes
    rect(360, 360, mouse_x + 1, mouse_x + 1)  # location: x, y, and size:width, length


if __name__ == '__main__':
    run()
