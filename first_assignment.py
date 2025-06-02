#Write a Python program that asks the user for the following information:
#Name, Age, GPA (0-5, can be decimals), Field of Interest, Graduated ("yes" or "no").
#1- Print a nicely formatted 
#2- Based on the info, determine and print:
#If the user is eligible for a scholarship (age < 25, GPA ≥ 3.5, has graduated)
#If the user is eligible for an internship (age < 30, GPA ≥ 2.5)
#If neither, recommend they apply again later.
#Repository name should be: `python-profile-checker`
#-------------inputs-----------------
Name=(str(input("enter your name: ")))
Age=(int(input("enter your age:")))
GPA=(float(input("enter your GPA (0-5):")))
feild_of_intrest=(str(input("enter your field of intrest:")))
Graduated=(str(input("are you graduated?(yes or no only)")))
#-------------all info--------------
print("-----user information-----")
print("name:",Name)
print("age:",Age)
print("GPA:",GPA)
print("feild of intrest:",feild_of_intrest)
print("graduated:",Graduated)
#-----to see if eligible for scholarship-----
if Age<25 and GPA>=3.5 and Graduated=="yes":
     print("you",Name,"are eligible to a scholarship")
#-----to see if eligible to a intership
elif Age<30 and GPA>=2.5:
    print("you",Name,"are eligibal to an internship")
#-----neither-----
else:
    print("you",Name,"should apply again later")