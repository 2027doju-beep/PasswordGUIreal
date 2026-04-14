import sqlite3


def createUserTable():


   con = sqlite3.connect("user.db")  # create/access database file


   cur = con.cursor()  # we need this to do anything in our database


   cur.execute("DROP TABLE users") # create a new table
   cur.execute("CREATE TABLE users(name, email, password, birthdate)") # create a new table


   con.commit() # save changes

   con.close() # end connection

def createRoleTable():
    con = sqlite3.connect("user.db") #create or access database file
    cur = con.cursor() #WE need this to do anything in our database

    cur.execute("CREATE TABLE roles(email, role, viewuser, updateuser, deleteuser)")  # create a new table

    con.commit()  # save changes
    con.close()  # end connection


#login function -> check for matchign username + password combo

def loginAttempt(email, password):
    """
    Login a user or return false
    :param email: email address
    :param password: password
    :return: True if found false otherwise
    """
    con = sqlite3.connect("user.db")  # create/access database file

    cur = con.cursor()  # we need this to do anything in our database

    #find the user with this email address
    results = cur.execute("SELECT email, password FROM users")  # create a new table
    for curRow in results.fetchall():
        if email in curRow[0]:  #if we do --> check if the password matches to the email.
            if password == curRow[1]: #yes --> successful login! Return true
                print("Login successful")
                con.close() #end connection
                return True
            #yes --> return True
            print(curRow[1])
            con.close()
            return True

    con.close() #end connection
    return True
    #if we dont --> return False
loginAttempt("2027doju@seisen.com", "juliepassword")

def lookupUser(email):
   con = sqlite3.connect("user.db")  # create/access database file


   cur = con.cursor()  # we need this to do anything in our database


   results = cur.execute("SELECT email FROM users")  # create a new table
   for CurRow in results.fetchall():
       if email in CurRow:
           con.close()  # end connection
           return True


   con.close()  # end connection
   return False


print(lookupUser("2027doju@seisen.com"))

def createUser(name, email, password, birthdate = None):
   if lookupUser(email) == False:
       con = sqlite3.connect("user.db")  # create/access database file


       cur = con.cursor()  # we need this to do anything in our database


       cur.execute("INSERT INTO users VALUES(?,?,?,?)", (name, email, password, birthdate)) # create a new table
       cur.execute("INSERT INTO roles VALUES(?,?,?,?,?)", (email, "user", False, False, False))

       con.commit()  # save changes
       con.close()  # end connection
   else:
       print("User already exists.")


    #only creates user when they didnt exist)

#createUserTable()
#createUser("Julie", "2027doju@seisen.com", "juliepassword", "0815")


#createRoleTable()
