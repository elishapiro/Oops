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
        self.startPage = GraphWin("", 500, 500)
        self.startPage.setCoords(0, 0, 100, 100)
        self.startPage.setBackground("antiquewhite")

        # create welcome label
        welcomeLabel = Text(Point(50, 90), "Welcome to Oops!")
        welcomeLabel.setSize(36)
        welcomeLabel.setTextColor("black")
        welcomeLabel.setStyle("bold")
        welcomeLabel.draw(self.startPage)

        # create label for number of players
        numPlayers = Text(Point(50, 80), "How many players?")
        numPlayers.setSize(20)
        numPlayers.setTextColor("black")
        numPlayers.setStyle("bold")
        numPlayers.draw(self.startPage)

        # create buttons for number of players
        playerButtons = []  # initialize buttons list
        center = Point(30, 65)  # initialize button center
        for numPlayers in range(2, self.MAX_NUM_PLAYERS + 1):
            # create button
            playNumButton = SquareButton(self.startPage, center, 20, 20, "{0}".format(numPlayers))

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
            p = self.startPage.getMouse()
            # determine whether a button is clicked
            for button in playerButtons:
                if button.clicked(p):
                    button.deactivate()
                    butPressed = True

        # create start button
        startButton = SquareButton(self.startPage, Point(50, 10), 80, 15, "Start")
        startButton.color("antiquewhite")
        startButton.setLabelStyle("bold")
        startButton.setLabelSize(20)
        startButton.activate()

        # get the number of players that the user has chosen
        numPlayers = self.getChosenNum(playerButtons)

        # denote each relevant player on start page
        playersText = self.denotePlayers(numPlayers, [])

        # denote button allowing user to determine if player is CPU (one for
        #   each player) on start page
        CPUButtons = self.denoteCPUs(numPlayers, [])

        # initialize boolean for if user has pressed startButton
        startPressed = False
        # wait for user to press start button
        while not startPressed:
            # check for mouse click
            p = self.startPage.getMouse()
            # determine whether a player # button is clicked
            for outerNumButton in playerButtons:
                if outerNumButton.clicked(p):
                    # activate all player buttons...
                    for innerNumButton in playerButtons:
                        innerNumButton.activate()
                    # deactivate button just clicked
                    outerNumButton.deactivate()

            # determine number of players
            numPlayers = self.getChosenNum(playerButtons)
            # denote each relevant player on start page
            playersText = self.denotePlayers(numPlayers, playersText)
            # denote button allowing user to determine if player is CPU (one for
            #   each player) on start page
            CPUButtons = self.denoteCPUs(numPlayers, CPUButtons)

            for CBut in CPUButtons:  # loop through CPU buttons
                if CBut.clickedActiveOrNot(p):  # if button is clicked
                    if CBut.isDeactivated():  # if CBut is deactivated
                        # activate CBut
                        CBut.activate()
                    else:  # if CBut is activated
                        # deactivate CBut
                        CBut.deactivate()

            # if start button is clicked
            if startButton.clicked(p):
                # initialize list of booleans indicating which players are CPUs
                isCPU = []
                for button in CPUButtons:  # loop through CPUButtons
                    if button.isDeactivated():  # if button is deactivated
                        isCPU.append(True)  # it's clicked, so player is CPU
                    else:
                        isCPU.append(False)  # otherwise, player is human

                # close start page
                self.startPage.close()
                # create an oops application with specified # of human/CPU players
                oops = OopsApp(numPlayers, isCPU)
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

    def getChosenNum(self, playerButtons):
        """ Helper method that gets the user's chosen quantity of players """

        # initialize numPlayers
        numPlayers = 0

        for index in range(3):  # loop through player buttons
            # if a player button is deactivated, it holds the # of players
            if playerButtons[index].isDeactivated():
                numPlayers = index + 2
                break

        return numPlayers

    def denotePlayers(self, numPlayers, playersText):
        """ Helper method that resets the textual display of each player on
            start page. """

        if numPlayers > len(playersText):  # if increase in number of players
            # determine center of next player text
            if len(playersText) == 0:
                textCenter = Point(20, 46)
            elif len(playersText) == 1:
                textCenter = Point(40, 46)
            elif len(playersText) == 2:
                textCenter = Point(60, 46)
            elif len(playersText) == 3:
                textCenter = Point(80, 46)
            # append and draw appropriate number of CPU buttons
            for playerNum in range(len(playersText), numPlayers):
                # create player text
                playerText = Text(textCenter, "Player {0}".format(playerNum + 1))
                playerText.setSize(20)
                playerText.setStyle("bold")
                # draw playerText
                playerText.draw(self.startPage)
                # add playerText
                playersText.append(playerText)
                # move center
                textCenter.move(20, 0)
        elif numPlayers < len(playersText):  # if decrease in number of players
            # undraw and remove each playerText not needed anymore
            for text in playersText[numPlayers:len(playersText)]:
                text.undraw()
                playersText.remove(text)

        return playersText

    def denoteCPUs(self, numPlayers, CPUButtons):
        """ Helper method that resets the CPU buttons of each player on
            start page. """

        if numPlayers > len(CPUButtons):  # if increase in number of players
            # determine center of next CPU button
            if len(CPUButtons) == 0:
                buttonCenter = Point(20, 32.5)
            elif len(CPUButtons) == 1:
                buttonCenter = Point(40, 32.5)
            elif len(CPUButtons) == 2:
                buttonCenter = Point(60, 32.5)
            elif len(CPUButtons) == 3:
                buttonCenter = Point(80, 32.5)
            # append and draw appropriate number of CPU buttons
            for index in range(len(CPUButtons), numPlayers):
                # create & draw button
                CPUButton = SquareButton(self.startPage, buttonCenter, 20, 20, "CPU")
                if index + 1 == 1:
                    CPUButton.color("gold")
                elif index + 1 == 2:
                    CPUButton.color("lightgreen")
                elif index + 1 == 3:
                    CPUButton.color("pink")
                elif index + 1 == 4:
                    CPUButton.color("lightblue")
                CPUButton.activate()
                CPUButton.setLabelSize(25)
                CPUButton.setLabelStyle("bold")
                # add button
                CPUButtons.append(CPUButton)
                # move center
                buttonCenter.move(20, 0)

        elif numPlayers < len(CPUButtons):  # if decrease in number of players
            # undraw and remove each button not needed anymore
            for button in CPUButtons[numPlayers:len(CPUButtons)]:
                button.undraw()
                CPUButtons.remove(button)

        return CPUButtons


if __name__ == "__main__":
    Start()

