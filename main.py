import tkinter as tk
from tkinter import *
import mysql.connector

root = tk.Tk()
first = Frame(root)
second = Frame(root)
third = Frame(root)

first.grid(row = 0, column=0,sticky="nsew")
second.grid(row = 0, column=0,sticky="nsew")
third.grid(row = 0, column=0, sticky="nsew")


label1 = Label(first, text= 'Welcome to the BEST BANK')
label1.pack(pady = 20)
label12 = Label(first, text= 'Do you have an Account?')
label12.pack(pady = 20)
label2 = Label(second, text= 'CREATE AN ACCOUNT')
label2.pack(pady = 20)
label3 = Label(third, text= 'SIGN IN')
label3.pack(pady = 20)

button1 = Button(first, text="NO", command=lambda:second.tkraise())
button2 = Button(first, text="Yes", command=lambda:third.tkraise())
button1.pack()
button2.pack()

lastname = Label(second, text="Lastname: ")

lastname_field = Entry()

# first is the welcome page
# second is the create account page
# third is the sign in page

#second page



first.tkraise()
root.geometry("650x650")
root.title("Best Bank!")
root.resizable(False, False)


root.mainloop()


connection = mysql.connector.connect(user = 'Dilmi',database='database',password='Themesha2007@')

cursor = connection.cursor()

def create():
    username = int(input("create your userId NUMBERS ONLY: "))
    last = input("what is your lastname: ")
    first = input("what is your firstname: ")
    insert = "INSERT INTO h (personId, lastname, firstname) VALUES (%s,%s,%s)"
    val = (username,last,first)
    cursor.execute(insert,val)
    #putting the values into a table, so that user can sign in later
    print("Please RUN again, and go to Sign-in page")
    connection.commit()
    cursor.close()
    connection.close()

def login():
    count = 0
    while True: 
        select = "SELECT * FROM h WHERE personId= %s"
        logger = int(input("What is your userId: "))
        cursor.execute(select, (logger, ))
        if cursor.fetchall():
        # looking through all the entries in the table to make sure userId is there
            print("Successfully logged in")
            break
        else:
            count += 1
            if count >= 3:
                print("Sorry you cannot login :/")
                break
            else:
                print("Please try again: ")

    menu()
                


def menu():
    while True:
        print("""
            1. Deposit Money
            2. Withdrawal Money
            3. Create new Account
            4. View Account
            5. Delete Account
            6. exit 
            
            """)
        choice = int(input("choose an option: "))
        #user has to pick the choices they want to make
        if choice == 1:
            deposit()
        elif choice == 2:
            withdrawal()
        elif choice == 3:
            create()
        elif choice == 4:
            view()
        elif choice == 5:
            delete()
        elif choice ==6:
            print("Thank you for visiting the best bank!")
            break
        else:
            print("Thats an Invalid option")
        # add choices 

def deposit():
    money = 0
   
    userId = int(input("Enter account userId: "))
    deposits = int(input("Enter your deposits: "))
    money = deposits
    insert = "INSERT INTO hello (money, deposits,checkUser)VALUES(%s, %s,%s)"
    val = (money, deposits,userId)
    cursor.execute(insert,val)
      
        
        # inserting all the 
    sql = "SELECT h.personId, hello.deposits FROM h INNER JOIN  hello ON h.personId = hello.checkUser;"  
    cursor.execute(sql) 
    result = cursor.fetchall()
    print("These are all your past deposits")
    for x in result:
        print(x)
    cursor.execute("SELECT SUM(deposits) FROM hello")
    print("Current balance")
    print(cursor.fetchall()[[0][0]])
    
        # I checked if the userId given was correct, and compared it to the personId in the mySQL table
        # I tried to join the tables so that the program can recognize that every user has a different balance
    connection.commit()


def withdrawal():
    money = 0
    userId = int(input("Enter account userId: "))
    withdrawal = int(input("Enter your withdrawal amount: "))
    money -= withdrawal
    insert = "INSERT INTO hello (money,withdrawal,checkUser)VALUES(%s,%s,%s)"
    val = (money, withdrawal,userId)
    cursor.execute(insert,val)
    
    # inserting all the 
    sql = "SELECT h.personId, hello.withdrawal FROM h INNER JOIN  hello ON h.personId = hello.checkUser;"  
    cursor.execute(sql) 
    result = cursor.fetchall()
    print("This is your withdrawal history")
    for x in result:
        print(x)
    cursor.execute("SELECT SUM(money) FROM hello")
    print("Current balance")
    print(cursor.fetchall()[[0][0]])
    # I checked if the userId given was correct, and compared it to the personId in the mySQL table
    # I tried to join the tables so that the program can recognize that every user has a different balance
    
 
    connection.commit()
    

def greeting():
    print("Welcome to the best bank in the world: ")
    user = input("Do you have an account")
    if user == "Y" or user == "y":
        login()
        # checking if user has an account already
    else:
        create()

def view():
    userId = input("Enter account userId: ")
    cursor.execute("SELECT * FROM h where personId= '"+ userId +"'")
    for i in cursor:
        print(i)
def delete():
    choice = input("Enter the userId of the account you want to delete: ")
    cursor.execute("DELETE FROM h where personId = '"+ choice + "'")
    print("Successfully deleted your account")
    connection.commit()
    # print account information



greeting()

        

