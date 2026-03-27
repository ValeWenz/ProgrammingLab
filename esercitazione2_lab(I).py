'''
#esercizio 1
lista=[1,2,3,4] #somma=10
def somma_lista(lista):
    sum=0
    for numero in lista:
        sum=sum+numero
    return sum
print(f"{somma_lista(lista)}")

#esercizio 2
def is_palyndrome(parola):
    out=True
    for i in range(int(len(parola)/2)):
        if parola[i] != parola[-i-1]:
            out=False
    return out
parola="anna"
print(f"{is_palyndrome(parola)}")

#esercizio 3
def scambia(lista, i, j):
    tmp=lista[i]
    lista[i]=lista[j]
    lista[j]=tmp
    return lista
lista=[1,2,3,4,5,6]
lista=scambia(lista,1,5)
print(f"{lista}")

#esercizio 4
def el_comune(lista1,lista2):
    out=False
    for elemento in lista1:
        for membro in lista2:
            if membro==elemento: out=True
    return out
lista1=[1,2,3,4]
lista2=[5,6]
print(f"{el_comune(lista1,lista2)}")

#esercizio 5
def converti(lista):
    num_let=["zero","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    i=0
    for numero in lista:
        lista[i]=num_let[int(lista[i])]
        i+=1
    return lista
lista=[1,0,7,9,8]
print(f"{converti(lista)}")
'''
#------------------------------------------------------------------------------------------------
'''
#esercizio 1
def create_dic(lista):
    count=0
    dic={}
    for parola in lista:
        for elemento in lista:
            if parola==elemento: count+=1
        dic[f"{parola}"]=count
        count=0
    return dic
lista=["ciao","caravagna","ciao","sgherro","sgherro","ciao"]
print(f"{create_dic(lista)}")

#esercizio 2
def somma_vendite(file):
    out=0
    with open(f'{file}','r')as file:
        next(file)
        for line in file:
            data,prezzi=line.split(',')
            out=out + float(prezzi)
    return out
print(somma_vendite('shampoo_sales(1).csv'))

#esercizio 3
def conta_parola(file,parola):
    count=0
    with open(f'{file}','r') as file:
        for riga in file:
            termini=riga.split(' ')
            print(termini)
            for elemento in termini:
                if elemento.strip()==parola: count+=1
    return count
print(conta_parola('testuale.txt', 'ciao'))
'''
'''
#esercizio 4
def conteggio(file):
    dic={}
    with open(f'{file}','r') as file:
        for rigas in file:
            riga=rigas.split(' ')
            for parola in riga:
                if parola.strip() in dic: dic[parola.strip()]+=1
                else: dic[parola.strip()]=1
    return dic
print(conteggio('testuale.txt'))

#esercizio 5
def unico(file1, file2):
    lista_tot=[]
    with open(f'{file1}','r') as file:
        for rigas in file:
            riga=rigas.strip()
            if riga.strip() not in lista_tot: lista_tot.append(riga)
    with open(f'{file2}', 'w') as file:
        for riga in lista_tot:
            file.write(riga+"\n")
print(unico('testuale.txt','testuale.txt'))
'''
