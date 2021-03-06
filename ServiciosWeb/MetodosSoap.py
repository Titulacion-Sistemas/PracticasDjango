from soaplib.serializers.clazz import Array
from soaplib.serializers.primitive import String

from soaplib.serializers import primitive as soap_types


from Sentencias.SentenciasPg import *

#Gestiona peticiones y respuesta para la generacion del WSDL
render = web.template.Template("$def with (var)\n$:var")

class Peticion_Respuesta:
    """Class for web.py """
    def start_response(self, status, headers):
        web.ctx.status = status
        for header, value in headers:
            web.header(header, value)

    def GET(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))

    def POST(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))



class SoapListar(SimpleWSGISoapApp):
    """Class for webservice """

    @soapmethod(_returns=Array(String))
    def listarCantones(self):
        """ Method for webservice"""
        return ListarCantones()

    #@soapmethod(soap_types.String, _returns=soap_types.String)
    #def hellowithsql(self, message):
    #    """ Method for webservice"""
    #    return leer_datos(message)






class SoapMiservicio(SimpleWSGISoapApp):
    """Class for webservice """

    @soapmethod(String, _returns=String)
    def hellowithsql(self, message):
        """ Method for webservice"""
        return "Hola Mundo con %s" % str(message)
