# не использовались символы квадрата и круга обозначающие корабли и пустые клетки, по причине того, что поле расползается и не соответствует координатам так же как и в самом задании. и игроку становится трудно определить координату клетки для выстрела
from random import randint

koorigroka = [1,1,1,3,1,5,3,4,3,1,3,2,5,4,6,4,4,6,6,6,2,1,6,1,4,2,1,3,6,3,6,4,5,6,6,6,3,4,3,6] #координаты всех кораблей
#print (koorigroka)                                  | граница
count = 0
popal='X'
promah='T'
pusto='O'
paluba='*'

class VistrelNeTuda (Exception):
    def __init__(self, soobschenie):
        self.soobschenie = soobschenie

    def __str__(self):
        print ('Исключение')
        return 'Упс, ошибочка вышла,{0}'.format(self.soobschenie)

class Pole:
    def __init__(self):
        self.name = 'ii'
        self.pool = [[pusto for _ in range(6)] for _ in range (6)] # o - открытая позиция
        #self.zapretdlyastrelbi = [['o' for _ in range(6)] for _ in range (6)]         #список с координатами куда уже был произведен выстрел
        self.zapretdlyakorablya = [[pusto for _ in range(6)] for _ in range (6)]        #список с координатами где уже стоит корабль и буферная зона вокруг него

class Ships(Pole):                                 #создаем класс кораблей
    def __init__(self, name_object_pole):
        #self.koordinatikorablya2 = []
        #self.koordinatikorablya3 = []
        self.name_object_pole = name_object_pole
        global count
        for u in range(4):
            t = False
            while not t:
                self.koordinatikorablya1 = []
                self.koordinatikorablya1=[koorigroka[count], koorigroka[count+1]]            #УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                count += 2  # УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #self.koordinatikorablya1 = list(map(int, ((input(f'введите координату {u +1}-го однопалубного корабля')).split() )))
                #print(self.koordinatikorablya1)
                t = rasstavitkorabli(self, self.name_object_pole)
            self.koordinatikorablya1 = []
        for u in range(2):
            t = False
            while not t:
                self.koordinatikorablya2 = []
                self.koordinatikorablya2 = [koorigroka[count], koorigroka[count + 1], koorigroka[count + 2], koorigroka[count + 3]]  # УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                count += 4  # УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #self.koordinatikorablya2 = list(map(int, ((input(f'введите координаты начала и конца {u +1}-го двухпалубного корабля')).split() )))
                #print(self.koordinatikorablya2)
                t = rasstavitkorabli(self, self.name_object_pole)
            self.koordinatikorablya2 = []
        t=False
        while not t:
            self.koordinatikorablya3 = []
            self.koordinatikorablya3 = [koorigroka[count], koorigroka[count + 1], koorigroka[count + 2], koorigroka[count + 3]]  # УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            count += 4  # УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #self.koordinatikorablya3 = list(map(int, ((input('введите координаты начала и конца трехпалубного корабля')).split())))
            #print(self.koordinatikorablya3)
            t = rasstavitkorabli(self, self.name_object_pole)
        self.koordinatikorablya3 = []
        #count=0
        #self.koordinatikorablya2 = list(map(int, ((input('vvedite cherez probeli koordinati nachala i konca dvuh dvupalubnih korablej, v formate: Nachalo_vert Nachalo_goriz Konec_vert Konec_goriz')).split())))
        #rasstavitkorabli(self, igrok)
        #self.koordinatikorablya3 = list(map(int, ((input('vvedite cherez probeli koordinatu nachala i konca trehpalubnogo korablya v formate: Nachalo_vert Nachalo_goriz Konec_vert Konec_goriz')).split())))
        #rasstavitkorabli(self, igrok)

