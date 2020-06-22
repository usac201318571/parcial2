
import paho.mqtt.client as paho
import logging
import time
#DSFO inportando librerias que se utilizaran

from brokerData import * #Informacion de la conexion

TOPIC = 'sensores'
DEFAULT_DELAY = 10 #1 minuto
LOG_FILENAME = 'mqtt.log'

#Configuracion inicial de logging
logging.basicConfig(
    level = logging.INFO, 
    format = '[%(levelname)s] (%(processName)-10s) %(message)s'
    )

#Handler en caso suceda la conexion con el broker MQTT
def on_connect(client, userdata, flags, rc): 
    connectionText = "CONNACK recibido del broker con codigo: " + str(rc)
    logging.info(connectionText)

#Handler en caso se publique satisfactoriamente en el broker MQTT
def on_publish(client, userdata, mid): 
    publishText = "Publicacion satisfactoria"
    logging.debug(publishText)

logging.info("Cliente MQTT con paho-mqtt") #Mensaje en conso


#Callback que se ejecuta cuando llega un mensaje al topic suscrito
def on_message(client, userdata, msg):
    #Se muestra en pantalla informacion que ha llegado
    logging.info("Ha llegado el mensaje al topic: " + str(msg.topic))
    logging.info("El contenido del mensaje es: " + str(msg.payload))
    
    #Y se almacena en el log 
    logCommand = 'echo "(' + str(msg.topic) + ') -> ' + str(msg.payload) + '" >> ' + LOG_FILENAME
    os.system(logCommand)



#Config. inicial del cliente MQTT

client = paho.Client(clean_session=True) #Nueva instancia de cliente
client.on_connect = on_connect #Se configura la funcion "Handler" cuando suceda la conexion
client.on_publish = on_publish #Se configura la funcion "Handler" que se activa al publicar algo
client.on_message = on_message #DSFO para que pueda recivir mensajes para enviarlos o mostrarlos
client.username_pw_set(MQTT_USER, MQTT_PASS) #Credenciales requeridas por el broker
client.connect(host=MQTT_HOST, port = MQTT_PORT) #Conectar al servidor remoto


#Nos conectaremos a distintos topics:
qos = 2
#Subscripcion simple con tupla (topic,qos)
client.subscribe((TOPIC, qos)) #DSFO suscripcion a topicos requeridos
client.loop_start()


def Teclado(topic,qos=0,retain=False):
    msg = input('Enviar--> ')
    msg = str(msg)
    client.publish(TOPIC, msg, qos=0, retain=False)
    logging.info("Los datos han sido enviados al broker") 



#Loop principal: leer los datos de los sensores y enviarlos al broker en los topics adecuados cada cierto tiempo
try:
    while True:
  
        #publishData(TOPIC, "loque se decea enviar", 25)

        #client.publish(TOPIC, "loque se decea enviar", qos=0, retain=False)

        Teclado(TOPIC)

        #logging.info("Los datos han sido enviados al broker")            

        #Retardo hasta la proxima publicacion de info
        time.sleep(DEFAULT_DELAY)

except KeyboardInterrupt:
    logging.warning("Desconectando del broker MQTT...")

finally:
    client.disconnect()
    logging.info("Se ha desconectado del broker. Saliendo...")
