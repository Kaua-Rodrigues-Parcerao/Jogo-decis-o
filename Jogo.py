input("Pense em um número, quando pensar aperte 'ENTER' para começar.... ")

c = input("Seu número é 5? ").lower()
if c == "sim":
    print("Seu número é o 5!")
if c == "não" or c == "nao":
    met = input("Então seu número é maior que 5? .... ").lower()
    if met == "sim":
        p = input("Seu número é par? .... ").lower()
        if p == "sim":#6 #8 # 10
            d = input("Seu número tem dois digitos? .... ").lower()
            if d == "sim":
                print("Seu numero é 10!")
            elif d == "não" or d == "nao":
                s = input("Seu número é 6? ").lower()
                if s == "sim":
                    print("Seu número é 6!")
                if s == "não" or s == "nao":
                    print("Seu número é 8!")
        elif p == "não" or p == "nao":#7 #9
            n = input("Seu número é 9? .... ").lower()
            if n == "sim":
                print("Seu número é 9!")
            if n == "não" or n == "nao":
                print("Seu número é 7!")
    elif met == "não" or met == "nao":
        p2 = input("Seu número é par? .... ").lower()
        if p2 == "sim": #2 #4
            q = input("Seu número é 2? ..... ")
            if q == "sim":
                print("Seu número é 2!")
            if q == "não" or q == "nao":
                print("Seu número é 4!")
        elif p2 == "não" or "nao": 
            u = input("Seu número é 1? .... ").lower()
            if u == "sim":
                print("Seu número é 1!")
            elif u == "não" or u == "nao":
                print("Seu número é 3!")