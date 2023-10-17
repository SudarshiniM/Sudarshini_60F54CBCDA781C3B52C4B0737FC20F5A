class Player:
  def play(self):
    print("the player is playing cricket")
class Batsman(Player):
  def play(self):
    print("The player is batting")
class Bowler(Player):
  def play(self):
    print("The player is bowling")
Player().play()
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()