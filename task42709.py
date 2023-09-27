def sum_digits(number):
 a=0
 while number!=0:
      a=a+number%10
      number=number//10
 return a 
number=int(input("Введите число:"))
print(sum_digits(number))