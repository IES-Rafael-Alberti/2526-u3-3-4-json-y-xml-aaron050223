import json
import xmltodict
try:
    with open("src/conversiones/originales/conversion.xml", 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        diccionario_json = xmltodict.parse(contenido)

    with open("src/conversiones/creados/conversion.json", "w", encoding="utf-8") as conversion:
        json.dump(diccionario_json, conversion, indent=4)
        
except FileNotFoundError:
    print("ERROR: No se encuentra el JSON")
except Exception as error:
    print(f"ERROR: {error}")