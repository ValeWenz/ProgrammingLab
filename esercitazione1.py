"""
#esercizio 1
def convertire_minuti(minuti):
    minuti_resto = minuti % 60
    return minuti_resto
def convertire_ore(minuti):
    ore = minuti // 60
    return ore

ore=convertire_ore(538)
minuti_resto=convertire_minuti(538)
print(f"{ore}h, {minuti_resto}min")

#esercizio 2
x=input("inserisci un numero\n")
x=int(x)
print(f"{x*x}")
print(f"{x*x*x}")

#esercizio 3
x=input("inserisci un numero\n")
x=int(x)
if(x%2==0):
    print("il numero è pari")
else:
    print("il numero è dispari")

#esercizio 4
def conta_lettera(parola, lettera):
    contatore=0
    for i in parola:
        if(i ==lettera):
            contatore=contatore+1
    return contatore
parola=input("inserisci una parola\n")
lettera=input("inserisci una lettera\n")
rep=conta_lettera(parola,lettera)
print(f"{rep}")

#esercizio 5
def isPrime(numero):
    check=2
    for i in range(numero):
        if(numero%check==0):
            return 0
    return 1
numero=input("inserisci un numero\n")
numero=int(numero)
print(f"{isPrime(numero)}")

#esercizio 6
n=input("inserisci un numero, per fermarti digita 0\n")
n=int(n)
sum=0
while(n!=0):
    sum=sum+n
    n=input("inserisci un numero, per fermarti digita 0\n")
    n=int(n)
print(f"{sum}")

#esercizio 7
def fattoriale_it(numero):
    ret=1
    num=1
    for i in range(numero):
        ret=ret*num
        num+=1
    return ret
numero=input("inserisci un numero\n")
numero=int(numero)
print(f"{fattoriale_it(numero)}")

#esercizio 8
def is_triangle(a,b,c):
    if(a+b<c or a+c<b or b+c<a): 
        print("non può essere un triangolo")  #controllo la somma
        return -1
    elif(a-b>c or a-c>b or b-c>a):
        print("non può essere un triangolo")  #controllo la differenza
        return -1
    elif(a==b and b==c):
        print("è un triangolo equilatero")
        return 0
    elif(a==b or b==c or a==c):
        print("è un triangolo isoscele")
        return 0
    print("è un triangolo scaleno")
    return 0

a=int(input("inserisci numero a\n"))
b=int(input("inserisci numero b\n"))
c=int(input("inserisci numero c\n"))
is_triangle(a,b,c)

#esercizio 9
def count_voc(parola):
    count=0
    for lettera in parola:
        if(lettera=="a" or lettera=="e" or lettera=="i" or lettera=="o" or lettera=="u"):
            count+=1
    return count
parola=input("inserisci una parola\n")
print(f"il numero di vocali in {parola} è {count_voc(parola)}")
"""