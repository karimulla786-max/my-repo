#numbers = [1,2,3,4,5,6,7,8,9,10] 

#for number in numbers: 

 #   print(number**2) 



"""n =int(input("give  n value:"))

i=1

while i<=10:
    print(f"{n} * {i} ={n*i}")
    i+=1"""



#""""number = int(input("enter number:"))
#while number != 0:
 #   print(f'you entered {number}')
  #  number =int(input("enter a number:"))
#print("the end")""""



def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
 
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
 
    while not guessed:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1
 
            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()