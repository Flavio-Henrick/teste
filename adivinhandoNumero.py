nasc = int(input('por favor informe seu ano de nascimento      '))
num = int(input('por favor informe um numero entre 1 e 10     '))
num= num*2
num= num+5
num= num*50

aniv=int(input("voce ja fez aniversario esse ano? 1-sim 0-nao    "))

if aniv==1:
    num= num+1772
elif aniv==0:
    num= num+1771
else:
    aniv=int(input("o numero digitado foi invalido! respornda novamente: voce ja fez aniversario esse ano? 1-sim 0-nao     "))
    if aniv==1:
        num= num+1772
    elif aniv==0:
        num= num+1771

num= num-nasc

print("o resultado foi:",num,"onde:os primeiros digitos sao o numero que você pensou e ou ultimos a sua idade xD    ")