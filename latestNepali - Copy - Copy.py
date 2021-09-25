import tkinter
from tkinter import font
from tkinter import*
import string 
import random
from PIL import ImageTk ,Image
from PIL import ImageTk as itk
import string_utils
from tkinter import messagebox as mb

#---------creating random string----------  
# initializing size of string  
N = 8
sample_lettersA = 'डधभचतथगषय'
sample_lettersB = 'बकमनजवपस'
sample_lettersC = 'शहअखल'
sample_lettersD = 'डधभचतथगषयबकमनजवपसशहअखल'
resA = str(''.join((random.choices(sample_lettersA + " ",k=N))))

resB = str(''.join((random.choices(sample_lettersB + " ",k=N))))
resC = str(''.join((random.choices(sample_lettersC + " ",k=N))))
resD = str(''.join((random.choices(sample_lettersD + " ",k=N))))
index = 0
list_index = 0
list = []
word_count = 10


  
#---------------KeyBoardClass-------------------------#


class keyboard():
    DEFAULT_WIDTH = 9
    DEFAULT_HEIGHT = 2
    DEFAULT_BACKGROUND = "black"
    DEFAULT_FOREGROUND = "white"
    DEFAULT_ACTIVE_BACKGROUND = "green"
    DEFAULT_ACTIVE_FOREGROUND = "black"
    DEFAULT_FONT = "helvetica neue bold"
    DEFAULT_FONT_SIZE = 15

    def __init__(self, root, master, text, buttons,alt_buttons=None, enter_function=None, **cnf):
        all_ok = self.check_values(buttons, alt_buttons)
        if not(all_ok):
             raise ValueError
        self.frame = tkinter.Frame(master)
        self.frame.pack(padx=3,pady=3)
        self.text = text
        self.keys = {}
        self.button_values = []
        self.buttons = buttons
        self.alt_buttons = alt_buttons
        self.enter_function = enter_function
        self.Shift = False
        self.caps_lock = False
        self.button_width = cnf.get("button_width", self.DEFAULT_WIDTH)
        self.button_height = cnf.get("button_height", self.DEFAULT_HEIGHT)
        self.background = cnf.get("background", self.DEFAULT_BACKGROUND)
        self.foreground = cnf.get("foreground", self.DEFAULT_FOREGROUND)
        self.active_background = cnf.get("active_background", self.DEFAULT_ACTIVE_BACKGROUND)
        self.active_foreground = cnf.get("active_foreground", self.DEFAULT_ACTIVE_FOREGROUND)
        self.font = font.Font(family=cnf.get("font", self.DEFAULT_FONT),

                                     size=cnf.get("font_size", self.DEFAULT_FONT_SIZE))
    
    def build(self):

                i = 0
                r = 0
                c = 0
                for row in self.buttons:
                    for element in row:
                        value = tkinter.StringVar()
                        value.set(element)
                        self.button_values.append(value)
                        name = value.get()
                        columnspan = 1
                        rowspan = 1
                        wraplength = 0
                        width = self.button_width
                        height = self.button_height
                        if name == "BLANK":
                            frame = tkinter.Frame(self.frame, width=1, height=1)
                            frame.grid(row=r, column=c, columnspan=columnspan, rowspan=rowspan)
                        else:
                            callback = lambda v=value: self.key_press(v)
                            if name == "Space":
                                value.set(" ")
                                columnspan = 5
                                width =  49
                            elif name == "Shift":
                                columnspan = 2
                                width = 19
                                callback = lambda: self.toggle_Shift()
                            elif name == "Enter":
                                if self.enter_function is None:
                                    callback = self.enter_function
                                else:
                                    callback = lambda: self.enter_function()
                            elif name == "Del":
                                
                                callback = lambda: self.delete()
                            button = tkinter.Button(self.frame, textvariable=value, width=width, height=height, command=callback,
                                                    background=self.background, foreground=self.foreground,
                                                    activebackground=self.active_background,
                                                    activeforeground=self.active_foreground, font=self.font, wraplength=wraplength)
                            button.grid(row=r, column=c, columnspan=columnspan, rowspan=rowspan)
                            self.keys[name] = button
                            button.bind("<key>")
                        i = i + 1
                        c = c + columnspan
                    r = r + 1
                    c = 0
                
    def delete(self):
                if isinstance(self.Entry, tkinter.Entry):
                    self.Entry.delete(self.Entry.index(tkinter.INSERT) - 1)
                elif isinstance(self.Entry, tkinter.Entry):
                    self.Entry.delete("%s-1c" % tkinter.INSERT, tkinter.INSERT)

    def key_press(self, value):
                self.text.insert(tkinter.INSERT, value.get())
                if self.Shift:
                    self.toggle_Shift()

    def check_values(self, buttons, alt_buttons):
                if not (alt_buttons is None):
                    for i in range(len(buttons)):
                        for j in range(len(buttons[i])):
                            if not(isinstance(buttons[i][j], str)):
                                return False
                            try:
                                if not (isinstance(alt_buttons[i][j], str)):
                                    return False
                            except IndexError:
                                print("TkInterKeyboard.py: buttons and alt_buttons do not match up")
                                raise
                else:
                    for i in range(len(buttons)):
                        for j in range(len(buttons[i])):
                            if not(isinstance(buttons[i][j], str)):
                                return False
                return True

    def refresh_vars(self):
                  values = self.buttons
                  if self.Shift != self.caps_lock and not(self.alt_buttons is None):
                     values = self.alt_buttons
                  i = 0
                  for row in values:
                    for element in row:
                        self.button_values[i].set(element)
                        i = i + 1


    def toggle_Shift(self):
                self.Shift = not(self.Shift)
                if self.Shift:
                    self.keys.get("Shift").config(background=self.active_background, activebackground=self.background,
                                                  foreground=self.active_foreground, activeforeground=self.foreground)
                else:
                    self.keys.get("Shift").config(background=self.background, activebackground=self.active_background,
                                                  foreground=self.foreground, activeforeground=self.active_foreground)
                self.refresh_vars()

    def set_text(self, text):
                self.text = text
 
