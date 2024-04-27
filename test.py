import mysql.connector

connection = mysql.connector.connect(user = 'Dilmi',database='database',password='Themesha2007@')

cursor = connection.cursor()

def greeting(user):
    print("Welcome to the best bank in the world: ")
    if user == "Y" or user == "y":
        return True
        # checking if user has an account already
    elif user == "n" or "N":
        return True
    else:
        return False
    
print(greeting("n"))
print(greeting("y"))
print(greeting("x"))