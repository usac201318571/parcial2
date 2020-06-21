import socket
import os
import time
import logging
import binascii
import threading #Concurrencia con hilos


import sys       #Requerido para salir (sys.exit())









# Crea un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_ADDR = 'localhost' #La IP donde desea levantarse el server
IP_ADDR_ALL = '' #En caso que se quiera escuchar en todas las interfaces de red
IP_PORT = 9802 #Puerto al que deben conectarse los clientes
BUFFER_SIZE = 16 * 1024 #Bloques de 16 KB
serverAddress = (IP_ADDR_ALL, IP_PORT) #Escucha en todas las interfaces
sock.bind(serverAddress) #Levanta servidor con parametros especificados
sock.listen(10) #El argumento indica la cantidad de conexiones en cola
#------------------------------------------------------------------
#------------------------------------------------------------------


COMMAND_FTR = b'\x03'
COMMAND_ALIVE = b'\x04'
COMMAND_ACK = b'\x05'
COMMAND_OK = b'\x06'
COMMAND_NO = b'\x07'

USERS_FILENAME = '200819010'
ROOMS_FILENAME = 'salas'





lista = []












while True:
    # Esperando conexion
    print('Esperando conexion remota')
    connection, clientAddress = sock.accept()
    try:
        print('Conexion establecida desde', clientAddress)
        # Se envia informacion en bloques de BUFFER_SIZE bytes
        # y se espera respuesta de vuelta
        
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#-------------comandos---------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------


        data = connection.recv(BUFFER_SIZE)
        print(data)
        separador = bytes('$', "ascii")
        separacion = data.split(separador)
        print(separacion)
       
        comando = separacion[0]
        usu_sala = separacion[1].decode("utf-8")
        taman = separacion[2].decode("utf-8")
        print(comando, usu_sala, taman)
        
        if comando == binascii.unhexlify("03"):
            print("ingreso")
            while True:
                print(connection.recv(BUFFER_SIZE))

        
        
#------------------------------------------------------------------
#------------------------------------------------------------------
#-------------------hilos------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # cambionor = data.decode("utf-8") 
        # print(cambionor)
        
        # cambio = data.split(cambionor)
        # print(cambio)        
        
        
        
        
        
        
        
        # while True:
        #     data = connection.recv(BUFFER_SIZE)
        #     print('Recibido: {!r}'.format(data))
        #     if data: #Si se reciben datos (o sea, no ha finalizado la transmision del cliente)
        #         print('Enviando data de vuelta al cliente')
        #         connection.sendall(data)
        #     else:
        #         print('Transmision finalizada desde el cliente ', clientAddress)
        #         break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
    
    
    
    
    except KeyboardInterrupt:
        sock.close()

    finally:
        # Se baja el servidor para dejar libre el puerto para otras aplicaciones o instancias de la aplicacion
        connection.close()















