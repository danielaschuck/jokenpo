#jokenpo
#acho q agora foi
#deixa o like se gostaram
import random
print("Digite pedra papel ou tesoura, digite com letra minuscula")
x=input()
print(" vc escolheu  " + x)
print("--"*22)
print("vez do pc escolher")
opcoes=["pedra","papel","tesoura"]
print("--"*22)
pc=random.choice(opcoes)
print(f'pc escolheu '+ pc)
print("--"*22)
if pc=="pedra" and x=="tesoura":
    print("pedea quebra tesoura vc perdeu")

elif pc== "papel" and x =="pedra":
    print("papel cobre pedra voce perdeu")

elif pc=="tesoura" and x=="pedra":
    print("pedra quebra tesoura voce ganhou")
    
elif pc== x:
    print("empatou tenta dnv")

elif pc=="papel" and x== "tesoura":
    print("tesoura corta papel voce venceu")

elif pc =="pedra" and x== "papel":
    print("papel cobre pedra voce venceu")

else :
    print("pedra quebra tesoura voce venceu")