def rasstavitkorabli(a, b):  # а-корабли b- игрок на поле на которого необходимо расставить

    if a.koordinatikorablya1:
        if b.zapretdlyakorablya[a.koordinatikorablya1[0] - 1][a.koordinatikorablya1[1] - 1] == pusto:
            b.pool[a.koordinatikorablya1[0] - 1][a.koordinatikorablya1[1] - 1] = paluba
            for z in range(-1, 2):
                for z1 in range(-1, 2):
                    if all([(a.koordinatikorablya1[0] - 1+z)>=0, (a.koordinatikorablya1[1] - 1+z1)>=0, (a.koordinatikorablya1[0] - 1+z)<=5, (a.koordinatikorablya1[1] - 1+z1)<=5]):
                        b.zapretdlyakorablya[a.koordinatikorablya1[0] - 1+z][a.koordinatikorablya1[1] - 1+z1] = '.' #ставим метки о невозможности постановки кораблей, в пределах игрового поля
            #pechatpolya(b.pool, b.zapretdlyakorablya)
            return True
        else:
            print ('проверьте правильность введенных координат, и попробуйте еще раз')
            return False


    if a.koordinatikorablya2:
        if b.zapretdlyakorablya[a.koordinatikorablya2[0] - 1][a.koordinatikorablya2[1] - 1] == pusto and b.zapretdlyakorablya[a.koordinatikorablya2[2] - 1][a.koordinatikorablya2[3] - 1] == pusto:
            for otr in range(0, 4, 2):
                b.pool[a.koordinatikorablya2[otr] - 1][a.koordinatikorablya2[otr+1] - 1] = paluba #всего 2 корабля по 4 координаты (начало и конец) в каждом=8 коорд
                for z in range(-1, 2):
                    for z1 in range(-1, 2):
                        if all([(a.koordinatikorablya2[otr] - 1+z)>=0, (a.koordinatikorablya2[otr+1] - 1+z1)>=0, (a.koordinatikorablya2[otr] - 1+z)<=5, (a.koordinatikorablya2[otr+1] - 1+z1)<=5]):
                            b.zapretdlyakorablya[a.koordinatikorablya2[otr] - 1+z][a.koordinatikorablya2[otr+1] - 1+z1] = '.' #ставим метки о невозможности постановки кораблей, в пределах игрового поля
            #pechatpolya(b.pool, b.zapretdlyakorablya)
            return True
        else:
            print ('проверьте правильность введенных координат, и попробуйте еще раз')
            return False

    if a.koordinatikorablya3:
        if all([b.zapretdlyakorablya[a.koordinatikorablya3[0] - 1][a.koordinatikorablya3[1] - 1] == pusto, b.zapretdlyakorablya[a.koordinatikorablya3[2] - 1][a.koordinatikorablya3[3] - 1] == pusto, b.zapretdlyakorablya[max(a.koordinatikorablya3[2], a.koordinatikorablya3[0]) - 2][a.koordinatikorablya3[1] - 1] == pusto if a.koordinatikorablya3[1] == a.koordinatikorablya3[3] else b.zapretdlyakorablya[a.koordinatikorablya3[2] - 1][max(a.koordinatikorablya3[3], a.koordinatikorablya3[1]) - 2] == pusto if a.koordinatikorablya3[0] == a.koordinatikorablya3[2] else False]):
            for otr in range(0, 4, 2):
                b.pool[a.koordinatikorablya3[otr] - 1][a.koordinatikorablya3[otr+1] - 1] = paluba #всего 1 корабль  4 координаты (начало и конец), нужно вычислить еще середину
                for z in range(-1, 2):
                    for z1 in range(-1, 2):
                        if all([(a.koordinatikorablya3[otr] - 1+z)>=0, (a.koordinatikorablya3[otr+1] - 1+z1)>=0, (a.koordinatikorablya3[otr] - 1+z)<=5, (a.koordinatikorablya3[otr+1] - 1+z1)<=5]):
                            b.zapretdlyakorablya[a.koordinatikorablya3[otr] - 1+z][a.koordinatikorablya3[otr+1] - 1+z1] = '.' #ставим метки о невозможности постановки кораблей, в пределах игрового поля
            #если корабль по горизонтали
            if a.koordinatikorablya3[0] == a.koordinatikorablya3[2]:
                b.pool[a.koordinatikorablya3[2] - 1][max(a.koordinatikorablya3[3], a.koordinatikorablya3[1]) - 2] = paluba
                for z in range(-1, 2):
                    for z1 in range(-1, 2):
                        if all([(max(a.koordinatikorablya3[3], a.koordinatikorablya3[1]) - 2+z)>=0, (a.koordinatikorablya3[2] - 1+z1)>=0, (max(a.koordinatikorablya3[3], a.koordinatikorablya3[1]) - 2+z)<=5, (a.koordinatikorablya3[2] - 1+z1)<=5]):
                            b.zapretdlyakorablya[(max(a.koordinatikorablya3[3], a.koordinatikorablya3[1]) - 2+z)][a.koordinatikorablya3[2] - 1+z1] = '.' #ставим метки о невозможности постановки кораблей, в пределах игрового поля
            #если корабль по вертикали
            elif a.koordinatikorablya3[1] == a.koordinatikorablya3[3]:
                b.pool[max(a.koordinatikorablya3[0], a.koordinatikorablya3[2]) - 2][
                    a.koordinatikorablya3[3] - 1] = paluba
                for z in range(-1, 2):
                    for z1 in range(-1, 2):
                        if all([(max(a.koordinatikorablya3[0], a.koordinatikorablya3[0]) - 2 + z) >= 0,
                                (a.koordinatikorablya3[3] - 1 + z1) >= 0,
                                (max(a.koordinatikorablya3[0], a.koordinatikorablya3[2]) - 2 + z) <= 5,
                                (a.koordinatikorablya3[3] - 1 + z1) <= 5]):
                            b.zapretdlyakorablya[(max(a.koordinatikorablya3[0], a.koordinatikorablya3[2]) - 2 + z)][
                                a.koordinatikorablya3[
                                    3] - 1 + z1] = '.'  # ставим метки о невозможности постановки кораблей, в пределах игрового поля
            else: #если не вертикаль, не горизонталь не подходят, то получается диагональ
                print('проверьте правильность введенных координат, и попробуйте еще раз')
                return False

            #pechatpolya(b.pool, b.zapretdlyakorablya)
            return True
        else:
            print ('проверьте правильность введенных координат, и попробуйте еще раз')
            return False
    #pechatpolya(igrok.pool, ii.pool)


