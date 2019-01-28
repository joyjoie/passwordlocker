import pyperclip

class User:
    '''
    class that generates new instances of user
    '''
    user_list = []
    def __init__(self,username,,password,email,):
        '''__init__ methods helps us define properties for out objects
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
  
   