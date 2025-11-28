import json

def mostrar_datos():
    with open("src/json/datos_usuarios_orig.json", "r") as archivo:
        datos = json.load(archivo)
    
    lista_de_usuarios = datos["usuarios"]

    print("--- Contenido Actual del JSON ---")

    for usuario in lista_de_usuarios:
        print(f"ID: {usuario["id"]}, Nombre: {usuario["nombre"]}, Edad: {usuario["edad"]}")

    print("--- Fin del Contenido ---")

def main():
    mostrar_datos()
if __name__ == "__main__":
    main()
