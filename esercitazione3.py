'''
#esercizio 1
lista=[n for n in range(9) if n%2!=0]
#print(lista)

#eserczio 2
Input=[[1,2,3],[4,5],[6,7,8,1]]
lista2=[elem for sottolista in Input for elem in sottolista]
#print(lista2)

#esercizio 3
lista_a=[1,3,5,7]
lista_b=[2,4,6]
lista3=[x*y for x in lista_a for y in lista_b if(x*y)>10]
#print(lista3)

#esercizio 4
def pitagora(a,b,c):
    if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c ==a*a): return True
    else: return False

lista4=[(a,b,c) for a in range(1,21) for b in range(1,21) for c in range(1,21) if pitagora(a,b,c)]
#print(lista4)

#esercizio 5
list_a=[0,1,3,4]
list_b=['a','b','c']

lista5=[(num,elem) for num in list_a if num%2==0 for idx,elem in enumerate(list_b) if idx%2!=0]
print(lista5)

#esercizio 8
sentence="the cat sat on the mat the cat"
dict8={parola: sentence.count(parola) for parola in sentence.split(' ')}
print(dict8)
'''