import mysql.connector


connection = mysql.connector.connect(user = 'Dilmi',database='database',password='Themesha2007@')

cursor = connection.cursor()



def create():
    username = int(input("create your userId NUMBERS ONLY: "))
    last = input("what is your lastname: ")
    first = input("what is your firstname: ")
    insert = "INSERT INTO h (personId, lastname, firstname) VALUES (%s,%s,%s)"
    val = (username,last,first)
    cursor.execute(insert,val)
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
            5. exit 
            
            """)
        choice = int(input("choose an option: "))
        if choice == 1:
            deposit()
        elif choice == 2:
            withdrawal()
        elif choice == 3:
            create()
        elif choice == 4:
            view()
        elif choice == 5:
            print("Thank you for visiting the best bank!")
            break
        else:
            print("Thats an Invalid option")
        # add choices 

def deposit():
    money = 0
    deposit = int(input("Enter your deposits: "))
    money += deposit
        
    insert = "INSERT INTO hello (money,deposits)VALUES(%s,%s)"
    val = (money, deposit)
    cursor.execute(insert,val)
    connection.commit()
    cursor.close()
    connection.close()

def withdrawal(money):
    withdrawal = int(input("Enter your withdrawal: "))
    money -= withdrawal
        
    insert = "INSERT INTO hello (money,withdrawal)VALUES(%s,%s)"
    val = (money, withdrawal)
    cursor.execute(insert,val)
    connection.commit()
    cursor.close()
    connection.close()

def greeting():
    print("Welcome to the best bank in the world: ")
    exists = input("Do you have an existing account: ")
    if exists == "Y" or exists == "y":
        login()
    else:
        create()

def view():
    print("This is your account: ")

    # print account information



greeting()

        

