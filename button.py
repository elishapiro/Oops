# button.py
# This class is heavily inspired by the version of it in "Python
#    Programming: An Introduction to Computer Science" by John Zelle

import math
from graphics import *


class Button:
    """A button is a labeled shape in a window.
        It is activated or deactivated with the activate()
        and deactivate() methods. The clicked(p) method
        returns true if the button is active and p is inside it."""

    def clicked(self, p):
        """Returns true if button active and p is inside"""

    def color(self, color):
        """ Colors this button """

    def setLabelStyle(self, style):
        """ Sets this button's label's style """

    def setLabelSize(self, size):
        """ Sets this button's label's size """

    def setWidth(self, size):
        """ Sets this button's width """

    def getLabel(self):
        """Returns the label string of this button"""

    def getCenter(self):
        """Returns center of this button"""

    def activate(self):
        """Sets this button to 'active'."""

    def deactivate(self):
        """Sets this button to 'inactive'."""

    def isDeactivated(self):
        """ Returns boolean indicating whether button is deactivated """

    def undraw(self):
        """ Undraws button """


class SquareButton(Button):
    """ A square button. """

    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button, e.g.:
        qb = SquareButton(myWin, centerPoint, width, height, 'Quit')"""

        # create rectangle
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        self.p1 = Point(self.xmin, self.ymin)
        self.p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(self.p1, self.p2)
        self.rect.setFill("lightgrey")
        self.rect.draw(win)

        # record center of button
        self.center = self.rect.getCenter()

        # create label
        self.label = Text(center, label)
        self.label.draw(win)

        # initialize boolean indicating whether button is active
        self.active = False

        # deactivate button
        self.deactivate()

    def clicked(self, p):
        """Returns true if button active and p is inside"""
        return (self.active and p and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def color(self, color):
        """ Colors this button """
        self.rect.setFill(color)

    def setLabelStyle(self, style):
        """ Sets this button's label's style """
        self.label.setStyle(style)

    def setLabelSize(self, size):
        """ Sets this button's label's size """
        self.label.setSize(size)

    def setWidth(self, size):
        """ Sets this button's width """
        self.rect.setWidth(size)

    def getLabel(self):
        """ Returns the label string of this button """
        return self.label.getText()

    def getCenter(self):
        """ Returns center of this button """
        return self.center

    def activate(self):
        """ Sets this button to 'active'. """
        self.label.setFill("black")
        self.rect.setWidth(3)
        self.active = True

    def deactivate(self):
        """ Sets this button to 'inactive'. """
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False

    def isDeactivated(self):
        """ Returns boolean indicating whether button is deactivated """
        return not self.active

    def undraw(self):
        """ Undraws button """
        self.rect.undraw()
        self.label.undraw()


class CircButton(Button):
    """ A circular button. """

    def __init__(self, win, center, radius, label):
        """Creates a circular button, eg:
        qb = CircButton(myWin, centerPoint, width, height, 'Quit')"""

        # create circle
        self.circ = Circle(center, radius)
        self.center = center
        self.radius = radius
        self.circ.setFill("lightgrey")
        self.circ.draw(win)

        # create label
        self.label = Text(center, label)
        self.label.draw(win)

        # initialize boolean indicating whether button is active
        self.active = False

        # deactivate button
        self.deactivate()

    def clicked(self, p):
        """Returns true if button active and p is inside"""
        return (self.active and p and
                math.sqrt(abs(p.getX() - self.center.getX()) ** 2 +
                          abs(p.getY() - self.center.getY()) ** 2) < self.radius)

    def color(self, color):
        """ Colors this button """
        self.circ.setFill(color)

    def setLabelStyle(self, style):
        """ Sets this button's label's style """
        self.label.setStyle(style)

    def setLabelSize(self, size):
        """ Sets this button's label's size """
        self.label.setSize(size)

    def setWidth(self, size):
        """ Sets this button's width """
        self.circ.setWidth(size)

    def getLabel(self):
        """ Returns the label string of this button """
        return self.label.getText()

    def getCenter(self):
        """ Returns center of this button """
        return self.center

    def activate(self):
        """ Sets this button to 'active'. """
        self.label.setFill("black")
        self.circ.setWidth(3)
        self.active = True

    def deactivate(self):
        """ Sets this button to 'inactive'. """
        self.label.setFill("darkgrey")
        self.circ.setWidth(1)
        self.active = False

    def isDeactivated(self):
        """ Returns boolean indicating whether button is deactivated """
        return not self.active

    def undraw(self):
        """ Undraws button """
        self.circ.undraw()
        self.label.undraw()


class OopsButton(Button):
    """ An OopsButton is a square in Oops! """

    def __init__(self, win, center, width, height, label):
        """ Initializes this button """

        # initialize window
        self.win = win

        # create square
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        self.p1 = Point(self.xmin, self.ymin)
        self.p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(self.p1, self.p2)
        self.rect.setFill("lightgrey")
        self.rect.draw(win)

        # record center of button
        self.center = self.rect.getCenter()

        # create label
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = False
        self.deactivate()

        # create 'X' that will display that button is activated
        self.lineOne = Line(Point(self.center.getX() - width / 2,  self.center.getY() + height / 2),
                            Point(self.center.getX() + width / 2, self.center.getY() - height / 2))
        self.lineOne.setWidth(3)
        self.lineTwo = Line(Point(self.center.getX() + width / 2, self.center.getY() + height / 2),
                            Point(self.center.getX() - width / 2, self.center.getY() - height / 2))
        self.lineTwo.setWidth(3)

    def clicked(self, p):
        """Returns true if button active and p is inside"""
        return (self.active and p and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def color(self, color):
        """ Colors this button """
        self.rect.setFill(color)

    def setLabelStyle(self, style):
        """ Sets this button's label's style """
        self.label.setStyle(style)

    def setLabelSize(self, size):
        """ Sets this button's label's size """
        self.label.setSize(size)

    def setWidth(self, size):
        """ Sets this button's width """
        self.rect.setWidth(size)

    def getLabel(self):
        """ Returns the label string of this button """
        return self.label.getText()

    def getCenter(self):
        """ Returns center of this button """
        return self.center

    def activate(self):
        """ Activates this button """
        if not self.active:
            self.lineOne.draw(self.win)
            self.lineTwo.draw(self.win)
            self.active = True

    def deactivate(self):
        """ Deactivates this button """
        if self.active:
            self.lineOne.undraw()
            self.lineTwo.undraw()
            self.active = False

    def isDeactivated(self):
        """ Returns boolean indicating whether button is deactivated """
        return not self.active

    def undraw(self):
        """ Undraws button """
        self.rect.undraw()
        self.label.undraw()
