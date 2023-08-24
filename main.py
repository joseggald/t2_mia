import argparse
from diskClass import *
from comandosDisk import *
import os

class CaseInsensitiveArgumentParser(argparse.ArgumentParser):
    def _get_option_tuples(self, option_string):
        return super()._get_option_tuples(option_string.lower())
    

def main():
    parser = CaseInsensitiveArgumentParser(description="Analizador de comandos MIA")

    subparsers = parser.add_subparsers(dest="command", help="Comando a ejecutar")

    # Nuevo comando "execute"
    execute_parser = subparsers.add_parser("execute", help="Ejecutar comando execute")
    execute_parser.add_argument("-path", required=True, help="Ruta del archivo a abrir")

    # Mkdisk
    mkdisk_parser = subparsers.add_parser("mkdisk", help="Crear disco")   
    mkdisk_parser.add_argument("-size", required=True, type=int, help="Tamaño del disco")
    mkdisk_parser.add_argument("-path", required=True, help="Ruta donde se creará el disco")
    mkdisk_parser.add_argument("-unit", required=False, choices=["K", "M"], default="M", help="Unidad de tamaño (opcional)")

    # Rmdisk
    rmdisk_parser = subparsers.add_parser("rmdisk", help="Eliminar disco")
    rmdisk_parser.add_argument("-path", required=True, help="Ruta donde se encuentra el disco a eliminar")
    
    # Fdisk
    fdisk_parser = subparsers.add_parser("fdisk", help={"Particiones de Disco"})
    fdisk_parser.add_argument("-size", required=True, type=int, help="Tamaño de la particion")
    fdisk_parser.add_argument("-path", required=True, help="Ruta del disco")
    fdisk_parser.add_argument("-name", required=True, help="Nombre de la particion")
    fdisk_parser.add_argument("-unit", required=False, choices=["B","K", "M"], default="K", help="Unidad de tamaño (opcional)")
    fdisk_parser.add_argument("-type", required=True, choices=["P", "E"],help="Tipo de ajuste de disco")


    rep_parser = subparsers.add_parser("rep", help="Graficación")
    rep_parser.add_argument("-path", required=True, help="Ruta del archivo a abrir")

    args = parser.parse_args()
    if args.command == "execute":
        if os.path.exists(args.path):
            with open(args.path, 'r') as file:
                for line in file:
                    if "mkdisk" in line:
                        mkdisk_args = mkdisk_parser.parse_args(line.split()[1:])
                        ejecutarMkdisk(mkdisk_args)
                    elif "rmdisk" in line:
                        rmdisk_args = rmdisk_parser.parse_args(line.split()[1:])
                        ejecutarRmdisk(rmdisk_args)
                    elif "fdisk" in line:
                        fdisk_args = fdisk_parser.parse_args(line.split()[1:])
                        ejecutarFdisk(fdisk_args)
                    elif "rep" in line:
                        rep_args = rep_parser.parse_args(line.split()[1:])
                        ejecutarRep(rep_args)
        else:
            print(f"El archivo {args.path} no es existe segun la ruta.")
    else:
        print("Comando desconocido dentro del programa")

if __name__ == "__main__":
    main()