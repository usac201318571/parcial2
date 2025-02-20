
import paho.mqtt.client as paho
import logging
import time
#DSFO inportando librerias que se utilizaran

from brokerData import * #Informacion de la conexion

TOPIC = 'sensores'
DEFAULT_DELAY = 10 #1 minuto

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

logging.info("Cliente MQTT con paho-mqtt") #Mensaje en consola


#Config. inicial del cliente MQTT

client = paho.Client(clean_session=True) #Nueva instancia de cliente
client.on_connect = on_connect #Se configura la funcion "Handler" cuando suceda la conexion
client.on_publish = on_publish #Se configura la funcion "Handler" que se activa al publicar algo
client.username_pw_set(MQTT_USER, MQTT_PASS) #Credenciales requeridas por el broker
client.connect(host=MQTT_HOST, port = MQTT_PORT) #Conectar al servidor remoto


#DSFO esta funcin estructura el mensaje a enviar
def publishData(topicRoot, topicName, value, qos = 0, retain = False):
    topic = topicRoot + "/" + topicName
    client.publish(topic, value, qos, retain)



#Loop principal: leer los datos de los sensores y enviarlos al broker en los topics adecuados cada cierto tiempo
try:
    while True:
  
        #publishData(TOPIC, "loque se decea enviar", 25)

        client.publish(TOPIC, "loque se decea enviar", qos=0, retain=False)

        logging.info("Los datos han sido enviados al broker")            

        #Retardo hasta la proxima publicacion de info
        time.sleep(DEFAULT_DELAY)

except KeyboardInterrupt:
    logging.warning("Desconectando del broker MQTT...")

finally:
    client.disconnect()
    logging.info("Se ha desconectado del broker. Saliendo...")
