#import socket
#import binascii 
#import os 
#import logging

#HOST = '127.0.0.1'  #JJLS Dirección IP del servidor
#PORT = 65432        #JJLS El puerto utilizado por el servidor

#JJLS Se le indica al usuario la forma correctar de utilizar la aplicacion y se rocoge la entrada del usuario 
while True:
    print("\nIngrese la opcion que deseada.")
    print("1: Enviar texto.") 
    print("2: Enviar mensaje de voz.")
    print("3: Salir.")
    n = input(">")
    if n.isdigit():
        n = int(n)
        if n == 1:
            print("\nIngrese la opcion de envio de texto que deseada.")
            print("1: Enviar a usuario.") 
            print("2: Enviar a sala.")
            n = input(">")
            if n.isdigit():
                n = int(n)
                if n == 1: 
                    Enviar_texto_a_usuario()
                if n == 2:
                    Enviar_texto_a_cliente()
        if n == 2:
            print("\nIngrese la opcion de envio de audio que deseada.")
            print("1: Enviar a usuario.") 
            print("2: Enviar a sala.")
            n = input(">")
            if n.isdigit():
                n = int(n)
                if n == 1:
                    print("\nIngrese el tiempo de duracion del mensaje de audio.")
                    n = input(">")
                    if n.isdigit():
                        n = int(n) 
                        Enviar_grabacion_a_usuario(n)
                if n == 2:
                    print("\nIngrese el tiempo de duracion del mensaje de audio.")
                    n = input(">")
                    if n.isdigit():
                        n = int(n) 
                        Enviar_grabacion_a_cliente(n)
        if n == 3:
        break
    else:
        print("****Ingrese una opcion correcta***")

#JJLS Dependiedo de lo que el usuario escoja se verifica en sentencias condicionales para enviar los datos al servidor 
#if n == 1:
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.connect((HOST, PORT))
#        s.sendall(binascii.unhexlify("01"))
#        data = s.recv(1024)
#    print('Received', repr(data))
#elif n == 2:
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.connect((HOST, PORT))
#        s.sendall(binascii.unhexlify("02"))
#        data = s.recv(1024)
#    print('Received', repr(data))
#elif n == 3:
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.connect((HOST, PORT))
#        s.sendall(binascii.unhexlify("03"))
#        data = s.recv(1024)
#    print('Received', repr(data))



#logging.basicConfig(
#    level = logging.DEBUG, 
#    format = '%(message)s'
#   )
#logging.info('Comenzando grabacion')
#os.system('arecord -d 10 -f U8 -r 8000 prueba.mp3')

#logging.info('Grabacion finalizada, inicia reproduccion')
#os.system('aplay prueba.mp3')
