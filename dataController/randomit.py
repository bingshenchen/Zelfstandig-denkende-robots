import random
import sqlite3
afbet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z']
Afbet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'U', 'W', 'X', 'Y', 'Z']
vowel = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v', 'w','x','y','z']
numbber = [i for i in range(-9,10)]

conn = sqlite3.connect("try.db")
curr = conn.cursor()

def creatdata():
    
    creatTableCommand = """CREATE TABLE IF NOT EXISTS NSA_DATA (
    username VARCHAR(50),
    phonenumber VARCHAR(15),
    password VARCHAR(50),
    baddeedcount INT,
    secrets VARCHAR(250)
    );

    """

    curr.execute(creatTableCommand)
    conn.commit()
def adddatat(username,phonenumber,password,baddeedcount,secrets):
    addData = 'INSERT INTO NSA_DATA VALUES(?,?,?,?,?)'
    curr.execute(addData,(username,phonenumber,password,baddeedcount,secrets))
    conn.commit()

def viewGeg():
    cur.execute("SELECT username FROM NSA_DATA")
    rows = cur.fetchall()
    con.close()
    return rows

def selectData():
    curr.execute("SELECT * FROM NSA_DATA")
    rows = curr.fetchall()
    return rows

def likeData(v):
    curr.execute("SELECT * FROM NSA_DATA WHERE username LIKE " + "'%" + str(v) + "%'")
    rows = curr.fetchall()
    return rows
    
def rdusern():
    username = ''
    for i in range(0,random.randint(4,11)):
        username += str(random.choice(afbet))
    return username

def rdtmn():
    teamname = ''
    for i in range(0,random.randint(5,11)):
        if len(teamname)%2 == 0:
            for i in range(1,random.randint(1,2)):
               teamname += str(random.choice(consonant))
        else:
            teamname += str(random.choice(vowel))
    return teamname

        
def rdtel():
    tel = ''
    for i in range(0,random.randint(8,11)):
        tel += str(random.randint(1,9))
    return tel

def rddata():
    adddatat(rdusern(),rdtel(),rdtel(),rdtel(),rdtel())

def doit(i):
    for n in range(0, i):
        rddata()
        
creatdata()
#adddatat('iker','123','123','123','123')
#conn.close()
