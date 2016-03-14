
import socket
import _compat_pickle
import datetime


host = "{{server_ip}}"
port = 6666

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
