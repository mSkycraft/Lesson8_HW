import Inpt
import Otpt
from Interface import Intface

Intface('Welcome')
Inpt.OpenFile()
while(True):
    Intface('Menu')
    i = Inpt.Variable()
    match i:
        case 1: 
            Inpt.AddPerson()
            Intface('End')
            if(Inpt.Variable() == 2): 
                break
        case 2: 
            Inpt.path = input('Введите название файла базы')
            Inpt.OpenFile()
            Intface('End')
            if(Inpt.Variable() == 2): 
                break 
        case 3:
            Inpt.DelPerson()
            Intface('End')
            if(Inpt.Variable() == 2): 
                break
        case 4:
            Inpt.FindPerson()
            Intface('End')
            if(Inpt.Variable() == 2): 
                break
        case 5: 
            Otpt.PrintJson(Inpt.base)
            Intface('End')
            if(Inpt.Variable() == 2): 
                break
        case 6:
            Inpt.SafeBase()
            Intface('End')
            if(Inpt.Variable() == 2): 
                break
        case 9: 
            Inpt.SafeBase()
            break