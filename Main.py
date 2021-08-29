from NameTemplateClasses.NameTemplate import NameTemplate
from NameMaker import NameMaker

#random names i thought of
#baseNames = ['bob','rick','david','stephen','chris','connor','sean','arthur','liam','ryan','bartholomew']
#baseNames = ['graham','gilbert','gary']
#baseNames = ['lauryn','kate','keri','victoria','samantha']
#baseNames = ['james','robert','arthur','david','ricciardo','ronald','sampson']
#whereduhwhego
#baseNames = ['geele','EilIe','lauorie','fae','jala','elsy','lexi','rayna']
#sovereign
#firstNames = ['khan','Dana','rohan','anker','zara']
#surNames = ['kottan','zen','shos','infes','vei']
#alfaran
firstNames = ['juranna','kalateth','tyrion','panthos','deon','baron','aronus','anthar','calana','sonia']
surNames = ['malcaster','ortogu','salthar','yrvan','inan','ceonos','alfar','delsos','ver dumo','miavar']
#griffinaux
#firstNames = ['Duraka', 'Mikara', 'Misana', 'Okaru','kali','morracca']
#surNames = ['Duraka', 'Mikara', 'Misana', 'Okaru','kali','morracca']


#way to get all names from user
'''
print('enter some names split by commas e.g brad,greg,jordan,rick')
inputNames = input()
baseNames = []
for name in inputNames.split(','):
    baseNames.append(name.replace(' ',''))
'''

ft = NameTemplate(firstNames,'firstnames')
st = NameTemplate(surNames,'surnames')
fm = NameMaker(ft)
sm = NameMaker(st)

def makeNames():
    print('How many names would you like')
    try:
        numberOfNames = int(input())
        firstNames = fm.generateNames(numberOfNames)
        surNames = sm.generateNames(numberOfNames)
        #print('in main')
        for i,name in enumerate(firstNames):
            print(name,surNames[i])
    except:
        print('please enter a number')
        makeNames()

makeNames()


'''
list = []

list.append(NamePart())
list.append(NamePart())
for item in list:
    print(item.id)



def removeTriplet(name):
    vowels = ['a','i','e','o','u','y']
    nameCopy = ''
    for j,letter in enumerate(name):
            if(letter):
                if j >= 2:
                    letterBehind = name[j-1]
                    letterBehindBehind = name[j-2]
                    ##print('letters',letter,letterBehind,letterBehindBehind)
                    areAllVowels = (vowels.__contains__(letter))and(vowels.__contains__(letterBehind))and(vowels.__contains__(letterBehindBehind))
                    areAllConsonants = ( (not (vowels.__contains__(letter))) and ( not(vowels.__contains__(letterBehind))) and  ( not (vowels.__contains__(letterBehindBehind))))
                    if areAllVowels or areAllConsonants:
                        print('removing',letter)
                        letter = ''
            nameCopy += letter
            print(j,nameCopy)
        ##print('after triple fixer',nameCopy)
    print('finished',nameCopy)

removeTriplet('eionele')
'''