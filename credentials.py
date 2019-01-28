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
        self.credential_detail = credentialdetail
        self.password = password
        self.email = email

    #cedential_list = [] # Empty credential list
    def save_credential(self):
        '''save_credential method saves credentials objects into list
        '''
        Credentials.credential_list.append(self)
    
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential ser from the user_list
        '''

        credential.credential_list.remove(self)
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
    def credentials_exist(cls,password):
        '''
        Method that checks if a credential exists from the user list.
        Args:
            password: Password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                    return True

        return False


