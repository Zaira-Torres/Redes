# Importacion de modulos necesarios
from uuid import getnode as get_mac  # Para obtener la direccion MAC
import socket  # Para obtener la informacion del Host
import urllib.request  # Para obtener la IP publica
import dns.resolver  # Para realizar consultas DNS

# Obtencion del nombre del host, la IP privada, la IP publica y la direccion MAC
hostname=socket.gethostname()  # Nombre del host
ipPrivada=socket.gethostbyname(hostname)  # IP privada del host
ipPublica=urllib.request.urlopen('https://ident.me').read().decode('utf8')  # IP publica del host
mac=get_mac()  # Direccion MAC en formato decimal
macString=':'.join(("%012X" % mac) [i:i+2] for i in range(0,12,2))  # Formato de direccion MAC

# Funcion para obtener registros DNS de un dominio dado
def obtener_registros_dns(dominio):
    try:
        # Realizar una consulta DNS de tipo 'A' (registros  de direccion IPv4)
        respuesta = dns.resolver.resolve(dominio, 'A')
        
        # Mostrar los registros DNS obtenidos
        print(f"Registros DNS para el dominio {dominio}:")
        for registro in respuesta:
            print(f"Tipo: {registro.rdtype}, Valor: {registro.address}")

    except dns.resolver.NXDOMAIN:
        # Manejar la excepcion si el dominio no existe
        print(f"No se encontraron registros DNS para el dominio {dominio}")
    except dns.exception.DNSException as e:
        # Manejar otras excepciones de DNS
        print(f"Error al consultar los registros DNS: {e}")

# Impresion de la informacion recopilada del host
print("Host: "+hostname)
print ("IP privada del host: "+ipPrivada)
print ("IP pública del host: "+ipPublica)
print("MAC: "+macString)
# Interaccion con el usuario para ingresar un dominio a consultar 
dominio_a_consultar = input("Ingresa el dominio que deseas consultar: ")
# Llamada a la funcion para obtener registros DNS del dominio ingresado
obtener_registros_dns(dominio_a_consultar)