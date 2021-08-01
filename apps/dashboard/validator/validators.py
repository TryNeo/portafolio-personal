import re


from django.core.exceptions import ValidationError

class Validators(object):
    def __init__(self, value):
        self.value = value
        self.regex_string = '^[a-zA-ZáéíóñÁÉÍÓÚÑ \-]+$'
        
    def validateStringLength(self,message,minLength):
        if len(self.value) >= minLength:
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )
    
    def validateString(self,message):
        if(re.search(self.regex_string,self.value)):
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )    

    def validateEmptyField(self,message):
        if len(str(self.value)) >= 2:
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )