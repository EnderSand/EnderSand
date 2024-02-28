import random

options = ["scissors", "paper", "rock"]

print ("Hello, this is rock, paper, scissors against RNG. Good luck. It is RNG.")
playerScore = 0
computerScore = 0
ties = 0
while True:
  RNG = options[random.randint(0,2)]
  player = input("choose paper, scissors or rock:")

  if player == "rock":
    if RNG == "rock":
      print("The RNG chose rock. Its a tie.")
      ties += 1
    
    elif RNG == "scissors":
      print("The RNG chose scissors. You win!")
      playerScore += 1
    
    elif RNG == "paper":
      print("The RNG chose paper. You lose.")
      computerScore += 1

  elif player == "paper":
    if RNG == "rock":
      print("The RNG chose rock. You win!.")
      playerScore += 1
    
    elif RNG == "scissors":
      print("The RNG chose scissors. You lose.")
      computerScore += 1
    
    elif RNG == "paper":
      print("The RNG chose paper. It's a tie.")
      ties += 1
  
  elif player == "scissors":
    if RNG == "rock":
      print("The RNG chose rock. You lose.")
      computerScore += 1
    
    elif RNG == "scissors":
      print("The RNG chose scissors. It's a tie.")
      ties += 1
    
    elif RNG == "paper":
      print("The RNG chose paper. You win!")
      playerScore += 1
  print ("player score:" + str(playerScore))
  print ("RNG score:" + str(computerScore))
  print ("Ties:" + str(ties))

