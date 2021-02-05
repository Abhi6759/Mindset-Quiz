import  sqlite3
conn  =  sqlite3 . connect ( 'myresults.db' )
cursor  =  conn.cursor ()
s_name = input('Enter your Name:')
s_surname = input('Enter your Surname:')
s_email = input('Enter your Email:')

print ("(01)Intelligence is something you are born with that can't be changed.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer1=(int(input("Enter your answer as 1,2,3,4\n")))
if answer1==1:
	answer1marks=0
elif answer1==2:
	answer1marks=1
elif answer1==3:
	answer1marks=2
elif answer1==4:
	answer1marks=3
print("thanks here is your next question\n")

print ("(02)No matter how intelligent you are, you can always be more intelligent.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer2=(int(input("Enter your answer as 1,2,3,4\n")))
if answer2==1:
	answer2marks=0
elif answer2==2:
	answer2marks=1
elif answer2==3:
	answer2marks=2
elif answer2==4:
	answer2marks=3
print("thanks here is your next question\n")

print ("(03)You can always substantially change just how intelligent you are.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer3=(int(input("Enter your answer as 1,2,3,4\n")))
if answer3==1:
	answer3marks=3
elif answer3==2:
	answer3marks=2
elif answer3==3:
	answer3marks=1
elif answer3==4:
	answer3marks=0
print("thanks here is your next question\n")

print ("(04)You are a certain kind of person and there is not much that can be done to really change that.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer4=(int(input("Enter your answer as 1,2,3,4\n")))
if answer4==1:
	answer4marks=0
elif answer4==2:
	answer4marks=1
elif answer4==3:
	answer4marks=2
elif answer4==4:
	answer4marks=3
print("thanks here is your next question\n")

print ("(05)You can always change basic things about the kind of person you are.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer5=(int(input("Enter your answer as 1,2,3,4\n")))
if answer5==1:
	answer5marks=3
elif answer5==2:
	answer5marks=2
elif answer5==3:
	answer5marks=1
elif answer5==4:
	answer5marks=0
print("thanks here is your next question\n")



print ("(06)Musical talent can be learned by anyone.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer6=(int(input("Enter your answer as 1,2,3,4\n")))
if answer6==1:
	answer6marks=3
elif answer6==2:
	answer6marks=2
elif answer6==3:
	answer6marks=1
elif answer6==4:
	answer6marks=0
print("thanks here is your next question\n")

print ("(07)Only a few people will be truly good at sports - you have to be born with it")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer7=(int(input("Enter your answer as 1,2,3,4\n")))
if answer7==1:
	answer7marks=0
elif answer7==2:
	answer7marks=1
elif answer7==3:
	answer7marks=2
elif answer7==4:
	answer7marks=3
print("thanks here is your next question\n")


print ("(08)Mathematics is much easier to learn if you are male or you come from a culture that values it.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer8=(int(input("Enter your answer as 1,2,3,4\n")))
if answer8==1:
	answer8marks=0
elif answer8==2:
	answer8marks=1
elif answer8==3:
	answer8marks=2
elif answer8==4:
	answer8marks=3
print("thanks here is your next question\n")

print ("(09)The harder you work at something the better you will get at it.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer9=(int(input("Enter your answer as 1,2,3,4\n")))
if answer9==1:
	answer9marks=3
elif answer9==2:
	answer9marks=2
elif answer9==3:
	answer9marks=1
elif answer9==4:
	answer9marks=0
print("thanks here is your next question\n")


print ("(10)No matter what kind of person you are you can always change substantially.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer10=(int(input("Enter your answer as 1,2,3,4\n")))
if answer10==1:
	answer10marks=3
elif answer10==2:
	answer10marks=2
elif answer10==3:
	answer10marks=1
elif answer10==4:
	answer10marks=0
print("thanks here is your next question\n")

print ("(11)Trying new things is often stressful for me, so I tend to avoid it.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer11=(int(input("Enter your answer as 1,2,3,4\n")))
if answer11==1:
	answer11marks=0
elif answer11==2:
	answer11marks=1
elif answer11==3:
	answer11marks=2
elif answer11==4:
	answer11marks=3
print("thanks here is your next question\n")


print ("(12)Some people are good and kind, and some are not - it's not often that people change.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer12=(int(input("Enter your answer as 1,2,3,4\n")))
if answer12==1:
	answer12marks=0
elif answer12==2:
	answer12marks=1
elif answer12==3:
	answer12marks=2
elif answer12==4:
	answer12marks=3
print("thanks here is your next question\n")


print ("(13)I appreciate when others give feedback about my performance.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer13=(int(input("Enter your answer as 1,2,3,4\n")))
if answer13==1:
	answer13marks=3
elif answer13==2:
	answer13marks=2
elif answer13==3:
	answer13marks=1
elif answer13==4:
	answer13marks=0
print("thanks here is your next question\n")


print ("(14)I often get angry if I get negative feedback about my performance.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer14=(int(input("Enter your answer as 1,2,3,4\n")))
if answer14==1:
	answer14marks=0
elif answer14==2:
	answer14marks=1
elif answer14==3:
	answer14marks=2
elif answer14==4:
	answer14marks=3
print("thanks here is your next question\n")


print ("(15)All human beings are capable of learning.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer15=(int(input("Enter your answer as 1,2,3,4\n")))
if answer15==1:
	answer15marks=3
elif answer15==2:
	answer15marks=2
elif answer15==3:
	answer15marks=1
elif answer15==4:
	answer15marks=0
print("thanks here is your next question\n")


print ("(16)You can learn new things, but you can't really change how intelligent you are.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer16=(int(input("Enter your answer as 1,2,3,4\n")))
if answer16==1:
	answer16marks=0
elif answer16==2:
	answer16marks=1
elif answer16==3:
	answer16marks=2
elif answer16==4:
	answer16marks=3
print("thanks here is your next question\n")


print ("(17)You can do things differently, but the important part of who you are can't really be changed.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer17=(int(input("Enter your answer as 1,2,3,4\n")))
if answer17==1:
	answer17marks=0
elif answer17==2:
	answer17marks=1
elif answer17==3:
	answer17marks=2
elif answer17==4:
	answer17marks=3
print("thanks here is your next question\n")

print ("(18)Human beings are basically good, but sometimes make terrible decisions.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer18=(int(input("Enter your answer as 1,2,3,4\n")))
if answer18==1:
	answer18marks=3
elif answer18==2:
	answer18marks=2
elif answer18==3:
	answer18marks=1
elif answer18==4:
	answer18marks=0
print("thanks here is your next question\n")


print ("(19)An important reason why I study/learn is that I simply enjoy learning new things.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer19=(int(input("Enter your answer as 1,2,3,4\n")))
if answer19==1:
	answer19marks=3
elif answer19==2:
	answer19marks=2
elif answer19==3:
	answer19marks=1
elif answer19==4:
	answer19marks=0
print("thanks here is your next question\n")

print ("(20)Truly smart people do not need to try hard.")
print ("(1) Strongly agree\n(2) Agree\n (3)Disagree\n (4) Strongly disagree")
answer20=(int(input("Enter your answer as 1,2,3,4\n")))
if answer20==1:
	answer20marks=0
elif answer20==2:
	answer20marks=1
elif answer20==3:
	answer20marks=2
elif answer20==4:
	answer20marks=3
print("thanks here is your next question\n")


resultsofquiz =(answer1marks+answer2marks+answer3marks+answer4marks+answer5marks+answer6marks+answer7marks+answer8marks+answer9marks+answer10marks+answer11marks+answer12marks+answer13marks+answer14marks+answer15marks+answer16marks+answer17marks+answer18marks+answer19marks+answer20marks)
print("Your Mindset Score is {}".format(resultsofquiz))

s_results = (resultsofquiz)
cursor.execute("""
INSERT INTO Mindset( name, surname, Email, results )
VALUES (?,?,?,?)
""", ( s_name, s_surname, s_email, s_results))
conn.commit ()
print ( 'Data entered successfully.' )


