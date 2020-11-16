import sqlite3, time

def is_valid_username(username):
   
    find_user = ("SELECT * FROM user WHERE username = ?")
    cursor.execute(find_user,[(username)])
    results = cursor.fetchall()             
    return results

def is_valid_password(username, password):

    find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
    cursor.execute(find_user, [(username), (password)])
    result = cursor.fetchall()
    return result

def create_new_user():
    while True:
        username = input("Enter a new username: ")
        find_user = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(find_user, [(username)])

        if (cursor.fetchall()):
            print("Username taken, please try again")
        else:
            break
    firstName = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    password = input("Enter your password: ")
    repassword = input("Reenter your password: ")
    while password != repassword:
        print("Passwords do not match, try again.")
        password = input("Enter your password: ")
        repassword = input("Reenter your password: ")
    insert = "INSERT INTO user(username, firstname, surname, password) VALUES(?,?,?,?)"
    cursor.execute(insert, [(username), (firstName), (surname), (password)])
    db.commit()
    print("Account created")
    time.sleep(2)
    return

with sqlite3.connect("Users.db") as db:
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    userID INTEGER PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL);
    ''')
        
for i in range(3):
    username = input("Please input username: ")
    if (is_valid_username(username)):
        password = input("Please input password: ")
        if is_valid_password(username, password):
            print('Username and password accepted, welcome.')
            time.sleep(3)
            exit()
        else:
            print("Incorrect password, please try again?: ")
    else:
        Q1 = input("Not valid user. Would you like to create an account?: ")
        reply_yes = ('y', 'yes')
        if Q1.lower() in reply_yes:
            create_new_user()
            

