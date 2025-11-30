import json

def cargar_json(nombre_fichero: str) -> dict:
    """
    Carga el contenido de un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.

    Returns:
        (dict): Contenido del archivo JSON como un diccionario, o None si no se pudo cargar.
    """
    try:
        with open(nombre_fichero, "r") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")

    return None


def guardar_json(nombre_fichero: str, datos: dict):
    """
    Guarda los datos en un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.
        datos (dict): Datos a guardar.
    """
    try:
        with open(nombre_fichero, "w") as archivo:
            json.dump(datos, archivo, indent = 4)

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")        

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")


def actualizar_usuario(datos: dict, id_usuario: int, nueva_edad: int):
    """
    Actualiza la edad de un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a actualizar.
        nueva_edad (int): Nueva edad del usuario.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            usuario["edad"] = nueva_edad
            print(f"Usuario con ID {id_usuario} actualizado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(datos: dict, nuevo_usuario: dict):
    """
    Inserta un nuevo usuario.

    Args:
        datos (dict): Diccionario con los datos actuales.
        nuevo_usuario (dict): Diccionario con los datos del nuevo usuario.
    """
    datos["usuarios"].append(nuevo_usuario)
    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(datos: dict, id_usuario: int):
    """
    Elimina un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a eliminar.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            datos["usuarios"].remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")

def mostrar_datos(datos: dict):
    if not datos:
        print("No hay usuarios")

    else:
        lista_usuarios = datos["usuarios"]

        print("--- Contenido Actual del JSON ---")

        for i in range(len(lista_usuarios)):
            usuario = lista_usuarios[i]
            print(f"ID: {usuario["id"]}, Nombre: {usuario["nombre"]}, Edad: {usuario["edad"]}")

        print("--- Fin del Contenido ---\n")

def inicializar_datos(nombre_fichero: str):
    try:
        with open(nombre_fichero, "r") as archivo:
            datos = json.load(archivo)
        with open("src/practica3.4/json/datos_usuarios.json", "w") as archivo:
            json.dump(datos, archivo, indent = 4)
    except FileNotFoundError:
        print("ERROR | Archivo no encontrado")
    except json.JSONDecodeError:
        print("ERROR | Problemas al decodificar el archivo JSON.")
    
    print("Datos inicializados desde 'datos_usuarios_orig.json' a 'datos_usuarios.json'.")

def limpiarConsola():
    print("\n"*50)

def main():
    """
    Función principal que realiza las operaciones de gestión de un archivo JSON.
    """
    # Nombre del fichero JSON
    nombre_fichero = "src/practica3.4/json/datos_usuarios_orig.json"

    # Paso 1
    limpiarConsola()

    # Paso 2
    inicializar_datos(nombre_fichero)

    # Paso 3
    datos = cargar_json(nombre_fichero)

    if datos is None:
        # Inicializamos datos vacíos si hay error
        datos = {"usuarios": []}
    
    # Paso 4
    mostrar_datos(datos)

    # Paso PAUSA
    input("Pulse ENTER para continuar")

    # Paso 5
    actualizar_usuario(datos, id_usuario = 1, nueva_edad = 31)

    # PAUSA
    input("Pulse ENTER para continuar")

    # Paso 6
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(datos, nuevo_usuario)

    # PAUSA
    input("Pulse ENTER para continuar")

    # Paso 7
    eliminar_usuario(datos, id_usuario = 2)

    # PAUSA
    input("Pulse ENTER para continuar")

    # Paso 8
    guardar_json(nombre_fichero, datos)

    mostrar_datos(datos)

    inicializar_datos(nombre_fichero)

    print("Operaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()
