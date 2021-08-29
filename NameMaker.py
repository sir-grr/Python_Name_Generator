from random import randint,seed,choice
import uuid
import copy
from copy import deepcopy
from NameTemplateClasses.NameTemplate import NameTemplate

class NameMaker():

    def __init__(self,nameTemplate):
        self.nameTemplate = nameTemplate
        seed(uuid.uuid1())

    def grammarAsList(self,grammar):
        glist  = (grammar.split('.'))
        if glist[0] == '':
            glist = glist[1:]
        return glist

    #this generates a single name based on an input NameTemplate

    def generateName(self):
        #y is included here as a vowel so it can be included in triple consonants 
        vowels = ['a', 'e', 'i', 'o', 'u','y' ]
        grammar = self.grammarAsList(choice(self.nameTemplate.nameGrammars))
        name = ''
        for instruction in grammar:
            if instruction:
                textAvailable = []
                for part in self.nameTemplate.nameParts:
                    if part:
                        if part['partType'] == instruction:
                            textAvailable.append(part['partText'])
                name += choice(textAvailable)
        #print('after using grammar')
        #print(name)
        nameCopy = ''
            
        if (name.__len__() > 2):
            #works by making a copy of the string and then creating a new one without unwanted duplicates
            for p,letter in enumerate(name):
                if(letter):
                    if p>0:
                        previousLetter = name[p-1]
                        if (letter == previousLetter) and (not(self.nameTemplate.repeatableLetters.__contains__(letter))):
                            letter = ''
                nameCopy += letter

            #the reason we are deep copying the name we just made as a copy is to avoid the original name having its properties while things change in the loop or when we set it to blank
            ##print('after double fixer',nameCopy)
            name = copy.deepcopy(nameCopy)
            nameCopy = ''

            for j,letter in enumerate(name):
                if(letter):
                    if j >= 2:
                        letterBehind = name[j-1]
                        letterBehindBehind = name[j-2]
                        #print('letters',letter,letterBehind,letterBehindBehind)
                        areAllVowels = (vowels.__contains__(letter))and(vowels.__contains__(letterBehind))and(vowels.__contains__(letterBehindBehind))
                        areAllConsonants = ( (not (vowels.__contains__(letter))) and ( not(vowels.__contains__(letterBehind))) and  ( not (vowels.__contains__(letterBehindBehind))))
                        if areAllVowels or areAllConsonants:
                            #print('removing',letter)
                            letter = ''
                nameCopy += letter
                #print(nameCopy)
            #print('after triple fixer',nameCopy)
            name = copy.deepcopy(nameCopy)

        nameLength = name.__len__()
        if (nameLength < self.nameTemplate.minLength):
            return self.generateName()
        else:
            if (nameLength > self.nameTemplate.maxLength):
                return self.generateName()
        name = name.capitalize()
        return name


    #this method generates random names based on entire name models.
    def generateNames(self, numberOfNames):
        pickedNames = []
        #print('using',self.nameTemplate.identifyingName)
        #Generate Names
        while numberOfNames > pickedNames.__len__():
            randomName = self.generateName()
            pickedNames.append(randomName)
            #print(randomName)
        return pickedNames
