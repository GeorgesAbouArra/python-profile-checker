
#-------------inputs-----------------
name=(str(input("enter your name: ")))
age=(int(input("enter your age:")))
gpa=(float(input("enter your GPA (0-5):")))
feild_of_intrest=(str(input("enter your field of intrest:")))
graduated=(str(input("are you graduated?(yes or no only)")))
#-------------all info--------------
print("-----user information-----")
print("name:",name)
print("age:",age)
print("GPA:",gpa)
print("feild of intrest:",feild_of_intrest)
print("graduated:",graduated)
#-----to see if eligible for scholarship-----
if age<25 and gpa>=3.5 and graduated=="yes":
     print("you",name,"are eligible to a scholarship")
#-----to see if eligible to a intership
elif age<30 and gpa>=2.5:
    print("you",name,"are eligibal to an internship")
#-----neither-----
else:
    print("you",name,"should apply again later")
