from uuid import uuid1


import uuid

class Instruction():
    def __init__(self):
        self.id = uuid.uuid1()
        self.nameGrammarId = ''
        self.instructionText = ''

    @classmethod
    def fillInstruction(self,id,nameGrammarId,instructionText):
        self.id = id
        self.nameGrammarId = nameGrammarId
        self.instructionText = instructionText

    @classmethod
    def newInstruction(self,nameGrammarId,instructionText):
        self.id = uuid.uuid1()
        self.nameGrammarId = nameGrammarId
        self.instructionText = instructionText