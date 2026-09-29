Idade = input("Digite sua idade: ")

if int(Idade) < 18:
    print("És menor de idade. Então vamos ver a tua abilidades matemática.")
    Num1= input(" Digite um número maior que 10: ")
    Num2= input(" Agora digite outro número maior que 10: ")

    if int(Num1) < 10 or int(Num2) < 10:
     print("Não digitou um número maior que 10. Deverás estar mais atento nas instruções. Tenta novamente.")
    else: 
       Numrecebido = input(" Digite o Produto desses dois números: ")
       if int(Numrecebido) == int(Num1) * int(Num2):
        print("Parabéns, acertaste o produto!")
       else:
        print("Erraste o produto, tenta novamente. E deverás estudar mais matemática.") 

else:
    print("És maior de idade.")
    Work= input('Qual seu trabalho?')
    print('Agora iremos fazer um teste:')
    Multidade= input('Qual é sua idade multiplicado por 45?:')

    if int(Multidade) == int(Idade) * 45:
      print('És bom em matemática.')
      print(f'O que é impresionate para uma pessoa com {Idade} e que trabalha como {Work}!')
    else:
      print('Tens de voltar a estudar matematica')






