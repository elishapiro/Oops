# graphicinterface.py

from button import *
import copy


class GraphicInterface:
    """ Graphical interface for Oops! """

    def __init__(self):
        """ Initializes Ooops! graphical interface. """

        # initialize graphics window
        BOARD_WIDTH = 1312.50
        BOARD_HEIGHT = 937.50
        self.win = GraphWin("", BOARD_WIDTH, BOARD_HEIGHT)
        # set up graphics window coordinates
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground("antiquewhite")
        # create header
        header = Text(Point(50, 95), "Oops!")
        header.setSize(50)
        header.setFill("black")
        header.setStyle("bold")
        header.draw(self.win)

        # create draw card button
        self.drawCard = SquareButton(self.win, Point(50, 60), 15, 10, "Draw Card")
        self.drawCard.setLabelStyle("bold")
        self.drawCard.setLabelSize(30)
        # create quit button
        self.quit = SquareButton(self.win, Point(95, 95), 9, 9, "Quit")
        self.quit.setLabelStyle("bold")
        self.quit.setLabelSize(30)
        self.quit.color("antiquewhite")

        # create forfeit turn button
        self.forfeit = SquareButton(self.win, Point(95, 30), 9, 9, "Forfeit")
        self.forfeit.setLabelStyle("bold")
        self.forfeit.setLabelSize(30)
        self.forfeit.color("antiquewhite")

        # initialize board
        self.board = []

        # create squares
        self.__makeUpperSquares()
        self.__makeRightSquares()
        self.__makeBottomSquares()
        self.__makeLeftSquares()
        # create starts
        self.__drawStarts()
        # create safety zones & homes
        self.__drawHomes()
        # create sliders
        self.__drawSliders()

        # initialize list of all players' pawns
        self.allPawns = []

    def movePawns(self, pawns):
        """ Draws pawns according to their position; inputs list of players' and
        list of pawn positions. """

        # create constants for home and start positions
        START_POS = 0
        HOME_POS = 65
        # undraw all previous pawns
        for pawn in self.allPawns:
            pawn.undraw()
        # initialize updated list of all players' pawns
        self.allPawns = []
        # loop through players
        for playerNum in range(1, len(pawns) + 1):
            # get player's board
            board = self.getBoard(playerNum)
            # get player's pawn positions
            positions = []
            for pawn in pawns[playerNum - 1]:
                positions.append(pawn.getPosition())
            # initialize counter representing pawnNum
            pawnNum = 0
            for pos in positions:  # loop through player's pawns' positions
                # increment counter
                pawnNum = pawnNum + 1
                # denote where pawn is
                pawnPlace = board[pos]
                # initialize pawn location
                pawnLoc = copy.deepcopy(pawnPlace.getCenter())
                if pos == START_POS or pos == HOME_POS:  # if pawn is home...
                    if pawnNum == 1:  # first pawn
                        pawnLoc.move(-2, 2)
                    elif pawnNum == 2:  # second pawn
                        pawnLoc.move(2, 2)
                    elif pawnNum == 3:  # third pawn
                        pawnLoc.move(-2, -2)
                    else:  # counter == 4:
                        pawnLoc.move(2, -2)  # fourth pawn
                # create pawn
                pawn = CircButton(self.win, pawnLoc, 1, "")
                # set pawn button
                pawns[playerNum-1][pawnNum-1].setPawnBut(pawn)
                # color pawn according to player
                if playerNum == 1:
                    pawn.color("gold")
                elif playerNum == 2:
                    pawn.color("green")
                elif playerNum == 3:
                    pawn.color("red")
                else:
                    pawn.color("blue")
                # add pawn to list of all pawns
                self.allPawns.append(pawn)

    def __makeUpperSquares(self):
        """ Helper function to make upper squares of Oops! board. """

        center = Point(10, 85)  # denote center of leftmost square
        for i in range(16):  # draw 16 squares
            rect = OopsButton(self.win, center, 5, 5, "")  # create square with button functionality
            rect.color("white")
            self.board.append(rect)  # add square to board list
            center.move(5, 0)

    def __makeRightSquares(self):
        """ Helper function to make right squares of Oops! board. """

        center = Point(85, 80)  # denote center of highest square
        for i in range(15):  # draw 15 squares
            rect = OopsButton(self.win, center, 5, 5, "")  # create square with button functionality
            rect.color("white")
            self.board.append(rect)  # add square to board list
            center.move(0, -5)

    def __makeBottomSquares(self):
        """ Helper function to make bottom squares of Oops! board. """

        center = Point(80, 10)  # denote center of rightmost square
        for i in range(15):  # draw 15 squares
            rect = OopsButton(self.win, center, 5, 5, "")  # create square with button functionality
            rect.color("white")
            self.board.append(rect)  # add square to board list
            center.move(-5, 0)

    def __makeLeftSquares(self):
        """ Helper function to make left squares of Oops! board. """

        center = Point(10, 15)  # denote center of rightmost square
        for i in range(14):  # draw 14 squares
            rect = OopsButton(self.win, center, 5, 5, "")
            rect.color("white")
            self.board.append(rect)  # add square to board list
            center.move(0, 5)

    def __drawStarts(self):
        """ Helper function to make 'Start' modules of Oops! board. """

        # list of square positions where "Start" is directly above
        YELLOW_POS = 19
        GREEN_POS = 34
        RED_POS = 49
        BLUE_POS = 4
        StartTable = [YELLOW_POS, GREEN_POS, RED_POS, BLUE_POS]
        # initialize list of starts
        self.starts = []

        for boardPos in StartTable:
            squareCenter = self.board[boardPos].getCenter()  # get square center
            squareX = squareCenter.getX()
            squareY = squareCenter.getY()
            if boardPos == YELLOW_POS:
                circ = CircButton(self.win, Point(squareX - 10, squareY), 7.3, "")  # create and draw start
                self.starts.append(circ)  # add circle to start list
                circ.color("yellow")
            elif boardPos == GREEN_POS:
                circ = CircButton(self.win, Point(squareX, squareY + 10), 7.3, "")  # create and draw start
                self.starts.append(circ)  # add circle to start list
                circ.color("lightgreen")
            elif boardPos == RED_POS:
                circ = CircButton(self.win, Point(squareX + 10, squareY), 7.3, "")  # create and draw start
                self.starts.append(circ)  # add circle to start list
                circ.color("pink")
            else:  # boardPos == BLUE_POS
                circ = CircButton(self.win, Point(squareX, squareY - 10), 7.3, "")  # create and draw start
                self.starts.append(circ)  # add circle to start list
                circ.color("lightblue")

    def __drawHomes(self):
        """ Helper function to make Safety Zones and Homes of Oops! board. """

        # create constant for home radius
        HOME_RADIUS = 7.3

        # list of square positions where "Safety Zone" is directly above
        YELLOW_POS = 17
        GREEN_POS = 32
        RED_POS = 47
        BLUE_POS = 2
        HomeTable = [YELLOW_POS, GREEN_POS, RED_POS, BLUE_POS]
        # initialize list of safety zone lists
        self.safetyZones = []

        for boardPos in HomeTable:
            squareCenter = copy.deepcopy(self.board[boardPos].getCenter())  # get square center
            squareY = squareCenter.getY()  # get y-value of base square center
            squareX = squareCenter.getX()  # get x-value of base square center
            safetyZone = []  # initialize player's safety zone list

            if boardPos == YELLOW_POS:
                for i in range(5):  # loop through each square in safety zone
                    # move square center
                    squareCenter.move(-5, 0)
                    # create & draw square
                    rect = OopsButton(self.win, squareCenter, 5, 5, "")
                    rect.color("yellow")
                    # add square to safety zone list
                    safetyZone.append(rect)
                # get x-value of square center
                squareX = squareCenter.getX()
                # create and draw home
                circ = CircButton(self.win, Point(squareX - 8, squareY), HOME_RADIUS, "")
                circ.color("yellow")
                # add home to safety zone list
                safetyZone.append(circ)
                # add to list of safety zone lists
                self.safetyZones.append(safetyZone)
            elif boardPos == GREEN_POS:
                for i in range(5):  # loop through each square in safety zone
                    # move square center
                    squareCenter.move(0, 5)
                    # create & draw square
                    rect = OopsButton(self.win, squareCenter, 5, 5, "")
                    rect.color("lightgreen")
                    # add square to safety zone list
                    safetyZone.append(rect)
                # get y-value of square center
                squareY = squareCenter.getY()
                # create and draw home
                circ = CircButton(self.win, Point(squareX, squareY + 8), HOME_RADIUS, "")
                circ.color("lightgreen")
                # add home to safety zone list
                safetyZone.append(circ)
                # add to list of safety zone lists
                self.safetyZones.append(safetyZone)
            elif boardPos == RED_POS:
                for j in range(5):  # loop through each square in safety zone
                    # move square center
                    squareCenter.move(5, 0)
                    # create & draw square
                    rect = OopsButton(self.win, squareCenter, 5, 5, "")
                    rect.color("pink")
                    # add square to safety zone list
                    safetyZone.append(rect)
                # get x-value of square center
                squareX = squareCenter.getX()
                # create and draw home
                circ = CircButton(self.win, Point(squareX + 8, squareY), HOME_RADIUS, "")
                circ.color("pink")
                # add home to safety zone list
                safetyZone.append(circ)
                # add to list of safety zone lists
                self.safetyZones.append(safetyZone)
            else:  # boardPos == BLUE_POS
                for j in range(5):  # loop through each square in safety zone
                    # move square center
                    squareCenter.move(0, -5)
                    # create & draw square
                    rect = OopsButton(self.win, squareCenter, 5, 5, "")
                    rect.color("lightblue")
                    # add square to safety zone list
                    safetyZone.append(rect)
                # get y-value of square center
                squareY = squareCenter.getY()
                # create and draw home
                circ = CircButton(self.win, Point(squareX, squareY - 8), HOME_RADIUS, "")
                circ.color("lightblue")
                # add home to safety zone list
                safetyZone.append(circ)
                # add to list of safety zone lists
                self.safetyZones.append(safetyZone)

    def __drawSliders(self):
        """ Helper function to make sliders of Oops! board. """

        # table of slider positions
        BLUE_POS1 = 1
        BLUE_POS2 = 9
        YELLOW_POS1 = 16
        YELLOW_POS2 = 24
        GREEN_POS1 = 31
        GREEN_POS2 = 39
        RED_POS1 = 46
        RED_POS2 = 54
        sliderTable = [BLUE_POS1, BLUE_POS2, YELLOW_POS1, YELLOW_POS2,
                       GREEN_POS1, GREEN_POS2, RED_POS1, RED_POS2]
        # draw each slider
        for sliderPos in sliderTable:
            if sliderPos == YELLOW_POS1:
                self.__drawSlider(sliderPos, 3, "yellow", "v", "b")
            elif sliderPos == YELLOW_POS2:
                self.__drawSlider(sliderPos, 4, "yellow", "v", "b")
            elif sliderPos == GREEN_POS1:
                self.__drawSlider(sliderPos, 3, "lightgreen", "h", "b")
            elif sliderPos == GREEN_POS2:
                self.__drawSlider(sliderPos, 4, "lightgreen", "h", "b")
            elif sliderPos == RED_POS1:
                self.__drawSlider(sliderPos, 3, "pink", "v", "f")
            elif sliderPos == RED_POS2:
                self.__drawSlider(sliderPos, 4, "pink", "v", "f")
            elif sliderPos == BLUE_POS1:
                self.__drawSlider(sliderPos, 3, "lightblue", "h", "f")
            elif sliderPos == BLUE_POS2:
                self.__drawSlider(sliderPos, 4, "lightblue", "h", "f")

    def __drawSlider(self, pos, length, color, hv, fb):
        """ Helper function to draw a slider. For example,
        self.drawSlider(2, 3, "lightgreen", "h", "b") draws a
        slider with base at square 2 with length 3, green color, that's horizontal
        and going backwards. """

        # get center coordinates of base
        baseX = self.board[pos].getCenter().getX()
        baseY = self.board[pos].getCenter().getY()
        # draw sliders
        if hv == "h":
            if fb == "b":
                # draw rectangle and circle of slider
                rect, circ = self.__drawSliderHelperH(baseX, baseY, pos, length)
                # draw startpoint
                triangle = Polygon(Point(baseX + 1.3, baseY + 2.5), Point(baseX + 1.3, baseY - 2.5),
                                   Point(baseX - .8, baseY))
                triangle.draw(self.win)
                # color everything
                rect.setFill(color)
                circ.setFill(color)
                triangle.setFill(color)
            else:
                # draw rectangle and circle of slider
                rect, circ = self.__drawSliderHelperH(baseX, baseY, pos, length)
                # draw startpoint
                triangle = Polygon(Point(baseX - 1.3, baseY + 2.5), Point(baseX - 1.3, baseY - 2.5),
                                   Point(baseX + .8, baseY))
                triangle.draw(self.win)
                # color everything
                rect.setFill(color)
                circ.setFill(color)
                triangle.setFill(color)
        else:
            if fb == "b":
                # draw rectangle and circle of slider
                rect, circ = self.__drawSliderHelperV(baseX, baseY, pos, length)
                # draw startpoint
                triangle = Polygon(Point(baseX + 2.5, baseY + 1.3), Point(baseX - 2.5, baseY + 1.3),
                                   Point(baseX, baseY - .8))
                triangle.draw(self.win)
                # color everything
                rect.setFill(color)
                circ.setFill(color)
                triangle.setFill(color)
            else:
                # draw rectangle and circle of slider
                rect, circ = self.__drawSliderHelperV(baseX, baseY, pos, length)
                # draw startpoint
                triangle = Polygon(Point(baseX + 2.5, baseY - 1.3), Point(baseX - 2.5, baseY - 1.3),
                                   Point(baseX, baseY + .8))
                triangle.draw(self.win)
                # color everything
                rect.setFill(color)
                circ.setFill(color)
                triangle.setFill(color)

    def __drawSliderHelperV(self, baseX, baseY, pos, length):
        """ Draws vertical sliders' rectangle and circle. """

        # get rectangle coordinates
        minX = baseX - 1
        maxX = baseX + 1
        minY = baseY
        maxY = self.board[pos + length].getCenter().getY()
        # create & draw rectangle
        rect = Rectangle(Point(minX, minY), Point(maxX, maxY)).draw(self.win)
        # create & draw endpoint
        circ = Circle(self.board[pos + length].getCenter(),
                      1.8).draw(self.win)
        # return rectangle and endpoint
        return rect, circ

    def __drawSliderHelperH(self, x, y, pos, length):
        """ Draws horizontal sliders' rectangle and circle. """

        # get rectangle coordinates
        minX = x
        maxX = self.board[pos + length].getCenter().getX()
        minY = y - 1
        maxY = y + 1
        # create & draw rectangle
        rect = Rectangle(Point(minX, minY), Point(maxX, maxY)).draw(self.win)
        # create & draw endpoint
        circ = Circle(self.board[pos + length].getCenter(),
                      1.8).draw(self.win)
        # return rectangle and endpoint
        return rect, circ

    def getBoard(self, player):
        """ Returns board of Player X (board is a list of relevant objects in
        chronological order). e.g., for Player 1,the board begins with "Start", goes
        the perimeter, and ends with the "Safety Zone" followed by the "Weird Spot." """

        if player == 1:  # create yellow player's board
            newBoard = [self.starts[0]]  # initialize new board
            # add squares in subsequent positions
            for squarePos in range(19, 60, 1):
                newBoard.append(self.board[squarePos])
            # continue adding squares in subsequent positions
            for squarePos in range(18):
                newBoard.append(self.board[squarePos])
            # add safety zone & home
            yellowSafe = self.safetyZones[0]
            for safetyPos in range(6):
                newBoard.append(yellowSafe[safetyPos])
            # add square between start & home; the "weird spot"
            newBoard.append(self.board[18])
        elif player == 2:  # create green player's board
            newBoard = [self.starts[1]]  # initialize new board
            # add squares in subsequent positions
            for squarePos in range(34, 60, 1):
                newBoard.append(self.board[squarePos])
            # continue adding squares in subsequent positions
            for squarePos in range(33):
                newBoard.append(self.board[squarePos])
            # add safety zone & home
            greenSafe = self.safetyZones[1]
            for safetyPos in range(6):
                newBoard.append(greenSafe[safetyPos])
            # add square between start & home; the "weird spot"
            newBoard.append(self.board[33])
        elif player == 3:  # create red player's board
            newBoard = [self.starts[2]]  # initialize new board
            # add squares in subsequent positions
            for squarePos in range(49, 60, 1):
                newBoard.append(self.board[squarePos])
            # continue adding squares in subsequent positions
            for squarePos in range(48):
                newBoard.append(self.board[squarePos])
            # add safety zone & home
            redSafe = self.safetyZones[2]
            for safetyPos in range(6):
                newBoard.append(redSafe[safetyPos])
            # add square between start & home; the "weird spot"
            newBoard.append(self.board[48])
        else:  # create blue player's board
            newBoard = [self.starts[3]]  # initialize new board
            # add squares in subsequent positions
            for squarePos in range(4, 60, 1):
                newBoard.append(self.board[squarePos])
            # continue adding squares in subsequence positions
            for squarePos in range(3):
                newBoard.append(self.board[squarePos])
            # add safety zone & home
            blueSafe = self.safetyZones[3]
            for safetyPos in range(6):
                newBoard.append(blueSafe[safetyPos])
            # add square between start & home
            newBoard.append(self.board[3])

        # return board
        return newBoard

    def getWindow(self):
        """ Returns Oops! window. """
        return self.win

    def getPawnButs(self):
        """ Returns pawn buttons. """
        return self.allPawns

    def getDrawCard(self):
        """ Returns draw card button. """
        return self.drawCard

    def getQuit(self):
        """ Returns quit button. """
        return self.quit

    def getForfeit(self):
        """ Returns quit button. """
        return self.forfeit
