import turtle, random, time

def puan(x,y):
    global p
    p = p + 1
    yaz.clear()
    yaz.write('Puan: {}'.format(p), align='center', font = ('Courier', 24, 'normal'))
    ok.goto(random.randint(-300,300),random.randint(-300,300))
    

pencere = turtle.Screen()
pencere.title('Refleks Oyunu')
pencere.bgcolor('lightblue')
pencere.setup(width=600, height=600)

ok = turtle.Turtle()
ok.speed(0)
ok.shape('circle')
ok.color('red')
ok.shapesize(3)
ok.penup()
ok.goto(random.randint(-300,300),random.randint(-300,300))

p = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('black')
yaz.penup()
yaz.goto(0,260)




sure = 7
while True:
    baslangicSure = time.time()
    while (time.time() - baslangicSure) < sure:
        ok.onclick(puan)
        #yaz2.clear()
        #yaz2.write('Süre: {}'.format(time.time() - baslangicSure), align='Center',font = ('Courier', 24, 'normal'))
    else:
        p = 0
        yaz.clear()
        yaz.write('Başla', align='center', font = ('Courier', 24, 'normal',))
