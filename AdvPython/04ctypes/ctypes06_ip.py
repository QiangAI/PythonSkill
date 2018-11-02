#!/usr/bin/python
#coding=utf-8

import socket
import  struct
from ctypes import *

class IP(Structure):
    _fields_ = [
        ("ihl",             c_ubyte, 4),
        ("version",         c_ubyte, 4),
        ("tos",             c_ubyte),
        ("len",             c_ushort),
        ("id",              c_ushort),
        ("offset",          c_ushort),
        ("ttl",             c_ubyte),
        ("protocol_num",    c_ubyte),
        ("sum",             c_ushort),
        ("src",             c_uint),
        ("dst",             c_uint),
    ]
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
    def __init__(self, socket_buffer=None):
        self.src_address = socket.inet_ntoa(struct.pack("<I", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<I", self.dst))
        self.ver=self.version
sk=socket.socket(socket.AF_INET,socket.SOCK_RAW,0)
while True:
    buf=sk.recv(2048,0)
    ip_header = IP(buf[:20]) #可以使用from_buffer
    print(ip_header.src_address)
    print(ip_header.dst_address)
    print(ip_header.ver)