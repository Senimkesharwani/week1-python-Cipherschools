# Nested If-else, Exercise 1 solution of Python
winning_number=5
user_number=input("guess a number between 1-10: ")
user_number=int(user_number)
if winning_number==user_number:
    print("You Win")
else:
    if user_number>winning_number:
        print("too high") 
    else:
        print("too low")    