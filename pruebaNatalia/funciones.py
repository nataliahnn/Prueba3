import json

def agregar_categoria(CategoriaID:int, Nombre):
    with open ('biblioteca.json', mode='r') as lecturaJson:
        leerJson=json.load(lecturaJson)

        diccionarioAdd={
            "CategoriaID": len(leerJson['categoria', CategoriaID])+1,
            "Nombre": Nombre,
        }
        leerJson['categoria'].append(diccionarioAdd)

    with open ('biblioteca.json', mode='w') as lecturaJson:
        leerJson=json.load(lecturaJson)
    print("agregar Categoria... ejecutado correctamente" (diccionarioAdd))
    

def editar_categoria(categoriaID: int, nombre):
    with open ('biblioteca.json', mode='r') as escrituraJson:
        leerJson=json.load(escrituraJson)

        contador=0
        for categoria in leerJson['categoria']:
            if categoria["id"]==categoriaID:
                break
            contador+=1
        leerJson['categoria'] [contador]['nombre']=nombre
    with open ('biblioteca.json', mode='w') as escrituraJson:
        leerJson=json.dump( leerJson,escrituraJson, indent=4)
        print("editando producto..." [categoria][contador])


def eliminar_categoria(id:int):
    with open ('biblioteca.json', mode='r') as lecturaJson:
        leerJson=json.load(lecturaJson)

        contador=0
        for categoria in leerJson['categoria']:
            if categoria['id']==id:
                break
            contador+=1
        del leerJson['categoria'][contador]
        with open ('biblioteca.json', mode='w') as escrituraJSon:
            json.dump(leerJson, escrituraJSon, indent=4)

def listar_categoria():
    with open ('biblioteca.json', mode='r') as lecturaJson:
        leerJson=json.load(lecturaJson)
    print("id  nombre")
    for i in leerJson['categoria']:
        print(i)