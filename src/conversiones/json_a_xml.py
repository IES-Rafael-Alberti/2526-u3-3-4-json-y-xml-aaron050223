import json
import xmltodict

try:
    with open("src/conversiones/originales/conversion.json", 'r', encoding='utf-8') as archivo:
        diccionario_datos = json.load(archivo) # 'load()' es para guardar archivo como diccionario directamente

    diccionario_con_raiz = { # esto falta la raiz para que pueda pasarse a xml
    "usuarios": diccionario_datos
    }

    xml_salida = xmltodict.unparse(diccionario_con_raiz, pretty = True, short_empty_elements = True)

    with open("src/conversiones/creados/conversion.xml", "w", encoding="utf-8") as conversion:
        conversion.write(xml_salida)

except FileNotFoundError:
    print("ERROR: No se encuentra el JSON")
except Exception as error:
    print(f"ERROR: {error}")