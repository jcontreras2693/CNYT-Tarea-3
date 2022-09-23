import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def accmatvec(mat,vec):
    """accion de una matriz sobre un vector, puede ser de enteros o complejos.
    """
    resp=[]
    for i in range(len(mat)):
        x=mat[i]
        for j in range(len(x)):
            y=(valmultvecrealcomp(mat[i],vec))
        resp.append(y)
    return resp

def valmultvecrealcomp(arr1,arr2):
    """calcula el producto de un vector por otro, puede ser de enteros o de numeros complejos.
    """
    sumai=(0,0)
    sumatoria=0
    x=False
    for i in range(len(arr1)):
        try:
            sumai=suma(sumai,producto(arr1[i],arr2[i]))
            x=True
        except TypeError:
            sumatoria+=arr1[i]*arr2[i]
    if x:
        return sumai
    return sumatoria

def canicas(mat,vec,clicks):
    """se ingresa como parametro la matriz, el vector y la cantidad de clicks
    """
    for k in range(int(clicks)):
        vec=accmatvec(mat,vec)
    return vec

def transmat(mat):
    """traspone una matriz
    """
    for i in range(len(mat)):
        x=mat[i]
        try:
            for j in range(len(x)):
                if i<=j:
                    temp=mat[i][j]
                    mat[i][j]=mat[j][i]
                    mat[j][i]=temp
        except TypeError:
            return mat
    return mat

def multrendijas(mat,vec,clicks):
    """se ingresa como parametro la matriz, el vector y la cantidad de clicks, da como resultado un vector, pueden usarse enteros o numeros complejos.
    """
    trans=transmat(mat)
    for i in range(len(mat)):
        if sum(trans[i])!=1:
            return False
    for j in range(int(clicks)):
        vec = accmatvec(mat, vec)
    return vec

def suma(a, b):
    """retorna la suma entre dos numeros complejos"""
    return (a[0] + b[0]), (a[1] + b[1])

def producto(a,b):
    """retorna el producto entre dos numeros complejos"""
    if a==(0,0) and b==(0,0):
        return a
    elif a[0]==b[0] and a[1]==(b[1]*-1):
        return (a[0]**2)+(a[1]**2),0
    return ((a[0]*b[0])-(a[1]*b[1])),((a[0]*b[1])+(a[1]*b[0]))

def plothistogram(vec):
    """recive un vector normalizado y retorna una grafica con las probabilidades de cada entrada
    """
    counts={}
    vecnormal=[]
    if sum(vec)==1:
        for i in range(1,len(vec)+1):
            q=str(i)
            counts[q]=vec[i-1]
    elif sum(vec)>1 or sum(vec)<1:
        vecnormal=normalizar(vec)
        for j in range(1,len(vecnormal)+1):
            q=str(j)
            counts[q]=vec[j-1]
    plot_histogram(counts)
    plt.show()
    return

def division(a,b):
    """retorna la division de dos numero complejo"""
    x=producto(a,conjug(b))
    return ((x[0])/producto(b,conjug(b))),((x[1])/producto(b,conjug(b)))

def conjug(a):
    """retorna el conjugado de un numero complejo"""
    return a[0],(a[1]*(-1))

def modulovecpow2(vec):
    """devuelve el modulo al cuadrado de un vector
    """
    sumar=[]
    modulo=[(0,0)]

    for i in range(len(vec)):
        if type(vec[i])==tuple:
            sumar.append(producto(vec[i],vec[i]))
        elif type(vec[i])==int:
            sumar.append(vec[i]**2)
    for j in range(len(sumar)):
        if sumar[j]==int:
            modulo[0]=suma(modulo[0],(sumar[j],0))
        elif sumar[j]==tuple:
            modulo[0]=suma(modulo[0],sumar[j])
    return modulo
def normalizar(vec):
    """normaliza un vector de complejos
    """
    modulo=modulovecpow2(vec)
    resp=[]
    for k in range(len(vec)):
        if vec[k]==tuple:
            resp.append(division(vec[k],modulo[0]))
        elif vec[k]==int:
            resp.append(division((k,0),modulo[0]))
    return resp
def producto(a, b):
    """retorna el producto entre dos numeros complejos"""
    if a == (0, 0) and b == (0, 0):
        return a
    elif a[0] == b[0] and a[1] == (b[1] * -1):
        return (a[0] ** 2) + (a[1] ** 2), 0
    return ((a[0] * b[0]) - (a[1] * b[1])), ((a[0] * b[1]) + (a[1] * b[0]))

print(plothistogram([0.25,0.2,0.2,0.35]))
# counts = {'1':0.25, '2':0.2, '3':0.2,'4':0.35}