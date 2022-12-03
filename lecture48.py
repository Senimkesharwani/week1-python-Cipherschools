#my solution
user_name=input("Enter your name: ")
age=input("Enter your age: ")
age=int(age)
#user_name[1]==A,a
x=user_name[0]
y=x=="a" or x=="A"
if y and age==10:
    print("You van watch coco")
else:
    print("Sorry!you cannot watch coco") 