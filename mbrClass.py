import ctypes
import struct
import random
from partionClass import Particion
import graphviz

const = 'I I'

class MBR(ctypes.Structure):
    _fields_ = [
        ('tamano', ctypes.c_int),
        ('unit', ctypes.c_int )
    ]

    def __init__(self):
        self.tamano = 0
        self.unit = 0
        self.part1 = Particion()
        self.part2 = Particion()
        self.part3 = Particion()
        self.part4 = Particion()


    def set_tamano(self, tamano):
        self.tamano = tamano

    def set_unit(self):
        self.unit = random.randint(1, 1000)

    def setDataMBR(self, tamano):
        self.set_tamano(tamano)
        self.set_unit()
    
    def display_info(self):
        print(f"tamano: {self.tamano}")
        print(f"unit: {self.unit}")
        

    def doSerialize(self):
        mbr_data = struct.pack(const, self.tamano, self.unit)
        particiones_data = self.part1.doSerialize()+ self.part2.doSerialize() + self.part3.doSerialize() + self.part4.doSerialize() 
        return mbr_data + particiones_data

    def doDeserialize(self, data):
        size_mbr = struct.calcsize(const)
        spart1 = struct.calcsize(self.part1.get_const())
        spart2 = struct.calcsize(self.part2.get_const())
        spart3 = struct.calcsize(self.part3.get_const())

        data_mrb = data[:size_mbr]
        self.tamano, self.unit = struct.unpack(const, data_mrb)

        dataP1 = data[size_mbr:size_mbr + spart1]
        self.part1.doDeserialize(dataP1)

        dataP2 = data[size_mbr + spart1:size_mbr + spart1 + spart2]
        self.part2.doDeserialize(dataP2)

        dataP3 = data[size_mbr + spart1 + spart2:size_mbr + spart1 + spart2 + spart3]
        self.part3.doDeserialize(dataP3)

        dataP4 = data[size_mbr + spart1 + spart2 + spart3:]
        self.part4.doDeserialize(dataP4 )
    
    def generarGrafo(self):
        dot = graphviz.Digraph(format='png', engine='dot')
        dato1=str(self.part1.name)
        dato2=str(self.part2.name)
        dato3=str(self.part3.name)
        dato4=str(self.part4.name)
        part_names = ["Particion1", "Particion2", "Particion3", "Particion4"]

        part_row = '|'.join(part_names)

        # Crear la fila de la tabla en HTML
        table_html = f'''
        <table border="0" cellborder="1" cellspacing="0">
        <tr><td>MBR</td></tr>
        <tr><td>{part_row}</td></tr>
        </table>
        '''

        # Agregar el nodo con contenido HTML
        dot.node('mbr', table_html, shape='none')

        dot.render("ReporteMBR")

        return "Se ha generado correctamente el reporte!"