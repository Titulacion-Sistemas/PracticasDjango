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

url = 'http://localhost:8080/miservicio?wsdl'
client = Client(url)

msj = client.service.hellowithsql("Andrea Loaiza")
print type(msj), "\n"
print msj