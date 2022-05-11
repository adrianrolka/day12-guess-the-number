import random
def game():
  print('Welcome to the Number Guessing Game!')
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1,100)
  difficulty_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty_chosen == "hard":
    lives = 5
  else:
    lives = 10
  game_over = False
  while not game_over:
    if lives == 0:
      print('You run out of lives, game over!')
      game_over = True
    else:
      print(f'You have {lives} lives remaining to guess the number. Good luck! :)')
      guess = int(input("Make a guess: "))
      if guess == number:
        print('You guessed correctly, nois!')
        game_over = True
      elif guess > number:
        print('Too high!')
        lives -= 1
      elif guess < number:
        print('Too low!')
        lives -= 1
      else: 
        game_over = True
  retry = input('Do you want to play again? Type yes or no: ')
  if retry == "yes":
    game()

game()


  