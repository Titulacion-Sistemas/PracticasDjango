__author__ = 'Jhonsson'

import psycopg2

DSN = "dbname=EOT " \
      "user=postgres " \
      "password=root " \
      "host=localhost " \
      "port=5432"

con = None
cur = None

def conectar():
    print "\n\nConectando a la base de datos..."
    try:
        global con
        global cur
        con = psycopg2.connect(DSN)
        cur = con.cursor()
        print "CONECTADO\n"
    except Exception, e:
        print "Error al CONECTAR a la Base de Datos... \nError %s\n" % str(e)

def desconectar():
    print "\n\nDesconectando de la base de datos..."
    try:
        cur.close()
        con.close()
        print "DESCONECTADO\n"
    except Exception, e:
        print "Error al DESCONECTAR de la Base de Datos... \nError %s\n" % str(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()