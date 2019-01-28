#!/usr/bin/env python3.6
import pyperclip
​
def create_user(username,password,email):
  '''
  Function to create a newuser
  '''
  new_user = User(username,password,email)
  return new_user
​
def save_user(user):
  '''
  Function to save user
  '''
  user.save_user()
​
def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()
​
def create_credential (username,password):
  '''
  Function that allows user to add new details in their account
  '''
  create_credent = Credentials(username ,password)
  return create_credent

def save_credential (credential):
      '''
  Function that allows user to save new details in their account
  '''
  return create_credent

def verify_user(name):
    	'''
	Function that checks if the username already exists in the system
	'''
	checking_user = Credentials.find_by_name(name)
	return checking_user

def find_credentials(credential_details):
   '''
     Function to find credentials that exist
    '''
   return Credentials.find_by_name(credential_details)

def check_existing_credentials(cedential_details):
       '''
   Function to check if an inputed credential name exists
    '''
   return Credentials.find_by_name(credential_details)

def copy_credential(credential_details):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_credential(credential_details)
