from os import remove, path, makedirs

def crearDisk(nombre):
    try:
        makedirs(path.dirname(nombre), exist_ok=True)
        fileOpen = open(nombre, "wb+") 
        print("El disco se ha creado!")
        return fileOpen
    except Exception as e:
        print(f"Error al crear disco: {e}")

def eliminarDisk(nombre):
    if path.exists(nombre):
        remove(nombre)
        print("Disco eliminado!")
    else:
        print("Error el archivo no se encontro.")


def manejoEspacioDisk(archivo, espacio, unidad):
    buffer = b'\0' 
    if unidad == "K":
        bytes_per_unit = 1024
    elif unidad == "M":
        bytes_per_unit = 1024 * 1024 
    else:
        print("Unidad de tamaño No correspondiente")
        return

    timeWrite = espacio * bytes_per_unit
    for i in range(timeWrite):
        archivo.write(buffer)

def writeDisk(file, des,obj):
        try:
                data = obj.doSerialize()
                file.seek(des)
                file.write(data)
                print("Ha sido procesada la escritura en el disco")
        except Exception as e:
                print(f"Error al escribir en el disco disco: {e}")

def readDisk(nom, des, objeto):
        with open(nom, "rb") as fileOpen:
                try:
                        fileOpen.seek(des)
                        data = fileOpen.read(len(objeto.doSerialize()))
                        objeto.doDeserialize(data)
                        print("Lectura completa de Disco")
                except Exception as e:
                        print(f"Error reading object err: {e}")

