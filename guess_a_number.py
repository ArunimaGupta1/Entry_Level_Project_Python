import random
def guess(x):
             random_number = random.randint(1,x)
             guess = 0
             while guess!=random_number:
                          guess = int(input(f"Enter a number between 1 and {x}"))
                          if guess < random_number:
                                       print("too low, enter some higher values")
                          elif guess > random_number:
                                       print("too high, enter some lower value")

             print(f"Congrats! You have entered correct number {random_number}")
