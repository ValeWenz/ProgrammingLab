"""
#esercizi 1 e 3
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
        
#esercizio 2
class NumericalCSVFile(CSVFile):
    def __init__(self,nome):
        super().__init__(nome)
    def get_data(self):
        try:
            with open(self.nome, 'r') as file:
                data=[]
                for line in file:
                    riga_pulita=line.strip().split(',')
                    for idx in range(1,len(riga_pulita)):
                        try: 
                            riga_pulita[idx]=float(riga_pulita[idx])
                        except Exception:
                            print(f"la colonna {idx} presenta valore non valido")
                            #riga_pulita[idx]="NA"
                            riga_pulita=False
                            break
                    if riga_pulita: data.append(riga_pulita)
        except FileNotFoundError:
            print("path file non valido, mi spiace")
            raise FileNotFoundError
        return(data)
    
file=NumericalCSVFile("shampoo_sales(1).csv")
#print(file.get_data())

#esercizio 5
from datetime import datetime
attualmente=datetime.now()
stringa=input("inserisci la tua data di nascita nel formato (dd/mm/yyyy): ")
gg,mm,yy=map(int,stringa.split('/'))
compleanno=[]
if (attualmente.month>mm):
    compleanno.append(gg)
    compleanno.append(mm)
    compleanno.append(attualmente.year+1)
else:
    if(attualmente.month==mm):
        if(attualmente.day>gg):
            compleanno.append(gg)
            compleanno.append(mm)
            compleanno.append(attualmente.year+1)
        if(attualmente.day==gg):
            print("buon compleanno!!!")
            compleanno.append(gg)
            compleanno.append(mm)
            compleanno.append(attualmente.year+1)
    if(attualmente.month<mm):
        compleanno.append(gg)
        compleanno.append(mm)
        compleanno.append(attualmente.year)

compleanno=datetime(compleanno[2],compleanno[1],compleanno[0])
countdown=["gg","h","min","sec"]

gap=compleanno-attualmente
countdown[0]=gap.days
countdown[1]=gap.seconds//3600
resto=gap.seconds%3600
countdown[2]=resto//60
countdown[3]=resto%60
print(f"al prossimo compleanno mancano {countdown[0]} giorni, {countdown[1]} ore, {countdown[2]} minuti e {countdown[3]} secondi")


#esercizio 6
print("ciao! iniziamo")
while(True):
    N=input("inserisci un numero intero perfavore: ")
    try: 
        N=int(N)
        print(f"il quadrato è: {N*N}")
        break
    except Exception:
        print("ti ho chiesto un numero intero, riprova dai...")
"""

#esercizio 7
while(True):
    print("salve,che cosa vuoi fare? Digita:\n1)somma di due numeri\n2)differenza di due numeri\n3)uscire\n")
    ctrl=input("inserisci il codice: ")
    try:
        ctrl=int(ctrl)
    except Exception:
        print("non è un numero intero, mona")
    if(ctrl==1):
        x=int(input("inserisci il primo addendo: "))
        y=int(input("inserisci il secondo addendo "))
        print(f"la somma è: {x+y}")
    if(ctrl==2):
        x=int(input("inserisci il primo numero: "))
        y=int(input("inserisci il secondo numero: "))
        print(f"la sottrazione è: {x-y}")
    if(ctrl==3):
        print("grazie per aver usato il programma, arrivederci")
    if(ctrl!=1 and ctrl!=2 and ctrl!=3):
        print("input non valido, ti ho detto di mettere 1-2-3, non è difficile dai. Riprova")
        print("per uscire digita 3")
    else:
        break