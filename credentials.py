import pyperclip
import random
import string
class Credentials:
    '''
    class that generates  instances of credential
    '''
    credential_list = []
    def __init__(self,credential_detail,password,):
        '''__init__ methods helps us define properties for our objects
        '''
        #this is an example of a comment
        self.credential_detail = credential_detail
        self.password = password
      

    #credential_list = [] # Empty credential list
    def save_credential(self):
        '''save_credential method saves credentials objects into list
        '''
        Credentials.credential_list.append(self)
    
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential ser from the user_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_name(cls,credential_detail):
        '''
        This method helps to search through the credential list using the username.
        '''
        for credential in cls.credential_list:
            if credential.credential_detail ==credential_detail:
                return credential

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: password to search for
        Returns :
            credentials of person that matches the password.
        '''

        for credentials in cls.credential_list:
            if credentials.password== password:
                return credentials

    @classmethod
    def display_credential(cls):
        """
        Method which displays all credentials list
        """
        return cls.credential_list

    def generate_password(stringLength=8,char= string.ascii_letters+string.digits):
        '''
        This is a method to generate random string passwords for the application
        '''

        gen_pass = ''.join(random.choice(char) for i in range(stringLength))
        return gen_pass

    @classmethod
    def credential_exists(cls,name):
        '''
        The method would check if any credential exists
    
        '''
        for credentials in cls.credential_list:
            if credential.credential_detail == name:
                    return True

        return False


