import random
#Создаем функции
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta jarjendisse
    """
    f=open(file,'r')
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_

def pscontrol(psword:str)->bool:
    """Функция вернет True если пароль будет соответстсвовать всем проверкам.
    """
    for i in range (0,13):
        if psword[i].isdigit == True:
            digit = "True"
        if psword[i].isalpha == True:
            alpha = "True"
        if psword[i].isupper == True:
            upper = "True"
        if psword[i].islower == True:
            lower = "True"
        break
    if digit=="True" and upper=="True" and lower=="True" and alpha=="True":
        ans=True
    else:
        ans=False
    return ans

def faili_sisu_umberkirjutamine(file:str,list_:list):
    with open(file,'w') as f:
        for slovo in list_:
            f.write(text+'\n')

def passautomat()->str:
    """Пароль создается машиной
    """
    str0=".,:;!_*-+()/#%@"
    str1= '0123456789'
    str2= 'qwertyuiopasdfghjklzxcvbnm'
    str3= str2.upper()
    str4= str0+str1+str2+str3
    ls = list(str4) #Список [".",",",":"...]
    random.shuffle(ls) #Перемешивает значения 
#Извлекаем из списка 12 произвольных значений
    psword = ''.join ([random.choice(ls) for x in range (12)])
#Пароль готов
    return psword
