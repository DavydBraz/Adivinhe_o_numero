#adivinhador basico de um numero
#se for rapido, faco de uma letra

#importando a biblioteca random, que vai ser importante para gerar um numero aleatorio
import random

#Funcao advinhador
def Advinhador():
  #O escolha serve para permitir que o jogador escolha ate o numero que dejesar ir para advinhar
  escolha=int(input("\nQual o valor maximo para se advinhar: "))

  #Variavel que vai gerar o numero para se advinhar
  sorteio=int(random.randint(0,escolha))

  #laco infinito ate acertar
  while True:  
    #o valor que quer "chutar" para advinhar
    chute=int(input("\nChute qual o numero: "))

    #se o numero chutado for menor que o que quer advinhar, informe
    if chute<sorteio:
      print("\nO numero que deseja advinhar é maior que o valor digitado, tente novamente!")
    #se nao, se o numero for maior que o que quer advinhar, informe
    elif chute>sorteio:
      print("\nO numero que deseja advinhar é menor que o valor digitado, tente novamente!")
    #se nenhuma das opcoes acima, informe que acertou e pare a execucao
    else:
      print("\nVOCE ACERTOU PARABENS!!!!!!!!!!")
      break

#chamando a funcao
Advinhador()
