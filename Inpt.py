from collections import defaultdict
import os
import json
import Otpt
file = None
path = 'Base.json'

base = {}
base = defaultdict(list)

def addinbase(FIO,Type,Number):
    global base
    print(base)
    base[Type].append({
        'FIO' : FIO,
        'Type': Type,
        'Num': Number
    })

def FindPerson():
    prson = input('Введите точное ФИО для поиска: ')
    global base
    keys = base.keys()
    flag = False
    count = 0
    fbase = {}
    fbase = defaultdict(list)
    for types in keys:
        for i in range(len(base[types])):
            if(base[types][i]['FIO']==prson):
                fbase[types].append(base[types][i])
                flag = True
                count +=1
    if flag == True:
        print(f'Найдено {count} элементов')
        Otpt.PrintJson(fbase)
    else:
        print(f'Элемент {prson} не найден в базе')

def DelPerson():
    prson = input('Введите точное ФИО для удаления: ')
    global base
    keys = base.keys()
    flag = False
    count = 0
    for types in keys:
        for i in range(len(base[types])):
            if(base[types][i]['FIO']==prson):
                base[types].pop(i)
                flag = True
                count += 1
    if flag == True:
        print(f'Удалено {count} элементов')
    else:
        print(f'Элемент {prson} не найден в базе')

def AddPerson():
    addinbase(input('Введите ФИО: '),input('Введите группу: '),input('Введите номер телефона: '))

def OpenFile():
    global file
    global path
    global base
    if(file == None):
        file = open(path,'r')
    else:
        file.close()
        file = open(path,'r')
    if(os.path.getsize(path)!=0):
        print('Load base')
        base = json.load(file)
        file.close()

def SafeBase():
    global file
    global base
    if(file != None):
        file.close()
        file = open(path,'w')
        json.dump(base,file)
        file.close()
        file = None

def Variable():
    return int(input('Введите номер действия'))