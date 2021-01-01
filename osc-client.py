# -*- coding: utf-8 -*-
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = '127.0.0.1'
PORT = 6700

# UDPのクライアントを作る
client = udp_client.UDPClient(IP, PORT)

# /colorに送信するメッセージを作って送信する
msg = OscMessageBuilder(address='/color')
msg.add_arg(0)
msg.add_arg(228)
msg.add_arg(123)
m = msg.build()

client.send(m)