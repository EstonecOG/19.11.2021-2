from Funktsioonid import *
users=["Kliment"]
passwords=["12345"]

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
        #
    elif v==3:
        print("Valja")
        break
        #
    else:
        print("On vaja valida 1,2 voi 3")