# define the base class player
class player:
 def play(selt):
  print("the player is playing cricket.")
#define the derived class batstman
class batsman(player):
   def play(selt):
    print("the batsman is batting.")
#define the derived class bowler
class Bowler(player):
  def play(selt):
    print("the bowler is bowling.")
# create object of bastman and bowler class
batstman=batsman()
bowler=Bowler()
#call the play() method for each object
batstman.play()
bowler.play()