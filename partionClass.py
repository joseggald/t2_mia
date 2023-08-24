import ctypes
import struct
from utilitie import coding_str

const = '1s 1s I I 16s'

class Particion(ctypes.Structure):
    _fields_ = [
        ('status', ctypes.c_char),
        ('type', ctypes.c_char),
        ('start', ctypes.c_int),
        ('size', ctypes.c_int),
        ('name', ctypes.c_char * 16)
    ]
    def __init__(self):
        self.status = b'\0'
        self.type = b'\0'
        self.start = 0
        self.size = 0
        self.name = b'\0' * 16

    def setStatus(self, status):
        self.status = coding_str(status, 1)

    def setType(self, type):
        self.type = coding_str(type, 1)

    def setStart(self, start):
        self.start = start

    def setSize(self, s):
        self.size = s

    def setName(self, name):
        self.name = coding_str(name, 16)

    def set_infomation(self, status, type, start, size, name):
        self.setStatus = status
        self.setType = type
        self.start = start
        self.size = size
        self.name = name

    def get_const(self):
        return const
    
    def display_info(self):
        print(f"Status: {self.status}")
        print(f"Type: {self.type}")
        print(f"Fit: {self.fit}")
        print(f"Start: {self.start}")
        print(f"Size: {self.size}")
        print(f"Name: {self.name}")
        

    def doSerialize(self):
        return struct.pack(
            const,
            self.status,
            self.type,
            self.start,
            self.size,
            self.name
        )

    def doDeserialize(self, data):
        self.status, self.type, self.start, self.size, self.name = struct.unpack(const, data)