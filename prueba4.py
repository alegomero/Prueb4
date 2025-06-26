# Lista para guardar usuarios
usuarios = []

# Función para validar contraseña
def es_contraseña_valida(contraseña):
    if len(contraseña) < 8:
        return False
    if ' ' in contraseña:
        return False
    tiene_letra = False
    tiene_numero = False
    for caracter in contraseña:
        if caracter.isalpha():
            tiene_letra = True
        if caracter.isdigit():
            tiene_numero = True
    return tiene_letra and tiene_numero

# Función para ingresar usuario
def ingresar_usuario():
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        existe = False
        for u in usuarios:
            if u["nombre"] == nombre:
                existe = True
                break
        if existe:
            print("Usuario ya existe. Intento otro.")
        else:
            break

    while True:
        sexo = input("Ingrese sexo: ").upper()
        if sexo != "M" and sexo != "F":
            print("Debe ingresar M o F solamente. Intente de nuevo.")
        else:
            break

    while True:
        contraseña = input("Ingrese contraseña: ")
        if es_contraseña_valida(contraseña):
            print("Contraseña valida.")
            break
        else:
            print("Contraseña no valida. Intente otra.")

    nuevo_usuario = {
        "nombre": nombre,
        "sexo": sexo,
        "contraseña": contraseña
    }
    usuarios.append(nuevo_usuario)
    print("Usuario ingresado con exito!!")

# Función para buscar usuario
def buscar_usuario():
    nombre = input("Ingrese usuario a buscar: ")
    encontrado = False
    for u in usuarios:
        if u["nombre"] == nombre:
            print(f"El sexo del usuario es: {u['sexo']} y la contraseña es: {u['contraseña']}")
            encontrado = True
            break
    if not encontrado:
        print("El usuario no se encuentra.")

# Función para eliminar usuario
def eliminar_usuario():
    nombre = input("Ingrese usuario a buscar: ")
    for u in usuarios:
        if u["nombre"] == nombre:
            usuarios.remove(u)
            print("Usuario eliminado con éxito!")
            return
    print("No se pudo eliminar usuario!")

# --------- Programa ---------

while True:
    print("\nMENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
    
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        ingresar_usuario()
    elif opcion == "2":
        buscar_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("Programa terminado..")
        break
    else:
        print("Debe ingresar una opción válida!!")
        