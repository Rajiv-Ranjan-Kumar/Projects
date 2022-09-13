"""Problem Statement: You have to write a Word Puzzle Game in which the user has to form
the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each
wrong answer. At last print the final score. You can store any number of words in the list, but
in each round of the game only 5 words are shown to the user.
Sample output of the game:
Arrange the letters to form a valid word:
RAEHTF
Father
Correct
Arrange the letters to form a valid word:
KABRE
Barke
Wrong
Arrange the letters to form a valid word:
CYROTNU
Cry
Wrong
Arrange the letters to form a valid word:
RENEG
green
Correct
Arrange the letters to form a valid word:
OAERELANP
aeroplane
Correct
Net Score is 1"""

#======================================Coding Start==================================
#import Some Module
from os import system
import random

points = [] #create Blank List for store score
level = 1 #global variable for game level

# userDetail function for get some detail by user
def userDetail():
    userName = input("Enter Your Name : ")
    return userName

# word function for storage of words
def word():
    words1 = ["father","mother","sister","brother","son",
                "sunday","monday","tuesday","wednesday",
                "thursday","friday","saturday","january",
                "february","march","april","jun","july",
                "august","september","october","november",
                "december"] #Question List
    word = random.choice(words1)
    return word

# game function for give the words to the user and get the Ans. by user
def game(word):
    x = str(word).upper()
    print("QUES : ",end="")
    for e in x[::-1]:
        print(e,end="")
    print()
    ANS = input("ANS  : ")
    return ANS

#ansValidetion function for check the Ans. is corect or not
def ansValidetion(ANS):
    wordAns = {"father","mother","sister","brother","son",
                "sunday","monday","tuesday","wednesday",
                "thursday","friday","saturday","january",
                "february","march","april","jun","july",
                "august","september","october","november",
                "december"}#Ans. Set
    if str(ANS).lower() in wordAns: #if the Ans Is corect
        print("\t\t\t Correct")
        return 1 #return 1
    else : # not corect
        print("\t\t\t Worng")
        return -1 #return -1

#collectPoints function for colect the score
def collectPoints(point):
    points.append(point)

#disp function
def disp():
    print(" ================================")
    print("|  Welcome To Word Puzzle Game   |")
    print(" ================================")

#disp2 function
def disp2(userName,level,score):
    print("Good Luck : Mr.",str(userName).upper())#show user name in upper case
    print("Level : %d\t\tScore : %d" %(level,score))#show level and score
    print("---------------------------------")
    print("Arrange the letters toform a\nvalid word:\n")

#------------------------------------function colling-------------------------------
disp() #call disp function
userName = userDetail() #call userDetail Function

#1'st while loop start
while level < 4:
    QuestionCount = 0 # QuestionCount variable for store no. of questions
    score = int(sum(points)) #score variable for store some of all points
    system("cls") #call system function and pass argument of 'cls' for clear screen
    disp() #call disp function
    disp2(userName,level,score) #call disp2 function

    #2'nd while loop start
    while QuestionCount < 5:
        ques = word() #ques variable for store question when return word function
        ans = game(ques) #ans variable for store ans. when return game function
        score1 = ansValidetion(ans) #score1 variable for store score when return ansValidation function
        collectPoints(score1) #call collectPoints function and pass score in argument form
        QuestionCount += 1 #increase QuestionCount
    #close 2'nd while loop
    #while else strat
    else:
        score = int(sum(points)) #store sum of all points
        print("\tLevel : %d Complited \n\tNet Score Is : %d"%(level,score)) #display level,score
    #while else end
    if level < 3:
        choice = input("\nDo You Want to Continew Next Level[Y/N]? : ")
        if choice in ('Y','y'):
            level += 1 #increase level
        else:
            print("\t  Thank You")
            break
    else:
        level += 1 #increase level
#1'st while loop end
#1'st while else start
else:
    print("\tGame Is Complited")
    print("your Score history is : ",points)
#1'st while else end
#=======================================coding End==================================