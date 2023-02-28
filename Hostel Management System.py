from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
from tkinter.ttk import Combobox


root=Tk()
root.geometry("1350x700+0+0")
root.title("Hostel Management System")
root.configure(background="cadet blue")



def filecreater():
    file=open("project.txt","a")
    file.close()
    #line=file.readline().rstrip("\n")
    #line=line.split("\t")
   # line=line.strip()
    file=open("project.txt","r")
    line1=file.readline()
    file.close()
    #reg=line[0]
    if line1=="":
    #if reg=="Reg#:"
        file=open("project.txt","a")
        print(line1)
        file.write("Reg#:".ljust(10)+"\t"+"NAME:".ljust(25)+"\t"+"PROGRAM:".ljust(20)+"\t"+"SEMESTER:".ljust(10)+"\t"+"ROOM:"+"\n")
        file.close()
    # Get the input from entries
    Program=ProgEntry.get()    
    room=RoomEntry.get()
    name=NameEntry.get()
    Id=IdEntry.get()
    semester=Combo.get()
    
    # Check for vacancy
    file=open("project.txt", "r")
    c=0
    line=file.readline()
    while line !='':
        line=line.rstrip("\n")
        LineList=line.split("\t")
        R=LineList[4]
        if room==R:
            c=c+1
        line=file.readline()
    file.close()
    
    # Check Registration Number
    file=open("project.txt", "r")
    line=file.readline()
    found= False
    while line !='':
        line=line.rstrip("\n")
        LineList=line.split("\t")
        Reg=LineList[0].rstrip()
        if Id==Reg:
            found= True  
        line=file.readline()
    file.close()
    
    

    # Conditions
    if room=='' or name=='' or Id=='' or semester=='' or semester=="select" or Program=='':
        tkinter.messagebox.showinfo('Oops','Please Fill All The Fields!')
    elif int(room)>100:
        tkinter.messagebox.showinfo('Oops','There Is No Such Room!')
    elif c >=3:
        tkinter.messagebox.showinfo('Oops','Entered Room Is Full!')
    elif found== True:
        tkinter.messagebox.showinfo('Oops','Student with Reg#'+Id+' is Hostalite!')
        
    # Enter The Data
    else:    
        file=open("project.txt", "a")
        string=(Id.ljust(10)+"\t"+name.ljust(25)+"\t"+Program.ljust(20)+"\t"+semester.ljust(10)+"\t"+room+"\n")

        file.write(string)
        file.close
        NameEntry.delete(0,END)
        RoomEntry.delete(0,END)
        IdEntry.delete(0,END)
        ProgEntry.delete(0,END)
        Combo.delete(0,END)
        OutputVar.set('Data is Entered!')
def Searcher():
    ID=SrchDelEntry.get()
    if ID=='':
        tkinter.messagebox.showinfo('Oops','Please Enter Registration Number!')
    else:
        remove=tree.get_children()
        for child in remove:
            tree.delete(child)
    
        file=open("project.txt","r")
        status="TRUE"
        for line in file:
            words=line.split()
            word=words[0]
            if word==ID:
                line=line.rstrip("\n")
                line=line.split("\t")
                reg=line[0].strip()
                name=line[1].strip()
                prog=line[2].strip()
                sem=line[3].strip()
                room=line[4].strip()
                tree.insert("","end",text="",values=("",reg,name,prog,sem,room))
                status="FALSE"
                SrchDelEntry.delete(0,END)
        if status=="TRUE":
            OutputVar.set("No record found")
        file.close()
        


def Deleter():
    identity=SrchDelEntry.get()
    if identity=="":
        tkinter.messagebox.showinfo('Oops','Please Enter Registration Number!')
    else:
        f=open("project.txt","r")
        fnew=open("new.txt","a")
        status="FALSE"
        for line in f:
            words=line.split()
            Id=words[0]
            if identity != Id:
                fnew.write(line)
            else:
                status="TRUE"
        f.close()
        fnew.close()
        os.remove("project.txt")
        os.rename("new.txt","project.txt")
        if status=="TRUE":
            OutputVar.set("data deleted")
        elif status=="FALSE":
            OutputVar.set("data not found")
        SrchDelEntry.delete(0,END)

