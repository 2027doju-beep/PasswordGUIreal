import sqlite3
import hashlib

def createUserTable():
   con = sqlite3.connect("user.db")
   cur = con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS users(name, email, password, birthdate)")

   con.commit() # save changes

   con.close() # end connection

def createRoleTable():
    con = sqlite3.connect("user.db") #create or access database file
    cur = con.cursor() #WE need this to do anything in our database

    cur.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        email TEXT,
        role TEXT,
        viewuser BOOLEAN,
        updateuser BOOLEAN,
        deleteuser BOOLEAN
    )
    """)

    con.commit()  # save changes
    con.close()  # end connection

#login function -> check for matchign username + password combo

def loginAttempt(email, password):
    """
    Login a user or return false
    :param email: email address
    :param password: password
    :return: True if found, false otherwise
    """
    con = sqlite3.connect("user.db")  # only open once
    cur = con.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    results = cur.execute("SELECT email, password FROM users")
    for curRow in results.fetchall():
        if email == curRow[0]:
            if hashed_password == curRow[1]:
                print("Login successful")
                con.close()
                return True
            con.close()
            return False

    con.close()
    return False
    # return password == result[0]

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

def updateRole(email, role):
    VALID_ROLES = ["admin", "user", "employee"]

    if role not in VALID_ROLES:
        print(f"Invalid role '{role}'. Must be one of: {VALID_ROLES}")
        return False

    con = sqlite3.connect("user.db")
    cur = con.cursor()

    cur.execute("SELECT email FROM roles WHERE email = ?", (email,))
    result = cur.fetchone()

    if result is None:
        print(f"No user found with email '{email}'. No change made.")
        con.close()
        return False

    cur.execute("UPDATE roles SET role = ? WHERE email = ?", (role, email))
    con.commit()
    print(f"Role updated to '{role}' for {email}.")
    con.close()
    return True


def lookupRole(email, password):
    conn = sqlite3.connect("user.db")
    cur = conn.cursor()

    sql = """
    SELECT users.email, roles.role
    FROM users
    JOIN roles
    ON users.email = roles.email
    WHERE users.email=? AND users.password=?
    """

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cur.execute(sql, (email, hashed_password))
    result = cur.fetchone()
    print(result)

    conn.close()

    if result:
        return result[1]
    else:
        return None

from datetime import datetime

def isOldEnough(birthdate):
    birth = datetime.strptime(birthdate, "%m/%d/%y")  # ← lowercase %y instead of %Y
    today = datetime.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age >= 13

def createUser(name, email, password, birthdate = None):
   if lookupUser(email) == False:
       con = sqlite3.connect("user.db")  # create/access database file


       cur = con.cursor()  # we need this to do anything in our database

       hashed_password = hashlib.sha256(password.encode()).hexdigest() #This converts the plain text password into a hash, then passing hashed_password into the INSERT instead of password.
       cur.execute("INSERT INTO users VALUES(?,?,?,?)", (name, email, hashed_password, birthdate))
       cur.execute("INSERT INTO roles VALUES(?,?,?,?,?)", (email, "user", False, False, False))
       con.commit()  # save changes
       con.close()  # end connection
   else:
       print("User already exists.")


    #only creates user when they didnt exist)
