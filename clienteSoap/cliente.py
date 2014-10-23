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

url = 'http://127.0.0.1/sw/usuario.wsdl'
client = Client(url)

msj = client.service.login('Jhonsson', '1234')
print type(msj), "\n"
print msj