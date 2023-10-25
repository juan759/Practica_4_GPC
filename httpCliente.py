import socket
import sys

def ussage():
    print("El funcionamiento es:",end=" ")
    print("python3 httpCliente.py <host> <http_method> <url> <user_agent> <encoding> <connection>")
    print("[+]http_method: GET,HEAD")
    print("[+]user_agent:Motorola,Samsung,Apple,Windows-Edge,MacOS-Safari,Roku-Ultra,Ubuntu-Firefox")
    print("[+]connection:keep-alive,close")

def processArguments(): 
    """
    Función para procesar los argumentos pasados por command line al cliente.
    Return
    ---------
    argumentos: list(str).
    Una lista con los parametros obtenidos de command line. 
    """
    host=sys.argv[1]
    http_method=sys.argv[2]
    url=sys.argv[3]
    user_agent=sys.argv[4]
    encoding=sys.argv[5]
    connection=sys.argv[6]

    aux = [host,http_method,url,user_agent,encoding,connection]
    return aux

def getAgent(name):
    """
    Función que recibe el nombre de algunos de los User Agent disponibles y regresa su valor especifico.

    Parameters
    -----------
    name:str.
    El nombre de alguno de nuestros user agent.

    Return
    --------
    agente:str.
    El User-Agent verdadero para realizar la petición.
    """
    user_agents = {
    "Motorola": "Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Samsung": "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Apple": "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
    "Windows-Edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "MacOS-Safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Roku-Ultra": "Roku4640X/DVP-7.70 (297.70E04154A)",
    "Ubuntu-Firefox": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    }
    if name in user_agents:
        return user_agents[name]


def constructHTTPRequest(arguments):
    """
    Función donde se crea en su totalidad la petición HTTP que se realizará al servidor.

    Parameters
    ----------
    arguments: list(str).
    Lista de los argumentos para nuestra petición:host http_method url user_agent encoding connection.

    Return
    ---------
    peticion:str.
    La petición ya creada con sus parametros necesarios.
    """
    #Construcción de la linea de la Petición.
    http_method=arguments[1]
    url=arguments[2]
    version="HTTP/1.1"
    request_line=http_method+ " "+url+ " "+version+ "\r\n"

    #Construcción de headers.
    host = "Host: "+arguments[0]
    if(getAgent(arguments[3])):
        user_agent = "User-Agent: " +getAgent(arguments[3])
    else:
        print("Agent not found.")
        ussage()
        sys.exit()
    accept = "Accept: text/html;charset=US-ASCII, text/html;charset=UTF-8, text/plain;charset=US-ASCII,text/plain;charset=UTF-8"
    encoding = "Accept-Encoding: "+arguments[4]
    language = "Accept-Language: en-US"
    connection = "Connection: "+arguments[5]

    #Crear la petición completa.
    cabeceras = host + "\r\n"+ \
                user_agent + "\r\n"+ \
                accept + "\r\n"+ \
                encoding + "\r\n"+ \
                language + "\r\n"+ \
                connection + "\r\n"
    end = "\r\n"

    peticion=request_line + \
                 cabeceras + \
                 end

    return peticion



def TCPConnection(server,request):
    """
    Función para ya conectar con el server que buscamos y además crear la petición para esperar la respuesta que nos arroje el servidor.

    Parameters
    -----------
    request:str.
    La petición con todas sus cabeceras y para esperar la respuesta del server.
    """

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((server,80))

    s.send(request.encode())

    response=s.recv(1024)
    if response == "":
        print("No hay respuesta del servidor.")
    else:  
        print(response.decode())

    s.close()
    print("Conexión cerrada con el servidor.")

try:
    arguments=processArguments()
    request= constructHTTPRequest(arguments)
    TCPConnection(arguments[0],request)
except:
    ussage()
