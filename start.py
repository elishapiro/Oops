# start.py

from button import *
from oopsapp import *


class Start:
    """ Start page for Oops! game; allows users to decide number of players """

    def __init__(self):
        """ Initializes start page """

        # create constant for maximum number of players
        self.MAX_NUM_PLAYERS = 4

        # initialize number of player that won as None
        winner = None

        # create start window
        startPage = GraphWin("", 500, 500)
        startPage.setCoords(0, 0, 100, 100)
        startPage.setBackground("antiquewhite")

        # create welcome label
        welcomeLabel = Text(Point(50, 90), "Welcome to Oops!")
        welcomeLabel.setSize(36)
        welcomeLabel.setTextColor("black")
        welcomeLabel.setStyle("bold")
        welcomeLabel.draw(startPage)

        # create label for number of players
        numPlayers = Text(Point(50, 75), "How many players?")
        numPlayers.setSize(20)
        numPlayers.setTextColor("black")
        numPlayers.setStyle("bold")
        numPlayers.draw(startPage)

        # create buttons for number of players
        playerButtons = []  # initialize buttons list
        center = Point(30, 60)  # initialize button center
        for numPlayers in range(2, self.MAX_NUM_PLAYERS + 1):
            # create button
            playNumButton = SquareButton(startPage, center, 20, 20, "{0}".format(numPlayers))

            if numPlayers == 2:
                playNumButton.color("lightgreen")
            elif numPlayers == 3:
                playNumButton.color("pink")
            else:
                playNumButton.color("lightblue")

            playNumButton.setLabelStyle("bold")
            playNumButton.setLabelSize(35)
            playerButtons.append(playNumButton)

            # move center
            center.move(20, 0)

        # activate buttons
        for button in playerButtons:
            button.activate()

        #  initialize boolean for if user has pressed a button
        butPressed = False
        # wait for user to press a button
        while not butPressed:
            # check for mouse click
            p = startPage.getMouse()
            # determine whether a button is clicked
            for button in playerButtons:
                if button.clicked(p):
                    button.deactivate()
                    butPressed = True

        # create start button
        startButton = SquareButton(startPage, Point(50, 10), 80, 15, "Start")
        startButton.color("antiquewhite")
        startButton.setLabelStyle("bold")
        startButton.setLabelSize(20)
        startButton.activate()

        # initialize boolean for if user has pressed startButton
        startPressed = False
        # wait for user to press start button
        while not startPressed:
            # check for mouse click
            p = startPage.getMouse()
            # determine whether a player # button is clicked
            for outerNumButton in playerButtons:
                if outerNumButton.clicked(p):
                    # activate all player buttons...
                    for innerNumButton in playerButtons:
                        innerNumButton.activate()
                    # deactivate button just clicked
                    outerNumButton.deactivate()
            # if start button is clicked
            if startButton.clicked(p):
                # loop through player buttons
                for numPlayers in range(3):
                    # if a player button is deactivated, it holds the # of players
                    if playerButtons[numPlayers].isDeactivated():
                        # close start page
                        startPage.close()
                        # create an oops application with specified # of players
                        oops = OopsApp(numPlayers+2)
                        # commence oops game, get which player won
                        winner = oops.game()
                        # denote that start button has been pressed to get out of loop
                        startPressed = True

        if winner is not None:  # if game finished with a player winning
            # create end page
            endPage = GraphWin("", 500, 500)
            endPage.setCoords(0, 0, 100, 100)
            endPage.setBackground("antiquewhite")

            # create label indicating which player won
            if winner == 1:
                endLabel = Text(Point(50, 50), "{0} Wins!".format("Yellow"))
                endLabel.setTextColor("gold")
            elif winner == 2:
                endLabel = Text(Point(50, 50), "{0} Wins!".format("Green"))
                endLabel.setTextColor("green")
            elif winner == 3:
                endLabel = Text(Point(50, 50), "{0} Wins!".format("Red"))
                endLabel.setTextColor("red")
            else:  # winner == 4
                endLabel = Text(Point(50, 50), "{0} Wins!".format("Blue"))
                endLabel.setTextColor("blue")
            # stylize label
            endLabel.setSize(50)
            endLabel.setStyle("bold")
            endLabel.draw(endPage)

            # pause for 5 seconds
            time.sleep(5)

            # close end page
            endPage.close()


if __name__ == "__main__":
    Start()

