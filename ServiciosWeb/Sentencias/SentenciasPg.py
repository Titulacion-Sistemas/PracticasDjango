import Conexion.ConexionPg as c


def FilaEnColumna(matriz, colum):
    return [fila[colum] for fila in matriz]


def FilasXColumnas(matriz):
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]


def Listar(kuery, retorno):

#   valores del retorno posibles
#   0  valor [0,0]                  str
#   1  fila de la consulta [0]      []
#   2  todas las filas              [[]]

    lista = None
    c.conectar()
    try:
        c.cur.execute(kuery)

        if retorno == 0:
            lista = str(c.cur.fetchone()[0])
        elif retorno == 1:
            lista = c.cur.fetchone()
        elif retorno == 2:
            lista = c.cur.fetchall()
        else:
            lista = None

            #lista = c.cur.fetchall()
        print 'Listar ...', kuery
    except:
        print "No se pudo Listar ", kuery
    c.desconectar()
    return lista

#######################################################################################
#comienzan las sentencias

def ListarCantones():
    return FilaEnColumna(Listar("Select nom_can from canton", 2), 0)


#if "__main__" == __name__:
#    Listar("Select cod_can||'', nom_can from canton", 1)