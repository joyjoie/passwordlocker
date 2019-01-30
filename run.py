#!/usr/bin/env python3.6
import pyperclip
from user import User
from credentials import Credentials

def create_user(username,password,email):
  '''
  Function to create a new user
  '''
  new_user = User(username,password,email)
  return new_user
def save_user(user):
  '''
  Function to save user
  '''
  user.save_user()
def delete_user(user):
    '''
    This function deletes a user 
    '''
    user.delete_user()

def create_new_credential(credential_detail,password):
    ''' 
    This function allows a user create a new credential account
    '''
    new_credential = Credentials(credential_detail ,_password)
    return new_credential

def save_new_credentials(credential):
    ''' 
    This is a function to save new credentials created 
    '''
    credential.save_credential()

def delete_credentials(credential):
    '''
    This is a function to delete credentials by the user 
    '''
    return Credentials.delete_credential(credential)

def verify_user(name):
	'''
	Function that checks if the username already exists in the system
	'''
	checking_user = Credentials.find_by_name(name)
	return checking_user
 
def find_credentials(credential_detail):
   '''
     Function to find stored credentials
    '''
   return Credentials.find_by_name(credential_detail)

def check_existing_credentials(name):
   '''
   Function to check if an inputed credential name exists
    '''
   return Credentials.find_by_name(name)

def copy_credential(credential_detail):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_credential(credential_detail)

def display_credential():
    '''
    Function to display credentials of an account
    '''
    return Credentials.display_credential()

def generate_password():
    '''
    This is a function to generate random password
    '''
    gen_pass = Credentials.generate_password()
    return gen_pass
def display_user():
    '''
    Function to display user of an account
    '''
    return User.display_user()


def main():
    print("Hello Welcome to your login. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
        print("Use these short codes : cd - create new details, dc - display details, ex -exit the program  ")
        short_code = input().lower()
        if short_code == 'cd':
            print("New Contact")
            print("-"*10)
            user_name = input()
            print ("User name ....")
            email = input()
            print("Email address ...")
            password = input()
            print("Password ...")
                  
            save_user(create_user(user_name,email,password)) # create and save new details.
            print ('\n')
            print(f"New User {user_name} {email} {password} created")
            print ('\n')
        elif short_code == 'dc':
            
                print("Here is a list of your details")
                print('\n')
                for user in display_user():
                    print(f"{user_name}... {email} .....")
                    print('\n')
                    
            # print(f"{user_name} {email} {password}")
            # else:
            #     print('\n')
            #     print("You dont seem to have any details saved yet")
            #     print('\n')
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    
    main()