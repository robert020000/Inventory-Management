#import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox

conn=mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='')
mycursor = conn.cursor()
mycursor.execute("SELECT from inventory")
result = mycursor.fetchall()
for r in result:
    id=r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
         self.master=master
         self.heading=Label(master,text="Stocks Update",font=('arial 40 bold'),fg='steelblue')
         self.heading.place(x=400,y=0)



          #text box for the log
         self.tbBox=Text(master,width=150,height=18)
         self.tbBox.place(x=75,y=75)
         self.tbBox.insert(END,"stocks :"+str(id))
         

    def search(self, *args, **kwargs):
         mycursor.execute("SELECT * FROM inventory WHERE stock=%s",[self.id_leb.get()])
         result = mycursor.fetchall()
         for r in result:
              self.n1 = r[1]  # name
              self.n2 = r[2]  # stock
              self.n3 = r[3]  # cp
         conn.commit()

          #inster into the enteries to update
         self.name_e.delete(0,END)
         self.name_e.insert(0, str(self.n1))

         self.stock_e.delete(0, END)
         self.stock_e.insert(0, str(self.n2))

         self.cp_e.delete(0, END)
         self.cp_e.insert(0, str(self.n3))

    def update(self,*args,**kwargs):
          self.u1=self.name_e.get()
          self.u2 = self.stock_e.get()
          self.u3 = self.cp_e.get()


          mycursor.execute("UPDATE  inventory SET name=%s,stock=%s,price=%s WHERE id=%s",[self.u1,self.u2,self.u3,self.id_leb.get()])
          conn.commit()
          tkinter.messagebox.showinfo("Success","Update Database successfully")

root=Tk()
b=Database(root)
root.geometry("1366x768+0+0")
root.title("Update to the database")
root.mainloop()