'''
#esercizio 1
class Veicolo():
    def __init__(self,modello,marca,anno):
        self.modello=modello
        self.marca=marca
        self.anno=anno
        self.speed=0
    def __str__(self):
        return 'Veicolo "{} {} {} {}"'.format(self.modello, self.marca, self.anno, self.speed)
    def accelerare(self):
        self.speed+=5
        return self.speed
    def frenare(self):
        self.speed-=5
        return self.speed
    def get_speed(self):
        return self.speed
#---------------------------------------------
'''
#esercizio 2
class CSVFile():
    def __init__(self,nome):
        if type(nome)==str:
            self.nome=nome
        else:
            raise Exception('il nome non è una stringa')
    def get_data(self,start=None,end=None):
        try:
            open(self.nome,'r')
        except FileNotFoundError:
            print("impossibile aprire il file")
        else:
            data=[]
            with open(self.nome,'r') as file:
                if start>end:
                    raise("start>end, non valido")
                if start<0 or start>len(file):
                    raise("formato start non valido")
                if end>len(file) or end<0:
                    raise("formato end non valido")
                if type(end) or type(start) != int:
                    raise("start e end devono essere interi")
                if start==None:
                    start=0
                if end==None:
                    end=0 
                for i in range(start):
                    next(file)
                counter=1
                for line in file:
                    if counter<(end-start):
                        elementi=line.strip().split(',')
                        if elementi != ' ': 
                            data.append(elementi)
                    counter+=1
            return data

#--------------------------------------------
'''

#esercizio
class Canguro():
    def __init__(self):
        self.contenuto_tasca=[]
    def intasca(self,other):
        self.contenuto_tasca.append(other)
    def __str__(self):
        return '{}'.format(self.contenuto_tasca)

can=Canguro()
guro=Canguro()
can.intasca(9)
can.intasca(10)
print(f"questo è can {can}")
print(f"questo è guro {guro}")
'''
#---------------------------------------------
'''
#esercizio 1
class Persona:
    def __init__(self,ruolo,nome,cognome):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome
    def saluta(self):
        print('ciao sono',self.ruolo+",", self.nome, self.cognome)
class Studente(Persona):
    def __init__(self,nome,cognome,corso):
        super().__init__("Studente UNITS",nome,cognome)
        self.corso=[]
    def saluta(self):
        Persona.saluta(self)
        print(">ho frequentato: ", self.corso)
class Docente(Persona):
    def __init__(self,nome,cognome,corso):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso=[]
    def saluta(self):
        Persona.saluta(self)
        print(">docente dei corsi: ", self.corso)

Irene=Studente('irene','rossi','')
corsi_di_irene=["programmazione", "laboratorio", "analisi", "geometria"]
for elem in corsi_di_irene:
    Irene.corso.append(elem)
Irene.saluta()


#esercizio 2
class Auto(Veicolo):
    def __init__(self, modello, marca, anno,numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte=numero_porte
    def __str__(self):
        return 'Auto {} {} {} {} {}'.format(self.modello, self.marca, self.anno, self.speed, self.numero_porte)
    
class Moto(Veicolo):
    def __init__(self,modello,marca,anno,tipo):
        super().__init__(modello,marca,anno)
        self.tipo=tipo
    def __str__(self):
        return 'Moto {} {} {} {} {}'.format(self.modello, self.marca, self.anno, self.speed, self.tipo)

bmw=Auto('a4', 'bmw',2006,4)
bmw.accelerare()
honda=Moto('a4','honda',2007,'sportiva')
honda.accelerare()
honda.accelerare()

#esercizio 3
def controllo(studente,docente):
    for materia in docente.corso:
        if materia not in studente.corso:
            return False
    return True
Irene=Studente('irene','rossi','')
corsi_di_irene=["programmazione", "laboratorio", "analisi", "geometria"]
for elem in corsi_di_irene:
    Irene.corso.append(elem)
Eva=Docente('eva','sinchich','')
corsi_di_eva=["programmazione", "laboratorio", "analisi", "algebra"]
for elem in corsi_di_eva:
    Eva.corso.append(elem)
print(f'{controllo(Irene,Eva)}')

#esercizio 4
class Poligono():
    def __init__(self,lati):
        self.lati=lati
    def __str__(self):
        return (f'sono un poligono con {self.lati} lati')
class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
    def __str__(self):
        return ('sono un quadrilatero')
class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()
        self.base=base
        self.altezza=altezza
    def __str__(self):
        return 'sono un rettangolo'
    def perimetro(self):
        return (2*self.base) + (2*self.altezza)
    def area(self):
        return self.base*self.altezza
class Triangolo(Poligono):
    def __init__(self, lato1,lato2,lato3):
        super().__init__(3)
        self.lato1=lato1
        self.lato2=lato2
        self.lato3=lato3
    def __str__(self):
        return 'sono un triangolo'
    def perimetro(self):
        return self.lato1+self.lato2+self.lato3
    def is_equilatero(self):
        if (self.lato1==self.lato2==self.lato3): return True
        else: return False
'''
#----------------------------------