normalboard = True

#Driver code

def main():
    
   
    root = tkinter.Tk()
    #root.title("Nepali Typing Keyboard")
    root.resizable(1,1)
    

    #------------------------------------------Levels Of difficulty-------------------------------
    def levelA():
        my_string_var.set(resA)     
    def levelB():
        my_string_var.set(resB)
    def levelC():
        my_string_var.set(resC)
    def levelD():
        my_string_var.set(resD)
        
    my_string_var= StringVar()

    
    #----------------------------------------photo icon at label----------------------------
    logo = Image.open(r'flag.ico')
    
    resized = logo.resize((40,30),Image.ANTIALIAS)
    newLogo = ImageTk.PhotoImage(resized)

    w1 = tkinter.Label(root,image=newLogo,bg="white",fg='green',font=('Arial',20,)).place(x=0,y=5)

    w2 = tkinter.Label(root,text="Nepali Type Tutor",bg="white",fg='black',font=('Gabriola',18,'bold')).place(x=43,y=0)
    
    w=tkinter.Label(root,textvariable=my_string_var,height=9,pady=25,bg="white",fg='black',font=('Arial',26,'bold'))
    w.pack()
    
    
        
    
    enFrame=tkinter.Frame(root)
    


    def select(value):
        if value == "Space":
            text.insert(INSERT,' ')
            
        elif value == "Tab":
            text.insert(INSERT,'  ')
            
        elif value == "Enter":
            text.insert(INSERT,'\n ')
            
        elif value == "Del":
            char=text.get(1.0,END)
            val=len(char)
            text.delete(1.0,END)
            text .insert(1.0,char[:val-2])

        elif value == "<-":
            char=text.get(1.0,END)
            val=len(char)
            text.delete(1.0,END)
            text .insert(1.0,char[:val-2])
        
        else:
            text.insert(INSERT,value)
        
  
        


    


    engButtons = [

    '!','Q','W','E','R','T','Y','U','I','O','P','<-','7','8','9','-',
    'Tab','A','S','D','F','G','H','J','K','L','[',']','4','5','6','+',
    'Shift','Z','X','C','V','B','N','M','<','>','?','/','1','2','3','/',
    'Ctrl','Fn','win','Alt','Space',':','"','Enter','{','}','0','Del',
    ]


    varRow = 4
    varColumn = 0


   


    for button in engButtons:
        command = lambda x=button: select(x)
       
        if button == "Space":
           tkinter.Button(enFrame,width=26,height=2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=3,columnspan=6)
        
        elif button == ":":
           tkinter.Button(enFrame,width=5,height= 2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=8)
        elif button == '"':
           tkinter.Button(enFrame,width=5,height= 2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=9)
        elif button == 'Enter':
           tkinter.Button(enFrame,width=5,height= 2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=10)
        elif button == "{":
           tkinter.Button(enFrame,width=5,height= 2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=11)
        elif button == "}":
           tkinter.Button(enFrame,width=5,height= 2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=12)
        elif button == "0":
           tkinter.Button(enFrame,width=5,height= 2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=13)
        elif button == "Del":
           tkinter.Button(enFrame,width=12,height=2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=14,columnspan=2)
        elif button == "Shift":
           tkinter.Button(enFrame,width=12,height=2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,columnspan=2)
        elif button == "win":
           tkinter.Button(enFrame,width=5,height=2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=2)
        elif button == "Alt":
           tkinter.Button(enFrame,width=5,height=2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=3)
        else:
              tkinter.Button(enFrame,width=5,height= 2,padx=3,pady=3,bd=3,font=('Times',12,'bold'),fg="white"
                           ,bg='black',activebackground="gray",activeforeground="black",relief='raised',text=button,command=command).grid(row=varRow,column=varColumn)
             


      
        

        varColumn +=1
        if varColumn>15 and varRow==4:
            varColumn = 0
            varRow +=1
        if varColumn>15 and varRow==5:
            varColumn = 0
            varRow +=1
        if varColumn>15 and varRow==6:
            varColumn=0
            varRow+=1



    def eng_click():
        global normalboard
        if normalboard:
            #self.Frame.pack_forget()

            enFrame.pack(side = TOP)
            
            normalboard = False
        else:
            print('show nepali')
            enFrame.pack_forget()
            normalboard = True
    
        #------------------------------StartGAme---------------------------------------
    

         
    def restrictUnmatched(input):#Validating input
        
        x = str((w['text']))
        y = ((Entry.get()))
        
        if x.startswith (input):
            
            return True
            
        else :
            return False
                            
       

        
            
          
            
            
        
            
            
        
            
        
    def startGame(event): # Testing the matched string
         x = str((w['text']))
        
         y = ((Entry.get()))
        
        
            
        
          
         if x == y:
             print("matched")
             my_string_var.set(string_utils.shuffle(w['text']))#if two strings match shuffle the string
             
         else:
             print("not matched")
             
            
            
         Entry.delete(0,END)


    def msgBox():
        mb.showinfo("This is Nepali Typing Tutor")
         
        
       
        
         
    
   
    menubar = Menu(root,font=("Times",6,"bold"))  
    Sound = Menu(menubar,activeforeground='black', activebackground='#AFEEEE',tearoff=0) 
    Level = Menu(menubar,activeforeground='black', activebackground='#AFEEEE',tearoff=0)
    Level.add_radiobutton(label="Level 1",command=levelA)
    Level.add_radiobutton(label="Level 2",command = levelB)
    Level.add_radiobutton(label="Level 3",command = levelC)
    Level.add_radiobutton(label="Level 4",command=levelD)
    Level.add_separator() 
    Sound.add_radiobutton(label="On")  
    Sound.add_radiobutton(label="Off")  
      
      
    Sound.add_separator()  
        
      
    menubar.add_cascade(label="Sound", menu=Sound)  
    Font = Menu(menubar,activeforeground='black', activebackground='#AFEEEE', tearoff=0)  
     
    Font.add_separator()
     
      
    menubar.add_cascade(label="Font", menu=Font)
    menubar.add_cascade(label="Level", menu=Level)

    Language = Menu(menubar,activeforeground='black', activebackground='#AFEEEE', tearoff=0)  
    Language.add_checkbutton(label="English",command = eng_click)
    Language.add_checkbutton(label="Nepali") 
    menubar.add_cascade(label="Language", menu=Language)
    Language.add_separator()
    
    About = Menu(menubar,activeforeground='black', activebackground='#AFEEEE', tearoff=0)
    menubar.add_cascade(label="About", command = msgBox)
    About.add_separator()
      
    root.config(menu=menubar) 
    buttons = [ 

                ['ड','ध','भ', 'च', 'त', 'थ','ग','ष','य','ू','ृ','े','=','7','8','9'],
                ['ब', 'क', 'म', 'ा', 'न', 'ज', 'व', 'प','ि', 'स', 'ु','्','4','5','6','+'],
                ['श', ' ह', 'अ' ,'ख' , 'द', 'ल', 'फ','ै','ी','र',',','|','1','2','3','/',],
                ['Shift','win','Alt','Space',':','"','Enter','{','}','0','Del',]]

            


    alt_buttons =[
                    ['ढ','ध','भ','छ',' ट',' ठ',' घ','औ', 'य', 'उ','ृ','ऋ','ऐ','7','8','9'],
                    ['ब', 'क', 'ण','आ','ञ','झ','व','ओ','इ','स','ऊ','ं','4','5','6','+'],
                    ['श', ' ह', 'अ' ,'ख','ल','ः','ऐ','ई','.','ँ',',','|','1','2','3','/'],
                    ['Shift','win','Alt','Space',':','"','Enter','{','}','0','Del',]]

    
    map = {'q':'ड',
           'Q':'ड',
        
           'w':'ध',
           'e':'भ',
           'r':'च',
           't':'त',
           'y':'थ',
           'u': 'घ',
           'i':'ग',
           'o':'ष',
           'p':'य',
           '[':'ू',
           ']':'ृ',
           '/':'े',
            'a':'ब',
           's':'क',
           'd':'म',
           'f':'ा',
           'g':'न',
           'h':'ज',
           'j':'व',
           'k':'प',
           'l':'ि',
           ';':'स',
           "'":'ु',
           '':'्',
           'z':'श',
           'x':'ह',
           'c':'अ',
           'v':'ख',
           'b':'द',
           'n':'ल',
           'm':'फ',
           ',':'ै',
           '.':'ी',
           '/':'र',}
           
           
        

    



    
    

  
        
    
    Entry = tkinter.Entry(root,validate="key",justify="center",bd=0,width=80,font=('Helvetica',25,'bold'))
    Entry.focus()  
    
    
    
    def keymap(event):
        
        if event.char in map:
            Entry.insert("insert", map[event.char])
            return "break"
        
    Entry.pack(padx=100,pady=40)
    Entry.bind("<Key>",keymap)
    root.bind("<Return>",startGame)
    reg1 = root.register(restrictUnmatched)
    Entry.config(validate = "key",validatecommand = (reg1,'%P'))
    
    
    
    
    enter_function = lambda: print("enter")
    kb = keyboard(root, root, Entry,buttons, alt_buttons, enter_function)
    kb.build()
    root.geometry('1920x1080')
    root.configure(bg="white")
    root.attributes('-alpha',0.97)
   # root.iconbitmap(r'c:\Users\barsha\Desktop\typing icon.ico')
    root.mainloop()

    
if __name__ == "__main__":
        main()
        





