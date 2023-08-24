from diskClass import *
from mbrClass import *
import os
from mbrClass import MBR


def ejecutarMkdisk(args):
    if args.size > 0:
        newDisk = crearDisk(args.path)
        manejoEspacioDisk(newDisk, args.size, args.unit)
        mbr = MBR()
        mbr.setDataMBR(args.size)
        writeDisk(newDisk, 0, mbr)
        newDisk.close()
        getMbr = MBR()
        readDisk(args.path, 0, getMbr)
        getMbr.display_info()
        newDisk.close()
    else:
        print("El tamaño del disco debe ser positivo y mayor que 0.")
        
def ejecutarRmdisk(args):   
    op = (input("AVISO, Desea eliminarlo? Seleccione: S-si N-no")).lower()
    if op == "s":
        eliminarDisk(args.path)
    else:
        print("No se elimino el disco!") 

def ejecutarFdisk(args):
    print("**** PARTICIONES ****")
    if args.size > 0:
        if os.path.exists(args.path):
            diskSelect = MBR()
            readDisk(args.path, 0, diskSelect)
            if diskSelect.part1.status == b'\0':
                setPartion(diskSelect, 1, '1', args.name, args.unit, args.size)
                updatePartion(args.path, diskSelect)
                print("Particion " + args.name +" ha sido agregada!")
            elif diskSelect.part2.status == b'\0':
                setPartion(diskSelect, 2, '1', args.name, args.unit, args.size)
                updatePartion(args.path, diskSelect)
                print("Particion " + args.name +" ha sido agregada!")
            elif diskSelect.part3.status == b'\0':
                setPartion(diskSelect, 3, '1', args.name, args.unit, args.size)
                updatePartion(args.path, diskSelect)
                print("Particion " + args.name +" ha sido agregada!")
            elif diskSelect.part4.status == b'\0':
                setPartion(diskSelect, 4, '1', args.name, args.unit, args.size)
                updatePartion(args.path, diskSelect)
                print("Particion " + args.name +" ha sido agregada!")
            else:
                print("No hay particiones libres actualmente")

        else:
            print("Error de Disco no existente.")
    else:
        print("Error: El tamaño de la particion debe ser positivo y mayor que 0.")
        
def setPartion(discoMbr , posPartion, status, name, unit, size):
    if posPartion == 1:
        discoMbr.part1.setStatus(status)
        discoMbr.part1.setName(name)
        if unit == "B":
            discoMbr.part1.setSize(size)
        elif unit== "K":
            sk = size * 1024
            discoMbr.part1.setSize(sk)
        elif unit == "M":
            sw = size * 1024 * 1024
            discoMbr.part1.setSize(sw)
        else:
            print("unidad no existente")
    elif posPartion == 2:
        discoMbr.part2.setStatus(status)
        discoMbr.part2.setName(name)
        if unit == "B":
            discoMbr.part2.setSize(size)
        elif unit== "K":
            sk = size * 1024
            discoMbr.part2.setSize(sk)
        elif unit == "M":
            sw = size * 1024 * 1024
            discoMbr.part2.setSize(sw)
        else:
            print("unidad no existente")
    elif posPartion == 3:
        discoMbr.part3.setStatus('1')
        discoMbr.part3.setName(name)

        if unit == "B":
            discoMbr.part3.setSize(size)
        elif unit== "K":
            sk = size * 1024
            discoMbr.part3.setSize(sk)
        elif unit == "M":
            sw = size * 1024 * 1024
            discoMbr.part3.setSize(sw)
        else:
            print("unidad no existente")
    elif posPartion == 4:
        discoMbr.part4.setStatus('1')
        discoMbr.part4.setName(name)

        if unit == "B":
            discoMbr.part4.setSize(size)
        elif unit== "K":
            sk = size * 1024
            discoMbr.part4.setSize(sk)
        elif unit == "M":
            sw = size * 1024 * 1024
            discoMbr.part4.setSize(sw)
        else:
            print("unidad no existente")

def updatePartion(rutaDisco, dataMBR):
    diskSelect = open(rutaDisco, "rb+")
    writeDisk(diskSelect, 0, dataMBR)
    diskSelect.close()

def ejecutarRep(path):
    mbrDisco = MBR()
    print("**** Generando Reporte ****")
    readDisk(path.path, 0, mbrDisco)
    data=mbrDisco.generarGrafo()
    print(data)