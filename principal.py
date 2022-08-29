from os import close, system


while True:
    print("========================================")
    print("*            Menu Principal            *")
    print("*  1) Cargar Archivo .xml              *")
    print("*  2) Mostrar Pacientes                *")
    print("*  3) Generar Patrones                 *")
    print("*  4) Salir                            *")
    print("========================================")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("Cargando archivo de .xml")
    elif opcion == "2":
        print("mostrando pacientes")
    elif opcion == "3":
        print("generando los patrones")
    elif opcion == "4":
        break
    else:
        print("opcion no valida")

