#did these all in pieces in seperate files and then threw them in here for consolidation

#EXERCISE ONE:

list1 = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]

def longest(var):
    top = len(var[0])
    word = var[0]
    for i in var:
        if len(i)>top:
            top = len(i)
            word = i
            print(f'longest word? its {word}, {top} letters long.')
       

longest(list1)

#EXERCISE TWO:
# this one is slightly incomplete, especially since I know i need to organize
#the text import into words, and not just letters. I just couldnt get the
#most basic .txt file import to work in VScode today, and ran out of time to
#troubleshoot fully. This is the bones of the changes I'd need
import random

w = open('words.txt', encoding = 'uft-8')
print(w)
t = 0
list2 = []
while t<7:
    list.append(w.random)


def longest(var):
    top = len(var[0])
    word = var[0]
    for i in var:
        if len(i)>top:
            top = len(i)
            word = i
            print(f'longest word? its {word}, {top} letters long.')
       
longest(list2)


#EXERCISE THREE:
import random
plants = {'ash':'tree','thyme':'shrub','apple':'tree','blueberry':'shrub'}

print(plants.keys())

extra_plant = {'boxwood':'shrub'}
plants.update(extra_plant)
print(plants)

k = plants.items()
print(k)

plants.pop('ash') #big L for ash trees recently. RIP.

#EXERCISE FOUR:
# i want to create a student class that is able to be called for different people's info
#I'll want this to include auto-generated school emails(not accurate with numbers since i dont have student name counts)
#plus a grade input and GPA calculator

class student():
    def __init__(self,name_first,name_last):
        self.name_first = name_first
        self.name_last = name_last

    def email(self):
        first = self.name_first[0:1]
        last = self.name_last[0:4]
        print(f'your school email is {first}{last}@binghamton.edu')

    def grade(self, score):
        self.score = score
        if self.score >97:
            print('thats a sweet 4.0!')
        elif self.score >93 and self.score <96:
            print('4.0, nice job! thats an A+')
        elif self.score >90 and self.score <92:
            print('4.0, nice job! thats an A')
        elif self.score >87 and self.score <89:
            print('your gpa is a 3.7, or an A-!')
        elif self.score >83 and self.score <86:
            print('your gpa is a 3.3, or a B+')
        elif self.score >80 and self.score <82:
            print('your gpa is a 3.0, or a B')
        elif self.score >77 and self.score <79:
            print('your gpa is a 2.7, or a B-')
        elif self.score >73 and self.score <76:
            print('your gpa is a 2.3, or a C+')
        elif self.score >70 and self.score <72:
            print('your gpa is a 2.0, or a C')
        elif self.score >67 and self.score <69:
            print('your gpa is a 1.7, or a C-')
        elif self.score >65 and self.score <66:
            print('your gpa is a 1.0, or a D')
        else:
            print('thats a fail, unfortunately')

me = student('aine','gunn')
me.email()
me.grade(84)


#EXERCISE FIVE:
#this version isnt working fully, but I had less time than I thought. The project was a
#better review than I'd expected and I'll be continuing to work on it 
#personally as a mini project to learn basic GUIs early
class hangman():
    def __init__(self,car):
       self.car = 0

    def playgame(self,word = 'games',list1 = list(word), dict1 = {},progress = [],count = 0,player = input('pick a letter, any letter!')):
        self.word = 'games'
        self.list1 = list(word)
        self.dict1 = {}
        self.progress = []
        self.count = 0
        self.player = input('pick a letter, any letter!')
        while count < 5:
                for i in list1:
                    progress.extend('_')
                    print(progress)
                    if player in list1 and player not in dict1:
                        dict1[list1.index(i)] = i
                        list1.remove(i)
                        progress.inset(i,list1.index(i))
                        print('correct!')
                        player = input('pick another: ')
                    elif player in dict1:
                        player = input('you already guessed that! try again:')
                    elif player not in list1 and player not in dict1:
                        count +=1
                        player = input('oop, try again!')

                if list1 == [] and count != 5:
                    print('you won! __ was the word!')
                elif count >= 5:
                    print("dang, you lost bud")
        
