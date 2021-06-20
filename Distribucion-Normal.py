import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,normaltest
from statistics import stdev,mean


def hallarMediaYDesviacion():
    cantidadDeDatos=int(input("Ingrese la cantidad de datos\n"))
    datos=[int(input("Ingrese el valor "+str(i+1)+"\n")) for i in range(cantidadDeDatos)]
    m=mean(datos)
    s=stdev(datos)
    print("El valor de la media es ", m, "El valor de la desviacion es ",s)
    

def graficarCurvaDeDistribucionNormal(media,desviacion,X1,X2,respuesta):
    normal = norm(media, desviacion)
    x = np.linspace(normal.ppf(0.01),normal.ppf(0.99), 100)
    fp = normal.pdf(x)
    plt.plot(x, fp)
    plt.fill_between(x,0, fp,where=(X2>x) & (x>X1))
    plt.title('Distribución Normal'+"\nProbabilidad = "+str(respuesta))
    plt.ylabel('Probabilidad')
    plt.xlabel('Valores')
    plt.show()


def pantallaPrincipal():
    print("DISTRIBUCION NORMAL")
    print("Operaciones disponibles:")
    print("1-Probabilidad entre un X1 y X2 para una distribucion normal no estandar")
    print("2-Probabilidad por debajo de un X para una distribucion normal no estandar")
    print("3-Probabilidad por encima de un X para una distribucion normal no estandar")
    print("4-Probabilidad por debajo de un X para una distribucion normal estandar")
    print("5-Probabilidad por encima de un X para una distribucion normal estandar")
    print("6-Probabilidad entre un X1 y X2 para una distribucion normal estandar")
    print("7-Tipificar")
    print("8-Encontrar x dados la media, la desviacion y la probabilidad")
    print("9-Encontrar x para una distribucion normal estandar dada la probabilidad")
    print("10-Encontrar x dados la media, la desviacion y z")
    print("11-Encontrar la media y la desviacion para una serie de datos")
    print("12-Salir")

def probabilidadEntreX1X2NoEstandar():
    m=float(input("Ingrese la Media\n"))
    s=float(input("Ingrese la desviacion tipica\n"))
    x1=float(input("Ingrese X1\n"))
    x2=float(input("Ingrese X2\n"))
    izquierda=norm.cdf(x1,m,s)
    derecha=norm.cdf(x2,m,s)
    respuesta=derecha-izquierda
    print("La probabilidad es de",respuesta)
    graficarCurvaDeDistribucionNormal(m, s, x1, x2, respuesta)
    
def probabilidadDebajoDeXNoEstandar():
    m=float(input("Ingrese la Media\n"))
    s=float(input("Ingrese la desviacion tipica\n"))
    x=float(input("Ingrese x\n"))
    respuesta=norm.cdf(x,m,s)
    print("La probabilidad es de",respuesta)
    graficarCurvaDeDistribucionNormal(m,s, norm(m,s).ppf(0.01), x, respuesta)

def probabilidadEncimaDeXNoEstandar():
    m=float(input("Ingrese la Media\n"))
    s=float(input("Ingrese la desviacion tipica\n"))
    x=float(input("Ingrese x\n"))
    respuesta=norm.sf(x,m,s)
    print("La probabilidad es de",respuesta)
    graficarCurvaDeDistribucionNormal(m, s, x, norm(m,s).ppf(0.99), respuesta)

def probabilidadDebajoDeXEstandar():
    x=float(input("Ingrese x\n"))
    respuesta=norm.cdf(x,0,1)
    print("La probabilidad es de",respuesta)
    graficarCurvaDeDistribucionNormal(0,1, norm(0,1).ppf(0.01), x, respuesta)

def probabilidadEncimaDeXEstandar():
    x=float(input("Ingrese x\n"))
    respuesta=norm.sf(x,0,1)
    print("La probabilidad es de",respuesta)
    graficarCurvaDeDistribucionNormal(0, 1, x, norm(0,1).ppf(0.99), respuesta)
def probabilidadEntreX1X2Estandar():
    x1=float(input("Ingrese x1\n"))
    x2=float(input("Ingrese x2\n"))
    respuesta=norm.cdf(x2,0,1)-norm.cdf(x1,0,1)
    print("La probabilidad es de",respuesta)
    graficarCurvaDeDistribucionNormal(0, 1, x1, x2, respuesta)

def tipificar():
    x=float(input("Ingrese x\n"))
    m=float(input("Ingrese la media\n"))
    s=float(input("Ingrese la desviacion\n"))
    respuesta=(x-m)/s
    print("Despues de tipicar tenemos N(0,1) con z=",respuesta)

def encontrarXNoEstadar():
    prob=float(input("Ingrese la probabilidad\n"))
    m=float(input("Ingrese la media\n"))
    s=float(input("Ingrese la desviacion\n"))
    respuesta=norm.ppf(prob,m,s)
    print("El valor de x es",respuesta)

def encontrarXEstadar():
    prob=float(input("Ingrese la probabilidad\n"))
    respuesta=norm.ppf(prob,0,1)
    print("El valor de x es",respuesta)


def encontrarXNoEstadarDadoZ():
    z=float(input("Ingrese z\n"))
    m=float(input("Ingrese la media\n"))
    s=float(input("Ingrese la desviacion\n"))
    respuesta=s*z+m
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
            encontrarXNoEstadarDadoZ()
        if seleccion==11:
            hallarMediaYDesviacion()
        if seleccion==12:
            break
        input("Presiona enter para continuar\n")


main()