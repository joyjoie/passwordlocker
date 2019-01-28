import pyperclip

class Credentials:
    '''
    class that generates  instances of credential
    '''
   credential_list = []
    def __init__(self,user_detail,password,):
        '''__init__ methods helps us define properties for our objects
        '''
        #this is an example of a comment
        self.username = username
        self.password = password
        self.email = email

    #user_list = [] # Empty user list
    def save_user(self):
        '''save_user method saves user objects into user list
        '''
        user.user_list.append(self)
    
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        user.user_list.remove(self)
  
    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: password to search for
        Returns :
            user of person that matches the password.
        '''

        for user in cls.user_list:
            if user.password== password:
                return user
    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            password: Password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.password == password:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,password):
        user_found = user.find_by_password(password)
        pyperclip.copy(user_found.email) 
