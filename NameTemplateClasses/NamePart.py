import uuid

class NamePart():
    def __init__(self):
        self.id = uuid.uuid1()
        self.partType = ''
        self.partText = ''
        self.pickCount = 0
        self.nameTemplateId = ''
        
    def fillNamePart(self,id,partType,partText,pickCount,nameTemplateId):
        self.id = id
        self.partType = partType
        self.partText = partText
        self.pickCount = pickCount
        self.nameTemplateId = nameTemplateId

    def newNamePart(self,partType,partText,pickCount,nameTemplateId):
        self.id = uuid.uuid1()
        self.partType = partType
        self.partText = partText
        self.pickCount = pickCount
        self.nameTemplateId = nameTemplateId
