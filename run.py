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
  user.save_contact()
​
def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()
​
def create_credential (user,password):
  '''
  Function that finds a user by number and returns the contact
  '''
  return Contact.find_by_number(number)
​
def check_existing_contacts(user_details,password):
  '''
  Function that checks if a user exists with that password and return a Boolean
  '''
  return Contact.contact_exist(number)
​
def display_contacts():
  '''
  Function that returns all the saved contacts
  '''
  return Contact.display_contacts()
​
def main():
      print("Hello Welcome to your contact list. What is your name?")
      user_name = input()
​
      print(f"Hello {user_name}. what would you like to do?")
      print('\n')
​
      while True:
          print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")
​
          short_code = input().lower()
​
          if short_code == 'cc':
              print("New Contact")
              print("-"*10)
​
              print ("First name ....")
              f_name = input("please enter your first name: ")
​
              print("Last name ...")
              l_name = input()
​
              print("Phone number ...")
              p_number = input()
​
              print("Email address ...")
              e_address = input()
​
​
              save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
              print ('\n')
              print(f"New Contact {f_name} {l_name} created")
              print ('\n')
​
          elif short_code == 'dc':
​
              if display_contacts():
                  print("Here is a list of all your contacts")
                  print('\n')
​
                  for contact in display_contacts():
                      print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")
​
                  print('\n')
              else:
                  print('\n')
                  print("You dont seem to have any contacts saved yet")
                  print('\n')
​
          elif short_code == 'fc':
​
              print("Enter the number you want to search for")
​
              search_number = input()
              if check_existing_contacts(search_number):
                  search_contact = find_contact(search_number)
                  print(f"{search_contact.first_name} {search_contact.last_name}")
                  print('-' * 20)
​
                  print(f"Phone number.......{search_contact.phone_number}")
                  print(f"Email address.......{search_contact.email}")
              else:
                  print("That contact does not exist")
​
          elif short_code == "ex":
              print("Bye .......")
              break
          else:
              print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
​
  main()      