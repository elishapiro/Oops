# pawn.py

class Pawn:
    """ Create Oops! pawn """

    def __init__(self, player, pawnNumber):
        """ Initializes Oops! pawn at 'Start' """

        # denote slider positions
        self.SLIDER1_3 = 13
        self.SLIDER2_3 = 28
        self.SLIDER3_3 = 43
        self.SLIDER1_4 = 21
        self.SLIDER2_4 = 36
        self.SLIDER3_4 = 51

        self.NUMBER_OF_PAWNS = 4  # denote constant number of pawns
        self.position = 0  # denote starting position
        self.player = player  # denote player
        self.number = pawnNumber  # denote pawn number
        self.pawnBut = None  # initialize pawn button

    def move(self, amt, playerBoards, pawns):
        """ Moves pawn by amt.
            Input: amt - integer amount to move pawn
                   playerBoards - list of each player's board
                   pawns - list of each player's list of pawns """

        # handling the case where pawn moves backwards 4 near "Start"
        if self.position in [1, 2, 3] and amt == -4:
            ds = 56
        elif (self.position == 4) and (amt == -4):
            ds = -5
        elif (self.position == -1) and (amt == -4):
            ds = 57
        elif (self.position == 66) and (amt == -4):
            ds = -10
        # handling the case where pawn moves backwards 1 near "Start"
        elif (self.position == 1) and (amt == -1):
            ds = -2
        elif (self.position == -1) and (amt == -1):
            ds = 60
        elif (self.position == 66) and (amt == -1):
            ds = -7
        # handling the case where pawn is on the "Weird Spot"
        elif self.position == -1:
            ds = amt + 1
        elif self.position == 66:
            ds = amt - 66
        else:  # else...
            ds = amt

        # denote player's pawn positions
        ourPositions = []
        for pawnNum in range(self.NUMBER_OF_PAWNS):
            ourPositions.append(pawns[self.player-1][pawnNum].getPosition())

        # get list of each player's pawns' positions, and get list of each  player's
        #    pawns' board places
        allPawnPositions, pawnPlaces = self.__getPosAndPlace(playerBoards, pawns)

        # if pawn moves beyond home or if pawn conflicts with another pawn
        if (self.position + ds > 65) or ((self.position + ds != 65) and (self.position + ds != 0) and
                                         (self.position + ds in ourPositions)):
            # do nothing
            pass
        # if pawn lands in home
        elif self.position + ds == 65:
            # move pawn to home
            self.position = self.position + ds
        else:
            # modify pawn's position
            self.position = self.position + ds
            # slide if appropriate
            if self.position in [self.SLIDER1_3, self.SLIDER2_3, self.SLIDER3_3,
                                 self.SLIDER1_4, self.SLIDER2_4, self.SLIDER3_4]:
                self.slide(playerBoards, pawns)
            # otherwise, if pawn lands on another pawn's position
            elif playerBoards[self.player - 1][self.position] in pawnPlaces:
                # determine where other pawn is in the list
                otherPawnNum = pawnPlaces.index(playerBoards[self.player - 1][self.position])
                otherPawnLoc = pawnPlaces[otherPawnNum]
                # send other pawn home
                self.__sendHome(otherPawnLoc, pawnPlaces, pawns)

    def swap(self, playerPawn, playerBoards, swapCard, pawns):
        """ Swap positions with another player's pawn.
            Inputs: playerPawn - [player #, pawn #] representing pawn to be swapped
                    playerBoards - list of each player's board
                    swapCard - card under which the swap is occurring (either "11" or "Oops!")
                    pawns - list of each player's list of pawns """

        # record which player (minus 1 for indexing)
        whichPlayer = playerPawn[0] - 1
        # record which pawn (minus 1 for indexing)
        whichPawn = playerPawn[1] - 1
        # create list of each player's list of pawn positions
        pawnPositions = []
        for playerNum in range(len(playerBoards)):
            playerPositions = []
            for pawnNum in range(self.NUMBER_OF_PAWNS):
                playerPositions.append(pawns[playerNum][pawnNum].getPosition())
            pawnPositions.append(playerPositions)

        # denote pawn positions of swappee player
        swappeePlayerPositions = pawnPositions[whichPlayer]
        # denote position of swappee pawn
        swappee = swappeePlayerPositions[whichPawn]
        # denote whichPlayer's board
        swappeeBoard = playerBoards[whichPlayer]
        # denote place on which the swappee lies
        swappeePlace = swappeeBoard[swappee]

        if swapCard == "11":
            try:
                # record new position for swapper
                swapperNewPos = playerBoards[self.player - 1].index(swappeePlace)
            except ValueError:
                # if the swapee is not on pawn's board, end function
                return ""
            # board of player to which this pawn belongs
            swapperBoard = playerBoards[self.player - 1]
            # denote object on which swapper lies
            swapperPlace = swapperBoard[self.position]
            try:
                # denote new position of swappee
                swappeeNewPos = swappeeBoard.index(swapperPlace)
            except ValueError:
                # if the pawn is not on swapee's board, end function
                return ""
            # modify swapper's position
            self.position = swapperNewPos
            # modify swappee's position
            pawns[whichPlayer][whichPawn].changePosition(swappeeNewPos)
        else:
            try:
                # denote new position of swapper
                swapperNewPos = playerBoards[self.player - 1].index(swappeePlace)
            except ValueError:
                # if the swappee is not on pawn's board, end function
                return ""
            # modify swapper's position
            self.position = swapperNewPos
            # send swappee to start
            pawns[whichPlayer][whichPawn].changePosition(0)

        # slide swapper if appropriate
        self.slide(playerBoards, pawns)
        # slide swappee if appropriate
        pawns[whichPlayer][whichPawn].slide(playerBoards, pawns)

    def slide(self, playerBoards, pawns):
        """ If this pawn has landed on the start-point of a slide
            whose color differs from its own, slide this pawn the appropriate
            amount.
            Input: playerBoards - list of each player's board
                   pawnPlaces - list of each player's list of their pawns' places on board
                   pawns - list of each player's list of pawns """

        # get list of each  player's pawns' board places
        _, pawnPlaces = self.__getPosAndPlace(playerBoards, pawns)

        # slide according to Oops! rules
        if self.position in [self.SLIDER1_3, self.SLIDER2_3, self.SLIDER3_3]:
            # modify pawn's position
            self.position = self.position + 3
            # iterate through squares just slid over
            for square in playerBoards[self.player - 1][self.position - 3:self.position + 1]:
                # send pawn back home if it's on the slider
                if square in pawnPlaces:
                    self.__sendHome(square, pawnPlaces, pawns)
        elif self.position in [self.SLIDER1_4, self.SLIDER2_4, self.SLIDER3_4]:
            self.position = self.position + 4
            # iterate through squares slided through
            for square in playerBoards[self.player - 1][self.position - 4: self.position + 1]:
                # send pawn back home if it's on the slider
                if square in pawnPlaces:
                    self.__sendHome(square, pawnPlaces, pawns)

    def __sendHome(self, square, pawnPlaces, pawns):
        """ This helper method eliminates a pawn if it's on square and
            not this player's pawn.
            Inputs: square - Oops! square under consideration
                    pawnPlaces - list of board spots on which current pawns reside
                    pawns - list of each player's list of pawns """

        # determine where other pawn is in the list
        whichPawn = pawnPlaces.index(square)
        if whichPawn <= 3:  # if other pawn is Player 1's
            # if other pawn is not this pawn
            if pawns[0][whichPawn] != self:
                # send other pawn back home
                pawns[0][whichPawn].changePosition(0)
        elif whichPawn <= 7:
            # if other pawn is not this pawn
            if pawns[1][whichPawn % 4] != self:
                pawns[1][whichPawn % 4].changePosition(0)
        elif whichPawn <= 11:
            # if other pawn is not this pawn
            if pawns[2][whichPawn % 4] != self:
                pawns[2][whichPawn % 4].changePosition(0)
        else:
            # if other pawn is not this pawn
            if pawns[3][whichPawn % 4] != self:
                pawns[3][whichPawn % 4].changePosition(0)

    def __getPosAndPlace(self, playerBoards, pawns):
        """ This helper method creates and returns a list of each player's pawns'
            positions, starting with player 1's pawn 1 and ending
            with the last player's pawn 4.
            Inputs: playerBoards - list of each player's board
                    pawns - list of each player's list of pawns """

        # denote all players' pawn positions
        allPawnPositions = []
        for playerNum in range(len(playerBoards)):  # loop through players
            playerPositions = []  # initialize player's positions
            for pawnNum in range(self.NUMBER_OF_PAWNS):  # loop through pawns
                # add pawn position to player's positions
                playerPositions.append(pawns[playerNum][pawnNum].getPosition())
            # add player's pawn positions to all pawn positions
            allPawnPositions.append(playerPositions)

        # initialize list of start/squares/home where pawns lie
        pawnPlaces = []
        # create list of start/squares/home where pawns lie
        for playerNum in range(len(playerBoards)):
            for pawnPos in allPawnPositions[playerNum]:
                pawnPlaces.append(playerBoards[playerNum][pawnPos])

        return allPawnPositions, pawnPlaces

    def getPawnBut(self):
        """ Returns pawn button """
        return self.pawnBut

    def setPawnBut(self, newBut):
        """ Reassigns pawn button """
        self.pawnBut = newBut

    def getPawnNumber(self):
        """ Return pawn number """
        return self.number

    def getPosition(self):
        """ Returns position of pawn """
        return self.position

    def changePosition(self, newPos):
        """ Changes position of pawn to newPos """
        self.position = newPos

