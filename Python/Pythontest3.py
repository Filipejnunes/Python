Num1= int(input('Insira um numero: '))
Num2= int(input('Insira outro numero: '))
Num= int(input('Insira o numero de vezes que o programa vai rodar (no minimo 3 e multipos de 3): '))
range1= int(Num /3)

if Num2 < Num1:
  for i in range(range1):
      print(Num2)
      Num3=(Num1 + Num2)
      print(Num3)
      Num1=(Num2 + Num3)
      print(Num1)
      Num2 = (Num1 + Num3)
else:
   for i in range(range1):
         print(Num1)
         Num3= (Num1 + Num2)
         print(Num3)
         Num1= (Num2 + Num3)
         print(Num1)
         Num2= (Num1 + Num3)
         print(Num2)
       
  
