from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x250')

sat = ttk.Treeview(ws)
sat.pack()

sat['columns'] = ('id', 'full_Name', 'award')
sat.column("#0", width=0, stretch=NO)
sat.column("id", anchor=CENTER, width=80)
sat.column("full_Name", anchor=CENTER, width=80)
sat.column("award", anchor=CENTER, width=80)

sat.heading("#0", text="", anchor=CENTER)
sat.heading("id", text="ID", anchor=CENTER)
sat.heading("full_Name", text="Full_Name", anchor=CENTER)
sat.heading("award", text="Award", anchor=CENTER)

sat.insert(parent='', index='end', iid=0, text='',
           values=('101', 'john', 'Gold'))
sat.insert(parent='', index='end', iid=1, text='',
           values=('102', 'jack', "Silver"))
sat.insert(parent='', index='end', iid=2, text='',
           values=('103', 'joy', 'Bronze'))

# button


btn = Button(ws, text="Exit", command=ws.destroy)
btn.pack()

ws.mainloop()
