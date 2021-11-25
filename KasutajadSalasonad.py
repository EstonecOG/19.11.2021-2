from Funktsioonid import*
from Too_failidega import*
users=loe_failist_listisse("users.txt")
passwords=loe_failist_listisse("passwords.txt")
print(users)
print(passwords)

while True:
    print("Reg-1,Avt-2,Valja-3")
    v=int(input())
    if v==1:
        print("Registreerimine")
        while 1:
            log=input("Kasutajatunnus")
            if log in users:
                print("Tunnus soobib")
                break
            else:
                print("See nimi juba on olemas listis")
        v=input("Arvuti-A voi ise-I loob parool")
        if v.upper() == "A":
            pas=pscontrol(psword)
        elif v.upper() == "I":
            pas=input("Sisestma oma parool")
            tulemus=pscontrol(pas)
            if tulemus == True:
                users:append(log)
                passwords.append(pas)
                break
        #
    elif v==2:
        print("Avtoriseerimine")
        log=input("Login:")
        if log not in users:
            print ("Sina ei ole registreeritud")
        pas=input("Password:")
        if pas not in passwords:
            print("Vale parool")
        if passwords.index(pas)==users.index(user):
            print("Tere tulemast")
        #
    elif v==3:
        print("Valja")
        faili_sisu_umberkirjutamine("users.txt",users)
        faili_sisu_umberkirjutamine("passwords.txt",passwords)
        break
        #
    else:
        print("On vaja valida 1,2 voi 3")