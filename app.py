# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import tix
from tkinter import font as tkFont
import MultiListbox as table
import sys

NAME = 0
SURNAME = 1
BIRTH_NUMBER = 2
STREET = 3
NUMBER = 4
CITY = 5
ZIP = 6
NOTE = 7
data = [
        # Jméno, Příjmení, RČ,       ulice,         čp,   město,     PSČ,  poznámka
       ["Petr", "Bílý","045214/1512","17. Listopadu", 15, "Ostrava", 70800,"poznamka"],
       ["Jana", "Zelený","901121/7238","Vozovna", 54, "Poruba", 78511,""],
       ["Karel", "Modrý","800524/5417","Porubská", 7, "Praha", 11150,""],
       ["Martin", "Stříbrný","790407/3652","Sokolovská", 247, "Brno", 54788,"nic"]]

class App(object):

    def hello(self):
        print("ahoj")

    def __init__(self, master):
        self._row = IntVar()
        self._row = None
        self._jmeno = StringVar()
        self._surname = StringVar()
        self._birth_number = StringVar()
        self._street = StringVar()
        self._number = StringVar()
        self._city = StringVar()
        self._zip = StringVar()
        self._someText = StringVar()

        # menu - TODO

        self._menu = Menu( master )
        self._menu.add_command( label = "Soubor", command = self.hello )
        self._menu.add_command( label = "Nastavení", command = self.hello )
        self._menu.add_command( label = "Nápověda", command = self.hello )

        master.config( menu = self._menu )

        self._menuRightClick = Menu( master )
        self._menuRightClick.add_command( label = "Nový záznam", command = self._new )
        self._menuRightClick.add_command( label = "Uložit záznam", command = self._save )
        self._menuRightClick.add_command( label = "Konec", command = self._endProgram )

        def popup(event):
            self._menuRightClick.post(event.x_root, event.y_root)

        # -- New Button
        self._ImageButtonsFrame = Frame( master, relief=GROOVE )

        self._ImageButtonsFrame.bind( "<Button-3>", popup )

        self._imageButtonNew = Button( self._ImageButtonsFrame,
         command = self._new )
        self._photoOne = PhotoImage( file="newfile.png" )
        self._imageButtonNew.config( image = self._photoOne, width = 100, height = 100)
        self._imageButtonNew.pack( side = LEFT, padx = 8, pady = 1 )

        # -- Save Button
        self._imageButtonSave = Button( self._ImageButtonsFrame,
         command = self._save, width = 10, height = 4 )
        self._photoTwo = PhotoImage( file="savefile.png" )
        self._imageButtonSave.config( image = self._photoTwo, width = 100, height = 100)
        self._imageButtonSave.pack( side = LEFT, padx = 8, pady = 1 )

        self._ImageButtonsFrame.pack( fill = X, padx = 8, pady = 1 )

        self._mlb = table.MultiListbox(master, (('Jméno', 20), ('Příjmení', 20), ('Rodné číslo', 12)))
        
        for i in range(len(data)):
            self._mlb.insert(END, (data[i][0], data[i][1],data[i][2]))
        self._mlb.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        #self._mlb.subscribe( lambda row: self._edit( row ) )
        self._mlb.subscribe( self._edit)
    
        # form - TODO

        # -- Frame pro dalsi sekci
        self._frameAddNext = Frame( master, relief = GROOVE )
        self._frameAddNext.pack( fill = X, expand = 1, padx = 2, pady = 2 )

        # -- Frame pro pridani textu
        self._frameAddText = Frame( self._frameAddNext, relief = GROOVE )
        self._frameAddText.pack( fill = X, side = LEFT, expand = 1, padx = 2, pady = 2 )
        # -- Frame pro pridani inputu
        self._frameAddInput = Frame( self._frameAddNext, relief = GROOVE )
        self._frameAddInput.pack( fill = X, side = RIGHT, expand = 1, padx = 2, pady = 2 )
        
        # -- Frame pro jmeno
        self._frameAddInfo = Frame( self._frameAddText, relief = GROOVE )
        self._frameAddInfo.pack( side = RIGHT, padx = 2, pady = 2 )
        # -- Text k jmenu
        self._labelName = Label( self._frameAddInfo, text = "Jméno:")
        self._labelName.pack( padx = 8, pady = 1 )
        # -- Text k prijmeni
        self._labelSurname = Label( self._frameAddInfo, text = "Příjmeni:")
        self._labelSurname.pack( padx = 8, pady = 1 )
        # -- Text k rodnemu cislu
        self._labelPIN = Label( self._frameAddInfo, text = "Rodné číslo:")
        self._labelPIN.pack( padx = 8, pady = 1 )

        # -- Frame pro jmeno
        self._frameAddData = Frame( self._frameAddInput, relief = GROOVE )
        self._frameAddData.pack( side = LEFT, padx = 2, pady = 2 )
        # -- Misto k zapsani jmena
        self._inputName = Entry( self._frameAddData, width = 14 )
        self._inputName.pack( padx = 8, pady = 1 )
        # -- Misto k zapsani prijmeni
        self._inputSurname = Entry( self._frameAddData, width = 14 )
        self._inputSurname.pack( padx = 8, pady = 1 )
        # -- Misto k zapsani rodneho cisla
        self._inputPIN = Entry( self._frameAddData, width = 14 )
        self._inputPIN.pack( padx = 8, pady = 1 )
        
        # tabs - TODO
        
        # -- Frame pro pridani inputu
        self._frameAddNoteBook = Frame( master, relief = GROOVE, )
        self._frameAddNoteBook.pack( fill = BOTH, expand = 1, padx = 2, pady = 2 )
        
        self.nb = tix.NoteBook( self._frameAddNoteBook )
        self.nb.add("page1", label="Adresa" )
        self.nb.add("page2", label="Poznámka" )
        self.p1 = self.nb.subwidget_list["page1"]
        self.p2 = self.nb.subwidget_list["page2"]
        self.nb.pack(expand=1, fill=BOTH)
        #A1
        self._adressFrame = Frame( self.p1, relief = GROOVE, borderwidth = 2 )
        # -- Frame pro prvni radek
        self._firstRow = Frame( self.p1, relief = GROOVE )
        self._addressLabel = Label( self._firstRow, text = "Ulice:")
        self._addressLabel.pack( side = LEFT, padx = 8, pady = 1 )
        self._addressInput = Entry( self._firstRow, width = 14 )
        self._addressInput.pack( side = LEFT, padx = 8, pady = 1 )
        self._numberDescLabel = Label( self._firstRow, text = "č.p.:")
        self._numberDescLabel.pack( expand = 1, side = LEFT, padx = 18, pady = 1 )
        self._numberDescInput = Entry( self._firstRow, width = 14 )
        self._numberDescInput.pack( expand = 1, side = LEFT, padx = 8, pady = 1 )
        self._firstRow.pack( fill = X, expand = 1 )
        # -- Frame pro druhy radek
        self._secondRow = Frame( self.p1, relief = GROOVE )
        self._cityLabel = Label( self._secondRow, text = "Město:")
        self._cityLabel.pack( side = LEFT, padx = 8, pady = 1 )
        self._cityInput = Entry( self._secondRow, width = 14 )
        self._cityInput.pack( side = LEFT, padx = 8, pady = 1 )
        self._secondRow.pack( fill = X, expand = 1 )
        # -- Frame pro treti radek
        self._thirdRow = Frame( self.p1, relief = GROOVE )
        self._PSCLabel = Label( self._thirdRow, text = "PSČ:")
        self._PSCLabel.pack( side = LEFT, padx = 8, pady = 1 )
        self._PSCInput = Entry( self._thirdRow, width = 14 )
        self._PSCInput.pack( side = LEFT, padx = 8, pady = 1 )
        self._thirdRow.pack( fill = X, expand = 1 )

        self._adressFrame.pack( fill = X, expand = 1 )
        #B1
        self._someTextFrame = Frame( self.p2, relief = GROOVE, borderwidth = 2 )
        self._someTextLabel = Label( self._someTextFrame, text="Poznámka")
        self._someTextLabel.pack( side = LEFT, padx = 8, pady = 1 )
        self._someTextInput = Entry( self._someTextFrame, width = 14 )
        self._someTextInput.pack( side = LEFT, padx = 8, pady = 1 )
        self._someTextFrame.pack( fill = BOTH, expand = 1 )

        # buttons - TODO

        self._buttonFrame = Frame( master, relief = GROOVE )
        self._ButtonEnd = Button( self._buttonFrame, text = "Konec",
         command = self._endProgram, width = 10, height = 1 )
        self._ButtonEnd.pack( side = LEFT, pady = 2, padx = 4 )
        self._ButtonNew = Button( self._buttonFrame, text = "Nový záznam",
         command = self._new, width = 10, height = 1 )
        self._ButtonNew.pack( side = LEFT, pady = 2, padx = 4 )
        self._ButtonSave = Button( self._buttonFrame, text = "Uložit záznam",
         command = self._save, width = 10, height = 1 )
        self._ButtonSave.pack( side = LEFT, pady = 2, padx = 4 )
        self._buttonFrame.pack()

        self._fullNameLabel = Label( master, text = "")      
        self._fullNameLabel.pack( side = LEFT, padx = 8, pady = 1 )

    def _endProgram(self):
        print('konec')
        sys.exit()

    def _new(self):
        self._row = None
        self._inputName.delete( 0, END )
        self._inputSurname.delete( 0, END )
        self._inputPIN.delete( 0, END )
        self._addressInput.delete( 0, END )
        self._numberDescInput.delete( 0, END )
        self._cityInput.delete( 0, END )
        self._PSCInput.delete( 0, END )
        self._someTextInput.delete( 0, END )
        print('novy')

    def _save(self):
        self._mlb.delete(0,END)
        if self._row == None:
            data.append([
                self._inputName.get(),
                self._inputSurname.get(),
                self._inputPIN.get(),
                self._addressInput.get(),
                self._numberDescInput.get(),
                self._cityInput.get(),
                self._PSCInput.get(),
                self._someTextInput.get()
                ])
        else:
            data[ self._row ][ 0 ] = self._inputName.get()
            data[ self._row ][ 1 ] = self._inputSurname.get() 
            data[ self._row ][ 2 ] = self._inputPIN.get() 
            data[ self._row ][ 3 ] = self._addressInput.get() 
            data[ self._row ][ 4 ] = self._numberDescInput.get() 
            data[ self._row ][ 5 ] = self._cityInput.get() 
            data[ self._row ][ 6 ] = self._PSCInput.get() 
            data[ self._row ][ 7 ] = self._someTextInput.get() 
            
        for i in range(len(data)):
            self._mlb.insert(END, (data[i][0], data[i][1],data[i][2]))
        print( 'ulozit' )

    def _edit(self, row):
        print("now")
        # assign actual values to variables - TODO

        self._row = row
        self._jmeno = data[ self._row ][ 0 ]
        self._surname = data[ self._row ][ 1 ]
        self._birth_number = data[ self._row ][ 2 ]
        self._street = data[ self._row ][ 3 ]
        self._number = data[ self._row ][ 4 ]
        self._city = data[ self._row ][ 5 ]
        self._zip = data[ self._row ][ 6 ]
        self._someText = data[ self._row ][ 7 ]

        # deleting - TODO

        self._inputName.delete( 0, END )
        self._inputSurname.delete( 0, END )
        self._inputPIN.delete( 0, END )
        self._addressInput.delete( 0, END )
        self._numberDescInput.delete( 0, END )
        self._cityInput.delete( 0, END )
        self._PSCInput.delete( 0, END )
        self._someTextInput.delete( 0, END )
        
        # inserting - TODO

        self._inputName.insert( 0, self._jmeno ) 
        self._inputSurname.insert( 0, self._surname ) 
        self._inputPIN.insert( 0, self._birth_number ) 
        self._addressInput.insert( 0, self._street ) 
        self._numberDescInput.insert( 0, self._number ) 
        self._cityInput.insert( 0, self._city ) 
        self._PSCInput.insert( 0, self._zip ) 
        self._someTextInput.insert( 0, self._someText ) 

        self._fullNameLabel['text'] = self._jmeno + ' ' + self._surname
        
        # new window - TODO
        
        print (data[row])
             
def main():
    root = tix.Tk()
    root.wm_title("Formulář")
    app = App(root)
    root.mainloop()
    
main()

