
'''
from wsgiref.simple_server import make_server
def application(environ, start_response):
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response('200 OK', headers)
    return ['Hola gente de códigofacilito'.encode('utf-8')]
server = make_server('localhost', 8080, application)
server.serve_forever()
'''

'''
from wsgiref.simple_server import make_server
def application(environ, start_response):
    # Guardo la salida que devolveré como respuesta
    respuesta = "<p>Página web construida con <strong>Python!!!</strong></p>"
    # Se genera una respuesta al navegador 
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [respuesta.encode('utf-8')]    
if __name__ == '__main__':    
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
'''

'''
def application(environ, start_response):
    if environ["PATH_INFO"]=="/":
        respuesta = "<p>Página inicial</p>"
    elif environ["PATH_INFO"]=="/hola":
        respuesta = "<p>Bienvenidos a mi página web</p>"
    else:
        respuesta = "<p><trong>Página incorrecta</strong></p>"
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [respuesta.encode('utf-8')]    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
'''

'''
def application(environ, start_response):
	respuesta=environ["REQUEST_METHOD"]+environ["SCRIPT_NAME"]\
	+environ["PATH_INFO"]+environ["CONTENT_TYPE"]+environ["SERVER_NAME"]
	start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	return [respuesta.encode('utf-8')]
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
'''

'''
def application(environ, start_response):
    if environ["PATH_INFO"]=="/":
        respuesta = "<p>Página inicial</p>"
    elif environ["PATH_INFO"]=="/suma":
        params=environ["QUERY_STRING"].split("&")
        suma=0
        for par in params:
                suma=suma+int(par.split("=")[1])
        respuesta="<p>La suma es %d</p>" % suma
    else:
        respuesta = "<p><trong>Página incorrecta</strong></p>"
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [respuesta.encode('utf-8')]
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
'''

    