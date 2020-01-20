
import sqlite3

conn = sqlite3.connect("drill1.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fname TEXT)") 
conn.commit()
conn.close()

import os

for file in os.listdir("C:\\Users\\thebl\\OneDrive\\Desktop\\pyDrill2"):
    x = (os.path.join("C:\\Users\\thebl\\OneDrive\\Desktop\\pyDrill2", file))
    if file.endswith(".txt"):
        conn = sqlite3.connect("drill1.db")
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_txt(col_fname) VALUES (?)",(x,))
            conn.commit()
conn.close()
        
    
conn = sqlite3.connect("drill1.db")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname FROM tbl_txt")
    varPerson = cur.fetchall()
    print (varPerson)

