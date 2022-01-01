# player.py

from pawn import Pawn
from graphics import *


class Player:
    """ Creates Oops! player """

    def __init__(self, whichPlayer, deck, interface):
        """" Initializes player's attributes; must input interface """

        # initialize number of pawns
        self.NUMBER_OF_PAWNS = 4
        # initialize home location
        self.HOME_LOCATION = 65
        # initialize weird spot locationS
        self.WEIRD_LOCATIONS = [-1, 66]
        # initialize start location
        self.START_LOCATION = 0

        # denote which player
        self.player = whichPlayer

        # create deck
        self.deck = deck

        # initialize interface
        self.interface = interface

        # initialize quit button and forfeit button
        self.quit = self.interface.getQuit()
        self.forfeit = self.interface.getForfeit()

        # initialize oops window
        self.oopsWindow = self.interface.getWindow()

        # initialize draw card
        self.drawCard = None

        # create list of pawns
        self.pawns = []
        for i in range(self.NUMBER_OF_PAWNS):
            self.pawns.append(Pawn(self.player, i + 1))

    def doTurn(self, playerBoards, pawns):
        """ Player does turn """

        # activate draw card button
        self.drawCard = self.interface.getDrawCard()
        if self.player == 1:
            self.drawCard.color("yellow")
        elif self.player == 2:
            self.drawCard.color("lightgreen")
        elif self.player == 3:
            self.drawCard.color("pink")
        else:  # self.whichPlayer == 4:
            self.drawCard.color("lightblue")
        self.drawCard.activate()

        # activate quit button
        self.quit.activate()

        while True:
            # get a mouse click
            p = self.oopsWindow.checkMouse()

            if p and (self.drawCard.clicked(p) or self.quit.clicked(p)):

                if self.quit.clicked(p):  # if quit button clicked
                    return "quit"  # tell oopsApp user quit

                # deactivate draw card
                self.drawCard.deactivate()
                # draw card
                card = self.deck.draw()

                # deactivate quit button
                self.quit.deactivate()

                # determine what to do based on the card
                if card == 1:
                    self.__showCard(1)  # show card
                    self.__implementCard(1, playerBoards, pawns)  # implement card
                    break  # get out of while loop
                elif card == 2:
                    self.__showCard(2)
                    self.__implementCard(2, playerBoards, pawns)
                    # undraw card
                    self.Crect.undraw()
                    self.Ctext.undraw()
                    return "2"  # repeat turn
                elif card == 3:
                    self.__showCard(3)
                    self.__implementCard(3, playerBoards, pawns)
                    break
                elif card == 4:
                    self.__showCard(4)
                    self.__implementCard(4, playerBoards, pawns)
                    break
                elif card == 5:
                    self.__showCard(5)
                    self.__implementCard(5, playerBoards, pawns)
                    break
                elif card == 7:
                    self.__showCard(7)
                    self.__implementCard(7, playerBoards, pawns)
                    break  # get out of while loop
                elif card == 8:
                    self.__showCard(8)
                    self.__implementCard(8, playerBoards, pawns)
                    break
                elif card == 10:
                    self.__showCard(10)
                    self.__implementCard(10, playerBoards, pawns)
                    break
                elif card == 11:
                    self.__showCard(11)
                    self.__implementCard(11, playerBoards, pawns)
                    break
                elif card == 12:
                    self.__showCard(12)
                    self.__implementCard(12, playerBoards, pawns)
                    break
                else:  # card == "Oops!"
                    self.__showCard("Oops!")
                    self.__implementCard("Oops!", playerBoards, pawns)
                    break

        # undraw card
        self.Crect.undraw()
        self.Ctext.undraw()

    def __implementCard(self, cardNum, playerBoards, pawns):
        """ This method performs necessary actions for a given cardNum """

        # record list of player's pawns
        pPawns = pawns[self.player - 1]
        # record player's board
        playerBoard = playerBoards[self.player - 1]

        # initialize list of activated start/squares/home
        #   in some scenarios, activatedButtons contains other relevant information
        activatedButtons = []

        # make sure forfeit is deactivated
        self.forfeit.deactivate()

        # initialize boolean indicating whether turn is over
        toBreak = False
        # initialize counter
        counter = 0

        if cardNum == 1:
            # initialize pawn index
            pawnIndex = 0
            # activate appropriate pawns & places
            for pos in self.getPawnPositions():
                if pos == self.START_LOCATION:
                    if pos+1 not in self.getPawnPositions():
                        # activate home button
                        playerBoard[self.START_LOCATION].activate()
                        activatedButtons.append([pPawns[pawnIndex], playerBoard[self.START_LOCATION]])
                elif pos != self.HOME_LOCATION:
                    if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        newPos = 1  # square after start
                    else:
                        newPos = pos + 1
                    if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                        # activate button after pawn
                        playerBoard[newPos].activate()
                        # activatedButtons elements are (pawn, new board location)
                        activatedButtons.append([pPawns[pawnIndex], playerBoard[newPos]])
                # increment pawnIndex
                pawnIndex += 1

            # if user can't do anything
            if len(activatedButtons) == 0:
                # activate forfeit button
                self.forfeit.activate()

            # get user input
            while True:
                p = self.oopsWindow.checkMouse()
                # forfeit turn is so chosen by user
                if p and self.forfeit.clicked(p):
                    # deactivate appropriate pawns & places
                    for but in activatedButtons:
                        but[1].deactivate()
                    break  # get out of while true loop
                for place in range(len(playerBoard)):  # loop through player board
                    if p and playerBoard[place].clicked(p):  # if pos clicked
                        for button in activatedButtons:  # iterate through (pawn, place) pairs
                            if place == playerBoard.index(button[1]):  # if place is clicked
                                # move appropriate pawn
                                button[0].move(1, playerBoards, pawns)
                                toBreak = True
                                break  # get out of for pawn loop
                        break  # get out of for place loop
                if toBreak:
                    # deactivate appropriate pawns & places
                    for but in activatedButtons:
                        but[1].deactivate()
                    break  # get out of while true loop
        elif cardNum == 2:
            # initialize pawn index
            pawnIndex = 0
            # activate appropriate pawns & places
            for pos in self.getPawnPositions():
                if pos == self.START_LOCATION:
                    if pos + 1 not in self.getPawnPositions():
                        # activate home button
                        playerBoard[self.START_LOCATION].activate()
                        activatedButtons.append([pPawns[pawnIndex], playerBoard[self.START_LOCATION]])
                elif pos not in [64, self.HOME_LOCATION]:
                    if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        newPos = 2
                    else:
                        newPos = pos + 2
                    if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                        # activate button after pawn
                        playerBoard[newPos].activate()
                        # activatedButtons elements are (pawn, new board location)
                        activatedButtons.append([pPawns[pawnIndex], playerBoard[newPos]])
                # increment pawnIndex
                pawnIndex += 1

            # if user can't do anything
            if len(activatedButtons) == 0:
                # activate forfeit button
                self.forfeit.activate()

            # get user input
            while True:
                p = self.oopsWindow.checkMouse()
                # forfeit turn is so chosen by user
                if p and self.forfeit.clicked(p):
                    # deactivate appropriate pawns & places
                    for but in activatedButtons:
                        but[1].deactivate()
                    break  # get out of while loop

                for place in range(len(playerBoard)):  # loop through player board
                    if p and playerBoard[place].clicked(p):  # if pos clicked
                        for button in activatedButtons:  # iterate through (pawn, place) pairs
                            if place == playerBoard.index(button[1]):  # if place is clicked
                                if place == self.START_LOCATION:
                                    # move appropriate pawn
                                    button[0].move(1, playerBoards, pawns)
                                    toBreak = True
                                    break  # get out of for pawn loop
                                else:
                                    # move appropriate pawn
                                    button[0].move(2, playerBoards, pawns)
                                    toBreak = True
                                    break  # get out of for pawn loop
                        break  # get out of for place loop
                if toBreak:
                    # deactivate appropriate pawns & places
                    for but in activatedButtons:
                        but[1].deactivate()
                    break  # get out of while loop
        elif cardNum == 3:
            # simple implementation
            self.__implementSimpleCard(3, playerBoards, pawns)
        elif cardNum == 4:
            # activate appropriate pawns & places
            for pos in self.getPawnPositions():
                if pos in [1, 2, 3]:
                    if pos + 56 not in self.getPawnPositions():
                        playerBoard[pos + 56].activate()
                        # activatedButtons stores pairs of (pawn, corresponding activated place, offset)
                        activatedButtons.append([pPawns[counter],
                                                 playerBoard[pos + 56], -4])
                elif pos == 4:
                    if -1 not in self.getPawnPositions():  # -1 is weird spot
                        # activate weird spot
                        playerBoard[-1].activate()
                        activatedButtons.append([pPawns[counter],
                                                 playerBoard[-1], -4])
                elif pos == -1:  # if pos is weird spot
                    if 56 not in self.getPawnPositions():
                        # activate place 56
                        playerBoard[56].activate()
                        activatedButtons.append([pPawns[counter],
                                                playerBoard[56], -4])
                else:
                    if pos != self.START_LOCATION and pos != self.HOME_LOCATION:
                        if pos - 4 not in self.getPawnPositions():
                            playerBoard[pos - 4].activate()
                            activatedButtons.append([pPawns[counter],
                                                     playerBoard[pos - 4], -4])
                counter = counter + 1  # increment counter

            # if user can't do anything
            if len(activatedButtons) == 0:
                # activate forfeit button
                self.forfeit.activate()

            # get user input
            self.__ambiguousUserInput(playerBoards, pawns, activatedButtons)

        elif cardNum == 5:
            # simple implementation
            self.__implementSimpleCard(5, playerBoards, pawns)
        elif cardNum == 7:
            # initialize pawnIndex counter
            pawnIndex = 0
            # initialize list of active pawns
            activePawns = []
            for pos in self.getPawnPositions():  # iterate through player's pawns' positions
                if pos not in [self.START_LOCATION, self.HOME_LOCATION]:  # if pawn in "play area"
                    # add to activePawns
                    activePawns.append(pPawns[pawnIndex])
                # increment pawn index
                pawnIndex = pawnIndex + 1
            if len(activePawns) <= 1:  # if there's one or fewer active pawns
                # simple implementation
                self.__implementSimpleCard(7, playerBoards, pawns)
            elif len(activePawns) > 1:  # if there's more than one active pawn
                squaresLeft = 7  # initialize squaresLeft to 7
                pawnsMoved = []  # initialize list of pawns already moved

                while len(pawnsMoved) < 2:  # while user hasn't already moved two pawns
                    # if user moved first pawn by 7
                    if squaresLeft == 0:
                        break  # exit while loop
                    activatedButtons = []  # reset activated buttons

                    # if I've already moved a pawn
                    if len(pawnsMoved) == 1:
                        # initialize pawnIndex counter
                        pawnIndex = 0
                        # activate appropriate pawns & places
                        for pos in self.getPawnPositions():
                            if (pos not in ([self.START_LOCATION] + list(range(self.HOME_LOCATION - squaresLeft + 1,
                                                                               self.HOME_LOCATION + 1))) and
                                    pPawns[pawnIndex] not in pawnsMoved):
                                if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                                    newPos = squaresLeft
                                else:
                                    newPos = pos + squaresLeft
                                if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                                    # activate newPos - pos positions after pawn
                                    playerBoard[newPos].activate()
                                    activatedButtons.append([pPawns[pawnIndex], playerBoard[newPos]])
                            # increment pawn index
                            pawnIndex = pawnIndex + 1
                        # get user input
                        self.__simpleUserInput(squaresLeft, playerBoards, pawns, activatedButtons)
                        # break from while loop
                        break
                    else:
                        # initialize pawnIndex
                        pawnIndex = 0
                        # activate appropriate places
                        for pos in self.getPawnPositions():
                            # make sure position is not start, home
                            if pos != self.START_LOCATION and pos != self.HOME_LOCATION:
                                for offset in range(1, squaresLeft + 1):
                                    if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                                        newPos = offset
                                    else:
                                        newPos = pos + offset
                                    # make sure we're moving pawn within board and
                                    #   not onto another pawn of the same team
                                    if (newPos <= self.HOME_LOCATION and (newPos == self.HOME_LOCATION or
                                                                          newPos not in self.getPawnPositions())):
                                        # make sure user isn't in an impossible
                                        #   situation (i.e., user can only move one more pawn and
                                        #   but all places are occupied)
                                        if self.__canMoveFirstWith7(pPawns[pawnIndex], offset):
                                            # activate board place
                                            playerBoard[newPos].activate()
                                            # add (pawn, place, offset) to activatedButtons
                                            activatedButtons.append([pPawns[pawnIndex],
                                                                     playerBoard[newPos], offset])
                            pawnIndex = pawnIndex + 1  # increment counter

                        # if user can't do anything
                        if len(activatedButtons) == 0:
                            # activate forfeit button
                            self.forfeit.activate()

                        # get user click
                        p = self.oopsWindow.checkMouse()
                        # forfeit turn if so chosen by user; and if no pawn moved already
                        if p and self.forfeit.clicked(p):
                            # deactivate appropriate pawns & places
                            for but in activatedButtons:
                                but[1].deactivate()
                            break  # get out of while loop
                        for button in activatedButtons:  # loop through player board
                            if p and button[1].clicked(p):  # if pos clicked
                                implicatedPawns = []  # initialize list of which pawns are implicated
                                otherButs = []  # initialize list of other buttons
                                for otherBut in activatedButtons:  # determine # of pawns button[1] corresponds to
                                    if (otherBut[1].getCenter().getX() == button[1].getCenter().getX() and
                                            otherBut[1].getCenter().getY() == button[1].getCenter().getY()):
                                        implicatedPawns.append(otherBut[0].getPawnNumber())
                                        otherButs.append(otherBut)
                                if len(implicatedPawns) == 1:  # if only one pawn corresponds to but[1]
                                    # move appropriate pawn by offset
                                    button[0].move(button[2], playerBoards, pawns)
                                    # update pawn positions
                                    self.__updatePawnPositions(pawns)
                                    # update squaresLeft
                                    squaresLeft = squaresLeft - button[2]
                                    # update pawnsMoved
                                    pawnsMoved.append(button[0])
                                    # deactivate appropriate buttons
                                    for but in activatedButtons:
                                        but[1].deactivate()
                                    break  # get out of for button loop
                                else:  # if more than one pawn corresponds to but[1]
                                    # deactivate all but clicked button
                                    for innerButton in activatedButtons:
                                        if innerButton[1] != button[1]:
                                            innerButton[1].deactivate()
                                    # activate appropriate pawns
                                    for pawnNum in implicatedPawns:
                                        pPawns[pawnNum - 1].getPawnBut().activate()
                                    # get user input
                                    while True:
                                        point = self.oopsWindow.checkMouse()
                                        # iterate through implicated pawn numbers
                                        for pawnNum in implicatedPawns:
                                            # if pawn is clicked
                                            if p and pPawns[pawnNum - 1].getPawnBut().clicked(point):
                                                # loop through implicated (pawn, button, offset) 3-tuples
                                                for otherB in otherButs:
                                                    # if corresponding pawn's # is pawnNum
                                                    if otherB[0].getPawnNumber() == pawnNum:
                                                        # move corresponding pawn by offset
                                                        pPawns[pawnNum - 1].move(otherB[2], playerBoards, pawns)
                                                        # update pawn positions
                                                        self.__updatePawnPositions(pawns)
                                                        # update pawnsMoved
                                                        pawnsMoved.append(pPawns[pawnNum - 1])
                                                        # update squares left
                                                        squaresLeft = squaresLeft - otherB[2]
                                                # flip toBreak boolean flag
                                                toBreak = True
                                                # deactivate appropriate buttons
                                                for but in activatedButtons:
                                                    but[1].deactivate()
                                                break  # break from for pawnNum loop
                                        if toBreak:
                                            break  # break from while loop
                                break  # break from for button loop
        elif cardNum == 8:
            # simple implementation
            self.__implementSimpleCard(8, playerBoards, pawns)
        elif cardNum == 10:
            # activate appropriate pawns & places
            for pos in self.getPawnPositions():
                if pos not in [self.START_LOCATION, 56, 57, 58, 59, 60, 61, 62, 63, 64, self.HOME_LOCATION]:
                    if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        newPos = 10
                    else:
                        newPos = pos + 10
                    if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                        # activate ten positions after pawn
                        playerBoard[newPos].activate()
                        # activatedButtons consists of 3-tuples: (pawn, activated board spot, offset)
                        activatedButtons.append([pPawns[counter], playerBoard[newPos], 10])
                if pos not in [self.START_LOCATION, self.HOME_LOCATION]:
                    if pos == 1:  # if pawn is on position after start
                        if -1 not in self.getPawnPositions():
                            # activate "the weird spot"
                            playerBoard[-1].activate()
                            activatedButtons.append([pPawns[counter], playerBoard[-1], -1])
                    elif pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        if 59 not in self.getPawnPositions():
                            # activate place 59
                            playerBoard[59].activate()
                            activatedButtons.append([pPawns[counter], playerBoard[59], -1])
                    else:
                        if pos - 1 not in self.getPawnPositions():
                            # activate position before pawn
                            playerBoard[pos - 1].activate()
                            activatedButtons.append([pPawns[counter], playerBoard[pos - 1], -1])
                counter = counter + 1  # increment counter

            # if user can't do anything
            if len(activatedButtons) == 0:
                # activate forfeit button
                self.forfeit.activate()

            # get user input
            self.__ambiguousUserInput(playerBoards, pawns, activatedButtons)

        elif cardNum == 11:
            # initialize boolean for whether there's an activated pawn
            isActivePawn = False

            for pos in self.getPawnPositions():  # iterate through player's pawns' positions
                if pos not in [self.START_LOCATION, 60, 61,
                               62, 63, 64, self.HOME_LOCATION]:  # if pawn in "play area"
                    # flip boolean flag
                    isActivePawn = True
                    if pos not in [self.START_LOCATION, 55, 56, 57, 58, 59]:  # if pawn can move 11
                        if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                            newPos = 11  # add an extra space
                        else:
                            newPos = pos + 11
                        # ensure we don't indicate that user can move pawn on top of
                        #      another same-team pawn
                        if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                            # activate 11 positions after pawn
                            playerBoard[newPos].activate()
                            activatedButtons.append(playerBoard[newPos])

            # if user can't move pawn 11
            if len(activatedButtons) == 0:
                # activate forfeit button
                self.forfeit.activate()

            # activate other players' pawns if player has an active pawn
            if isActivePawn:
                activatedButtons = self.__activateOtherPawns(pawns, activatedButtons)

            # get user input
            while True:
                p = self.oopsWindow.checkMouse()
                # forfeit turn if so chosen by user
                if p and self.forfeit.clicked(p):
                    # deactivate appropriate pawns & places
                    for but in activatedButtons:
                        but.deactivate()
                    break  # exit while true loop

                # determine whether user wants to swap
                for playerIndex in range(len(playerBoards)):  # iterate through each player index
                    for pawn in pawns[playerIndex]:  # loop through each player's pawns
                        if pawn.getPawnBut().clicked(p):
                            # flip boolean flag
                            toBreak = True
                            # deactivate appropriate pawns & places
                            for but in activatedButtons:
                                but.deactivate()
                            # activate players' active pawns
                            for ourPawn in pPawns:
                                if ourPawn.getPosition() not in [self.START_LOCATION, self.HOME_LOCATION,
                                                                 64, 63, 62, 61, 60]:
                                    ourPawn.getPawnBut().activate()
                            # initialize boolean flag for if user picked a pawn to swap
                            pickedPawn = False
                            # initialize variable for pawn to swap
                            toSwap = None
                            while True:
                                # get user click
                                point = self.oopsWindow.checkMouse()
                                for ourPawn in pPawns:  # loop through our pawns
                                    if ourPawn.getPawnBut().clicked(point):
                                        # record pawn user picked to swap
                                        toSwap = ourPawn
                                        # flip boolean flag
                                        pickedPawn = True
                                        break  # exit for ourPawn loop
                                if pickedPawn:  # if use picked a pawn
                                    # swap toSwap with [playerIndex + 1, pawn.getPawnNumber()]
                                    toSwap.swap([playerIndex + 1, pawn.getPawnNumber()],
                                                playerBoards, "11", pawns)
                                    break  # break from inner while true loop
                        if toBreak:
                            # deactivate appropriate pawns
                            for activePawn in pPawns:
                                activePawn.getPawnBut().deactivate()
                            break  # break from for pawn loop
                    if toBreak:
                        break  # break from for playerIndex loop

                # determine whether player wants to move 11
                for place in range(len(playerBoard)):  # loop through player board
                    if p and playerBoard[place].clicked(p):  # if pos clicked
                        # move appropriate pawn
                        for pawn in pPawns:
                            if pawn.getPosition() + 11 == place:
                                pawn.move(11, playerBoards, pawns)
                                toBreak = True
                                break  # get out of for pawn loop
                        break  # get out of for place loop

                if toBreak:
                    # deactivate appropriate pawns & places
                    for but in activatedButtons:
                        but.deactivate()
                    break  # get out of while true loop

        elif cardNum == 12:
            # simple implementation
            self.__implementSimpleCard(12, playerBoards, pawns)
        else:  # cardNum == "Oops!"
            # initialize boolean flag indicating whether there's a pawn in start
            pawnInStart = False
            # initialize counter representing pawn index
            pawnIndex = 0
            # initialize variable for this player's pawn to swap
            toSwap = None
            for pos in self.getPawnPositions():
                if pos == self.START_LOCATION:  # if pawn position is 0
                    # set ourPawn to this pawn in start
                    toSwap = pPawns[pawnIndex]
                    # flip boolean flag
                    pawnInStart = True
                    break  # exit for pos loop
                pawnIndex = pawnIndex + 1  # increment pawnIndex
            if pawnInStart:
                # activate buttons corresponding to other players' active pawns
                activatedButtons = self.__activateOtherPawns(pawns, activatedButtons)

            # if user can't do anything
            if len(activatedButtons) == 0:
                # activate forfeit button
                self.forfeit.activate()

            # get user input
            while True:
                p = self.oopsWindow.checkMouse()
                # forfeit turn if so chosen by user
                if p and self.forfeit.clicked(p):
                    # deactivate appropriate pawns & places
                    for but in activatedButtons:
                        but.deactivate()
                    break  # exit while true loop
                # determine whether user wants to swap
                for playerIndex in range(len(playerBoards)):  # loop through player indices
                    for pawn in pawns[playerIndex]:  # loop through given player's pawns
                        if pawn.getPawnBut().clicked(p):  # if pawn button is clicked
                            toBreak = True  # flip boolean flag
                            # deactivate appropriate pawns & places
                            for but in activatedButtons:
                                but.deactivate()
                            # swap this player's pawn in start with other player's clicked-on pawn
                            toSwap.swap([playerIndex + 1, pawn.getPawnNumber()], playerBoards, "Oops!", pawns)
                            break  # exit for pawn loop
                    if toBreak:
                        break  # exit for playerIndex loop
                if toBreak:
                    break  # exit while true loop
        # deactivate forfeit
        self.forfeit.deactivate()

    def __canMoveFirstWith7(self, pawnToMove, amountToMove):
        """ This method returns a boolean indicating whether a user can move pawnToMove by amountToMove
            as the first move after drawing Card 7. That is, it determines whether any active pawn other
            than pawnToMove can move by 7 - amountToMove after the first move. """

        # denote slider positions
        self.SLIDER1_3 = 13
        self.SLIDER2_3 = 28
        self.SLIDER3_3 = 43
        self.SLIDER1_4 = 21
        self.SLIDER2_4 = 36
        self.SLIDER3_4 = 51

        if amountToMove == 7:  # if user moves pawnToMove by 7
            # don't need to worry about moving another pawn, so return true
            return True
        else:
            # initialize boolean flag for whether this pawn can move a certain amount
            canMove = False
            # initialize variable representing required amount for second move
            amountSecondMove = 7 - amountToMove
            # initialize pawnToMove's new position
            if pawnToMove.getPosition() in self.WEIRD_LOCATIONS:
                # add an extra space
                newPawnPos = amountToMove
            else:
                newPawnPos = pawnToMove.getPosition() + amountToMove

            # create player's pawn positions excluding pawn moved
            otherPawnPositions = []
            for pos in self.getPawnPositions():
                if pos != pawnToMove.getPosition():
                    otherPawnPositions.append(pos)

            # if pawnToMove lands on the beginning of a length-3 slider
            if newPawnPos in [self.SLIDER1_3, self.SLIDER2_3, self.SLIDER3_3]:
                # increment newPawnPos by 3
                newPawnPos += 3
                # iterate through other pawn positions
                for pos in otherPawnPositions:
                    # if position is on slider
                    if newPawnPos - 3 < pos <= newPawnPos:
                        # remove position from otherPawnPositions
                        otherPawnPositions.remove(pos)

            # if pawnMoved lands on the beginning of a length-4 slider
            elif newPawnPos in [self.SLIDER1_4, self.SLIDER2_4, self.SLIDER3_4]:
                # increment newPawnPos by 4
                newPawnPos += 4
                # iterate through other pawn positions
                for pos in otherPawnPositions:
                    # if position is on slider
                    if newPawnPos - 4 < pos <= newPawnPos:
                        # remove position from otherPawnPositions
                        otherPawnPositions.remove(pos)

            # loop through pawn positions
            for pos in otherPawnPositions:
                if pos not in ([self.START_LOCATION] +
                               list(range(self.HOME_LOCATION - amountSecondMove + 1,
                                          self.HOME_LOCATION + 1))):  # if position viable
                    if pos in self.WEIRD_LOCATIONS:  # if pos is weird spot
                        if (amountSecondMove not in otherPawnPositions and
                                amountSecondMove != newPawnPos):  # add extra space
                            # flip boolean flag
                            canMove = True
                            break  # exit for pos loop
                    else:
                        if (pos + amountSecondMove not in otherPawnPositions and
                                pos + amountSecondMove != newPawnPos):
                            # flip boolean flag
                            canMove = True
                            break  # exit for pos loop

            return canMove

    def __implementSimpleCard(self, cardNum, playerBoards, pawns):
        """ This method performs necessary actions in the most simple (yet most
            common) scenarios. """

        # initialize activated buttons
        activatedButtons = []
        # initialize player board
        playerBoard = playerBoards[self.player-1]
        # initialize pawnIndex
        pawnIndex = 0
        # activate appropriate pawns & places
        for pos in self.getPawnPositions():
            if pos not in ([self.START_LOCATION] + list(range(self.HOME_LOCATION - cardNum + 1,
                                                              self.HOME_LOCATION + 1))):
                if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                    newPos = cardNum
                else:
                    newPos = pos + cardNum
                if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                    # activate cardNum positions after pawn
                    playerBoard[newPos].activate()
                    activatedButtons.append([pawns[self.player-1][pawnIndex], playerBoard[newPos]])
            # increment pawnIndex
            pawnIndex += 1

        # if user can't do anything
        if len(activatedButtons) == 0:
            # activate forfeit button
            self.forfeit.activate()

        # get user input
        self.__simpleUserInput(cardNum, playerBoards, pawns, activatedButtons)

    def __simpleUserInput(self, cardNum, playerBoards, pawns, activatedButtons):
        """ This method implements getting and acting on user input within a
            simple move scenario. """

        # initialize boolean flag for when user completes turn
        toBreak = False
        # initialize player board
        playerBoard = playerBoards[self.player - 1]
        while True:
            p = self.oopsWindow.checkMouse()

            # forfeit turn is so chosen by user
            if p and self.forfeit.clicked(p):
                # deactivate appropriate pawns & places
                for but in activatedButtons:
                    but[1].deactivate()
                break  # get out of while loop

            for place in range(len(playerBoard)):  # loop through player board
                if p and playerBoard[place].clicked(p):  # if pos clicked
                    for button in activatedButtons:  # iterate through (pawn, place) pairs
                        if place == playerBoard.index(button[1]):  # if place is clicked
                            # move appropriate pawn
                            button[0].move(cardNum, playerBoards, pawns)
                            toBreak = True
                            break  # get out of for pawn loop
                    break  # get out of for place loop

            if toBreak:
                # deactivate appropriate pawns & places
                for but in activatedButtons:
                    but[1].deactivate()
                break  # get out of while loop

    def __ambiguousUserInput(self, playerBoards, pawns, activatedButtons):
        """ This method implements getting and acting on user input within a
            move scenario in which the pawn that the user wants to move is
            potentially ambiguous. """

        # initialize boolean indicating whether user completed turn
        toBreak = False

        while True:
            # get user click
            p = self.oopsWindow.checkMouse()
            # forfeit turn if so chosen by user
            if p and self.forfeit.clicked(p):
                # deactivate appropriate pawns & places
                for but in activatedButtons:
                    but[1].deactivate()
                break  # get out of while true loop
            for but in activatedButtons:  # loop through activated buttons
                if p and but[1].clicked(p):  # if button clicked
                    implicatedButs = []  # initialize list of which buttons are implicated
                    for otherBut in activatedButtons:  # determine # of pawns but[1] corresponds to
                        if otherBut[1] == but[1]:
                            implicatedButs.append(otherBut)
                    if len(implicatedButs) == 1:  # if only one pawn corresponds to but[1]
                        # move appropriate pawn
                        but[0].move(but[2], playerBoards, pawns)
                        toBreak = True  # flip boolean flag
                        break  # exit for but loop
                    else:  # if more than one pawn corresponds to but[1]
                        # deactivate all but clicked button
                        for otherBut in activatedButtons:
                            if otherBut not in implicatedButs:
                                otherBut[1].deactivate()
                        # activate appropriate pawns
                        for impBut in implicatedButs:
                            impBut[0].getPawnBut().activate()
                        while True:
                            # get user click
                            point = self.oopsWindow.checkMouse()
                            for aButton in implicatedButs:  # loop through implicated
                                #                   (pawn, board spot, offset) 3-tuples
                                # if associated pawn is clicked
                                if p and aButton[0].getPawnBut().clicked(point):
                                    # move that pawn by offset
                                    aButton[0].move(aButton[2], playerBoards, pawns)
                                    toBreak = True  # flip boolean flag
                                    break  # break from for aButton loop
                            if toBreak:
                                break  # break from inner while true loop
                    break  # break from for but loop
            if toBreak:
                # deactivate appropriate pawns & places
                for but in activatedButtons:
                    but[1].deactivate()
                break  # break from outer while true loop

    def __showCard(self, card):
        """ Helper function that graphically displays card drawn """

        # create card outline
        rect = Rectangle(Point(45, 40), Point(55, 50))
        rect.setWidth(6)
        if self.player == 1:
            rect.setFill("yellow")
        elif self.player == 2:
            rect.setFill("lightgreen")
        elif self.player == 3:
            rect.setFill("pink")
        else:  # whichPlayer == 4:
            rect.setFill("lightblue")
        # draw card outline
        rect.draw(self.oopsWindow)

        # create text
        text = Text(rect.getCenter(), "{0}".format(card))
        text.setStyle("bold")
        if card == "Oops!":
            text.setSize(36)
        else:
            text.setSize(50)
        # draw text
        text.draw(self.oopsWindow)

        # create instance variables to undraw
        self.Crect = rect
        self.Ctext = text

    def __updatePawnPositions(self, pawns):
        """ This method updates pawnPositions and moves pawns accordingly on
            graphical interface.
            Input: list of each player's list of pawns """

        # initialize list of each players' list of pawn positions
        pawnPositions = []
        for player in range(len(pawns)):  # iterate through players
            newPositions = []  # initialize player's list of pawn positions
            for pawn in range(self.NUMBER_OF_PAWNS):  # iterate through pawns
                # append to new pawn positions of player
                newPositions.append(pawns[player][pawn].getPosition())
            # append to new list of players' pawn positions
            pawnPositions.append(newPositions)
        self.interface.movePawns(pawns)  # update pawns graphically

    def __activateOtherPawns(self, pawns, activatedButtons):
        """ This helper method activates the buttons corresponding to each
            other player's active pawns. It returns an updated list of currently
            activated buttons.
            Input: pawns - list of each player's list of pawns
                   activatedButtons - list of currently activated buttons
                                      on Oops! board """

        for player in range(len(pawns)):  # loop through other players
            if player + 1 != self.player:  # if other player isn't our player
                for pawn in pawns[player]:  # loop through other player's pawns
                    # if pawn is active
                    if pawn.getPosition() not in [self.START_LOCATION, self.HOME_LOCATION,
                                                  64, 63, 62, 61, 60]:
                        # activate pawn
                        pawn.getPawnBut().activate()
                        activatedButtons.append(pawn.getPawnBut())

        return activatedButtons

    def getPawnPositions(self):
        """ Returns list of player's pawn positions """

        # create list of the player's pawn positions
        pawnPositions = []
        for pawn in self.pawns:
            pawnPositions.append(pawn.getPosition())
        return pawnPositions

    def getPawns(self):
        """ Returns list of player's pawns """
        return self.pawns