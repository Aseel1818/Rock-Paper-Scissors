#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def getOpponentLastMove(self):
        return self.last_opponent_move

    def getPlayerLastMove(self):
        return self.last_player_move


class RandomPlayer (Player):
    def move(self):
        choice = random.choice(moves)
        return choice


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Enter Rock, Paper or Scissors\n").lower()
            if choice in moves:
                return choice


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_opponent_move = None

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move

    def move(self):
        return self.last_opponent_move if self.last_opponent_move is not None \
            else 'rock'


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move_index = -1

    def learn(self, my_move, their_move):
        self.last_move_index = min(self.last_move_index + 1, len(moves) - 1)

    def move(self):
        return moves[self.last_move_index]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move2, move1):
            self.score2 += 1
            print("Player 2 Wins the round!")
        elif beats(move1, move2):
            self.score1 += 1
            print("Player 1 Wins the round!")
        else:
            print("Game Tied!")
        print(f"Player 1 Score {self.score1}")
        print(f"Player 2 Score {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.round += 1

    def play_game(self):
        print("Game start!")
        while True:
            print(f"Round {self.round}:")
            self.play_round()
            userInput = input("enter 'exit' to quit or Enter to play"
                              " another round: ").strip().lower()
            if userInput == 'exit':
                break
        print(f"Player 1  Final Score {self.score1}")
        print(f"Player 2  Final Score {self.score2}")
        if self.score2 > self.score1:
            print("Player 2 Wins the Game!")
        elif self.score1 > self.score2:
            print("Player 1 Wins the Game!")
        else:
            print("Game Tied!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
