import turtle
from turtle import *


while True:
  try:
      print("enter int > 2")
      n=int(input(">"))
      if not n >2:
        raise ValueError
      break
  except:
      pass

speed(5)

for i in range(1, n+1):
  if i == 1:
      print(" "*int(n-2),end="")
      print("*")
  
      pencolor("yellow")
      for _ in range(8):
          forward(75)
          left(144)
      left(108)

      penup()
      back(0.258819045 * 60 )
      left(60)
      forward(60)
      right(165)
      pendown()
      pencolor("green")

      for _ in range(i):
          forward(60)
          right(150)
          forward(60)
          left(150)
      left(105)
      forward(i * 0.258819045*60*2)##sin 15 = 0.258819045

      penup()
      left(75)
      forward(60)
      left(180)
      pendown()
      
  elif n == i:
      print(" "*int(n-2),end="")
      print("'",end="")
      print()
      right(180)
      forward(((n-1) * 0.258819045*60)-10)
      pencolor("brown")
      right(90)
      forward(30)
      left(90)
      forward(20)
      left(90)
      forward(30)


  else:
      print(" " * ((n-i)-1), end="")
      for a in range(i-1):
          print("'" + '"', end="")
      print("'", end="")
      for _ in range(i):
          forward(60)
          right(150)
          forward(60)
          left(150)
      left(105)
      forward(i * 0.258819045*60*2)
      if not n-1 == i:
        penup()
        left(75)
        forward(60)
        left(180)
        pendown()
      print()

done()
