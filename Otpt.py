import Inpt

def PrintJson(base):
    keys = base.keys()
    for types in keys:
        for person in Inpt.base[types]:
            pkey = person.keys()
            for k in pkey:
                print(f"{k} ",end=' | ')
            print('')
            for k in pkey:
                print(f'{person[k]}',end= ' | ')
            print('')
