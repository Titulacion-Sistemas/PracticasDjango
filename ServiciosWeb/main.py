from MetodosSoap import *
import web


urls = ("/EOT_Listar", "ServicioListar",
        "/EOT_Listar.wsdl", "ServicioListar",
        "/miservicio", "miServicio",
        "/miservicio.wsdl", "miServicio",)


class ServicioListar(Peticion_Respuesta, SoapListar):
    pass

class miServicio(Peticion_Respuesta, SoapMiservicio):
    pass


app = web.application(urls, globals())

if __name__ == "__main__":
    #Listar Las variables Globales
    #for k, v in globals().items():
    #    print k, "=", v

    app.run()