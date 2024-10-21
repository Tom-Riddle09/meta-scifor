import tkinter as tk
from tkinter import messagebox
import pickle

class Form(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Student Managment System")
    #self.geometry("500x400")
    self.info = {'name':'','age':'','gender':'','contact':'','id':0}
    #creating Screens
    self.homescreen = HomeScreen(self)
    self.addstudent = AddStudent(self)
    self.searchscreen = SearchScreen(self) 
    #self.modifyscreen = ModifyScreen(self)
    self.viewscreen = ViewScreen(self) # option to delete student details.

    self.switch_screen(self.homescreen)

  def switch_screen(self, screen):
    screen.tkraise()

class HomeScreen(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self,parent)
    self.grid(row=0,column=0,sticky='nsew')

    #creating widgets
    self.heading = tk.Label(self, text="Student Management System", font = ('Ariel',20))
    self.heading.grid(row=0, column=0, columnspan=2, padx=40, pady=30)

    self.addstudent_btn = tk.Button(self,text='Add Student', font = ('Ariel',16), command=lambda: parent.switch_screen(parent.addstudent))
    self.addstudent_btn.grid(row = 1, column = 0, padx = 120, pady = 10)

    self.searchstudent_btn = tk.Button(self,text='Search', font = ('Ariel',16),command= lambda: parent.switch_screen(parent.searchscreen))
    self.searchstudent_btn.grid(row= 2, column = 0, padx = 120, pady = 10)


class AddStudent(tk.Frame):
  def __init__(self,parent):
    tk.Frame.__init__(self,parent)
    self.grid(row=0,column=0,sticky='nsew')
    with open('database.p','rb') as file:
      self.data = pickle.load(file) #loading database file
    self.current_id = self.data['current_id']
    flag = False
    #creating widgets
    self.heading = tk.Label(self, text='Student Details', font = ('Ariel',20))
    self.heading.grid(row = 0, column = 0, columnspan = 2 , padx = 100 ,pady = 10)

    self.name_label = tk.Label(self, text = 'Name', font = ('Ariel',12))
    self.name_label.grid(row = 1, column=0,pady = 10)
    self.name_entry = tk.Entry(self, font = ('Ariel',12))
    self.name_entry.grid(row = 1, column = 1, pady = 10)

    self.age_label = tk.Label(self, text = 'Age', font = ('Ariel',12))
    self.age_label.grid(row = 2, column=0,pady = 10)
    self.age_entry = tk.Entry(self, font = ('Ariel',12))
    self.age_entry.grid(row = 2, column = 1, pady = 10)

    self.gender_label = tk.Label(self, text = 'Gender', font = ('Ariel',12))
    self.gender_label.grid(row = 3, column=0,pady = 10)
    self.gender_entry = tk.Entry(self, font = ('Ariel',12))
    self.gender_entry.grid(row = 3, column = 1, pady = 10)

    self.contact_label = tk.Label(self, text = 'Contact', font = ('Ariel',12))
    self.contact_label.grid(row = 4, column=0,pady = 10)
    self.contact_entry = tk.Entry(self, font = ('Ariel',12))
    self.contact_entry.grid(row = 4, column = 1, pady = 10)

    self.back_btn = tk.Button(self,text='< Back',font=('Ariel',10),borderwidth=0,command= lambda: parent.switch_screen(parent.homescreen))
    self.back_btn.grid(row=0,column=0,sticky='nw')

    self.current_id += 1

    self.submit_btn = tk.Button(self,text='Submit',font=('Ariel',14),command= self.submit)
    self.submit_btn.grid(row=5,column=0,columnspan=2,pady=10)

  def update_info(self,parent):
    self.name_entry.delete(0, tk.END)  # Clear any existing text
    self.name_entry.insert(0, parent.info['name'])

    self.age_entry.delete(0, tk.END)  # Clear any existing text
    self.age_entry.insert(0, parent.info['age'])

    self.gender_entry.delete(0, tk.END)  # Clear any existing text
    self.gender_entry.insert(0, parent.info['gender'])

    self.contact_entry.delete(0, tk.END)  # Clear any existing text
    self.contact_entry.insert(0, parent.info['contact'])

    self.current_id = parent.info['id']

  def submit(self):
    name = self.name_entry.get()
    age = self.age_entry.get()
    gender = self.gender_entry.get()
    contact = self.contact_entry.get()
    details = {'id':self.current_id,'name':name, 'age':age, 'gender':gender, 'contact':contact}
    self.data[name] = details
    self.data['current_id'] = self.current_id
    with open('database.p','wb') as file:
      pickle.dump(self.data,file)
    messagebox.showinfo('Student Added Successfully',f'Student ID generated: {self.current_id}')
    self.name_entry.delete(0,tk.END)
    self.age_entry.delete(0,tk.END)
    self.gender_entry.delete(0,tk.END)
    self.contact_entry.delete(0,tk.END)


class SearchScreen(tk.Frame):
  def __init__(self,parent):
    tk.Frame.__init__(self,parent)
    self.grid(row=0,column=0,sticky='nsew')
    with open('database.p','rb') as file:
      self.data = pickle.load(file) #loading database file

    #creating widgets
    self.heading = tk.Label(self, text='Search Student Details', font = ('Ariel',20))
    self.heading.grid(row = 0, column = 0, columnspan = 2 , padx = 100 , pady = 10)
    self.label = tk.Label(self, text = 'Enter Student Name', font = ('Ariel',12))
    self.label.grid(row = 1, column=0)
    self.search_entry = tk.Entry(self, font = ('Ariel',16))
    self.search_entry.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

    self.search_btn = tk.Button(self,text='Search',font=('Ariel',18),command=lambda:self.search(parent))
    self.search_btn.grid(row=3,column=0,columnspan=2,pady=10,padx=50)

    self.back_btn = tk.Button(self,text='< Back',font=('Ariel',10),borderwidth=0,command= lambda: parent.switch_screen(parent.homescreen))
    self.back_btn.grid(row=0,column=0,sticky='nw')

  def search(self,parent):
    #print(self.search_entry.get())
    entry = self.search_entry.get()
    if entry in self.data:
      parent.info = self.data[entry]
      print(f'parent info {parent.info}')
      self.search_entry.delete(0,tk.END)
      parent.viewscreen.update_info(parent) #update the details in viewscreen.
      parent.switch_screen(parent.viewscreen)
    else:
      messagebox.showinfo('Student Not Found','Student details not found in database')
      self.search_entry.delete(0,tk.END)

class ViewScreen(tk.Frame):
  def __init__(self,parent):
    tk.Frame.__init__(self,parent)
    self.grid(row=0,column=0,sticky='nsew')

    #creating widgets
    self.heading = tk.Label(self, text='View Student Details', font = ('Ariel',20))
    self.heading.grid(row = 0, column = 0, columnspan = 2 , padx = 100 ,pady = 10)

    self.name_label = tk.Label(self, text = 'Name', font = ('Ariel',12))
    self.name_label.grid(row = 1, column=0,pady = 10)
    self.name_info = tk.Label(self,text='', font = ('Ariel',12))
    self.name_info.grid(row = 1, column = 1, pady = 10)

    self.age_label = tk.Label(self, text = 'Age', font = ('Ariel',12))
    self.age_label.grid(row = 2, column=0,pady = 10)
    self.age_info = tk.Label(self, text='', font = ('Ariel',12))
    self.age_info.grid(row = 2, column = 1, pady = 10)

    self.gender_label = tk.Label(self, text = 'Gender', font = ('Ariel',12))
    self.gender_label.grid(row = 3, column=0,pady = 10)
    self.gender_info = tk.Label(self, text='', font = ('Ariel',12))
    self.gender_info.grid(row = 3, column = 1, pady = 10)

    self.contact_label = tk.Label(self, text = 'Contact', font = ('Ariel',12))
    self.contact_label.grid(row = 4, column=0,pady = 10)
    self.contact_info = tk.Label(self,text='', font = ('Ariel',12))
    self.contact_info.grid(row = 4, column = 1, pady = 10)

    self.id_label = tk.Label(self, text = 'ID', font = ('Ariel',12))
    self.id_label.grid(row = 5, column=0,pady = 10)
    self.id_info = tk.Label(self,text='', font = ('Ariel',12))
    self.id_info.grid(row = 5, column = 1, pady = 10)

    self.edit_btn = tk.Button(self,text='Edit',font = ('Ariel',14),command= lambda:self.edit(parent))
    self.edit_btn.grid(row=6,column=0,columnspan=2)

    self.back_btn = tk.Button(self,text='< Back',font=('Ariel',10),borderwidth=0,command= lambda: parent.switch_screen(parent.homescreen))
    self.back_btn.grid(row=0,column=0,sticky='nw')

  def update_info(self,parent):
    self.name_info.config(text=parent.info['name'])
    self.age_info.config(text=parent.info['age'])
    self.gender_info.config(text=parent.info['gender'])
    self.contact_info.config(text=parent.info['contact'])
    self.id_info.config(text=parent.info['id'])

  def edit(self,parent):
    parent.addstudent.update_info(parent)
    parent.switch_screen(parent.addstudent)


if __name__ == '__main__':
  app = Form()
  app.mainloop()





