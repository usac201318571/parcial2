import threading #Concurrencia con hilos
import time      #Retardos
import logging   #Logging
import sys       #Requerido para salir (sys.exit())

import socket
import os

SERVER_IP   = 'localhost'
SERVER_PORT = 9802
BUFFER_SIZE = 16 * 1024
# Se crea socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se conecta al puerto donde el servidor se encuentra a la escucha
server_address = (SERVER_IP, SERVER_PORT)
print('Conectando a {} en el puerto {}'.format(*server_address))
sock.connect(server_address)

COMMAND_FTR = b'\x03'
COMMAND_ALIVE = b'\x04'
COMMAND_ACK = b'\x05'
COMMAND_OK = b'\x06'
COMMAND_NO = b'\x07'














logging.basicConfig(
    level = logging.DEBUG, 
    format = '[%(levelname)s] (%(threadName)-10s) %(message)s'
    )



final = 0


def contador_seg(rango, delay, userID):
    global final 
    bandera = True
    entrada= round(time.time(),2)
    
    alive = b'\x04'
    usuario = bytes(userID, "ascii")
    separador = bytes('$', "ascii")
    final = alive +separador+ usuario
    contador = 0
    while bandera :        
        salida= round(time.time(),2)
        resta = round(salida - entrada,2)                   
        if resta == 2:
            entrada= round(time.time(),2)
            contador = contador + 1
            #print(contador, final)
            return final

t1 = threading.Thread(name = 'Contador de 1 segundo',
                        target = contador_seg,
                        args = (range(0,11),0.5, str(200819010)),
                        daemon = True
                        )



t1.start()


    
conta = 0    






    


try:

#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------


    #ingreso = input("ingrese su usuario(ej 200819010): ")
    
    
    #if ingreso == "200819010":
    print("bienvenido Estuardo")

    #------------------------------------------
    #------------------------------------------
    
                            # transferencia de archivos 
    
    #------------------------------------------
    #------------------------------------------
   
   
   
    ingreso = "200819010"
    codigo = bytes(ingreso, "ascii")

    tamanio = os.stat('200819010_servidor.wav').st_size #24044
    bitetama = bytes(str(tamanio), "ascii")        
    separador = bytes('$', "ascii")
    fusion = COMMAND_FTR+separador+codigo+separador+bitetama
    
    print(fusion)
    sock.sendall(fusion)
    #------------------------------------------
    #------------------------------------------
    #------------------------------------------
    while True:
        time.sleep(1)
        sock.sendall(final)
        print(final)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # usuario1 = bytes(lextlen, "ascii")

    # print(usuario,lextlen)
    # sock.sendall(usuario)
    # sock.sendall(usuario1)




    # bytesRecibidos = 0
    # bytesEsperados = len(usuario)
    
    # while bytesRecibidos < bytesEsperados:
    #     data = sock.recv(BUFFER_SIZE)
    #     bytesRecibidos += len(data)
    #     print('Recibido: {!s}'.format(data))







































#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

except KeyboardInterrupt:
    logging.warning("Desconectando del broker...")


finally:
    print('\n\nConexion finalizada con el servidor')
    sock.close()
    
    
    
    










































  
    
    
    