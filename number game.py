import random
myRandomNumber = random.randint(1, 99)
print(myRandomNumber)

userNumber = -94256
count = 0
numbersEqual= False #Boolean. changes if the user number is equal to the random number


#While loop will only run as long as the userNumber and myRandomNumber are not equal
while numbersEqual == False:
    userInput = input("I've picked a number between 1 and 99, can you guess it? ")
  
    if userInput.isnumeric():
        userNumber = int(userInput)
        
        if userNumber == myRandomNumber:
           print("You got it!")
           print("It took you {} guesses." .format(count))
           numbersEqual = True #changes the variable to true, so while loop will no longer run
        
        elif userNumber > myRandomNumber:
            print("Nope, it's not {}" .format(userNumber))
            print("Your guess is too high")
            count += 1
        else:
            print("Nope, it's not {}" .format(userNumber))
            print("Your guess is too low")
            count += 1
       
    else: 
        print("Error...please use digits")
