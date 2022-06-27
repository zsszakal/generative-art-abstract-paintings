from processing import *
from random import shuffle, uniform, choice, gauss

WIDTH = 1000
HEIGHT = 1000

colors = [
    (112, 112, 74, 150),  # green
    (112, 198, 110, 150),  # yellow
    (112, 229, 194, 150),  # cream
    (112, 106, 97, 150),  # light grey
    (112, 90, 34, 150),  # orange
    (112, 61, 0, 150)]  # red-orange

shuffle(colors)

brush = {"x": None, "y": None, "px": None, "py": None}


def setup():
    size(WIDTH, HEIGHT)
    base = colors.pop()
    background(base[0], base[1], base[2])


def draw():
    global brush

    if frameCount == 50:
        brush = {"x": mouseX, "y": mouseY, "px": mouseX - 1, "py": mouseY - 1}
    elif frameCount > 50:
        brush["x"] += (mouseX - brush["x"]) / 12
        brush["y"] += (mouseY - brush["y"]) / 12
        drizzle()
        brush["px"] = brush["x"]
        brush["py"] = brush["y"]


def drizzle():
    d = dist(brush["px"], brush["py"], brush["x"], brush["y"])
    s = min(15, 1 + 30 / (d + 0.000001))
    strokeWeight(s)
    stroke(30)
    line(brush["px"], brush["py"], brush["x"], brush["y"])
    stroke(255)
    line(WIDTH - brush["px"], HEIGHT - brush["py"], WIDTH - brush["x"], HEIGHT - brush["y"])


def stipple(x, y, c):
    noStroke()
    fill(c)
    for i in range(2):
        d = uniform(3, 13)
        ellipse(x + uniform(-30, 30), y + uniform(-30, 30), d, d)


def splatter(outer_x, outer_y):
    rgb = choice(colors)
    outer_x += uniform(-15, 15)
    outer_y += uniform(-15, 15)
    for i in range(80):
        x = outer_x + 5 * (mouseX - pmouseX) * gauss(0, 0.25)
        y = outer_y + 5 * (mouseY - pmouseY) * gauss(0, 0.25)
        d = dist(outer_y, outer_y, x, y)
        s = min(15, 1 + 30 / (d + 0.000001))
        alpha = 255 - s * 5
        noStroke()
        c = color(rgb[0], rgb[1], rgb[2], alpha)
        fill(c)
        ellipse(x, y, s, s)


def mouseMoved():
    if frameCount % 10 == 0:
        stipple(mouseX, mouseY, 255)
        stipple(WIDTH - mouseX, HEIGHT - mouseY, 0)
        splatter(mouseX, mouseY)
        splatter(WIDTH - mouseX, HEIGHT - mouseY)


run()