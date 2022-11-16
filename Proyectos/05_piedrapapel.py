import random  #Imports the module random
option = ("Piedra", "Papel", "Tijera")
round = 0
user_score = 0
computer_score = 0
while round < 3:
  print("*" * 10)
  print("Round", round)
  print("*" * 10)
  user_option = input("piedra, papel o tijera --> ")
  user_option = user_option.capitalize()
  user_computer = random.choice(option) #retrieves a random option fromn a selection
  
  if not user_option in option: # si la opcion del user no está en las opciones
    print("opcion no valida")
  else:
    print("Computer chose ", user_computer)
    print("User chose ", user_option)
    if user_option == user_computer:
      print("draw")
    elif user_option == "Papel" and user_computer == "Piedra":
      print("you won")  
      user_score += 1
      print ("user score is", computer_score)
      round += 1 
    elif user_option == "Tijera" and user_computer == "Papel":
      print("you won")  
      user_score += 1
      print ("user score is", computer_score)
      round += 1     
    elif user_option == "Piedra" and user_computer == "Tijera": 
      print("you won")  
      user_score += 1
      print ("user score is", computer_score)
      round += 1
    else:
      print("you lose")
      computer_score +=1
      print ("the computer score is", computer_score)
      round += 1

print("Final computer score is", computer_score)
print("Final user score is", user_score)
if user_score > computer_score:
  print("You won this match")
else:
  print("computer beat the hell out of you, too bad!")
      
  #continue sirve para que el ciclo continue con la otra parte de la lógica. salta el ciclo