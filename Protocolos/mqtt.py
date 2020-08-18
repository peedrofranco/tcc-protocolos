"""
Protocolo de ligação que específica como os bytes de dados são organizados e
transmitiros pela rede TCP/IP
"""
import paho.mqtt.client as mqtt
from functions_generics import date_formating, decode_utf


# The callback for when the client receives a CONNACK response from the server.
# O retorno de chamada para quando o cliente recebe uma resposta CONNACK do
# servidor.
def on_connect(client, userdata, flags, rc):
    print(f"Connect with result code: {rc}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    # Inscrever - se em on_connect() significa que, se perdermos a conexão e
    # reconectarmos, as assinaturas serão renovadas.\
    # subscribe(topic, qos)
    # padrão qos=0
    client.subscribe("$SYS/#", 2)


# The callback for when a PUBLISH message is received from the server.
# O retorno de chamada para quando uma mensagem PUBLISH é recebida do servidor.
def on_message(client, userdata, msg):
    # 'dup', 'info', 'mid', 'payload', 'properties', 'qos', 'retain',
    # 'state', 'timestamp', 'topic'
    # print(f"Testeee: {int.from_bytes(msg.payload, 'big')}")
    # print(f"Testeee 2: {msg.payload.decode('utf-8')}")

    print(f"""
Received message: {decode_utf(msg.payload)}
on topic:         {msg.topic}
with QoS:         {msg.qos}
with Mid:         {msg.mid}
with TimeStamp:   {date_formating(msg.timestamp)}
    """)
    print("-" * 80)


# QoS:
# -> 0: modo de transfêrencia mais rápido
# -> 1: modo de transfêrencia padrão
# -> 2: modo de transfêrencia mais seguro e mais lento


# Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311,
# transport="tcp")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# connect(host, port, keepalive, bind_address)
client.connect("mqtt.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

# Bloqueio de chamada que processa o tráfego de rede, despacha retornos de
# chamada e lida com a reconexão.
# Estão disponíveis outras funções de loop * () que fornecem uma interface
# encadeada e um interface manual.
client.loop_forever()

# publish(topic, payload, qos, retain)
