""" Santiago Tabares Escobar -
Daniela Martinez Rodriguez """

# Inicializar un diccionario vacío para almacenar datos personales
datos_personales = {
    "Nombre": "",
    "Apellido": "",
    "Edad": "",
    "Correo": "",
    "Sexo": "",
    "Direccion": "",
    "Color Favorito": ""
}

while True:
    
    menu = input("MENU\n1. Llenar\n2. Imprimir\n3. Eliminar\n4. Editar\n5. Salir\nElija una opción: ")
# Opción para llenar los datos personales
    if menu == "1":
        
        for clave in datos_personales:
            valor = input(f"Ingrese {clave}: ")
            datos_personales[clave] = valor
        print("Datos personales llenados correctamente.")

    elif menu == "2":
# Opción para imprimir los datos personales
        print("\nDatos Personales:")
        for clave, valor in datos_personales.items():
            print(f"{clave}: {valor}")

    elif menu == "3":
# Opción para eliminar un dato
        clave_a_eliminar = input("Ingrese el nombre de la clave que desea eliminar: ")
        if clave_a_eliminar in datos_personales:
            del datos_personales[clave_a_eliminar]
            print(f"{clave_a_eliminar} ha sido eliminado.")
        else:
            print(f"{clave_a_eliminar} no existe en los datos personales.")

    elif menu == "4":
 # Opción para editar un dato
        clave_a_editar = input("Ingrese el nombre de la clave que desea editar: ")
        if clave_a_editar in datos_personales:
            nuevo_valor = input(f"Ingrese el nuevo valor para {clave_a_editar}: ")
            datos_personales[clave_a_editar] = nuevo_valor
            print(f"{clave_a_editar} ha sido editado.")
        else:
            print(f"{clave_a_editar} no existe en los datos personales.")

    elif menu == "5":
 # Opción para salir del bucle
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")

