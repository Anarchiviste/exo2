import time


def chronometre(func):
    def myinner(x):
        start = time.time()
        result = func(x)
        elapsed = time.time() - start
        print(f"Beep Boop, j'ai du réfléchir pendant {elapsed} secondes ^_^")
        return result

    return myinner


# Exo 1


@chronometre
def grosse_multiplication(multiplicateur):
    multiplicande = 100000000000 * 9999
    resultat = 0
    for i in range(1, multiplicateur):
        resultat += multiplicande * multiplicateur * i
    return f"le résultat est : {resultat}"


print(grosse_multiplication(56897))
