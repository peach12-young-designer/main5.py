from operator import mod
from random import randint
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import gmpy2




































Form, Window = uic.loadUiType("app5.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
def simpnum():
    l = 0
    while l < 1:
        global p
        p = randint(10000, 99999)
        exam = 2
        j = 0
        while exam**2 < p and j !=1:
            if p % exam == 0:
                j = 1

            exam += 1
        if j != 1:
            l += 1
            k=str(p)
            form.label.setText(k)
form.samplenum1.clicked.connect(simpnum)

def simpnum2():
    l = 0
    while l < 1:
        global q
        q = randint(10000, 99999)
        if q == p:
            break
        exam = 2

        j = 0
        while exam ** 2 < p and j != 1:
            if q % exam == 0:
                j = 1

            exam += 1
        if j != 1:
            l += 1
            k = str(q)
            form.label_2.setText(k)
form.samplenum2.clicked.connect(simpnum2)

def opnekey():
    global N
    N = p*p*q
    k=str(N)
    form.label_3.setText(k)
form.openkey.clicked.connect(opnekey)

def find_mod_inv(a,m):

    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('The modular inverse does not exist.')
def closedkey():
    lcm = math.lcm(p - 1, q - 1)
    a = N
    m = lcm
    print(m)

    try:
        res=gmpy2.invert(N,lcm)
        global d
        d=res
        k=str(res)
        form.label_4.setText(k)
        print("The required modular inverse is: "+ str(res))

    except:
        print('The modular inverse does not exist.')
form.closedkey.clicked.connect(closedkey)

def shareopenkey():
    form.label_5.setText("Успешно")
form.shareopenkey.clicked.connect(shareopenkey)

def getopenley():
    form.label_6.setText(str(N))
form.getopenkey.clicked.connect(getopenley)


def shifr():

    global letter
    letter = form.lineEdit.text()
    global s
    s=letter
    letter = letter.replace('а', '1')
    letter = letter.replace('б', '2')
    letter = letter.replace('в', '3')
    letter = letter.replace('г', '4')
    letter = letter.replace('д', '5')
    letter = letter.replace('е', '6')
    letter = letter.replace('ж', '7')
    letter = letter.replace('з', '8')
    letter = letter.replace('и', '9')
    letter = letter.replace('й', '10')
    letter = letter.replace('к', '11')
    letter = letter.replace('л', '12')
    letter = letter.replace('м', '13')
    letter = letter.replace('н', '14')
    letter = letter.replace('о', '15')
    letter = letter.replace('п', '16')
    letter = letter.replace('р', '17')
    letter = letter.replace('с', '18')
    letter = letter.replace('т', '19')
    letter = letter.replace('у', '20')
    letter = letter.replace('ф', '21')
    letter = letter.replace('х', '22')
    letter = letter.replace('ц', '23')
    letter = letter.replace('ч', '24')
    letter = letter.replace('ш', '25')
    letter = letter.replace('щ', '26')
    letter = letter.replace('ъ', '27')
    letter = letter.replace('ы', '28')
    letter = letter.replace('ь', '29')
    letter = letter.replace('э', '30')
    letter = letter.replace('ю', '31')
    letter = letter.replace('я', '32')
    letter = letter.replace(' ', '33')
    while letter[len(letter) - 1] == '+': letter = letter[0:len(letter) - 1]
    form.label_7.setText(letter)
    m=int(letter)
    print(m)
    global  c
    c = gmpy2.powmod(m,N,N)
    print("c =", c)

form.shifrmessege.clicked.connect(shifr)

def sendmessege():
    form.label_8.setText("Успешно")
form.sharemessege.clicked.connect(sendmessege)

def getmessege():
    form.label_9.setText(letter)
form.pushButton.clicked.connect(getmessege)



def razshifr():
    letter = gmpy2.powmod(c,d,p*q)
    letter=form.lineEdit.text()
    letter = letter.replace('а', '1')
    letter = letter.replace('б', '2')
    letter = letter.replace('в', '3')
    letter = letter.replace('г', '4')
    letter = letter.replace('д', '5')
    letter = letter.replace('е', '6')
    letter = letter.replace('ж', '7')
    letter = letter.replace('з', '8')
    letter = letter.replace('и', '9')
    letter = letter.replace('й', '10')
    letter = letter.replace('к', '11')
    letter = letter.replace('л', '12')
    letter = letter.replace('м', '13')
    letter = letter.replace('н', '14')
    letter = letter.replace('о', '15')
    letter = letter.replace('п', '16')
    letter = letter.replace('р', '17')
    letter = letter.replace('с', '18')
    letter = letter.replace('т', '19')
    letter = letter.replace('у', '20')
    letter = letter.replace('ф', '21')
    letter = letter.replace('х', '22')
    letter = letter.replace('ц', '23')
    letter = letter.replace('ч', '24')
    letter = letter.replace('ш', '25')
    letter = letter.replace('щ', '26')
    letter = letter.replace('ъ', '27')
    letter = letter.replace('ы', '28')
    letter = letter.replace('ь', '29')
    letter = letter.replace('э', '30')
    letter = letter.replace('ю', '31')
    letter = letter.replace('я', '32')
    letter = letter.replace(' ', '33')
    qqq=form.lineEdit.text()
    form.label_10.setText(qqq)
form.pushButton_2.clicked.connect(razshifr)


def simp():

    for i in range(5):
        rnd = randint(1,p-1)
        wh = rnd
        rnd = randint(1, p - 1)

        if (rnd ** ( p - 1) % p != 1):
            print("notsimp")


    for i in range(5):

        rnd = randint(1,q-1)

        if (rnd ** ( q - 1) % q != 1):
            print("notsimp")


    form.label_11.setText("Числа простые")

form.pushButton_3.clicked.connect(simp)

def eratosfen():
    a=[i for i in range(p+1)]
    a[1]=0
    i=2
    while i<p**0.5:
        if a[i] != 0:
            j=i**2
            while j<=p:
                a[j]=0
                j=j+1
        i=i+1
    a=[i for i in a if a[i] != 0]
    form.label_12.setText("Числа простые")
form.pushButton_4.clicked.connect(eratosfen)

app.exec()
