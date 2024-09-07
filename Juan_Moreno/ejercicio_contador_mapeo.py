## Ejercicio en clase 

informacion_personal = {"nombre":"Juan",
                        "telefono":"0985413259",
                        "email":"jansebastian11@hotmail.com"
} 

# Contador de palabras dentro de un diccionario


def contar_palabras(informacion_personal):
    
    numero_de_palabras = 0
    
    for valor in informacion_personal.values():
        numero_de_palabras += len(valor.split())
    return numero_de_palabras

resultado = contar_palabras(informacion_personal)

print(f"Total de palabras en el diccionario: {resultado}")



# Mapeo de usuarios

## Apenas entienda bien todo esto, completare este ejercicio faltante, una disculpa
