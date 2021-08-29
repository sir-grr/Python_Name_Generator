import uuid

class NameGrammar:
    def __init__(self):
        self.id = uuid.uuid1()
        self.instructions = []
        self.pickCount = 0
        self.nameTemplateId = ''

    @classmethod
    def fillNameGrammar(self,id,instructions,pickCount,nameTemplateId):
        self.id = id
        self.instructions = instructions
        self.pickCount = pickCount
        self.nameTemplateId = nameTemplateId

    @classmethod
    def newNameGrammar(self,instructions,pickCount,nameTemplateId):
        self.id = uuid.uuid1()
        self.instructions = instructions
        self.pickCount = pickCount
        self.nameTemplateId = nameTemplateId