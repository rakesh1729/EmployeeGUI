import sqlite3

class Database:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee_list(id INTEGER PRIMARY KEY,name text,age integer,doj integer,email text)")
        self.conn.commit()
        # conn.close()

    def insert(self, name, age, doj, email):
        # conn=sqlite3.connect("company.db")
        # cur=conn.cursor()
        self.cur.execute("INSERT INTO  employee_list VALUES (NULL, ?, ?, ?, ?)",(name, age, doj, email))
        self.conn.commit()
        # conn.close()

    def view(self):
        # conn=sqlite3.connect("company.db")
        # cur=conn.cursor()
        self.cur.execute("SELECT * FROM employee_list")
        rows=self.cur.fetchall()
        # conn.close()
        return rows

    def search(self, name="", age="", doj="", email=""):
        # conn=sqlite3.connect("company.db")
        # cur=conn.cursor()
        self.cur.execute("SELECT * FROM employee_list WHERE name=? OR age=? OR doj=? OR email=?",(name, age, doj, email))
        rows=self.cur.fetchall()
        # conn.close()
        return rows

    def delete(self, id):
        # conn=sqlite3.connect("company.db")
        # cur=conn.cursor()
        self.cur.execute("DELETE FROM employee_list WHERE id=?" ,(id,))
        self.conn.commit()
        # conn.close()
        # return rows

    def update(self, id,name,age,doj,email):
        # conn=sqlite3.connect("company.db")
        # cur=conn.cursor()
        self.cur.execute("UPDATE employee_list SET name=?, age=?, doj=?, email=? WHERE id=?",(name,age,doj,email,id))
        self.conn.commit()
        # conn.close()

    def  __del__(self):
        self.conn.close()
