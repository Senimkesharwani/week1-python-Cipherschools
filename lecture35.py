#solution of exercise
nam1,char=input("Enter the name and character sepratred bu comma: ").split(",")
print(f"length of your name is: {len(nam1)}")
print(f"Character count: {nam1.lower().count(char.lower())}")    #casev insecsitive



#nam1.lower().count(char.lower())
