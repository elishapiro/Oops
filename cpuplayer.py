# cpuplayer.py

import time
from player import Player
from random import randrange


class CPUPlayer(Player):
    """ CPU Oops! player """

    def __init__(self, whichPlayer, deck, interface):
        """ Initializes CPU player """
        super().__init__(whichPlayer, deck, interface)

    def doTurn(self, playerBoards, pawns):
        """ Player does turn
           Input:  playerBoards - list of each player's board
                   pawns - list of each player's list of pawns """

        # draw & display card
        self.getCard()
        card = self.deck.draw()

        # determine what to do based on the card
        if card == 1:
            self.showCard(1)  # show card
            self.__implementCard(1, playerBoards, pawns)  # implement card
        elif card == 2:
            self.showCard(2)
            self.__implementCard(2, playerBoards, pawns)
            # undraw card
            self.Crect.undraw()
            self.Ctext.undraw()
            return "2"  # repeat turn
        elif card == 3:
            self.showCard(3)
            self.__implementCard(3, playerBoards, pawns)
        elif card == 4:
            self.showCard(4)
            self.__implementCard(4, playerBoards, pawns)
        elif card == 5:
            self.showCard(5)
            self.__implementCard(5, playerBoards, pawns)
        elif card == 7:
            self.showCard(7)
            self.__implementCard(7, playerBoards, pawns)
        elif card == 8:
            self.showCard(8)
            self.__implementCard(8, playerBoards, pawns)
        elif card == 10:
            self.showCard(10)
            self.__implementCard(10, playerBoards, pawns)
        elif card == 11:
            self.showCard(11)
            self.__implementCard(11, playerBoards, pawns)
        elif card == 12:
            self.showCard(12)
            self.__implementCard(12, playerBoards, pawns)
        else:  # card == "Oops!"
            self.showCard("Oops!")
            self.__implementCard("Oops!", playerBoards, pawns)

        # undraw card
        self.Crect.undraw()
        self.Ctext.undraw()

    def __implementCard(self, cardNum, playerBoards, pawns):
        """ This method performs necessary actions for a given cardNum.
            Input: cardNum - number of card to implement
                   playerBoards - list of each player's board
                   pawns - list of each player's list of pawns """

        # wait a second
        time.sleep(1)

        # record list of player's pawns
        pPawns = pawns[self.player - 1]
        # record player's board
        playerBoard = playerBoards[self.player - 1]

        # initialize list of feasible moves
        #   the information that feasibleMoves contains is dependent on the scenario
        feasibleMoves = []

        # make sure forfeit is deactivated
        self.forfeit.deactivate()

        # initialize pawnIndex
        pawnIndex = 0

        if cardNum == 1:
            # add appropriate pawns & places to feasibleMoves
            for pos in self.getPawnPositions():
                if pos == self.START_LOCATION:
                    if pos + 1 not in self.getPawnPositions():
                        # feasibleMoves elements are (pawn, new board location)
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[self.START_LOCATION]])
                elif pos != self.HOME_LOCATION:
                    if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        newPos = 1  # square after start
                    else:
                        newPos = pos + 1
                    if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                        # feasibleMoves elements are (pawn, new board location)
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[newPos]])
                # increment pawnIndex
                pawnIndex += 1

            # if CPU can't do anything
            if len(feasibleMoves) == 0:
                # do nothing
                pass
            else:
                # make a random move
                feasibleMoves[randrange(0, len(feasibleMoves))][0].move(1, playerBoards, pawns)
        elif cardNum == 2:
            # add appropriate pawns & places to feasibleMoves
            for pos in self.getPawnPositions():
                if pos == self.START_LOCATION:
                    if pos + 1 not in self.getPawnPositions():
                        # feasibleMoves elements are (pawn, new board location, offset)
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[self.START_LOCATION], 1])
                elif pos != self.HOME_LOCATION:
                    if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        newPos = 2
                    else:
                        newPos = pos + 2
                    if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                        # feasibleMoves elements are (pawn, new board location, offset)
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[newPos], 2])
                # increment pawnIndex
                pawnIndex += 1

            # if CPU can't do anything
            if len(feasibleMoves) == 0:
                # do nothing
                pass
            else:
                # make a random move
                ranIndex = randrange(0, len(feasibleMoves))
                feasibleMoves[ranIndex][0].move(feasibleMoves[ranIndex][2], playerBoards, pawns)
        elif cardNum == 3:
            # simple implementation
            self.__implementSimpleCard(3, playerBoards, pawns)
        elif cardNum == 4:
            # activate appropriate pawns & places
            for pos in self.getPawnPositions():
                if pos in [1, 2, 3]:
                    if pos + 56 not in self.getPawnPositions():
                        # feasibleMoves stores pairs of (pawn, corresponding activated place)
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[pos + 56]])
                elif pos == 4:
                    if -1 not in self.getPawnPositions():  # -1 is weird spot
                        # add weird spot to feasibleMoves
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[-1]])
                elif pos == -1:  # if pos is weird spot
                    if 56 not in self.getPawnPositions():
                        # add place 56 to feasibleMoves
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[56]])
                else:
                    if pos != self.START_LOCATION and pos != self.HOME_LOCATION:
                        if pos - 4 not in self.getPawnPositions():
                            feasibleMoves.append([pPawns[pawnIndex], playerBoard[pos - 4]])
                pawnIndex += 1  # increment pawnIndex

            # if CPU can't do anything
            if len(feasibleMoves) == 0:
                # do nothing
                pass
            else:
                # make random move
                feasibleMoves[randrange(0, len(feasibleMoves))][0].move(-4, playerBoards, pawns)

        elif cardNum == 5:
            # simple implementation
            self.__implementSimpleCard(5, playerBoards, pawns)
        elif cardNum == 7:
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
                    feasibleMoves = []  # reset feasible moves

                    # if CPU has already moved a pawn
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
                                    # add (pawn, place) to feasibleMoves
                                    feasibleMoves.append([pPawns[pawnIndex], playerBoard[newPos]])
                            # increment pawn index
                            pawnIndex = pawnIndex + 1
                        # move random pawn
                        randomIndex = randrange(0, len(feasibleMoves))
                        feasibleMoves[randomIndex][0].move(squaresLeft, playerBoards, pawns)
                        # add appropriate pawn to pawnsMoved
                        pawnsMoved.append(feasibleMoves[randomIndex][0])
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
                                        if self.canMoveFirstWith7(pPawns[pawnIndex], offset):
                                            # add (pawn, place, offset) to feasibleMoves
                                            feasibleMoves.append([pPawns[pawnIndex], playerBoard[newPos], offset])
                            pawnIndex += pawnIndex  # increment pawnIndex

                        # if CPU can't do anything
                        if len(feasibleMoves) == 0:
                            # do nothing
                            break  # get out of while len(pawnsMoved) loop
                        else:
                            # make random move
                            randomIndex = randrange(0, len(feasibleMoves))
                            feasibleMoves[randomIndex][0].move(feasibleMoves[randomIndex][2], playerBoards, pawns)
                            # add appropriate pawn to pawnsMoved
                            pawnsMoved.append(feasibleMoves[randomIndex][0])
                            # modify squares left
                            squaresLeft = squaresLeft - feasibleMoves[randomIndex][2]
        elif cardNum == 8:
            # simple implementation
            self.__implementSimpleCard(8, playerBoards, pawns)
        elif cardNum == 10:
            # add appropriate pawns & places to feasibleMoves
            for pos in self.getPawnPositions():
                if pos not in [self.START_LOCATION, 56, 57, 58, 59, 60, 61, 62, 63, 64, self.HOME_LOCATION]:
                    if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        newPos = 10
                    else:
                        newPos = pos + 10
                    if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                        # feasibleMoves consists of 3-tuples: (pawn, activated board spot, offset)
                        feasibleMoves.append([pPawns[pawnIndex], playerBoard[newPos], 10])
                if pos not in [self.START_LOCATION, self.HOME_LOCATION]:
                    if pos == 1:  # if pawn is on position after start
                        if -1 not in self.getPawnPositions() and 66 not in self.getPawnPositions():
                            # add "the weird spot" to feasibleMoves
                            feasibleMoves.append([pPawns[pawnIndex], playerBoard[-1], -1])
                    elif pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                        if 59 not in self.getPawnPositions():
                            # add 59 to feasibleMoves
                            feasibleMoves.append([pPawns[pawnIndex], playerBoard[59], -1])
                    else:
                        if pos - 1 not in self.getPawnPositions():
                            # add position before pawn to feasibleMoves
                            feasibleMoves.append([pPawns[pawnIndex], playerBoard[pos - 1], -1])
                pawnIndex += 1  # increment pawnIndex

            # if CPU can't do anything
            if len(feasibleMoves) == 0:
                # do nothing
                pass
            else:
                # make random move
                randomIndex = randrange(0, len(feasibleMoves))
                feasibleMoves[randomIndex][0].move(feasibleMoves[randomIndex][2], playerBoards, pawns)
        elif cardNum == 11:
            # initialize boolean for whether there's an activated pawn
            isActivePawn = False
            # initialize list of unsafe active pawns
            activePawns = []

            for pos in self.getPawnPositions():  # iterate through player's pawns' positions
                if pos not in [self.START_LOCATION, 60, 61,
                               62, 63, 64, self.HOME_LOCATION]:  # if pawn in "play area"
                    # flip boolean flag
                    isActivePawn = True
                    # add pawn to activePawns
                    activePawns.append(pPawns[pawnIndex])
                    if pos not in [self.START_LOCATION, 55, 56, 57, 58, 59]:  # if pawn can move 11
                        if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                            newPos = 11  # add an extra space
                        else:
                            newPos = pos + 11
                        # ensure we don't indicate that user can move pawn on top of
                        #      another same-team pawn
                        if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                            # add 11 positions after pawn to feasibleMoves
                            feasibleMoves.append([pPawns[pawnIndex], playerBoard[newPos]])
                # increment pawn index
                pawnIndex += 1

            # activate other players' pawns if player has an active pawn
            if isActivePawn:
                feasibleMoves = self.__activateOtherPawns(pawns, feasibleMoves)

            # if CPU can't do anything
            if len(feasibleMoves) == 0:
                # do nothing
                pass
            else:
                # get random feasible move
                randomIndex = randrange(0, len(feasibleMoves))
                # if random move is a swap
                if feasibleMoves[randomIndex][0].getPlayer() != self.player:
                    # get (player #, pawn #) of feasibleMoves[randomIndex][1]
                    swappeePlayer = feasibleMoves[randomIndex][0].getPlayer()
                    swappeeNum = feasibleMoves[randomIndex][0].getPawnNumber()
                    # swap a random one of our player's unsafe active pawns
                    activePawns[randrange(0, len(activePawns))].swap([swappeePlayer, swappeeNum],
                                                                     playerBoards, "11", pawns)
                else:
                    # move our pawn by 11
                    feasibleMoves[randomIndex][0].move(11, playerBoards, pawns)
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
                # add other players' unsafe active pawns to feasibleMoves
                feasibleMoves = self.__activateOtherPawns(pawns, feasibleMoves)

            # if CPU can't do anything
            if len(feasibleMoves) == 0:
                # do nothing
                pass
            else:
                # get random unsafe active pawn of opponent
                ranPawn = feasibleMoves[randrange(0, len(feasibleMoves))][0]
                # get random pawn's player
                swappeePlayer = ranPawn.getPlayer()
                # get random pawn's number
                swappeeNum = ranPawn.getPawnNumber()
                # swap toSwap with random pawn
                toSwap.swap([swappeePlayer, swappeeNum], playerBoards, "Oops!", pawns)

    def __implementSimpleCard(self, cardNum, playerBoards, pawns):
        """ This method performs necessary actions in the most simple (yet most
            common) scenarios.
            Input: cardNum - number of card to implement
                   playerBoards - list of each player's board
                   pawns - list of each player's list of pawns """

        # initialize activated buttons
        pawnPlace = []
        # initialize player board
        playerBoard = playerBoards[self.player - 1]
        # initialize pawn index
        pawnIndex = 0

        # add appropriate pawns & places to pawnPlace
        for pos in self.getPawnPositions():
            if pos not in ([self.START_LOCATION] + list(range(self.HOME_LOCATION - cardNum + 1,
                                                              self.HOME_LOCATION + 1))):
                if pos in self.WEIRD_LOCATIONS:  # if pawn is on weird spot
                    newPos = cardNum
                else:
                    newPos = pos + cardNum
                if newPos == self.HOME_LOCATION or newPos not in self.getPawnPositions():
                    # append (pawn, board pos) pair to pawnPlace
                    pawnPlace.append([pawns[self.player - 1][pawnIndex], playerBoard[newPos]])
            # increment pawn index
            pawnIndex += 1

        # if CPU can't do anything
        if len(pawnPlace) == 0:
            # do nothing
            pass
        else:
            # make a random move
            pawnPlace[randrange(0, len(pawnPlace))][0].move(cardNum, playerBoards, pawns)

    def __activateOtherPawns(self, pawns, pawnPlace):
        """ This helper method adds the buttons corresponding to each
            other player's active pawns to pawnPlace. It returns an updated list of currently
            feasible (pawns, place) pairs
            Input: pawns - list of each player's list of pawns
                   pawnPlace - list of (pawn, place) pairs representing feasible moves """

        for player in range(len(pawns)):  # loop through other players
            if player + 1 != self.player:  # if other player isn't our player
                for pawn in pawns[player]:  # loop through other player's pawns
                    # if pawn is active
                    if pawn.getPosition() not in [self.START_LOCATION, self.HOME_LOCATION,
                                                  64, 63, 62, 61, 60]:
                        # add pawn to pawnPlace
                        pawnPlace.append([pawn])

        return pawnPlace
