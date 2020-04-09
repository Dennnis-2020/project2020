import math
print('Решение квадратного уравнения')
print ('Введите почередно коэффициэнты квадратного уравнения: a, b и c')
a=int (input('a:'))
b=int (input('b:'))
c=int (input('c:'))
def diskrim(a0,b0,c0):
    return b0*b0-4*a0*c0
def koren_1(a1,b1,c1):
    return (-b1+math.sqrt(diskrim(a1,b1,c1)))/(2*a1)
def koren_2(a2,b2,c2):
    return (-b2-math.sqrt(diskrim(a2,b2,c2)))/(2*a2)

if b<0:
    if c<0:
        print('Уравнение имеет вид',a,'x*x',b,'x',c,'=0')
    else:
        print ('Уравнение имеет вид',a,'x*x',b,'x+',c,'=0')
else:
    if c < 0:
        print('Уравнение имеет вид', a, 'x*x+', b, 'x', c, '=0')
    else:
        print('Уравнение имеет вид', a, 'x*x+', b, 'x+', c, '=0')
print('Вычислив дискриминант квадратного уравнения D=b*b-4*a*c, найдем корни квадратного уранения')

print(diskrim(a,b,c))
if diskrim(a,b,c)>0:
    print('Имеем 2 корня квадратного уравнения')
    print('x1=',koren_1(a,b,c))
    print('x2=',koren_2(a,b,c))
elif diskrim(a,b,c)==0:
    print('Имеем 1 корень квадратного уравнения')
    print('x=',koren_1(a,b,c))
else:
    print('Корней у данного уравнения нет')

