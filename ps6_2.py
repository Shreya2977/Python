marks1=int(input("Enter marks 1:"))
marks2=int(input("Enter marks 2:"))
marks3=int(input("Enter marks 3:"))
total_percentage= ((marks1+marks2+marks3)*100)/300
if (total_percentage>=40 and marks1>=33 and 1marks2>=33 and marks3>=33):
    print("You are pass:",total_percentage)
else:
    print("you failed , try again next year")