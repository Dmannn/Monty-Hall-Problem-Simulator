import random

class Door():
    def __init__(self, id, prize):
        self.prize = prize
        self.id = id

class Player():
    def __init__(self, choice):
        self.choice = choice

class GameSim():
    def __init__(self, simulations, switch): # simulations = How many simulations you'd like to run, switch = boolean representing if you'd like the player to switch doors
        self.switch = switch
        self.simulations = simulations
        self.prizes = ['goat', 'goat', 'car']
        self.doorlist = []
        self.opened = None
        self.wins = 0
        self.losses = 0
        self.mainGame()
        print(self.outcomeCalc())

    def createDoors(self): # creates 3 doors, each with an id 1-3 and a prize ensuring there are 2 goats and 1 car
        for x in range(1, 4):
            prize = random.choice(self.prizes)
            door = Door(x, prize)
            self.prizes.pop(self.prizes.index(prize))
            self.doorlist.append(door)

    def chooseDoor(self): # Representing the player making a choice. Didn't really have to be its own function, but it's easier to visualize
        self.player = Player(1) # The player picks door number 1

    def openDoor(self):
        while True:
            self.opened = random.choice(self.doorlist) # Picks a random door that has a goat and is also not the players choice, and removes it from the doors to choose
            if self.opened.prize == 'goat' and self.opened.id != self.player.choice:
                self.doorlist.pop(self.doorlist.index(self.opened))
                self.opened = self.opened.id
                break
            else:
                continue

    def rechooseDoor(self): # If switch is True, then it check the door list and change the players choice to the other door
        if self.switch == True:
            for door in self.doorlist:
                if door.id != self.player.choice:
                    self.player.choice = door.id
                    break
                else:
                    continue
        else:
            pass

    def checkWin(self): # Simply checks if the players choice is a goat (a loss) or a car (a win) and increments the respective counter
        for door in self.doorlist:
            if door.id == self.player.choice and door.prize == 'car':
                self.wins += 1
                break
            elif door.id == self.player.choice and door.prize == 'goat':
                self.losses += 1
                break

    def outcomeCalc(self): # Calculates the percent of the simulations where a win or loss has occurred
        percentWin = self.wins/self.simulations * 100
        percentLost = self.losses/self.simulations * 100
        return f"Won {percentWin}% and Lost {percentLost}%"

    def mainGame(self): # Main function to organize the steps of the game
        for x in range(self.simulations):
            self.createDoors()
            self.chooseDoor()
            self.openDoor()
            self.rechooseDoor()
            self.checkWin()
            self.prizes = ['goat', 'goat', 'car']
            self.doorlist = []
            self.opened = None

game = GameSim(100000, True) # Example: here we run 100000 simulations where the player switches their choice after the reveal
