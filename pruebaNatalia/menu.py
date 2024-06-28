import funciones


while True:
    
    print("**********************************")
    print("*         1 MUNDO LIBRO           *")
    print("**********************************")
    print("[1] - Mantenedor de categorias")
    print("[2] - Reportes")
    print("[3] - Salir ")

    opc=int(input("¿Que deseea hacer?"))

    if opc==1:
            print("**********************************")
            print("*     MANTENEDOR CATEGORIAS      *")
            print("**********************************")
            print("[1] - Agregar categoria")
            print("[2] - Editar categoria")
            print("[3] - Eliminar categoria")
            print("[4] - Buscar categoria")
            print("[5] - Volver")
            opc=int(input("¿Que deseea hacer?"))

            if opc==1:
                    funciones.agregar_categoria
            elif opc==2:
                    funciones.editar_categoria
            elif opc==3:
                    funciones.eliminar_categoria
            elif opc==4:
                    funciones.listar_categoria
            elif opc==5:
                    print("saliendo...")
                    break
    if opc==3:
           print("saliendo...")
           break

    



