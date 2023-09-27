import math
def sum(num1,num2):
  print("Ответ:", num1+num2)
def diff(num1,num2):
   print("Ответ:", num1-num2)
def mult(num1,num2):
   print("Ответ:", num1*num2)
def div(num1,num2):
  print(num1/num2)
def exp(num):
  st=int(input("Введите степень:"))
  print(num**st)
def sqrt(num):
  print(math.sqrt(num))
def fact(num3):
  print(math.factorial(num3))
def sin(num):
  print(math.sin(num))
def cos(num):
  print(math.cos(num))
def tan(num):
  print(math.tan(num))
while choice!=11:
  print("1. Сложение")
  print("2. Вычитание")
  print("3. Умножение")
  print("4. Деление")
  print("5. Возведение в степень")
  print("6. Квадратный корень")
  print("7. Факториал")
  print("8. Синус")
  print("9. Косинус")
  print("10. Тангенс")
  print("11. Завершение программы")
  try:
    choice=int(input())
  except:
    print("Введите действие")
  if choice in range (1,11):
    if choice in range (1,5):
      try:
        num1=float(input("Введите число 1:"))
        num2=float(input("Введите число 2:"))
      except:
        print("Это не число!")
        continue
    if choice==1:
      sum(num1,num2)
    if choice==2:
     diff(num1,num2)
    if choice==3:
     mult(num1,num2)
    if choice==4:
      if num2==0:
        print("Число 2 не может равняться 0, введите число ещё раз")
        continue
      div(num1,num2);
    if choice in range (5,11):
     try:
      num=float(input("Введите число:"))
     except:
      print("Это не число!")
      continue
     if choice==5:
      exp(num)
     if choice==6:
      if num>=0:
        sqrt(num)
      else:
        print("Число не может быть отрицательным, введите его ещё раз:")
        continue
     if choice==7:
      num3 = int(num)
      if num>=0:
        fact(num3)
      else:
        print("Число не может быть отрицательным, введите его ещё раз:")
        continue
     if choice==8:
      sin(num)
     if choice==9:
      cos(num)
     if choice==10:
      tan(num)
    print("Выберете операцию ещё раз:")