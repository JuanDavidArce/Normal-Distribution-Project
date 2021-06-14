from scipy.stats import norm

#La distribucion normal es simetrica, la media, la moda y la mediana coinciden.

def pantallaPrincipal():
    print("DISTRIBUCION NORMAL")
    print("Operaciones disponibles:")
    print("1-Probabilidad entre un X1 y X2 con media difernte de 0 y desviacion diferente de 1")
    print("2-Probabilidad por debajo de un X con media diferente de 0 y desviacion diferente de 1")
    print("3-Probabilidad por encima de un X con media diferente de 0 y desviacion diferente de 1")
    print("4-Probabilidad por debajo de un X con media 0 y desviacion 1")
    print("5-Probabilidad por encima de un X con media 0 y desviacion 1")
    print("6-Probabilidad entre un X1 y X2 con media 0 y desviacion 1")
    print("7-Tipificar")
    print("8-Encontrar x dados la media, la desviacion y z")
    print("9-Encontrar x para una distribucion normal estandar")
    print("10-Salir")

def probabilidadEntreX1X2NoEstandar():
    m=float(input("Ingrese la Media\n"))
    s=float(input("Ingrese la desviacion tipica\n"))
    x1=float(input("Ingrese X1\n"))
    x2=float(input("Ingrese X2\n"))
    izquierda=norm.cdf(x1,m,s)
    derecha=norm.cdf(x2,m,s)
    respuesta=derecha-izquierda
    print("La probabilidad es de",respuesta)
    
def probabilidadDebajoDeXNoEstandar():
    m=float(input("Ingrese la Media\n"))
    s=float(input("Ingrese la desviacion tipica\n"))
    x=float(input("Ingrese x\n"))
    respuesta=norm.cdf(x,m,s)
    print("La probabilidad es de",respuesta)

def probabilidadEncimaDeXNoEstandar():
    m=float(input("Ingrese la Media\n"))
    s=float(input("Ingrese la desviacion tipica\n"))
    x=float(input("Ingrese x\n"))
    respuesta=norm.sf(x,m,s)
    print("La probabilidad es de",respuesta)

def probabilidadDebajoDeXEstandar():
    x=float(input("Ingrese x\n"))
    respuesta=norm.cdf(x,0,1)
    print("La probabilidad es de",respuesta)

def probabilidadEncimaDeXEstandar():
    x=float(input("Ingrese x\n"))
    respuesta=norm.sf(x,0,1)
    print("La probabilidad es de",respuesta)

def probabilidadEntreX1X2Estandar():
    x1=float(input("Ingrese x1\n"))
    x2=float(input("Ingrese x2\n"))
    respuesta=norm.cdf(x2,0,1)-norm.cdf(x1,0,1)
    print("La probabilidad es de",respuesta)

def tipificar():
    x=float(input("Ingrese x\n"))
    m=float(input("Ingrese la media\n"))
    s=float(input("Ingrese la desviacion\n"))
    respuesta=(x-m)/s
    print("Despues de tipicar tenemos N(0,1) con z=",respuesta)

def encontrarXNoEstadar():
    z=float(input("Ingrese z\n"))
    m=float(input("Ingrese la media\n"))
    s=float(input("Ingrese la desviacion\n"))
    respuesta=scipy.stats.norm.ppf(z,m,s)
    print("El valor de x es",respuesta)

def encontrarXEstadar():
    z=float(input("Ingrese z\n"))
    respuesta=scipy.stats.norm.ppf(z,0,1)
    print("El valor de x es",respuesta)

def main():
    while True:
        pantallaPrincipal()
        seleccion=int(input())
        if seleccion==1:
            probabilidadEntreX1X2NoEstandar()
        if seleccion==2:
            probabilidadDebajoDeXNoEstandar()
        if seleccion==3:
            probabilidadEncimaDeXNoEstandar()
        if seleccion==4:
            probabilidadDebajoDeXEstandar()
        if seleccion==5:
            probabilidadEncimaDeXEstandar()
        if seleccion==6:
            probabilidadEntreX1X2Estandar()
        if seleccion==7:
            tipificar()
        if seleccion==8:
            encontrarXNoEstadar()
        if seleccion==9:
            encontrarXEstadar()
        if seleccion==10:
            break
        input("Presiona enter para continuar\n")


main()