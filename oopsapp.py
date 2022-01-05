# oopsapp.py

from cpuplayer import CPUPlayer
from player import Player
from graphicinterface import GraphicInterface
from deck import *


class OopsApp:
    """ Creates a Oops! game. """

    def __init__(self, quantity, isCPU):
        """ Initializes the Oops! game.
         Input: quantity - number of players. """

        self.quantity = quantity  # denote quantity of players

        self.deck = Deck()  # create deck

        self.interface = GraphicInterface()  # creates interface

        self.oopsWin = self.interface.getWindow()  # record oops window

        self.players = []  # initialize player list
        for playerNum in range(1, quantity + 1):  # add user-specified quantity of players
            if isCPU[playerNum-1]:  # if this player is a CPU
                # add CPU player
                self.players.append(CPUPlayer(playerNum, self.deck, self.interface))
            else:
                # add human player
                self.players.append(Player(playerNum, self.deck, self.interface))

        self.pawns = []  # initialize list of players' lists of pawns
        for playerNum in range(quantity):
            # add player's list of pawns
            self.pawns.append(self.players[playerNum].getPawns())

        self.pawnPositions = []  # initialize list of players' list of pawn positions
        for playerNum in range(quantity):
            # create each player's pawn positions
            self.pawnPositions.append(self.players[playerNum].getPawnPositions())

        self.playerBoards = []  # initialize player boards
        for playerNum in range(1, quantity + 1):  # loop through players
            # add playerNum's board
            self.playerBoards.append(self.interface.getBoard(playerNum))

        # initialize variable denoting whose turn it is
        self.turn = self.players[0]

        # draw initial pawns
        self.__updatePawns()

    def game(self):
        """ Plays a game of Oops! """

        turnCount = 0  # initialize variable that denotes turn count
        while self.__gameNotOver():
            # play turn
            currTurn = self.__playTurn()
            if not currTurn:  # if user didn't click quit
                turnCount = turnCount + 1  # update turn count
                modTurnCount = turnCount % self.quantity  # get turnCount mod quantity
                self.turn = self.players[modTurnCount]  # cycle through players
            else:  # if user clicked quit
                break

        # close oops window
        self.oopsWin.close()

        # if game ends with a player winning
        if not self.__gameNotOver():
            # return which player won
            return self.pawnPositions.index([65]*4) + 1
        else:
            # otherwise, return None
            return None

    def __gameNotOver(self):
        """ Returns True if the game is not over, False if it is """
        return not ([65] * 4 in self.pawnPositions)

    def __playTurn(self):
        """ Plays one turn of Oops! """

        # user does turn
        currTurn = self.turn.doTurn(self.playerBoards, self.pawns)

        if currTurn == "quit":  # if user clicked quit
            return "quit"  # tell self.game() user quit
        elif currTurn == "2":  # if user rolled 2
            # update pawn positions
            self.__updatePawns()
            # replay turn
            self.__playTurn()
        else:
            # update pawns
            self.__updatePawns()

    def __updatePawns(self):
        """ Updates each player's list of pawn positions """

        # reset self.pawnPositions
        for playerNum in range(len(self.players)):
            # create each player's pawn positions
            self.pawnPositions[playerNum] = self.players[playerNum].getPawnPositions()

        # move pawns on Oops! board
        self.interface.movePawns(self.pawns)
