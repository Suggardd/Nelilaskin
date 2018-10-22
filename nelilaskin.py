def jakolasku(x, y):
    try: 
        n = x / y
        print("Tulos: {}".format(n))
    except ZeroDivisionError:
        print("Tällä ohjelmalla ei pääse äärettömyyteen")
        

def kertolasku(x, y):
    n = x * y
    print("Tulos: {}".format(n))

def yhteenlasku(x, y):
    n = x + y
    print("Tulos: {}".format(n))

def vahennuslasku(x, y):
    n = x - y
    print("Tulos: {}".format(n))



while True:
    valinta = input("Valitse operaatio (+, -, *, /): ")
    if valinta != '+' and valinta != '-' and valinta != '*' and valinta != '/':
        print("Operaatiota ei ole olemassa")
        break
   
    else:
        try:
            x = float(input("Anna luku x: "))
            y = float(input("Anna luku y: "))
        except ValueError:
            print("Ei tämä ole mikään luku")
            break
        except EOFError:
            print("Ei tämä ole mikään luku")
            break
    
        else:
            if valinta == '+':
                yhteenlasku(x, y)
                break
            elif valinta == '-':
                vahennuslasku(x, y)
                break
            elif valinta == '*':
                kertolasku(x, y)
                break
            elif valinta == '/':
                jakolasku(x, y)
                break
            
        



    
    




    

