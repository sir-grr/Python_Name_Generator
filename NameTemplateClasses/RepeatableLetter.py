import uuid

class RepeatableLetter():
    def __inti__(self):
        self.id = uuid.uuid1()
        self.nameTemplateId = ''
        self.letter = ''

    @classmethod
    def fillRepeatableLetter(self,id,nameTemplateId,letter):
        self.id = id
        self.nameTemplateId = nameTemplateId
        self.letter = letter

    @classmethod
    def newRepeatableLetter(self,nameTemplateId,letter):
        self.id = uuid.uuid1()
        self.nameTemplateId = nameTemplateId
        self.letter = letter