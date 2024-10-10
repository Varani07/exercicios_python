import random

class Player():
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.games_played
    
class HumanPlayer(Player):
    def make_move(self):
        print("Let the player make the decision!")

class ComputerPlayer(Player):
    def make_move(self):
        print("Run advanced algorithm to calculate best move!")

hp = HumanPlayer(games_played=30, victories=15)
cp = ComputerPlayer(games_played=1000, victories=999)

print(hp.win_ratio, cp.win_ratio)

game_players = [hp, cp]
starting_player = random.choice(game_players)
starting_player.make_move()


import random

class DentalHealthItem():
    def __init__(self, price):
        self.price = price
        
class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"
        
class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"
        
class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"
        
toothbrush = Toothbrush(5.99)
floss = Floss(6.99)
mouthwash = Mouthwash(4)

dental_health_kit = [toothbrush, floss, mouthwash]
random.shuffle(dental_health_kit)

actions = [obj.use() for obj in dental_health_kit]
print(actions)