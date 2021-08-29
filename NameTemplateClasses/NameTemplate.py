from NameTemplateClasses.NameGrammar import NameGrammar
import copy
from copy import deepcopy

class NameTemplate():

    def __init__(self,names,identifyingName):
        self.identifyingName = identifyingName
        self.nameParts = [
            {
                'partType':'',
                'partText':''
            }
        ]
        self.nameGrammars = []
        self.repeatableLetters = []
        self.minLength = names[0].__len__()
        self.maxLength = names[0].__len__()

        vowels = ['a','e','i','o','u']

        #make sure everything is lowercase
        namesCopy = []
        for name in names:
            namesCopy.append(name.lower())
        names = namesCopy

        for name in names:
            nameLength = name.__len__()
            if nameLength > self.maxLength:
                self.maxLength = nameLength
            if nameLength < self.minLength:
                self.minLength = nameLength

        #print('adding parts')
        for name in names:
            for i in range(2,4):
                partText = name[0:i]
                #print(partText)
                self.makePart('START',partText)
        
        for name in names:
            for i in range(2,4):
                partText = name[-i:]
                #print(partText)
                self.makePart('END',partText)

        previousLetter = ''
        for name in names:
            for letter in name:
                #print(letter)
                if vowels.__contains__(letter):
                    self.makePart('V',letter)
                else:
                    self.makePart('C',letter)

                if previousLetter != '':
                    if (previousLetter == letter) and (not (self.repeatableLetters.__contains__(letter))):
                        self.repeatableLetters.append(letter)
                    previousIsVowel = vowels.__contains__(previousLetter)
                    currentIsVowel = vowels.__contains__(letter)
                    if (previousIsVowel and (not currentIsVowel)) or (currentIsVowel and (not previousIsVowel)):
                        self.makePart('PH',previousLetter+letter)
                previousLetter = letter

        #print('parts added')
        #for part in self.nameParts:
        #    print(part)

        #print('Repeatable Letters')
        #for letter in self.repeatableLetters:
            #print(letter)

        #print('adding Grammars')
        for name in names:
            #print('making grammars for',name)
            self.makeGrammars(name,'')

        #print('grammars added')
        #for grammar in self.nameGrammars:
        #    print(grammar)

        self.nameParts = self.nameParts[1:]

    def makeGrammars(self,name,workingGrammar):
        namelength = name.__len__() + 1
        iterateCount = 4
        if iterateCount > namelength:
            iterateCount = namelength
        for i in range(0,iterateCount):
            for part in self.nameParts:
                if part['partText'] != '':
                    if part['partText'] == name[0:i]:
                        nameClone = copy.deepcopy(name[i:namelength])
                        newGrammar = workingGrammar + '.' +part['partType']
                        if (nameClone == '') and (newGrammar != '.'):
                            grammarPartsCount = workingGrammar.count('.') + 1
                            grammarAsList = self.grammarAsList(newGrammar)
                            grammarStart = grammarAsList[0]
                            grammarEnd = grammarAsList[-1]
                            if ((grammarStart == 'START') and (grammarEnd == 'END')) or (((grammarStart == 'START') or (grammarEnd == 'END')) and (grammarPartsCount < 3)):
                                if not (self.nameGrammars.__contains__(newGrammar)):
                                    #print('passed',newGrammar)
                                    self.nameGrammars.append(newGrammar)
                        else :
                            if nameClone != '':
                                self.makeGrammars(nameClone,newGrammar)

                    


    def makePart(self,partType,partText):
        canAdd = True
        for part in self.nameParts:
            if (part['partText'] == partText):
                canAdd = False
        
        if(canAdd):
            part = {
                'partType':partType,
                'partText':partText
            }
            self.nameParts.append(part)

    def grammarAsList(self,grammar):
        glist  = (grammar.split('.'))
        if glist[0] == '':
            glist = glist[1:]
        return glist

    '''
    #make sure and pass in full objects
    @classmethod
    def fillNameTemplate(self,id,identifyingName,nameParts,nameGrammars,repeatableLetters,minLength,maxLength):
        self.id = id
        self.identifyingName = identifyingName
        self.nameParts = nameParts
        self.nameGrammars = nameGrammars
        self.repeatableLetters = repeatableLetters
        self.minLength = minLength
        self.maxLength = maxLength
        self.setPickGroup(self)
        

    #object makes its own id
    @classmethod
    def newNameTemplate(self,identifyingName,nameParts,nameGrammars,repeatableLetters,minLength,maxLength):
        self.id = uuid.uuid1()
        self.identifyingName = identifyingName
        self.nameParts = nameParts
        self.nameGrammars = nameGrammars
        self.repeatableLetters = repeatableLetters
        self.minLength = minLength
        self.maxLength = maxLength
        self.setPickGroup(self)

    #makes a name template using a list of names
    @classmethod
    def makeNameTemplate(self,names,templateName):
        #getting all vowels so we can tell the difference between them and consonants later
        vowels = ['a','o','e','i','u']
        #print(vowels)
        #intitialising the objects we will use
        self.identifyingName = templateName
        part = NamePart()
        part.newNamePart('VOID','TOBEIGNORED',0,id)
        self.nameParts = []
        self.id = uuid.uuid1()
        self.nameGrammars = []
        self.repeatableLetters = []
        self.minLength = 0
        self.maxLength = 0
        self.nameParts.append(part)
        ##print(self.nameParts[0].partText)
        #using the names weve appended
        ##print(part.partText,part.partType)
        #setting the default max and min values
        self.maxLength = names[0].__len__()
        self.minLength = names[0].__len__()

        #looping for all the names
        for name in names:
            #getting the max and min values
            if name.__len__() > self.maxLength:
                self.maxLength = name.__len__()
            

            else:
                if name.__len__() < self.minLength:
                    self.minLength = name.__len__()
            #print(name)

        #print(self.maxLength)
        #print(self.minLength)

        #looping for all the names
        for name in names:
            #getting the starts of names
            for i in range(2,4):
                if i <= name.__len__():
                    start = name[0:i]
                    self.MakePart(self, start, 'START')

            

        #looping for all the names
        for name in names:
            #getting the ends of names
            for l in range(2,4):
                if l <= name.__len__():
                        end = name[-l:]
                        self.MakePart(self, end, 'END')

        #looping for all the names
        for name in names:
            #getting ph sounds and repeatables
            for i,letter in enumerate(name):
                if (i>0):
                    previousLetter = name[i-1]
                    ph = previousLetter + letter
                    if (vowels.__contains__(letter) and (not (vowels.__contains__(previousLetter)))) or (vowels.__contains__(previousLetter) and (not (vowels.__contains__(letter)))):
                        self.MakePart(self,ph,'PH')
                    if (previousLetter == letter):
                        rl = RepeatableLetter(self.id,letter)
                        self.repeatableLetters.append(rl)




            #getting c and v values
            for i,letter in enumerate(name):
                if (vowels.__contains__(letter)):
                    self.MakePart(self,letter, 'V')
                else:
                    self.MakePart(self,letter, 'C')

            #automatically generating grammars off the names we will pass in
            self.MakeGrammars(self,names)

            #setting pick counts for the grammars
            self.setPickGroup(self)
            return self

    #this appends a part to the part list if it meets cetain conditions
    def MakePart(self, partTextIn,  partTypeIn):
        np = NamePart()
        np.newNamePart(partTypeIn,partTextIn,1,self.id)
        #print(self.nameParts[0].partText)
        partIsNew = True
        #this loop checks the part doesnt already exist and if it does and is of the correct type we up its pick count
        for part in self.nameParts:
            if(part):
                ##print(part.partText)
                if ((partTextIn == part.partText) and (partTypeIn == part.partType)):
                    part.pickCount += 1
                    partIsNew = False
                else:
                    if (partTextIn == part.partText):
                        partIsNew = False
        if (partIsNew):
            #print(np.partText,np.partType)
            self.nameParts.append(np)
            #print(partTextIn, partTypeIn)
        
        
    def MakeGrammars(self, names):
        #here we will build an algorithm for creating grammars.
        usedGrammarsInForm = []
        for name in names:
            usedGrammarsInForm = self.MakeListGrammarsForName(self,name, [], usedGrammarsInForm)


    def MakeListGrammarsForName(self, unAnalysedPartOfName,currentGrammar,listOfGrammarsAsString):
        #loop for the size of the 
        for i in range(0, unAnalysedPartOfName.__len__() ):
            #if the part is at the start of the unAnalysed portion of the name
            isAPart = False
            np = NamePart()
            for part in self.nameParts:
                if(part):
                    if part.partText == unAnalysedPartOfName[0:unAnalysedPartOfName.__len__() - i]:
                        isAPart = True
                        np = part
            if (isAPart):
                #make a version of the grammar with self part type appended to it
                grammarWithPart = currentGrammar
                grammarWithPart.append(np.partType)

                #if self isnt the end of the name
                if (not ((unAnalysedPartOfName.__len__() - (unAnalysedPartOfName.__len__() - i)) == 0)):
                    #go down anoother level and pass through the part of the name you havent analysed and the state the grammar should be in
                    self.MakeListGrammarsForName(self,unAnalysedPartOfName[0:unAnalysedPartOfName.__len__() - i], grammarWithPart, listOfGrammarsAsString)
                else : # if it is the end of the name
                    #this part checks if the grammar avoids unwanted triplets
                    #default that it does
                    avoidsUnwantedTriples = True
                    if (grammarWithPart.__len__() >= 3):
                        lastIndex = grammarWithPart.__len__() - 1
                        #checks if this grammar fails to avoid unwanted triple consonants or vowels this is a tricky step but improves results alot
                        avoidsUnwantedTriples = (((grammarWithPart[lastIndex - 2] == ('C') or grammarWithPart[lastIndex - 2] == ('START') or grammarWithPart[lastIndex - 2] == ('PH')) and grammarWithPart[lastIndex - 1] == ('C') and grammarWithPart[lastIndex] == ('C'))) or ((grammarWithPart[lastIndex - 2] == ('C') and grammarWithPart[lastIndex - 1] == ('C')) and (grammarWithPart[lastIndex] == ('C') or grammarWithPart[lastIndex] == ('END') or grammarWithPart[lastIndex] == ('PH'))) or (((grammarWithPart[lastIndex - 2] == ('V') or grammarWithPart[lastIndex - 2] == ('START') or grammarWithPart[lastIndex - 2] == ('PH')) and grammarWithPart[lastIndex - 1] == ('V') and grammarWithPart[lastIndex] == ('V')) or (grammarWithPart[lastIndex] == ('V') and grammarWithPart[lastIndex] == ('V') and(grammarWithPart[lastIndex] == ('V') or grammarWithPart[lastIndex] == ('END') or grammarWithPart[lastIndex] == ('PH'))))
                        #inverse the result to find if it succeeds in avoiding triplets
                        avoidsUnwantedTriples = not avoidsUnwantedTriples
                    #if the grammar does try and avoid unwanted triplets
                    if (avoidsUnwantedTriples):
                        #if the grammar has already been appended
                        if (listOfGrammarsAsString.__contains__(str(grammarWithPart))):
                            #up its pick count
                            for grammar in self.nameGrammars:
                                if str(grammar) == str(grammarWithPart):
                                    grammar.pickCount += 1

                        #checks to see if the structure generated is a valid grammar and saves it to a list,
                        #this includes checking the grammar begins with a start and ends in an end or is made of few enough parts then checks of it starts correctly or ends correctly.
                        else:
                            if ((((grammarWithPart[0] == ('START')) and (grammarWithPart[-1] == ('END')))) or (((grammarWithPart.__len__() <= 2) and (grammarWithPart[0] == ('START') or grammarWithPart[-1] == ('END'))))):
                                #append it to your grammar checklist
                                listOfGrammarsAsString.append(str(grammarWithPart))
                                #append it to the models grammars
                                ng = NameGrammar()
                                ng.newNameGrammar(grammarWithPart,1,self.id)
                                ##print(str(ng))
                                self.nameGrammars.append(ng)
        return listOfGrammarsAsString

        
    def setPickGroup(self):
        self.pickGroup = []
        for grammar in self.nameGrammars:
            for _ in range(0,grammar.pickCount):
                self.pickGroup.append(grammar.id)

'''