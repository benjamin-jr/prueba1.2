opcion=int(input('''selecciona una opcion:
                 1.- Configurar una interfaz.
                 2.- Configurar una interfaz y crear un OSPF'''))
if opcion==1:

    print("\nconfigure lo siguiente")

    interface1=input("\nindique la interface:")
    ip=input("indique la ip:")
    masc=input("indique mascara subred:")
    nombre=input("indique su nombre:")

    print("\ninterface",interface1)
    print("no shut")
    print("ip address",ip,masc)
    print("Description ***",nombre,'''***
        speed
        duplex full
      
        consulte con los siguientes comandos:
      
         show ip interface brief
         sho run interface''',interface1, '''
         show interface''', interface1)

else:
    interface2=input("\ningrese la interfaz:")
    ip=input("indique la direccion ip:")
    masc2=input("indique la mascara subred:")
    nombre2=input("indique su nombre:")
    ospf=input("indique el numero de proceso OSPF:")
    ospf=str(ospf)
    router=input("indique ID OSPF:")
    area=input("indique area OSPF:")
    print("                         ")
    
    print("interface" ,interface2)
    print("no shutdown")
    print("ip address",ip,masc2)
    print('''Speed 100
        Duplex full
        ''')
    print("router OSPF", ospf)    
    print("network",ip, masc2)
    print("passive-interface",interface2)
    print("")
    print('''Consulte con los siguientes comandos:
          
          Show run | section ospf
          Show ip ospf neighbor
          Show ip interface brief''')

