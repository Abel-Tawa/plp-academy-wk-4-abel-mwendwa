print('welcome to simple calculator, input mumbers')
x=int(input(' write first number:'))
y=int(input(' write second number:'))
op=int(input('select operation 1.add 2.subtract 3. multiply 4.divide:'))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
if op==1 :
    print(x,'+',y,"=",add(x,y))
elif op==2 :
    print(x,'-',y,"=",sub(x,y))
elif op==3 :
    print(x,'*',y,"=",mul(x,y))
elif op==4 :
    print(x,'/',y,"=",div(x,y))
else:
    print ('invalid input')    
  


