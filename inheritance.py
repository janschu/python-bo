""" Modul mit Accounts für die IT Zugänge der BO (Rocketscience) """
class Account:
    """ Der Grundlegende Account zur Speicherung eines Namens """
    def __init__(self, name):                     #magic-method zur Initialisierung
        """ Initialisierung nur mit Namen """
        self.__name = name
        print (f"      Init Account: {name}")
    def __get_name (self):                        #gekapseltes Attribut
        return f"Mein Name ist: {self.__name}"
    name = property (__get_name,None, None,"""Die Property Name enthält den Accountname, der nur zur Initialisierung gesetzt werden kann""")

class Ma_Account (Account):                       #Klasse Ma_Account erbt von Account 
    """ Der Account für Mitarbeiter der BO - Die Nummerierung erfolgt selbständig """
    ma_account_no = 0                             #Klassenvariable zum Erzeugen einer laufenden Nummer
    """ Das Klassenattribut zur Speicherung der laufenden Mitarbeiternummer """
    def __init__(self, name):                     #Magic-Method zur Initialisierung
        """ Die Initialisierung mit Mitarbeiternamen """
        super().__init__(name)                    #über super() wird die übergeordnetet Klasse angesprochen
        print(f"    Init Ma Account: {name}")
        type(self).ma_account_no += 1             #mit type(self) wird die aktuelle Klasse angesprochen
    
    def __str__(self):                            #Magic Method zum Drucken
        """ Die Funktion zur Textdarstellung """
        return (f"Mitarbeiter/in: {self.name}, MA{self.ma_account_no}")
		
#Einführen einer weiteren Vererbung - analog zu Ma_Account
class St_Account (Account):                       #Klasse St_Account erbt von Account 
    st_account_no = 0                             #Klassenvariable zum Erzeugen einer laufenden Nummer
    def __init__(self, name):                     #Magic-Method zur Initialisierung
        super().__init__(name)                    #über super() wird die übergeordnetet Klasse angesprochen
        print(f"    Init St Account: {name}")
        type(self).st_account_no += 1             #mit type(self) wird die aktuelle Klasse angesprochen
    
    def __str__(self):                            #Magic Method zum Drucken
        return (f"Student/-in: {self.name}, ST{self.st_account_no}")	

#Einführen einer doppelten Vererbung - analog zu Ma_Account
class St_Ma_Account ( St_Account, Ma_Account):                    #Klasse St_Account erbt von Account 
                                                  
    def __init__(self, name):                     #Magic-Method zur Initialisierung
        super().__init__(name)                    #über super() wird die übergeordnetet Klasse angesprochen
        print(f"  Init St Ma Account: {name}")
                                                  
    
    def __str__(self):                            #Magic Method zum Drucken
        return (f"student. Mitarbeiter/-in: {self.name}, ST{self.st_account_no}, MA{self.ma_account_no}")		

#Self test
g = St_Ma_Account("Test")
if str(g) == "student. Mitarbeiter/-in: Mein Name ist: Test, ST1, MA1":
    print("module works fine")
else:
    print("module is wrong")