def Replacer():
    # Get the Input:
    repname=RepEntry.get()
    Id=NewIdEntry.get()
    semester=ReplaceCombo.get()
    Program=NewProgEntry.get()
    newname=NewNameEntry.get()
    
    if repname=='' or Id=='' or semester=='' or semester=="select" or Program=='' or newname=='':
        tkinter.messagebox.showinfo('Oops','Fill all the Fields!')
    else:
        file=open("project.txt","r")
        newfile=open("temp.txt","a")
        found= False
        line=file.readline()
        while line !='':
            linenew=line.rstrip("\n")
            lineL=linenew.split("\t")
            name=lineL[1]
            name=name.strip()
            name=name.lower()
            repname=repname.lower()
            if name==repname:
                room=lineL[4]
                string=(Id.ljust(10)+"\t"+newname.ljust(25)+"\t"+Program.ljust(20)+"\t"+semester.ljust(10)+"\t"+room+"\n")
                newfile.write(string)
                found= True
            else:
                newfile.write(line)
            line=file.readline()    
        file.close()
        newfile.close()
        os.remove("project.txt")
        os.rename("temp.txt","project.txt")
    if found== False:
        tkinter.messagebox.showinfo('Oops','Entered Name is not in list!')
    else:
        OutputVar.set('Entry Replaced!')
        RepEntry.delete(0,END)
        NewIdEntry.delete(0,END)
        ReplaceCombo.delete(0,END)
        NewProgEntry.delete(0,END)
        NewNameEntry.delete(0,END)


def ShowAll():
    remove=tree.get_children()
    for child in remove:
        tree.delete(child)
    file=open("project.txt","r")

    line=file.readline()
    line=file.readline()
    c=1
    while line !='':
        line=line.rstrip("\n")
        line=line.split("\t")
        reg=line[0].strip()
        name=line[1].strip()
        prog=line[2].strip()
        sem=line[3].strip()
        room=line[4].strip()
        tree.insert("","end",text="",values=(str(c)+":",reg,name,prog,sem,room,""))
    
        line=file.readline()
        c=c+1
    file.close()

def VacantSeats():
    remove=tree.get_children()
    for child in remove:
        tree.delete(child)
    for r in range(1,101):
        c=0
        file=open("project.txt","r")
        line=file.readline()
        while line !='':
            line=line.rstrip("\n")
            line=line.split("\t")
            room=line[4]
            if room==str(r):
                c=c+1
            line=file.readline()
        vacant=3-c
        if vacant>0:
            tree.insert("","end",text="",values=("","","","","","","Room "+str(r)+":      "+str(vacant)+" Seats"))
        
def RoomDetails():
    room=Roomentry.get()
    if room=="":
        tkinter.messagebox.showinfo('Oops','Please Enter Room Number!')
    else:
        remove=tree.get_children()
        for child in remove:
            tree.delete(child)
        found=False
    
        file=open("project.txt","r")
        line=file.readline()
        while line !='':
            line=line.rstrip("\n")
            line=line.split("\t")
            Room=line[4].strip()
            if Room==room:
                found=True
                reg=line[0].strip()
                name=line[1].strip()
                prog=line[2].strip()
                sem=line[3].strip()
                tree.insert("","end",text="",values=("",reg,name,prog,sem,Room,""))
            line=file.readline()
        OutputVar.set("")
        if found==False:
            OutputVar.set("Room#"+str(room)+"is Vacant")
        
    
def Exit():
    root.destroy()

#def Replacer:
    

# Top title frame and labels

