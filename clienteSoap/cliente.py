#
#
#__author__ = 'Jhonsson'
#
#from SOAPpy import WSDL
#
#url = 'http://192.168.10.13:8080'
#
#wsdlObject = WSDL.Proxy(url + '/hello.wsdl')
#
#for method in wsdlObject.methods.keys():
#    print(method)
#    ci = wsdlObject.methods[method]
#    print(ci)
#    print
#

from suds.client import Client

url = 'http://127.0.0.1/sw/usuarios.wsdl'

client = Client(url)
msj = client.service.getContratos()
print type(msj), "\n"
print msj

client = Client(url)
msj = client.service.login('jhonsson', '1234', '0000008-14')
print type(msj), "\n"
print msj

client = Client('http://127.0.0.1/sw/busquedas.wsdl')
msj = client.service.buscarMovil(1, 'A', 1, '4567890')
print type(msj), "\n"
print msj

client = Client(url)
msj = client.service.logout(1,'jhonsson', 'A')
print type(msj), "\n"
print msj