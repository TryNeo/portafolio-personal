import re


from django.core.exceptions import ValidationError

class Validators(object):
    def __init__(self, value):
        self.value = value
        self.regex_string = '^[a-zA-ZáéíóñÁÉÍÓÚÑ \-]+$'
        self.regex_integer = '^[0-9]+$'
        
    def validateStringLength(self,message,minLength):
        if len(self.value) >= minLength:
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            )
    
    def validateString(self,message):
        if re.search(self.regex_string,self.value):
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


    def validateNumber(self,message):
        if re.search(self.regex_integer,self.value):
            return False
        return ValidationError(
                (message),
                params={'value': self.value},
            ) 
    
    def validateExists(self,message,instance,table,filter):
        try:
            dato = filter
            if not instance.pk:
                return ValidationError(
                    (message),
                    params={'value': self.value},
                    )
            if instance.pk != dato.pk:
                return ValidationError(
                    ('No puedes actualizar el registro, ya existe'),
                    params={'value': self.value},
                    )
        except table.DoesNotExist:
            pass
        return False