TitleL=Label(root,
            font=('arial',40,'bold'),
            text="Hostel Management System",relief=GROOVE,
            bd=10,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
TitleL.pack(side=TOP,fill=X)

# Input frames , entry widgets and labels.

infoF=Frame(root,bg='cadet blue',bd=4,relief=GROOVE)
infoF.place(x=15,y=100,width=530,height=590)

label=Label(infoF,font=('arial',18,'bold'), text="New Entry",pady=10,bg="cadet blue")
NameL=Label(infoF,font=('arial',15,'bold'), text="Student Name:",bg="cadet blue")
NameEntry=Entry(infoF,font=('arial',13,'bold'),relief=GROOVE,bd=3)
label.grid(row=0,column=0,sticky="w")
NameL.grid(row=1, column=0,sticky="w")
NameEntry.grid(row=1, column=1,pady=5,padx=50,sticky="w")
IdLabel=Label(infoF,font=('arial',15,'bold'), text="Registration number:",bg='cadet blue')
IdEntry=Entry(infoF,font=('arial',13,'bold'),relief=GROOVE,bd=3)
IdLabel.grid(row=2,column=0,sticky="w")
IdEntry.grid(row=2,column=1,pady=5,padx=50,sticky="w")


ProgLabel=Label(infoF,font=('arial',15,'bold'), text="Program:",bg='cadet blue')
ProgEntry=Entry(infoF,font=('arial',13,'bold'),relief=GROOVE,bd=3)
ProgLabel.grid(row=3,column=0,sticky="w")
ProgEntry.grid(row=3,column=1,pady=5,padx=50,sticky="w")


SemLabel=Label(infoF,font=('arial',15,'bold'), text="Semester:",bg='cadet blue')
#SemEntry=Entry(infoF,font=('arial',13,'bold'),relief=GROOVE,bd=3)
s=["1st ","2nd ","3rd ","4th ","5th ","6th ","7th ","8th "]
Combo =Combobox(infoF,values=s,width=18,font=('arial',13,'bold'))
Combo.set("select")
SemLabel.grid(row=4,column=0,sticky="w")
Combo.grid(row=4,column=1,pady=5,padx=50,sticky="w")


RoomLabel=Label(infoF,font=('arial',15,'bold'), text="Room Number:",
                bg='cadet blue')
RoomEntry=Entry(infoF,font=('arial',13,'bold'),relief=GROOVE,bd=3)
RoomLabel.grid(row=5,column=0,sticky="w")
RoomEntry.grid(row=5,column=1,pady=5,padx=50,sticky="w")

button=Button(infoF,font=('arial',10),width=10,
              bg='light blue',fg="black",relief=RAISED, text="Enter Data",
              command=filecreater)
button.grid(row=6,column=1,padx=10,pady=5)

#ReplaceFrame=Frame(infoF,bg='cadet blue',bd=3,relief=RIDGE,width=445,height=282)
#ReplaceFrame.grid(row=6,column=0,columnspan=2)


label2=Label(infoF, font=('arial',18,'bold'),
                  text="Replace Old Entry",pady=10,bg='cadet blue')
label2.grid(row=7,column=0,sticky="w")
RepLabel=Label(infoF, font=('arial',18,'bold'),
                  text="Enter replace:",bg='cadet blue')
RepEntry=Entry(infoF,font=('arial',13,'bold'),relief=GROOVE,bd=2)

RepLabel.grid(row=8,column=0,sticky='w')
RepEntry.grid(row=8,column=1,pady=10,padx=20)
NewNameLabel=Label(infoF, font=('arial',18,'bold'),
                  text="New Name:",bg='cadet blue')
NewNameEntry=Entry(infoF,font=('arial',13,'bold'),bd=2,relief=GROOVE) 
NewIdLabel=Label(infoF, font=('arial',18,'bold'),
                  text="New Reg#:",bg='cadet blue')
NewIdEntry=Entry(infoF,font=('arial',13,'bold'),bd=2,relief=GROOVE)
NewProgLabel=Label(infoF,font=('arial',18,'bold'),justify=LEFT ,
                  text="Program:",bg='cadet blue')
NewProgEntry=Entry(infoF,font=('arial',13,'bold'),bd=2,relief=GROOVE)
NewSemLabel=Label(infoF, font=('arial',18,'bold'),
                  text="Semester:",bg='cadet blue')
#NewSemEntry=Entry(infoF,font=('arial',13,'bold'),bd=2,relief=GROOVE)

s=["1st ","2nd ","3rd ","4th ","5th ","6th ","7th ","8th "]
ReplaceCombo =Combobox(infoF,values=s,width=18,font=('arial',13,'bold'))
ReplaceCombo.set("select")
ReplaceButton=Button(infoF,font=('arial',10),width=10,
                    bg='light blue',relief=RAISED, text="Replace",
                    command=Replacer)

ReplaceButton.grid(row=11,column=1,padx=10,pady=8)



NewNameLabel.grid(row=9,column=0,sticky='w')
NewNameEntry.grid(row=9,column=1,pady=8,padx=20)
NewIdLabel.grid(row=10,column=0,sticky='w')
NewIdEntry.grid(row=10,column=1,pady=8,padx=20)
NewProgLabel.grid(row=11,column=0,sticky='w')
NewProgEntry.grid(row=11,column=1,pady=8,padx=20)
NewSemLabel.grid(row=12,column=0,sticky='w')
ReplaceCombo.grid(row=12,column=1,pady=8,padx=20)
ReplaceButton.grid(row=13,column=1,padx=10,pady=8)



#Search and delete frames.

ExtraFrame=Frame(root,bg='cadet blue',bd=4,relief=GROOVE,width=860,height=580)
ExtraFrame.place(x=560,y=100)


SrchDelLabel=Label(ExtraFrame,font=('arial',10,'bold'),fg='white',padx=5,pady=8,
                  text="Registration Number:",bg='cadet blue')
SrchDelEntry=Entry(ExtraFrame,bd=3,width=15,font=('arial',15,'bold'),relief=GROOVE)
SearchButton=Button(ExtraFrame,font=('arial',10),width=8,
                    bg='light blue',relief=RAISED, text="Search",
                    command=Searcher)
DeleteButton=Button(ExtraFrame,font=('arial',10),width=8,
                    bg='light blue',relief=RAISED, text="Delete",
                    command=Deleter)
Roomlabel=Label(ExtraFrame,font=('arial',10,'bold'),fg='white',
                  text="Room Number:",bg='cadet blue')
Roomentry=Entry(ExtraFrame,bd=3,width=15,font=('arial',15,'bold'),relief=GROOVE)
Roombutton=Button(ExtraFrame,font=('arial',10),width=8,
                    bg='light blue',relief=RAISED, text="Room",command=RoomDetails)

ShowButton=Button(ExtraFrame,font=('arial',10),width=15,
                    bg='light blue',relief=RAISED, text="Display All Record",
                    command=ShowAll)
SeatsButton=Button(ExtraFrame,font=('arial',10),width=10,
                    bg='light blue',relief=RAISED, text="Vacant Seats",
                    command=VacantSeats)

SrchDelLabel.grid(row=0,column=0,sticky="w")
SrchDelEntry.grid(row=0,column=1, pady=10, padx=20, sticky="w")
SearchButton.grid(row=0,column=2,padx=8,pady=10)
DeleteButton.grid(row=0,column=3,padx=8,pady=10)
SeatsButton.grid(row=0,column=4,padx=8,pady=10)
Roomlabel.grid(row=1,column=0,pady=10, padx=8, sticky="w")
Roomentry.grid(row=1,column=1,pady=10, padx=8, sticky="w")
Roombutton.grid(row=1,column=2,pady=10,padx=8,sticky="w")
ShowButton.grid(row=1,column=3,padx=8,pady=10)

OutputFrame=Frame(ExtraFrame,relief=RIDGE,bd=8,bg='white',width=790,height=50)
OutputFrame.grid(row=2,column=0,columnspan=5)

OutputVar=StringVar()
OutputVar.set("               ")
OutputLabel=Label(OutputFrame,font=('arial',10,'bold'),fg='black',padx=300,pady=10,textvariable=OutputVar)
OutputLabel.pack()

TableFrame=Frame(ExtraFrame,bg='cadet blue',bd=4,relief=RIDGE,width=800,height=700)
TableFrame.grid(row=3,column=0,columnspan=5,rowspan=4)


scroll_y=Scrollbar(TableFrame,orient=VERTICAL)
tree=ttk.Treeview(TableFrame,yscrollcommand=scroll_y.set,height=20)
tree['columns']=("#","Reg#","Name","Program","Semester","Room","Vacant Seats")

scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=tree.yview)
tree.pack(fill=BOTH,expand=1)
tree.heading("#0",text="",anchor="w")
tree.column("#0",anchor="w",width=5)

tree.heading("#",text="#",anchor="w")
tree.column("#",anchor="w",width=30)

tree.heading("Reg#",text="Reg#",anchor="w")
tree.column("Reg#",anchor="w",width=130)

tree.heading("Name",text="Name",anchor="w")
tree.column("Name",anchor="w",width=150)

tree.heading("Program",text="Program",anchor="w")
tree.column("Program",anchor="w",width=110)

tree.heading("Semester",text="Semester",anchor="w")
tree.column("Semester",anchor="w",width=95)

tree.heading("Room",text="Room",anchor="w")
tree.column("Room",anchor="w",width=90)

tree.heading("Vacant Seats",text="Vacant Seats",anchor="w")
tree.column("Vacant Seats",anchor="w",width=150)


root.mainloop()
