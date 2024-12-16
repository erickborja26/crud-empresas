
dic_empresas={}

def menu():
    print("""GESTIÓN DE EMPRESAS
          [1] REGISTRAR EMPRESA
          [2] MOSTRAR EMPRESA
          [3] ACTUALIZAR EMPRESA
          [4] ELIMINAR EMPRESA
          [5] SALIR
          """)

def mostrar_mensaje(texto):
    print("*"*50)
    print(""*10+ texto)
    print("*"*50)

def registrar():
    mostrar_mensaje("[1] REGISTRAR EMPRESA")
    ruc= input("RUC : ")
    razon_social= input("RAZON SOCIAL : ")
    direccion= input("DIRECCION: ")
    dic_empresa_nueva={
        ruc : {
            'razon social' : razon_social,
            'direccion' : direccion
        }
    }
    dic_empresas.update(dic_empresa_nueva)

def mostrar():
    mostrar_mensaje("[2] MOSTRAR EMPRESAS")
    for ruc,valor in dic_empresas.items():
        print(f"RUC : {ruc}")
        print(f"RAZON SOCIAL : {valor['razon social']}")
        print(f"DIRECCION : {valor['direccion']}")
        print("*"*50)

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR EMPRESA")
    ruc= input("RUC de la empresa a actualizar: ")
    if ruc in dic_empresas:
        print(f"EMPRESA A ACTUALIZAR: {dic_empresas[ruc]['razon social']}")
        ruc_nuevo= input("RUC NUEVO : ")
        razon_nueva= input("RAZON SOCIAL NUEVA : ")
        direccion_nueva= input("DIRECCION NUEVA :")
        dic_empresas.pop(ruc)
        dic_empresa_actualizada= {
            ruc_nuevo: {
                'razon social': razon_nueva,
                'direccion': direccion_nueva
            }
        }
        dic_empresas.update(dic_empresa_actualizada)
        print("EMPRESA ACTUALIZADA CON EXITO")
    else:
        print("NO SE ENCONTRO LA EMPRESA")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR EMPRESA")
    ruc= input("RUC DE LA EMPRESA A ELIMINAR: ")
    if ruc in dic_empresas:
        dic_empresas.pop(ruc)
        print("EMPRESA ELIMINADA CON EXITO")
    else:
        print("NO SE ENCONTRO LA EMPRESA")
