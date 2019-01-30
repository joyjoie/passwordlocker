import pyperclip

class User:
    '''
    class that generates new instances of user
    '''
    user_list = []
    def __init__(self,user_name,password,email,):
        '''__init__ methods helps us define properties for out objects
        '''
        #this is an example of a comment
        self.user_name = user_name
        self.password = password
        self.email = email

    #user_list = [] # Empty user list
    def save_user(self):
        '''save_user method saves user objects into user list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        '''
    Function to display user of an account
    '''
        return cls.user_list

    
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
  
   