def pechatpolya(a, b):   #отрисовка доски состоящей из двух полей
    st = ' '
    for i in range(1, 7):
        st += (f'|{i}' if i < 6 else f'|{i}|')
    print('   ', a.name, '              ', b.name)
    print(st, '    ', st)
    st = ''
    for g in range(6):
        st = str(g + 1)
        stigrok = ''
        stii = ''
        for v in range(6):
            stigrok += f'|{a.pool[g][v]}'
            stii += f"|{b.pool[g][v] if a.name== 'admin' else '.' if b.pool[g][v] in [paluba, pusto]  else b.pool[g][v]}"
        print(st + stigrok + '|      ' + st + stii + '|')
    print ('* - ваши корабли,  О - пустая ячейка,  Т - промах, Х - поражение корабля, . - скрытая ячейка противника (может есть корабль, а может и нет')

def hod(imya, protivnik):
    vistrel =[]
    try:
        if imya.name == 'ii':
            vistrel = [randint(1, 6), randint(1, 6)]
        else:
            vistrel = list(map(int, ((input(f'игрок {imya.name} введи координаты выстрела через пробел')).split())))
        if protivnik.pool[vistrel[0]-1][vistrel[1]-1] == paluba:  #esli korabl, to proveryem na pobedu, esli ne pobeda to esche raz hodi
            protivnik.pool[vistrel[0]-1][vistrel[1]-1] = popal
            pechatpolya(igrok, ii)
            if imya.name == 'ii':
                print(f'искусственный интеллект сделал ход {vistrel[0], vistrel[1]} ')
            print(f'{imya.name}, ты попал точно в цель')
            if paluba not in (sum(protivnik.pool, [])): #esli korablej na pole net to pobeda :-)
                print(f'победа игрока {imya.name}')
                return True
            if hod (imya, protivnik):
                return True
            return False
        elif protivnik.pool[vistrel[0]-1][vistrel[1]-1] == pusto: #tut proverka promaha, no v ramkah polya
            protivnik.pool[vistrel[0]-1][vistrel[1]-1] = promah
            pechatpolya(igrok,ii)
            if imya.name == 'ii':
                print(f'искусственный интеллект сделал ход {vistrel[0], vistrel[1]} ')
            print(f'{imya.name}, у тебя промах')
            return False
        elif protivnik.pool[vistrel[0]-1][vistrel[1]-1] == promah or popal:
            raise VistrelNeTuda ('сюда уже стреляли!')
    except VistrelNeTuda:
        if imya.name != 'ii':
            print ('сюда уже стреляли!')
        if hod(imya, protivnik):
            return True
        return False
    except:
        print (f'игрок {imya.name} проверь правильность введенных координат, попытайся еще разок')
        if hod(imya, protivnik):
            return True
        return False


def boj():
    pobeda =False
    kontrol_hoda=1
    while not pobeda:
        pobeda = hod(ii, igrok) if kontrol_hoda % 2 == 0 else hod(igrok, ii)
        #print('pobeda=', pobeda)
        kontrol_hoda+=1


igrok = Pole()
igrok.name = input('vvedite imya')
ii = Pole()
#pechatpolya(igrok.pool, ii.pool)
korabliigr = Ships(igrok)
#korabliigr.name=igrok.name
korabliii = Ships(ii)
#korabliii.name = ii.name
#print (korabliigr.name, korabliii.name)
#rasstavitkorabli(korabliigr,igrok)
#pustoepole = Pole()

pechatpolya(igrok, ii)
boj()

#print(korabli.koordinatikorablya1, korabli.koordinatikorablya2, korabli.koordinatikorablya3)

#shipigrok = Ship(input('введите координаты 4-х однопалубных кораблей'), input('введите координаты 2-х двупалубных кораблей'), input('введите координаты одного трехпалубного корабля'))
