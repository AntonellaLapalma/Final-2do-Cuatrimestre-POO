#Estimados, les dejo la consigna del trabajo final:

#ABM - Gestión Comercial
#Tendremos que gestionar un comercio (pueden elegir el rubro, ejemplo: kiosco, panadería, librería, indumentaria, calzado)
#Tendremos las siguientes clases principales: cliente, proveedor, artículo y las que consideren necesarias.
#Deberán dar de alta la base de datos teniendo en cuenta la relación entre las tablas a crear.

#Menú:
#   Proveedores:
#         - Alta/Baja/Modificación de Proveedor (DNI, Nombre de Fantasía, Direccion, Telefono, mail, Situacion IVA (Inscripto, Exento, etc..))
#         - Pedido de reposición a Proveedor
#         - Devolución a proveedor: se podrá realizar una baja de stock de articulos de un proveedor para devolver, habrá que completar un campo Observacion o Estado(vencido, dañado, etc)
#   Cliente:
#         - Alta/Baja/Modificacion de Cliente (Tendrá un registro con un cliente "Consumidor final" para aquel que cliente que no quiera registrarse) (campos: DNI, ApellidoNombre, Direccion, Telefono, mail, Situacion Iva)
#   Articulos:
#         - Alta/Baja/Modificacion de Articulo (Codigo de barra, nombre, rubro/categoría, precio, stock, DNI-proveedor)
#        - Ingreso de Remito: ingreso de stock de artículos de un proveedor.
#         - Listado de Artículos sin Stock
#   Ventas:
#         - Facturación: dado un cliente, podrá comprar uno o varios artículos mostrando el monto a pagar y descontando del stock en cada artículo.
#         - Listado de ventas del día: deberá mostrar todos los artículos vendidos en el día.

import code
import re
import os
import time
import mariadb
import datetime
#------------------------ C O N E C T O   B A S E -------------------------------------------------------------------------
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root", 
            autocommit=True)
print(mydb)

mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco")
#--------------------------------------------------------------------------------------------------------------------------
def limpioPantalla():
	sisOper = os.name
	if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
		os.system("clear")
	elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
		os.system("cls")
#--------------------------------------------------------------------------------------------------------------------------

#------------------------------ C L A S E S -------------------------------------------------------------------------------
class Inicio:   #------------------------------------ I N I C I O ---------------------------------------------------------
    def __init__(self):
        limpioPantalla()
        self.validar=Validaciones()                     #----------- INICIO DEL PROGRAMA -------------#
        print("\x1b[0;37m"+"================================================================================")
        print("\x1b[0;37m"+"                                   L O G I N                                    "'\x1b[0;m')
        print("\x1b[0;37m"+"================================================================================\n")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |      1. A D M I N I S T R A D O R      |")       
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |           2. E M P L E A D O           |")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |            3. C L I E N T E            |")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |                4. SALIR                |")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"\n================================================================================")
        self.opcion= input("> " )

        if self.opcion == "1":
            limpioPantalla()
            print("\x1b[0;37m"+"================================================================================")
            print("\x1b[0;37m"+"            I N G R E S E   U S U A R I O   Y   C O N T R A S E Ñ A             "'\x1b[0;m')
            print("\x1b[0;37m"+"================================================================================\n")
            self.usuario= input("> " )
            self.contrasenia= input("> " )
            if self.usuario == "admin" and self.contrasenia == "admin":
                MenuAdmin() #----- TENDRA ACCESO A TODAS LAS OPCIONES -----#
            else:
                print("\x1b[0;37m"+"================================================================================")
                print("\x1b[0;37m"+"> DATOS INCORRECTOS, POR FAVOR VUELVA A INGRESAR.                              "'\x1b[0;m')
                print("\x1b[0;37m"+"================================================================================\n")
                Inicio()

        elif self.opcion == "2":
            limpioPantalla()
            print("\x1b[0;37m"+"================================================================================")
            print("\x1b[0;37m"+"            I N G R E S E   U S U A R I O   Y   C O N T R A S E Ñ A             "'\x1b[0;m')
            print("\x1b[0;37m"+"================================================================================\n")
            self.usuario= input("> " )
            self.contrasenia= input("> " )
            if self.usuario == "123" and self.contrasenia == "123":
                MenuEmpleado()  #----- TENDRA ACCESO A LOS REGISTROS, MODIFICACIONES Y ELIMINACION DE CLIENTES, -----#
            else:                      #----- PROVEEDORS Y ARTICULOS, SECCION VENTA, PEDIDOS E INGRESO DE MERCADERIA -----#
                print("\x1b[0;37m"+"================================================================================")
                print("\x1b[0;37m"+"> DATOS INCORRECTOS, POR FAVOR VUELVA A INGRESAR.                              "'\x1b[0;m')
                print("\x1b[0;37m"+"================================================================================\n")
            time.sleep(3)
            Inicio()

        elif self.opcion == "3":
            limpioPantalla()
            print("\x1b[0;37m"+"================================================================================")
            print("\x1b[0;37m"+"                                   L O G I N                                    "'\x1b[0;m')
            print("\x1b[0;37m"+"================================================================================\n")
            print("\x1b[0;37m"+"                 ==========================================")
            print("\x1b[0;37m"+"                 |   1. C O N S U M I D O R   F I N A L   |")       
            print("\x1b[0;37m"+"                 ==========================================")
            print("\x1b[0;37m"+"                 ==========================================")
            print("\x1b[0;37m"+"                 | 2. C L I E N T E   R E G I S T R A D O |")
            print("\x1b[0;37m"+"                 ==========================================")
            print("\x1b[0;37m"+"\n================================================================================")
            self.opcion= input("> " )
            if self.opcion == "1":
                self.documento= "99999999"
                MenuClientes(self.documento)   #----- SOLO PODRA COMPRAR -----#

            elif self.opcion == "2":
                print("\x1b[0;37m"+"================================================================================")
                print("\x1b[0;37m"+"                       I N G R E S E   S U   D N I                              "'\x1b[0;m')
                print("\x1b[0;37m"+"================================================================================\n")
                self.documento= self.validar.validarIngresoDocumento()
                continuar=self.validar.validarExistenciaDocumentoC()
                if continuar == True:
                    MenuClientes(self.documento)   #----- SOLO PODRA COMPRAR -----#

                else:
                    print("\x1b[0;37m"+"================================================================================")
                    print("\x1b[0;37m"+"> POR FAVOR SOLICITE SU REGISTRO AL PERSONAL AUTORIZADO, GRACIAS.       "'\x1b[0;m')
                    print("\x1b[0;37m"+"================================================================================\n")
                    time.sleep(5)
                    Inicio()
            
            else:
                print("\x1b[0;37m"+"================================================================================")
                print("> OPCION INCORRECTA, INTENTE DE NUEVO.")
                print("\x1b[0;37m"+"================================================================================")

                time.sleep(3)
                Inicio()

        elif self.opcion == "4":
            limpioPantalla()
            print("\x1b[0;37m"+"================================================================================")
            print("                                  P R O G R A M A   F I N A L I Z A D O                      ")
            print("\x1b[0;37m"+"================================================================================")
            time.sleep(3)
            limpioPantalla()
            exit()          

        else:
            print("> OPCION INCORRECTA, INTENTE DE NUEVO.")
            print("\x1b[0;37m"+"================================================================================")

            time.sleep(3)
            limpioPantalla()
            Inicio()
#--------------------------------------------------------------------------------------------------------------------------

class MenuEmpleado:   #------------------------------------ S E C C I O N   E M P L E A D O S -----------------------------
    def __init__(self):
        limpioPantalla()
        print("\x1b[0;37m"+"================================================================================")
        print("\x1b[0;37m"+"                              B I E N V E N I D O                              "'\x1b[0;m')
        print("\x1b[0;37m"+"================================================================================\n")
        print("\x1b[0;33m"+"                 ==========================================")
        print("\x1b[0;33m"+"                 |           1. MENU PROVEEDORES          |")       
        print("\x1b[0;33m"+"                 ==========================================")
        print("\x1b[0;32m"+"                 ==========================================")
        print("\x1b[0;32m"+"                 |            2. MENU CLIENTES            |")
        print("\x1b[0;32m"+"                 ==========================================")
        print("\x1b[0;36m"+"                 ==========================================")
        print("\x1b[0;36m"+"                 |            3. MENU ARTICULOS           |")
        print("\x1b[0;36m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 |            4. REALIZAR VENTA           |")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |            5. CERRAR SESION            |")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"\n================================================================================")
        self.opcion= input("> ELEGIR MENU: " )
        print("\x1b[0;37m"+"================================================================================")

        if self.opcion == "1":
            self.proveedor1= Proveedores()

        elif self.opcion == "2":
            self.cliente1= Cliente()

        elif self.opcion == "3":
            self.articulos1= Articulos()

        elif self.opcion == "4":
            limpioPantalla()
            self.ventas1= Ventas()
            print("\x1b[0;31m"+"================================================================================")
            print("\x1b[0;31m"+"                              B I E N V E N I D O                              "'\x1b[0;m')
            print("\x1b[0;31m"+"================================================================================\n")
            print("\x1b[0;31m"+"                 ==========================================")
            print("\x1b[0;31m"+"                 |            1. REALIZAR VENTA           |")       
            print("\x1b[0;31m"+"                 ==========================================")
            print("\x1b[0;31m"+"                 ==========================================")
            print("\x1b[0;31m"+"                 |                 2. ATRAS               |")       
            print("\x1b[0;31m"+"                 ==========================================")
            print("\x1b[0;31m"+"\n================================================================================")
            self.opcion= input("> ELEGIR MENU: " )
            print("\x1b[0;31m"+"================================================================================")

            if self.opcion == "1":
                self.ventas1.opcionesCompra()

            elif self.opcion == "2":
                MenuEmpleado()  
            
        elif self.opcion == "5":
            Inicio()
        else:
            print("> OPCION INCORRECTA, INTENTE DE NUEVO.")
            print("\x1b[0;37m"+"================================================================================")

            time.sleep(3)
            limpioPantalla()
        MenuEmpleado()
        
#--------------------------------------------------------------------------------------------------------------------------

class MenuClientes:   #------------------------------------ S E C C I O N   C L I E N T E S -------------------------------
    def __init__(self,documento):
        self.validar=Validaciones()
        limpioPantalla()
        print("\x1b[0;37m"+"================================================================================")
        print("\x1b[0;37m"+"                              B I E N V E N I D O                              "'\x1b[0;m')
        print("\x1b[0;37m"+"================================================================================\n")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |           1. REALIZAR COMPRA           |")       
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |            2. CERRAR SESION            |")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"\n================================================================================")
        self.opcion= input("> ELEGIR MENU: " )
        print("\x1b[0;37m"+"================================================================================")

        if self.opcion == "1":
            self.venta1= Ventas()
            self.tipoCliente= documento
            self.venta1.compra(self.tipoCliente)
            MenuClientes(documento)

        elif self.opcion == "2":
            Inicio()           
        
        else:
            print("> OPCION INCORRECTA, INTENTE DE NUEVO.")
            print("\x1b[0;37m"+"================================================================================")

            time.sleep(3)
        MenuClientes(documento)
#--------------------------------------------------------------------------------------------------------------------------

class MenuAdmin:      #------------------------------------ S E C C I O N   A D M I N I S T R A D O R E S -----------------
    def __init__(self):   # MOSTRAR MENU INICIO
        limpioPantalla()
        print("\x1b[0;37m"+"================================================================================")
        print("\x1b[0;37m"+"                              B I E N V E N I D O                              "'\x1b[0;m')
        print("\x1b[0;37m"+"================================================================================\n")
        print("\x1b[0;33m"+"                 ==========================================")
        print("\x1b[0;33m"+"                 |           1. MENU PROVEEDORES          |")       
        print("\x1b[0;33m"+"                 ==========================================")
        print("\x1b[0;32m"+"                 ==========================================")
        print("\x1b[0;32m"+"                 |            2. MENU CLIENTES            |")
        print("\x1b[0;32m"+"                 ==========================================")
        print("\x1b[0;36m"+"                 ==========================================")
        print("\x1b[0;36m"+"                 |            3. MENU ARTICULOS           |")
        print("\x1b[0;36m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 |             4. MENU VENTAS             |")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"                 |            5. CERRAR SESION            |")
        print("\x1b[0;37m"+"                 ==========================================")
        print("\x1b[0;37m"+"\n================================================================================")
        self.opcion= input("> ELEGIR MENU: " )
        print("\x1b[0;37m"+"================================================================================")

        if self.opcion == "1":
            self.proveedor1= Proveedores()

        elif self.opcion == "2":
            self.cliente1= Cliente()

        elif self.opcion == "3":
            self.articulos1= Articulos()

        elif self.opcion == "4":
            self.adminVentas()

        elif self.opcion == "5":
            Inicio()
                      
        else:
            print("> OPCION INCORRECTA, INTENTE DE NUEVO.")
            print("\x1b[0;37m"+"================================================================================")
            time.sleep(3)
        MenuAdmin()

    def adminVentas(self):
        self.ventas1= Ventas()
        limpioPantalla()
        print("\x1b[0;31m"+"================================================================================")
        print("                                   MENU VENTAS")
        print("================================================================================\n")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 |            1. REALIZAR VENTA           |")       
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 |             2. LISTA VENTAS            |")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 ==========================================")
        print("\x1b[0;31m"+"                 |                 3. ATRAS               |")       
        print("\x1b[0;31m"+"                 ==========================================")
        print("\n================================================================================")  
        self.opcion= input("> ELEGIR OPCION: ")
        print("\n================================================================================")

        
        if self.opcion == "1":
            self.ventas1.opcionesCompra()

        elif self.opcion == "2":
            self.ventas1.listaVentas()

        elif self.opcion == "3":
            MenuAdmin()

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            time.sleep(3)
            return self.adminVentas()
#--------------------------------------------------------------------------------------------------------------------------



class Proveedores:   #-------------------------------- S E C C I O N   P R O V E E D O R E S ------------------------------
    def __init__(self):   # MOSTRAR MENU PROVEEDORES 
        self.validar= Validaciones()
        limpioPantalla()
        print("\x1b[0;33m"+"================================================================================")
        print("\x1b[0;33m"+"                              MENU PROVEEDORES                                 ")
        print("\x1b[0;33m"+"================================================================================\n")
        print("         ===========================        ===========================             ")
        print("         |    1. ALTA PROVEEDOR    |        | 2. MODIFICAR PROVEEDOR  |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |  3. ELIMINAR PROVEEDOR  |        | 4. PEDIDO DE REPOSICION |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |     5. DEVOLUCION       |        |  6. LISTA PROVEEDORES   |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |   7. BUSCAR PEDIDOS     |        |        8. ATRAS         |              ")
        print("         ===========================        ===========================              ")
        print("\n================================================================================")
        self.opcion= input("> ELEGIR OPCION: ")
        print("\n================================================================================")

        if self.opcion == "1":
            self.altaProveedor()

        elif self.opcion == "2":
            self.modificarProveedor()

        elif self.opcion == "3":
            self.eliminarProveedor()

        elif self.opcion == "4":
            self.pedidoReposicion()

        elif self.opcion == "5":
            self.devolucionProveedor()

        elif self.opcion == "6":
            limpioPantalla()
            print("\n=============================================================================================================")
            print(" {0:^8}{1:^20}{2:^20}{3:^10}{4:^30}{5:^8}".format("DNI","NOMBRE","DIRECCION","TELEFONO","MAIL", "SITUACION IVA"))  
            print("=============================================================================================================\n")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM proveedores")
            for ind in mycursor:
                print(" {0:^8}{1:^20}{2:^20}{3:^10} {4:^30} {5:^8}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind [5]))
            print("\n=============================================================================================================")
            print(" > PRESIONE ENTER PARA VOLVER.")
            print("=============================================================================================================")
            input(" > ")

        elif self.opcion == "7":
            limpioPantalla()
            print("\x1b[0;33m"+"================================================================================")
            print("\x1b[0;33m"+"                              BUSCAR PEDIDO                                 ")
            print("\x1b[0;33m"+"================================================================================\n")
            pedido=self.validar.validarIngresoCodigoVenta()
            print("\n============================================================================================")
            print(" {0:^16}{1:^8}{2:^10}{3:^20} {4:^15} {5:^15}".format("PEDIDO","PROVEEDOR","CODGIO","PRODUCTO","CANTIDAD","PRECIO"))  
            print("============================================================================================\n")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM pedidosrealizados where numeroPedido LIKE'%"+pedido+"%'")
            for ind in mycursor:
                print(" {0:^16}{1:^8} {2:^10}{3:^25} {4:^15} {5:^15}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind [5]))
            print("============================================================================================")
            print(" > PRESIONE ENTER PARA VOLVER.")
            print("============================================================================================")
            input(" > ")

        elif self.opcion == "8":
            return

        else:
            print("\x1b[0;33m"+"> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("\x1b[0;33m"+"================================================================================")
            time.sleep(3)
        Proveedores()
            
    def altaProveedor(self):   # REGISTRAR UN PROVEEDOR 
        limpioPantalla()
        print("\x1b[0;33m"+"================================================================================")
        print("                             REGISTRAR PROVEEDOR                ")
        print("================================================================================\n")
        self.documento = self.validar.validarIngresoDocumento()
        continuar = self.validar.validarInexistenciaDocumentoP()
        if continuar == True:
            self.nombre = input("> NOMBRE: ")
            self.direccion = input("> DIRECCION: ")
            self.telefono = self.validar.verificarTelefono()
            self.mail = self.validar.verificarCorreo()
            self.iva = input("> SITUACION IVA: ")
            
            mycursor = mydb.cursor()
            sql = "INSERT INTO proveedores (dni, nombre, direccion, telefono, mail, situacionIva) VALUES (%s, %s, %s, %s,%s, %s)"
            val = (self.documento, self.nombre, self.direccion, self.telefono, self.mail,self.iva)
            mycursor.execute(sql, val)
            mydb.commit()

            if mycursor.rowcount > 0:
                print("\n================================================================================")
                print("> EL PROVEEDOR ", self.nombre.upper() ," SE REGISTRO CORRECTAMENTE.")
                print("================================================================================\n\n")
                
            
            else:
                print("\n================================================================================")
                print("> ERROR AL CARGAR EL PROVEEDOR.")
                print("================================================================================\n\n")

        time.sleep(3)

    def modificarProveedor(self):   # MODIFICAR DATOS DE LOS PROVEEDORES 
#-------------------------------------------- MOSTRAR MENU --------------------------------------------------------------        
        limpioPantalla()
        print("================================================================================")
        print("                           QUE DATO VA A MODIFICAR             ")
        print("================================================================================\n")
        print("         ===========================        ===========================             ")
        print("         |         1. DNI          |        |        2. NOMBRE        |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |       3. DIRECION       |        |       4. TELEFONO       |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |         5. MAIL         |        |     6. SITUACION IVA    |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |   7. TODOS LOS DATOS    |        |        8. ATRAS         |              ")
        print("         ===========================        ===========================              ")
        print("\n================================================================================\n")
        opcion = input("> ")
        print("\n================================================================================\n\n")
        limpioPantalla()

        if opcion < "8":
            print("================================================================================")
            print("                      INGRESE EL DNI DEL PROVEEDOR          ")
            print("================================================================================\n")
            self.documento= self.validar.validarIngresoDocumento()
            continuar=self.validar.validarExistenciaDocumentoP()
            print("\n================================================================================\n\n")
            
            if continuar == True:
                
                mycursor = mydb.cursor()
                sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                limpioPantalla()
        #------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------- 1. MODIFICAR DNI --------------------------------------------------------------
                if opcion == ("1"):
                    print("\x1b[0;33m"+"================================================================================")
                    print("                             INGRESE EL DNI NUEVO            ")
                    print("================================================================================\n")
                    self.documentoNuevo=self.validar.validarIngresoDocumento()
                    continuar=self.validar.validarInexistenciaDocumentoP()
                    if continuar== True:
                        mycursor = mydb.cursor()
                        sql = "UPDATE proveedores SET dni = '"+str(self.documentoNuevo)+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                        mycursor.execute(sql)
                        mydb.commit()

                        sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documentoNuevo)+"%'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        for ind in myresultado:
                            print("\n================================================================================")
                            print("> EL DNI DEL PROVEEDOR ", str(ind[1]).upper() , " SE MODIFICO CORRECTAMENTE.")
                            print("================================================================================\n\n")
                        
                    time.sleep(3)
                    return self.modificarProveedor() 
        #------------------------------------------------------------------------------------------------------------------------
        #------------------------------------- 2. MODIFICAR NOMBRE --------------------------------------------------------------
                elif opcion == ("2"):
                    print("\x1b[0;33m"+"================================================================================")
                    print("                         INGRESE EL NOMBRE NUEVO            ")
                    print("================================================================================\n")
                    self.nombreNuevo = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE proveedores SET nombre = '"+self.nombreNuevo+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\n================================================================================")
                        print("> EL NOMBRE DEL PROVEEDOR "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")

                    time.sleep(3)
                    limpioPantalla()
                    return self.modificarProveedor()
        #------------------------------------------------------------------------------------------------------------------------
        #---------------------------------- 3. MODIFICAR DIRECCION --------------------------------------------------------------                 
                elif opcion == ("3"):
                    print("\x1b[0;33m"+"================================================================================")
                    print("                        INGRESE LA DIRECCION NUEVA            ")
                    print("================================================================================\n")
                    self.direccionNueva = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE proveedores SET direccion = '"+self.direccionNueva+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\n================================================================================")
                        print("> LA DIRECCION DEL PROVEEDOR "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    limpioPantalla()
                    return self.modificarProveedor()
        #------------------------------------------------------------------------------------------------------------------------
        #----------------------------------- 4. MODIFICAR TELEFONO --------------------------------------------------------------  
                elif opcion == ("4"):
                    print("\x1b[0;33m"+"================================================================================")
                    print("                       INGRESE EL TELEFONO NUEVO            ")
                    print("================================================================================\n")
                    self.telefonoNuevo = self.validar.verificarTelefono()
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE proveedores SET telefono = '"+str(self.telefonoNuevo)+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\n================================================================================")
                        print("> EL TELEFONO DEL PROVEEDOR "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    limpioPantalla()
                    return self.modificarProveedor()
        #------------------------------------------------------------------------------------------------------------------------
        #--------------------------------------- 5. MODIFICAR MAIL -------------------------------------------------------------- 
                elif opcion == ("5"):
                    print("\x1b[0;33m"+"================================================================================")
                    print("                       INGRESE EL MAIL NUEVO            ")
                    print("================================================================================\n")
                    self.mailNuevo = self.validar.verificarCorreo()
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE proveedores SET mail = '"+self.mailNuevo+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\n================================================================================")
                        print("> EL MAIL DEL PROVEEDOR "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    limpioPantalla()
                    return self.modificarProveedor()
        #------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------- 6. MODIFICAR IVA -------------------------------------------------------------- 
                elif opcion == ("6"):
                    print("\x1b[0;33m"+"================================================================================")
                    print("                   INGRESE LA SITUACION IVA NUEVA           ")
                    print("================================================================================\n")
                    self.ivaNuevo = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE proveedores SET situacionIva = '"+self.ivaNuevo+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\n================================================================================")
                        print("> LA SITUACION IVA DEL PROVEEDOR "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    limpioPantalla()
                    return self.modificarProveedor()
        #------------------------------------------------------------------------------------------------------------------------
        #---------------------------------- 7. MODIFICAR TODOS LOS DATOS -------------------------------------------------------- 
                elif opcion == ("7"):

                    

                    print("\x1b[0;33m"+"================================================================================")
                    print("                   MODIFICAR PROVEEDOR: INGRESE LOS DATOS NUEVOS                 ")
                    print("================================================================================\n")
                    
                    self.dniviejo=self.documento
                    self.documento= self.validar.validarIngresoDocumento()
                    continuar=self.validar.validarInexistenciaDocumentoP()
                    if continuar == True:

                        self.nombre = input("> NOMBRE: ")
                        self.direccion = input("> DIRECCION: ")
                        self.telefono = self.validar.verificarTelefono()
                        self.mail = self.validar.verificarCorreo()
                        self.iva = input("> SITUACION IVA: ")
                        
                        
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO proveedores (dni, nombre, direccion, telefono, mail, situacionIva) VALUES (%s, %s, %s, %s,%s, %s)"
                        val = (str(self.documento), self.nombre, self.direccion, self.telefono, self.mail,self.iva)
                        mycursor.execute(sql, val)
                        mydb.commit()

                        if mycursor.rowcount > 0:
                            print("\x1b[0;33m"+"\n================================================================================")
                            print("> EL PROVEEDOR ", self.nombre.upper() ," SE MODIFICO CORRECTAMENTE.")
                            print("================================================================================\n\n")
                        else:
                            print("\x1b[0;33m"+"\n================================================================================")
                            print("> ERROR AL CARGAR EL PROVEEDOR.")
                            print("================================================================================\n\n")
                        
                        mycursor = mydb.cursor()
                        sql = "DELETE FROM proveedores WHERE dni LIKE '%"+str(self.documento)+"%'"
                        mycursor.execute(sql)
                        mydb.commit()
                    
                    
                    else:
                        print("\x1b[0;33m"+"\n================================================================================")
                        print("> ERROR AL CARGAR EL PROVEEDOR, EL DNI SE ENCUENTRA EN USO.")
                        print("================================================================================\n\n")

                    
        #------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------- ERROR ------------------------------------------------------------------ 
                else:
                    print("\x1b[0;33m"+"================================================================================")
                    print("> ERROR, OPCION INVALIDA.")
                    print("================================================================================\n\n")

            return 
        #--------------------------------------------- 8. ATRAS ----------------------------------------------------------------- 
        elif opcion == "8":
            return
        #------------------------------------------------------------------------------------------------------------------------
        else:
            print("\x1b[0;33m"+"================================================================================")
            print("> ERROR, OPCION INVALIDA.")
            print("================================================================================\n\n")
        return 
        
    def eliminarProveedor(self):   # ELIMINAR PROVEEDOR 
        limpioPantalla()
        print("\x1b[0;33m"+"================================================================================")
        print("                        INGRESE EL DNI DEL PROVEEDOR          ")
        print("================================================================================\n")
        self.documento=self.validar.validarIngresoDocumento()
        continuar=self.validar.validarExistenciaDocumentoP()
        print("\n================================================================================\n\n")
        
        if continuar == True:
            mycursor = mydb.cursor()
            sql = "DELETE FROM proveedores WHERE dni LIKE '%"+str(self.documento)+"%'"
            mycursor.execute(sql)
            mydb.commit()
            
            if mycursor.rowcount > 0:
                print("\x1b[0;33m"+"\n================================================================================")
                print("> EL PROVEEDOR DE DNI ", self.documento ,"SE ELIMINO CORRECTAMENTE.")
                print("================================================================================\n\n")
            else:
                print("\x1b[0;33m"+"\n================================================================================")
                print("> ERROR AL ELIMINAR EL PROVEEDOR.")
                print("================================================================================\n\n")
        
        time.sleep(3)

    def pedidoReposicion(self): # REALIZAR PEDIDO A PROVEEDOR
        limpioPantalla()
        self.realizarPedido= RealizarPedido()
        
    def devolucionProveedor(self):   # DEVOLVER ARTICULO 
        limpioPantalla()
        self.fecha= datetime.datetime.now()
        print("\x1b[0;33m"+"================================================================================")
        print("                                    S T O C K           ")
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos ")

        for ind in mycursor:
            if ind[4]>0:
                print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("\n================================================================================\n")
        print("\x1b[0;33m"+"\n================================================================================")
        print("                                DEVOLVER ARTICULO           ")
        print("================================================================================\n") 
        self.producto = self.validar.validarIngresoCodigo()
        continuar=self.validar.validarExistenciaCodigoA()
        if continuar == True:
            self.cantidad= self.validar.validarCantidad() 
            self.motivo= input("> MOTIVO: ")

            mycursor = mydb.cursor()
            sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.producto)+"%'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()

            for ind in myresultado:
                if int(self.cantidad) == int(ind[4]):
                    self.total=int(ind[4])- int(self.cantidad)
                    self.nombre=ind[1]

                    mycursor2 = mydb.cursor()
                    sql2 = "INSERT INTO devoluciones (fecha, codigoArt, nombreArt, cantidad, motivo) VALUES (%s,%s, %s, %s,%s)"
                    val2 = (str(self.fecha.strftime("%d%m%Y%H%M%S")),self.producto, self.nombre, self.cantidad,self.motivo)
                    mycursor2.execute(sql2, val2)
                    mydb.commit()

                    mycursor = mydb.cursor()
                    sql = "UPDATE articulos SET stock = '"+str(self.total)+"' WHERE codigo = "+str(self.producto)
                    mycursor.execute(sql)
                    mydb.commit()
                    
                    print("\n================================================================================")
                    print("> ",mycursor.rowcount, " ARTICULO DEVUELTO.")
                    print("================================================================================\n\n")
                    time.sleep(3)

                elif int(self.cantidad) < int(ind[4]):
                    self.total=int(ind[4])- int(self.cantidad)
                    self.pedido=ind[0]
                    self.nombre=ind[1]
                    mycursor = mydb.cursor()
                    sql = "UPDATE articulos SET stock = '"+str(self.total)+"' WHERE codigo = "+str(self.producto)
                    mycursor.execute(sql)
                    mydb.commit()

                    print("\n================================================================================")
                    print("> ",mycursor.rowcount, " ARTICULO DEVUELTO.")
                    print("================================================================================\n\n")
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO devoluciones (fecha, codigoArt, nombreArt, cantidad, motivo) VALUES (%s,%s, %s, %s,%s)"
                    val = (str(self.fecha.strftime("%d%m%Y%H%M%S")),self.producto, str(self.nombre), self.cantidad, self.motivo)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    time.sleep(3)

                else:
                    print("\n================================================================================")
                    print("> ",mycursor.rowcount, " IMPOSIBLE DEVOLVER.")
                    print("================================================================================\n\n")
                    time.sleep(3)

class RealizarPedido:
    def __init__(self):   # MOSTRAR MENU DE PEDIDOS
        self.validar=Validaciones()
        self.fecha= datetime.datetime.now()
        self.pedido=self.fecha.strftime("%d%m%Y%H%M%S")
        print(self.fecha)
        limpioPantalla() 
        self.opcionesPedido()

    def stock(self):   # MUESTRA TODOS LOS ARTICULOS REGISTRADOS
        print("\x1b[0;33m"+"================================================================================")
        print("                                    S T O C K           ")
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos")

        for ind in mycursor:
            print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("\n================================================================================\n")
        
    def carrito(self):   # MUESTRA EL LISTADO DE COMPRA 
        self.totalAbonar=0
        self.pedidoNuemrico=int(self.pedido)
        print("\x1b[0;33m"+"================================================================================")
        print("                      P E D I D O   N U M E R O: "+ self.pedido)
        print("================================================================================")
        print("{0:^10}{1:^10}{2:^10} {3:^25}{4:^8} {5:^8}{6:^8}".format("PEDIDO","PROVEEDOR","CODIGO ART","NOMBRE","CANTIDAD","PRECIO", "TOTAL")) 
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM pedido where numeroPedido LIKE'%"+str(self.pedidoNuemrico)+"%'")
        print("================================================================================\n")
        for ind in mycursor:
            self.totalAbonar=self.totalAbonar+int(ind[6])
            print("{0:^10}{1:^10}{2:^10} {3:^25}{4:^8} {5:^8}{6:^8}".format(ind[0] , ind[1], ind[2], ind[3], ind[4], ind[5], ind[6]))
            print("\n================================================================================\n")

        else:
            print("\n================================================================================\n")
        print("> TOTAL: "+str(self.totalAbonar))
        print("\n================================================================================\n")

    def opcionesPedido(self):   # OPCIONES PARA AGREGAR / QUITAR / MODIFICAR / CANCELAR PEDIDO
        limpioPantalla()
        self.stock()
        print("\x1b[0;33m"+"\n================================================================================")
        print("                                REALIZAR PEDIDO           ")
        print("================================================================================\n")  
        print("         ===========================        ===========================             ")
        print("         |    1. PEDIR BEBIDAS     |        |   2. PEDIR GALLETITAS   |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |   3. PEDIR CHOCOLATES   |        |   4. PEDIR ALFAJORES    |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |    5. PEDIR SNAKS       |        |        6. ATRAS         |              ")
        print("         ===========================        ===========================              ")
        print("\n================================================================================\n")
        self.opcion= input("> ")

        if self.opcion == "1":
            self.agregarBebida()
            
        elif self.opcion == "2":
            self.agregarGalletitas()

        elif self.opcion == "3":
            self.agregarChocolates()

        elif self.opcion == "4":
            self.agregarAlfajores()

        elif self.opcion == "5":
            self.agregarSnacks()

        elif self.opcion == "6":
            return

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            return self.opcionesPedido()

    def agregarBebida(self):
        self.proveedorBebidas="30567279"
        limpioPantalla()
        print("\x1b[0;33m"+"================================================================================")
        print("               B E B I D A S:   P R O V E E D O R "+self.proveedorBebidas)
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos where categoria LIKE'%"+"Bebidas"+"%'")

        for ind in mycursor:
            print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("\n================================================================================\n")
        self.carrito()
        print("         ===========================        ===========================              ")
        print("         |   1. AGREGAR BEBIDAS    |        |    2. QUITAR BEBIDAS    |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |      3. FINALIZAR       |        |       4. CANCELAR       |              ")
        print("         ===========================        ===========================              ")
        print("\n================================================================================")
        self.opcion= input("> ")
        print("================================================================================\n")
        
        if self.opcion == "1":
            self.codigo= self.validar.validarIngresoCodigo()
            continuar= self.validar.validarExistenciaCodigoA()
            if continuar== True:
                continuar2= self.validar.validarExistenciaCodigoPedido()
                if continuar2 == True:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        self.cantidadNueva=int(ind[4])+int(self.cantidad)
                        self.totalNuevo= int(ind[5])*int(self.cantidadNueva)

                        sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadNueva)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 

                        sql = "UPDATE pedido SET total = '"+str(self.totalNuevo)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 
                        return self.agregarBebida()
     
                elif continuar2 == False:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()

                    for ind in myresultado:
                        self.codigoArt = ind[0]
                        self.producto = ind[1]
                        self.precioU = ind[3]
                        self.dniProveedor=ind[5]
                        self.ptotal=int(self.precioU)*int(self.cantidad)
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO pedido (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        val = (str(self.pedido), self.dniProveedor,self.codigoArt, self.producto, self.cantidad, self.precioU, self.ptotal)
                        mycursor.execute(sql, val)
                        mydb.commit()  

                else:
                    return  self.agregarBebida()               
            return self.agregarBebida()
        
        elif self.opcion == "2":
            limpioPantalla()
            self.carrito()
            print("================================================================================")
            print("                      ELIMINAR ELEMENTO DE LA LISTA        ")
            print("================================================================================\n")
            self.producto= self.validar.validarIngresoCodigo()
            continuar= self.validar.validarExistenciaCodigoPedido()
            if continuar== True:
                self.cantidad=self.validar.validarCantidad()
                print("\n================================================================================\n\n")
                
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.producto)+"%'")
                
                for ind in mycursor:
                    cantidadtotal= int(ind[4])
                    preciounidad= int(ind[5])
                    preciototal= int(ind[6]) - (preciounidad * int(self.cantidad))

                if self.cantidad < cantidadtotal:
                    self.cantidadComprar= cantidadtotal-self.cantidad
                    self.totalAbonar=self.totalAbonar-(preciounidad * int(self.cantidad))
                    mycursor = mydb.cursor()
                    sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadComprar)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()
                    mycursor = mydb.cursor()
                    sql = "UPDATE pedido SET total = '"+str(preciototal)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()
                    print("> ELEMENTOS ELIMINADOS.")
                    print("================================================================================\n\n")

                elif self.cantidad == cantidadtotal:
                    self.totalAbonar=self.totalAbonar-preciototal
                    mycursor = mydb.cursor()
                    sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.producto)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()
                    print("> ELEMENTOS ELIMINADOS.")
                    print("================================================================================\n\n")

                else:
                    print("ERROR.")
                    print("================================================================================\n\n")
            elif continuar2 == False:
                print("> NO SE ENCONTRO EL ARTICULO.")
                print("================================================================================\n\n")
            
            
            time.sleep(3)
            limpioPantalla()
            return self.agregarBebida()

        elif self.opcion == "3":
            limpioPantalla()
            self.carrito()
            print("\x1b[0;33m"+"\n================================================================================")
            print("                              FINALIZAR PEDIDO?          ")
            print("================================================================================\n") 
            self.finalizar= input("1. SI \n2. NO\n\n================================================================================\n> ")

            if self.finalizar == "1":
                limpioPantalla()
                mycursor = mydb.cursor()
                sql = "SELECT * FROM pedido"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                self.carrito()
                print("\x1b[0;33m"+"\n================================================================================")
                print("                            PEDIDO REALIZADO CON EXITO          ")
                print("================================================================================\n") 

                for ind in myresultado:
                    self.dato0= ind[0]   
                    self.dato1= ind[1] 
                    self.dato2= ind[2] 
                    self.dato3= ind[3] 
                    self.dato4= ind[4] 
                    self.dato5= ind[5] 
                    self.dato6= ind[6] 

                    mycursor = mydb.cursor()
                    sql = "INSERT INTO pedidosrealizados (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (self.dato0, self.dato1, self.dato2, self.dato3, self.dato4, self.dato5, self.dato6)
                    mycursor.execute(sql, val)

                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()

                time.sleep(3)
                return

            elif self.finalizar == "2":
                return self.agregarBebida()
            
            else:
                ("> OPCION INCORRECTA.")
                print("================================================================================\n") 
                return self.agregarBebida()

        elif self.opcion == "4":
            print("================================================================================")
            print("                            CANCELAR PEDIDO?           ")
            print("================================================================================\n")
            self.eliminar= input("1. SI \n2. NO\n\n================================================================================\n> ")
            print("\n================================================================================\n\n")

            if self.eliminar == "1":
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                
                print("> ",mycursor.rowcount, " ELEMENTOS ELIMINADOS.")
                print("================================================================================\n\n")
                time.sleep(3)
                return

            elif self.eliminar == "2":
                return self.agregarBebida()

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            return self.agregarBebida()
        
    def agregarGalletitas(self):
        limpioPantalla()
        self.proveedorGalletitas="56214893"
        print("\x1b[0;33m"+"================================================================================")
        print("            G A L L E T I T A S:   P R O V E E D O R "+self.proveedorGalletitas)
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos where categoria LIKE'%"+"Galletitas"+"%'")

        for ind in mycursor:
            print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("\n================================================================================\n")
        self.carrito()
        print("         ===========================        ===========================              ")
        print("         |  1. AGREGAR GALLETITAS  |        |  2. QUITAR GALLETITAS   |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |      3. FINALIZAR       |        |       4. CANCELAR       |              ")
        print("         ===========================        ===========================              ")
        print("\n================================================================================")
        self.opcion= input("> ")
        print("================================================================================\n")
        
        if self.opcion == "1":
            self.codigo= self.validar.validarIngresoCodigo()
            continuar= self.validar.validarExistenciaCodigoA()
            if continuar== True:
                continuar2= self.validar.validarExistenciaCodigoPedido()
                if continuar2 == True:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        self.cantidadNueva=int(ind[4])+int(self.cantidad)
                        self.totalNuevo= int(ind[5])*int(self.cantidadNueva)

                        sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadNueva)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 

                        sql = "UPDATE pedido SET total = '"+str(self.totalNuevo)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 
                        return self.agregarGalletitas()
     
                elif continuar2 == False:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()

                    for ind in myresultado:
                        self.codigoArt = ind[0]
                        self.producto = ind[1]
                        self.precioU = ind[3]
                        self.dniProveedor=ind[5]
                        self.ptotal=int(self.precioU)*int(self.cantidad)
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO pedido (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        val = (str(self.pedido), self.dniProveedor,self.codigoArt, self.producto, self.cantidad, self.precioU, self.ptotal)
                        mycursor.execute(sql, val)
                        mydb.commit()                   
            return self.agregarGalletitas()
        
        elif self.opcion == "2":
            limpioPantalla()
            self.carrito()
            print("================================================================================")
            print("                      ELIMINAR ELEMENTO DE LA LISTA        ")
            print("================================================================================\n")
            self.producto= self.validar.validarIngresoCodigo()
            self.cantidad=self.validar.validarCantidad()
            print("\n================================================================================\n\n")
            
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.producto)+"%'")
            
            for ind in mycursor:
                cantidadtotal= int(ind[4])
                preciounidad= int(ind[5])
                preciototal= int(ind[6]) - (preciounidad * int(self.cantidad))


            if self.cantidad < cantidadtotal:
                self.cantidadComprar= cantidadtotal-self.cantidad
                self.totalAbonar=self.totalAbonar-(preciounidad * int(self.cantidad))
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadComprar)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET total = '"+str(preciototal)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
            
            print("> ELEMENTOS ELIMINADOS.")
            print("================================================================================\n\n")
            time.sleep(3)
            limpioPantalla()
            return self.agregarGalletitas()

        elif self.opcion == "3":
            limpioPantalla()
            self.carrito()
            print("\x1b[0;33m"+"\n================================================================================")
            print("                              FINALIZAR PEDIDO?          ")
            print("================================================================================\n") 
            self.finalizar= input("1. SI \n2. NO\n\n================================================================================\n> ")

            if self.finalizar == "1":
                limpioPantalla()
                mycursor = mydb.cursor()
                sql = "SELECT * FROM pedido"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()

                for ind in myresultado:
                    self.dato0= ind[0]   
                    self.dato1= ind[1] 
                    self.dato2= ind[2] 
                    self.dato3= ind[3] 
                    self.dato4= ind[4] 
                    self.dato5= ind[5] 
                    self.dato6= ind[6] 

                    mycursor = mydb.cursor()
                    sql = "INSERT INTO pedidosrealizados (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (self.dato0, self.dato1, self.dato2, self.dato3, self.dato4, self.dato5, self.dato6)
                    mycursor.execute(sql, val)

                self.carrito()
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()

                print("\x1b[0;33m"+"\n================================================================================")
                print("                            PEDIDO REALIZADO CON EXITO          ")
                print("================================================================================\n") 
                time.sleep(3)

            elif self.finalizar == "2":
                return self.opcionesPedido()
            
            else:
                ("> OPCION INCORRECTA.")
                print("================================================================================\n") 
                return self.agregarGalletitas()

        elif self.opcion == "4":
            print("================================================================================")
            print("                            CANCELAR PEDIDO?           ")
            print("================================================================================\n")
            self.eliminar= input("1. SI \n2. NO\n\n================================================================================\n> ")
            print("\n================================================================================\n\n")

            if self.eliminar == "1":
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                
                print("> ",mycursor.rowcount, " ELEMENTOS ELIMINADOS.")
                print("================================================================================\n\n")
                time.sleep(3)
                limpioPantalla()
                return
                

            elif self.eliminar == "2":
                return self.agregarGalletitas()

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            return self.agregarGalletitas()

    def agregarChocolates(self):
        limpioPantalla()
        self.proveedorChocolates= "78445210"
        print("\x1b[0;33m"+"================================================================================")
        print("             C H O C O L A T E S:   P R O V E E D O R "+self.proveedorChocolates)
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos where categoria LIKE'%"+"Chocolates"+"%'")

        for ind in mycursor:
            print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("\n================================================================================\n")
        self.carrito()
        print("         ===========================        ===========================              ")
        print("         |  1. AGREGAR CHOCOLATES  |        |  2. QUITAR CHOCOLATES   |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |      3. FINALIZAR       |        |       4. CANCELAR       |              ")
        print("         ===========================        ===========================              ")
        print("\n================================================================================")
        self.opcion= input("> ")
        print("================================================================================\n")
        if self.opcion == "1":
            self.codigo= self.validar.validarIngresoCodigo()
            continuar= self.validar.validarExistenciaCodigoA()
            if continuar== True:
                continuar2= self.validar.validarExistenciaCodigoPedido()
                if continuar2 == True:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        self.cantidadNueva=int(ind[4])+int(self.cantidad)
                        self.totalNuevo= int(ind[5])*int(self.cantidadNueva)

                        sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadNueva)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 

                        sql = "UPDATE pedido SET total = '"+str(self.totalNuevo)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 
                        return self.agregarChocolates()
     
                elif continuar2 == False:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()

                    for ind in myresultado:
                        self.codigoArt = ind[0]
                        self.producto = ind[1]
                        self.precioU = ind[3]
                        self.dniProveedor=ind[5]
                        self.ptotal=int(self.precioU)*int(self.cantidad)
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO pedido (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        val = (str(self.pedido), self.dniProveedor,self.codigoArt, self.producto, self.cantidad, self.precioU, self.ptotal)
                        mycursor.execute(sql, val)
                        mydb.commit()  
            return self.agregarChocolates()
        
        elif self.opcion == "2":
            limpioPantalla()
            self.carrito()
            print("================================================================================")
            print("                      ELIMINAR ELEMENTO DE LA LISTA        ")
            print("================================================================================\n")
            self.producto= self.validar.validarIngresoCodigo()
            self.cantidad=self.validar.validarCantidad()
            print("\n================================================================================\n\n")
            
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.producto)+"%'")
            
            for ind in mycursor:
                cantidadtotal= int(ind[4])
                preciounidad= int(ind[5])
                preciototal= int(ind[6]) - (preciounidad * int(self.cantidad))


            if self.cantidad < cantidadtotal:
                self.cantidadComprar= cantidadtotal-self.cantidad
                self.totalAbonar=self.totalAbonar-(preciounidad * int(self.cantidad))
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadComprar)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET total = '"+str(preciototal)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
            
            print(">  ELEMENTOS ELIMINADOS.")
            print("================================================================================\n\n")
            time.sleep(3)
            limpioPantalla()
            return self.agregarChocolates()

        elif self.opcion == "3":
            limpioPantalla()
            self.carrito()
            print("\x1b[0;33m"+"\n================================================================================")
            print("                              FINALIZAR PEDIDO?          ")
            print("================================================================================\n") 
            self.finalizar= input("1. SI \n2. NO\n\n================================================================================\n> ")

            if self.finalizar == "1":
                limpioPantalla()
                mycursor = mydb.cursor()
                sql = "SELECT * FROM pedido"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()

                for ind in myresultado:
                    self.dato0= ind[0]   
                    self.dato1= ind[1] 
                    self.dato2= ind[2] 
                    self.dato3= ind[3] 
                    self.dato4= ind[4] 
                    self.dato5= ind[5] 
                    self.dato6= ind[6] 

                    mycursor = mydb.cursor()
                    sql = "INSERT INTO pedidosrealizados (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (self.dato0, self.dato1, self.dato2, self.dato3, self.dato4, self.dato5, self.dato6)
                    mycursor.execute(sql, val)
                self.carrito()
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                
                print("\x1b[0;33m"+"\n================================================================================")
                print("                            PEDIDO REALIZADO CON EXITO          ")
                print("================================================================================\n") 
                time.sleep(3)

            elif self.finalizar == "2":
                return self.opcionesPedido()
            
            else:
                ("> OPCION INCORRECTA.")
                print("================================================================================\n") 
                return self.agregarChocolates()

        elif self.opcion == "4":
            print("================================================================================")
            print("                            CANCELAR PEDIDO?           ")
            print("================================================================================\n")
            self.eliminar= input("1. SI \n2. NO\n\n================================================================================\n> ")
            print("\n================================================================================\n\n")

            if self.eliminar == "1":
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                
                print("> ",mycursor.rowcount, " ELEMENTOS ELIMINADOS.")
                print("================================================================================\n\n")
                time.sleep(3)
                return
                
            elif self.eliminar == "2":
                return self.agregarChocolates()

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            return self.agregarChocolates()

    def agregarAlfajores(self):
        limpioPantalla()
        self.proveedorAlfajores= "44807224"
        print("\x1b[0;33m"+"================================================================================")
        print("                A L F A J O R E S:   P R O V E E D O R "+self.proveedorAlfajores)
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos where categoria LIKE'%"+"Alfajores"+"%'")

        for ind in mycursor:
            print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("\n================================================================================\n")
        self.carrito()
        print("         ===========================        ===========================              ")
        print("         |  1. AGREGAR ALFAJORES   |        |   2. QUITAR ALFAJORES   |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |      3. FINALIZAR       |        |       4. CANCELAR       |              ")
        print("         ===========================        ===========================              ")
        print("\n================================================================================")
        self.opcion= input("> ")
        print("================================================================================\n")
        if self.opcion == "1":
            self.codigo= self.validar.validarIngresoCodigo()
            continuar= self.validar.validarExistenciaCodigoA()
            if continuar== True:
                continuar2= self.validar.validarExistenciaCodigoPedido()
                if continuar2 == True:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        self.cantidadNueva=int(ind[4])+int(self.cantidad)
                        self.totalNuevo= int(ind[5])*int(self.cantidadNueva)

                        sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadNueva)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 

                        sql = "UPDATE pedido SET total = '"+str(self.totalNuevo)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 
                        return self.agregarAlfajores()
     
                elif continuar2 == False:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()

                    for ind in myresultado:
                        self.codigoArt = ind[0]
                        self.producto = ind[1]
                        self.precioU = ind[3]
                        self.dniProveedor=ind[5]
                        self.ptotal=int(self.precioU)*int(self.cantidad)
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO pedido (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        val = (str(self.pedido), self.dniProveedor,self.codigoArt, self.producto, self.cantidad, self.precioU, self.ptotal)
                        mycursor.execute(sql, val)
                        mydb.commit()  
            return self.agregarAlfajores()
        
        elif self.opcion == "2":
            limpioPantalla()
            self.carrito()
            print("================================================================================")
            print("                      ELIMINAR ELEMENTO DE LA LISTA        ")
            print("================================================================================\n")
            self.producto= self.validar.validarIngresoCodigo()
            self.cantidad=self.validar.validarCantidad()
            print("\n================================================================================\n\n")
            
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.producto)+"%'")
            
            for ind in mycursor:
                cantidadtotal= int(ind[4])
                preciounidad= int(ind[5])
                preciototal= int(ind[6]) - (preciounidad * int(self.cantidad))

            if self.cantidad < cantidadtotal:
                self.cantidadComprar= cantidadtotal-self.cantidad
                self.totalAbonar=self.totalAbonar-(preciounidad * int(self.cantidad))
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadComprar)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET total = '"+str(preciototal)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
            
            print("> ELEMENTOS ELIMINADOS.")
            print("================================================================================\n\n")
            time.sleep(3)
            limpioPantalla()
            return self.agregarAlfajores()

        elif self.opcion == "3":
            limpioPantalla()
            self.carrito()
            print("\x1b[0;33m"+"\n================================================================================")
            print("                              FINALIZAR PEDIDO?          ")
            print("================================================================================\n") 
            self.finalizar= input("1. SI \n2. NO\n\n================================================================================\n> ")

            if self.finalizar == "1":
                limpioPantalla()
                mycursor = mydb.cursor()
                sql = "SELECT * FROM pedido"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()

                for ind in myresultado:
                    self.dato0= ind[0]   
                    self.dato1= ind[1] 
                    self.dato2= ind[2] 
                    self.dato3= ind[3] 
                    self.dato4= ind[4] 
                    self.dato5= ind[5] 
                    self.dato6= ind[6] 

                    mycursor = mydb.cursor()
                    sql = "INSERT INTO pedidosrealizados (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (self.dato0, self.dato1, self.dato2, self.dato3, self.dato4, self.dato5, self.dato6)
                    mycursor.execute(sql, val)

                self.carrito()
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                
                print("\x1b[0;33m"+"\n================================================================================")
                print("                            PEDIDO REALIZADO CON EXITO          ")
                print("================================================================================\n") 
                time.sleep(3)
                
            elif self.finalizar == "2":
                return self.agregarAlfajores()
            
            else:
                ("> OPCION INCORRECTA.")
                print("================================================================================\n") 
                return self.agregarAlfajores()

        elif self.opcion == "4":
            print("================================================================================")
            print("                            CANCELAR PEDIDO?           ")
            print("================================================================================\n")
            self.eliminar= input("1. SI \n2. NO\n\n================================================================================\n> ")
            print("\n================================================================================\n\n")

            if self.eliminar == "1":
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                
                print("> ",mycursor.rowcount, " ELEMENTOS ELIMINADOS.")
                print("================================================================================\n\n")
                time.sleep(3)

            elif self.eliminar == "2":
                return self.agregarAlfajores()

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            return self.agregarAlfajores()

    def agregarSnacks(self):
        self.proveedorSnacks= "55786432"
        limpioPantalla()
        print("\x1b[0;33m"+"================================================================================")
        print("                   S N A C K S:   P R O V E E D O R "+self.proveedorSnacks)
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos where categoria LIKE'%"+"Snacks"+"%'")

        for ind in mycursor:
            print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("\n================================================================================\n")
        self.carrito()
        print("         ===========================        ===========================              ")
        print("         |    1. AGREGAR SNACKS    |        |     2. QUITAR SNACKS    |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |      3. FINALIZAR       |        |       4. CANCELAR       |              ")
        print("         ===========================        ===========================              ")
        print("================================================================================\n")
        self.opcion= input("> ")
        print("================================================================================\n")
        if self.opcion=="1":
            self.codigo= self.validar.validarIngresoCodigo()
            continuar= self.validar.validarExistenciaCodigoA()
            if continuar== True:
                continuar2= self.validar.validarExistenciaCodigoPedido()
                if continuar2 == True:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        self.cantidadNueva=int(ind[4])+int(self.cantidad)
                        self.totalNuevo= int(ind[5])*int(self.cantidadNueva)

                        sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadNueva)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 

                        sql = "UPDATE pedido SET total = '"+str(self.totalNuevo)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit() 
                        return self.agregarSnacks()
     
                elif continuar2 == False:
                    self.cantidad= self.validar.validarCantidad()
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()

                    for ind in myresultado:
                        self.codigoArt = ind[0]
                        self.producto = ind[1]
                        self.precioU = ind[3]
                        self.dniProveedor=ind[5]
                        self.ptotal=int(self.precioU)*int(self.cantidad)
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO pedido (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        val = (str(self.pedido), self.dniProveedor,self.codigoArt, self.producto, self.cantidad, self.precioU, self.ptotal)
                        mycursor.execute(sql, val)
                        mydb.commit()  
            return self.agregarSnacks()
        
        elif self.opcion == "2":
            limpioPantalla()
            self.carrito()
            print("================================================================================")
            print("                      ELIMINAR ELEMENTO DE LA LISTA        ")
            print("================================================================================\n")
            self.producto= self.validar.validarIngresoCodigo()
            self.cantidad=self.validar.validarCantidad()
            print("\n================================================================================\n\n")
            
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM pedido WHERE codigoArt LIKE '%"+str(self.producto)+"%'")
            
            for ind in mycursor:
                cantidadtotal= int(ind[4])
                preciounidad= int(ind[5])
                preciototal= int(ind[6]) - (preciounidad * int(self.cantidad))

            if self.cantidad < cantidadtotal:
                self.cantidadComprar= cantidadtotal-self.cantidad
                self.totalAbonar=self.totalAbonar-(preciounidad * int(self.cantidad))
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET cantidadItem = '"+str(self.cantidadComprar)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                mycursor = mydb.cursor()
                sql = "UPDATE pedido SET total = '"+str(preciototal)+"' WHERE codigoArt LIKE '%"+str(self.producto)+"%'"
                mycursor.execute(sql)
                mydb.commit()
            
            print("> ELEMENTOS ELIMINADOS.")
            print("================================================================================\n\n")
            time.sleep(3)
            limpioPantalla()
            return self.agregarSnacks()

        elif self.opcion =="3":
            limpioPantalla()
            self.carrito()
            print("\x1b[0;33m"+"\n================================================================================")
            print("                              FINALIZAR PEDIDO?          ")
            print("================================================================================\n") 
            self.finalizar= input("1. SI \n2. NO\n\n================================================================================\n> ")

            if self.finalizar == "1":
                limpioPantalla()
                mycursor = mydb.cursor()
                sql = "SELECT * FROM pedido"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()

                for ind in myresultado:
                    self.dato0= ind[0]   
                    self.dato1= ind[1] 
                    self.dato2= ind[2] 
                    self.dato3= ind[3] 
                    self.dato4= ind[4] 
                    self.dato5= ind[5] 
                    self.dato6= ind[6] 

                    mycursor = mydb.cursor()
                    sql = "INSERT INTO pedidosrealizados (numeroPedido, proveedor, codigoArt, nombreItem, cantidadItem, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (self.dato0, self.dato1, self.dato2, self.dato3, self.dato4, self.dato5, self.dato6)
                    mycursor.execute(sql, val)

                self.carrito()
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()

                print("\x1b[0;33m"+"\n================================================================================")
                print("                            PEDIDO REALIZADO CON EXITO          ")
                print("================================================================================\n") 
                time.sleep(3)
                
            elif self.finalizar == "2":
                return self.agregarSnacks()
            
            else:
                ("> OPCION INCORRECTA.")
                print("================================================================================\n") 
                return self.agregarSnacks()

        elif self.opcion =="4":
            print("================================================================================")
            print("                            CANCELAR PEDIDO?           ")
            print("================================================================================\n")
            self.eliminar= input("1. SI \n2. NO\n\n================================================================================\n> ")
            print("\n================================================================================\n\n")

            if self.eliminar == "1":
                mycursor = mydb.cursor()
                sql = "DELETE FROM pedido WHERE numeroPedido LIKE '%"+str(self.pedido)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                
                print("> ",mycursor.rowcount, " ELEMENTOS ELIMINADOS.")
                print("================================================================================\n\n")
                time.sleep(3)
                limpioPantalla()
                return
                

            elif self.eliminar == "2":
                return self.agregarSnacks()

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            return self.agregarSnacks()
#--------------------------------------------------------------------------------------------------------------------------

class Cliente:   #------------------------------------ S E C C I O N   C L I E N T  E S -----------------------------------
    def __init__(self):   # MOSTRAR MENU CLIENTES 
        self.validar= Validaciones()
        limpioPantalla()
        print("\x1b[0;32m"+"================================================================================")
        print("                                  MENU CLIENTES                                 ")
        print("================================================================================")
        print("         ===========================        ===========================             ")
        print("         |     1. ALTA CLIENTE     |        |  2. MODIFICAR CLIENTE   |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |   3. ELIMINAR CLIENTE   |        |    4. LISTA CLIENTES    |              ")
        print("         ===========================        ===========================              ")
        print("                          ===========================              ")
        print("                          |        5. ATRAS         |              ")
        print("                          ===========================              ")
        print("\n================================================================================")
        self.opcion= input("> ELEGIR OPCION: ")
        print("\n================================================================================")

        if self.opcion == "1":
            self.altaCliente()

        elif self.opcion == "2":
            self.modificarCliente()

        elif self.opcion == "3":
            self.eliminarCliente()

        elif self.opcion == "4":
            limpioPantalla()
            print("\n============================================================================================")
            print(" {0:^8}{1:^20}{2:^20}{3:^10}{4:^20}{5:^8}".format("DNI","NOMBRE","DIRECCION","TELEFONO","MAIL", "SITUACION IVA"))  
            print("============================================================================================\n")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM clientes")
            for ind in mycursor:
                print(" {0:^8}{1:^20}{2:^20}{3:^10}{4:^20}{5:^8}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind [5]))
            print("============================================================================================")
            print(" > PRESIONE ENTER PARA VOLVER.")
            print("============================================================================================")
            input(" > ")    
            
        elif self.opcion == "5":
            return

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            time.sleep(3)
            
        Cliente()

    def altaCliente(self):   ## REGISTRA CLIENTE NUEVO 
        limpioPantalla()
        print("\x1b[0;32m"+"================================================================================")
        print("                             REGISTRAR CLIENTE                 ")
        print("================================================================================\n")
        self.documento = self.validar.validarIngresoDocumento()
        continuar= self.validar.validarInexistenciaDocumentoC()
        if continuar == True:
            self.nombre = input("> NOMBRE: ")
            self.direccion = input("> DIRECCION: ")
            self.telefono = self.validar.verificarTelefono()
            self.mail = self.validar.verificarCorreo()
            self.iva = input("> SITUACION IVA: ")
            
            mycursor = mydb.cursor()
            sql = "INSERT INTO clientes (dni, apellidoNombre, direccion, telefono, mail, situacionIva) VALUES (%s, %s, %s, %s,%s, %s)"
            val = (self.documento, self.nombre, self.direccion, self.telefono, self.mail,self.iva)
            mycursor.execute(sql, val)
            mydb.commit()

            if mycursor.rowcount > 0:
                print("\n================================================================================")
                print("> EL CLIENTE ", str(self.nombre).upper() ,"SE REGISTRO CORRECTAMENTE.")
                print("================================================================================\n\n")

            else:
                print("\n================================================================================")
                print("> ERROR AL CARGAR EL CLIENTE.")
                print("================================================================================\n\n")

        time.sleep(3)

    def modificarCliente(self):   # MODIFICAR DATOS DE LOS CLIENTES 
        limpioPantalla()
        print("\x1b[0;32m"+"================================================================================")
        print("                           QUE DATO VA A MODIFICAR             ")
        print("================================================================================")
        print("         ===========================        ===========================             ")
        print("         |         1. DNI          |        |        2. NOMBRE        |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |      3. DIRECCION       |        |       4. TELEFONO       |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |        5. MAIL          |        |    6. SITUACION IVA     |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |   7. TODOS LOS DATOS    |        |        8. ATRAS         |              ")
        print("         ===========================        ===========================              ")
        print("================================================================================\n")
        self.opcion = input("> ")
        print("\n================================================================================\n\n")
        limpioPantalla()
        if int(self.opcion) < 8:
            print("\x1b[0;32m"+ "================================================================================")
            print("                          INGRESE EL DNI DEL CLIENTE           ")
            print("================================================================================\n")
            self.documento= self.validar.validarIngresoDocumento()
            self.continuar=self.validar.validarExistenciaDocumentoC()
            if self.continuar == True:

                mycursor = mydb.cursor()
                sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                limpioPantalla()

                if self.opcion == "1":    ## 1. MODIFICAR EL DNI DEL CLIENTE
                    print("\x1b[0;32m"+"================================================================================")
                    print("                          INGRESE EL DNI NUEVO            ")
                    print("================================================================================\n")
                    self.documentoNuevo=self.validar.validarIngresoDocumento()
                    continuar= self.validar.validarInexistenciaDocumentoC()
                    if continuar == True:
                        mycursor = mydb.cursor()
                        sql = "UPDATE clientes SET dni = '"+str(self.documentoNuevo)+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                        mycursor.execute(sql)
                        mydb.commit()

                        sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documentoNuevo)+"%'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        for ind in myresultado:
                            print("\x1b[0;32m"+"\n================================================================================")
                            print("> EL DNI DEL CLIENTE "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                            print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarCliente() 

                elif self.opcion == "2":   # 2. MODIFICAR EL NOMBRE DEL CLIENTE
                    print("\x1b[0;32m"+"================================================================================")
                    print("                           INGRESE EL NOMBRE NUEVO            ")
                    print("================================================================================\n")
                    self.nombreNuevo = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE clientes SET apellidoNombre = '"+self.nombreNuevo+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\x1b[0;32m"+"\n================================================================================")
                        print("> EL NOMBRE DELCLIENTE "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarCliente()
                        
                elif self.opcion == "3":   # 3. MODIFICAR DIRECCION DEL CLIENTE
                    print("\x1b[0;32m"+"================================================================================")
                    print("                        INGRESE LA DIRECCION NUEVA           ")
                    print("================================================================================\n")
                    self.direccionNueva = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE clientes SET direccion = '"+self.direccionNueva+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\x1b[0;32m"+"\n================================================================================")
                        print("> LA DIRECCION DEL CLIENTE "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarCliente()

                elif self.opcion == "4":   # 4. MODIFICIAR TELEFONO DEL CLIENTE
                    print("\x1b[0;32m"+"================================================================================")
                    print("                          INGRESE EL TELEFONO NUEVO           ")
                    print("================================================================================\n")
                    self.telefonoNuevo = self.validar.verificarTelefono()
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE clientes SET telefono = '"+str(self.telefonoNuevo)+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\x1b[0;32m"+"\n================================================================================")
                        print("> EL TELEFONO DEL CLIENTE "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarCliente()

                elif self.opcion == "5":   # 5. MODIFICIAR MAIL DEL CLIENTE
                    print("\x1b[0;32m"+"================================================================================")
                    print("                         INGRESE EL MAIL NUEVO          ")
                    print("================================================================================\n")
                    self.mailNuevo = self.validar.verificarCorreo()
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE clientes SET mail = '"+self.mailNuevo+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\n================================================================================")
                        print("> EL MAIL DEL CLIENTE "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarCliente()

                elif self.opcion == "6":   # 6. MODIFICIAR IVA DEL CLIENTE
                    print("\x1b[0;32m"+"================================================================================")
                    print("                  INGRESE LA NUEVA SITUACION IVA DEL CLIENTE           ")
                    print("================================================================================\n")
                    self.ivaNuevo = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE clientes SET situacionIva = '"+self.ivaNuevo+"' WHERE dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\x1b[0;32m"+"\n================================================================================")
                        print("> LA SITUACION IVA DEL CLIENTE "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarCliente()

                elif self.opcion == "7":   # 7. MODIFICIAR TODOS LOS DATOS DEL CLIENTE
                    self.dniviejo=self.documento
                    print("================================================================================")
                    print("                              MODIFICAR CLIENTE                ")
                    print("================================================================================\n")
                    self.documento=self.validar.validarIngresoDocumento()
                    continuar=self.validar.validarInexistenciaDocumentoC()
                    if continuar ==True:
                        self.nombre = input("> NOMBRE: ")
                        self.direccion = input("> DIRECCION: ")
                        self.telefono = self.validar.verificarTelefono()
                        self.mail = self.validar.verificarCorreo()
                        self.iva = input("> SITUACION IVA: ")
                        
                        
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO clientes (dni, apellidoNombre, direccion, telefono, mail, situacionIva) VALUES (%s, %s, %s, %s,%s, %s)"
                        val = (str(self.documento), self.nombre, self.direccion, self.telefono, self.mail,self.iva)
                        mycursor.execute(sql, val)
                        mydb.commit()

                        if mycursor.rowcount > 0:
                            print("\x1b[0;32m"+"\n================================================================================")
                            print("> EL CLIENTE", (self.nombre).upper() ,"SE MODIFICO CORRECTAMENTE.")
                            print("================================================================================\n\n")
                        else:
                            print("\n================================================================================")
                            print("> ERROR AL CARGAR EL CLIENTE.")
                            print("================================================================================\n\n")

                        mycursor = mydb.cursor()
                        sql = "DELETE FROM clientes WHERE dni LIKE '%"+str(self.dniviejo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit()

                        time.sleep(3)
                        return self.modificarCliente()

            return self.modificarCliente()

        elif int(self.opcion) == 8:
            return

        else:                   # ERROR
            print("\x1b[0;32m"+"================================================================================")
            print("> ERROR, OPCION INVALIDA.")
            print("================================================================================\n\n")
            return self.modificarCliente()

    def eliminarCliente(self):   # ELIMINAR CLIENTE 
        limpioPantalla()
        print("\x1b[0;32m"+"================================================================================")
        print("                              ELIMINAR CLIENTE            ")
        print("================================================================================\n")
        self.documento=self.validar.validarIngresoDocumento()
        self.validar.validarExistenciaDocumentoC()
        print("\n================================================================================\n\n")

        mycursor = mydb.cursor()
        sql = "DELETE FROM clientes WHERE dni LIKE '%"+str(self.documento)+"%'"
        mycursor.execute(sql)
        mydb.commit()
        
        if mycursor.rowcount > 0:
            print("\x1b[0;32m"+"\n================================================================================")
            print("> EL CLIENTE CON DNI ", str(self.documento) ," SE ELIMINO CORRECTAMENTE.")
            print("================================================================================\n\n")

        else:
            print("\x1b[0;32m"+"\n================================================================================")
            print("> NO SE PUDO ELIMINAR EL CLIENTE.")
            print("================================================================================\n\n")

        time.sleep(3)
#-------------------------------------------------------------------------------------------------------------------------- 

class Articulos:   #---------------------------------- S E C C I O N   A R T I C U L O S ----------------------------------
    def __init__(self):   # MOSTRAR MENU ARTICULOS
        self.validar= Validaciones()
        limpioPantalla()
        print("\x1b[0;36m"+"================================================================================")
        print("                                 MENU ARTICULOS                                 ")
        print("================================================================================")
        print("         ===========================        ===========================             ")
        print("         |     1. ALTA ARTICULO    |        |  2. MODIFICAR ARTICULO  |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |   3. ELIMINAR ARTICULO  |        |  4. ARTICULOS SIN STOCK |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================              ")
        print("         |    5. LISTA ARTICULOS   |        |    6. INGRESO REMITO    |              ")
        print("         ===========================        ===========================              ")
        print("                           ===========================              ")
        print("                           |        7. ATRAS         |              ")
        print("                           ===========================              ")
        print("\n================================================================================")
        
        self.opcion= input("> ELEGIR OPCION: ")
        print("\n================================================================================")

        if self.opcion == "1":
            self.altaArticulo()

        elif self.opcion == "2":
            self.modificarArticulo()

        elif self.opcion == "3":
            self.eliminarArticulo()

        elif self.opcion == "4":
            limpioPantalla()
            self.articulosSinStock()

        elif self.opcion == "5":
            limpioPantalla()
            self.articulosRegistrados()
            
        elif self.opcion == "6":
            self.ingresarRemito() 
        
        elif self.opcion == "7":
            return 

        else:
            print("> OPCION INCORRECTA, POR FAVOR INTENTE DE NUEVO.")
            print("================================================================================")
            time.sleep(3)
            Articulos()

    def articulosSinStock(self):   # MOSTRAR ARTICULOS DISPONIBLES 
        print("\x1b[0;36m"+"================================================================================")
        print("                                    S T O C K           ")
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos")

        for ind in mycursor:
            if int(ind[4])==0:
                print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("================================================================================\n")
        print("================================================================================")
        print("> PRESIONE ENTER PARA VOLVER")
        print("================================================================================")
        input("> ")
        Articulos()

    def articulosRegistrados(self):
        print("\x1b[0;36m"+"================================================================================")
        print("                    A R T I C U L O S   R E G I S T R A D O S           ")
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos")

        for ind in mycursor:
            print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("================================================================================\n")
        print("================================================================================")
        print("> PRESIONE ENTER PARA VOLVER")
        print("================================================================================")
        input("> ")
        Articulos()

    def ingresarRemito(self):   # INGRESAR REMITO
        self.codigo=self.validar.validarIngresoCodigoVenta()
        continuar=self.validar.validarExistenciaPedido()
        if continuar == True:
            self.pedidoArt=[]
            self.pedidoCant=[]

            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM pedidosrealizados where numeroPedido LIKE '%"+str(self.codigo)+"%'")    
            myresultado = mycursor.fetchall()

            for ind in myresultado:
                self.pedidoArt.append(ind[2])
                self.pedidoCant.append(ind[4])

            for codigoarticulo in self.pedidoArt:
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM articulos WHERE codigo LIKE '%"+str(codigoarticulo)+"%'")
                
                for ind in mycursor:
                    self.stock= ind[4] + int(self.pedidoCant[0])
                
                mycursor = mydb.cursor()
                sql = "UPDATE articulos SET stock = '"+str(self.stock)+"' WHERE codigo LIKE '%"+str(codigoarticulo)+"%'"
                mycursor.execute(sql)
                mydb.commit()

                mycursor = mydb.cursor()
                sql = "DELETE FROM pedidosrealizados WHERE codigoArt LIKE '%"+str(codigoarticulo)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                self.pedidoCant.pop(0)
            else:
                print("================================================================================")
                print("STOCK ACTUALIZADO.") 
                print("================================================================================\n\n")
        else:
                print("================================================================================")
                print("ERROR.") 
                print("================================================================================\n\n")
        time.sleep(3)
        Articulos()

    def altaArticulo(self):   # REGISTRAR ARTICULO NUEVO
        limpioPantalla()
        print("\x1b[0;36m"+"================================================================================")
        print("                              REGISTRAR ARTICULO                ")
        print("================================================================================\n")
        self.codigo = self.validar.validarIngresoCodigo()
        continuar=self.validar.validarInexistenciaCodigoA()
        if continuar==True:
            self.nombre = input("> NOMBRE: ")
            self.categoria = input("> CATEGORIA: ")
            self.precio = self.validar.verificarPrecio()
            self.stock = self.validar.verificarStock()
            self.proveedor = self.validar.validarIngresoDocumento()
            continuar2=self.validar.validarExistenciaDocumentoP()
            if continuar2 ==True:
            
                mycursor = mydb.cursor()
                sql = "INSERT INTO articulos (codigo, nombre, categoria, precio, stock, dniProveedor) VALUES (%s, %s, %s, %s,%s, %s)"
                val = (str(self.codigo), self.nombre, self.categoria, self.precio, self.stock,self.proveedor)
                mycursor.execute(sql, val)
                mydb.commit()

                if mycursor.rowcount > 0:
                    print("\n================================================================================")
                    print("> EL ARTICULO", str(self.nombre).upper() ,"SE REGISTRO CORRECTAMENTE.")
                    print("================================================================================\n\n")

            elif continuar2==False:
                print("\n================================================================================")
                print("> ERROR AL CARGAR EL ARTICULO.")
                print("================================================================================\n\n")

        time.sleep(3)
        Articulos()

    def modificarArticulo(self):   # MODIFICAR ARTICULO
        limpioPantalla()
        print("\x1b[0;36m"+"================================================================================")
        print("                          QUE DATO VA A MODIFICAR            ")
        print("================================================================================")
        print("         ===========================        ===========================             ")
        print("         |        1. CODIGO        |        |        2. NOMBRE        |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |       3. CATEGORIA      |        |        4. PRECIO        |              ")
        print("         ===========================        ===========================              ")
        print("         ===========================        ===========================             ")
        print("         |         5. STOCK        |        |     6. DNI PROVEEDOR    |             ")
        print("         ===========================        ===========================             ")
        print("         ===========================        ===========================              ")
        print("         |   7. TODOS LOS DATOS    |        |        8. ATRAS         |              ")
        print("         ===========================        ===========================              ")
        print("================================================================================\n")
        opcion = input("> ")
        print("\n================================================================================\n\n")
        limpioPantalla()
        if opcion <"8":
            print("\x1b[0;36m"+ "================================================================================")
            print("                    INGRESE EL CODIGO DEL ARTICULO          ")
            print("================================================================================\n")
            self.codigo= self.validar.validarIngresoCodigo()
            continuar=self.validar.validarExistenciaCodigoA()
            if continuar == True:
                print("\n================================================================================\n\n")
                
                mycursor = mydb.cursor()
                sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()

                if opcion == ("1"):    # 1. MODIFICAR CODIGO DE ARTICULO
                    limpioPantalla()
                    print("\x1b[0;36m"+"================================================================================")
                    print("                        INGRESE EL CODIGO NUEVO             ")
                    print("================================================================================\n")
                    self.codigoNuevo=self.validar.validarIngresoCodigo()
                    continuar2=self.validar.validarInexistenciaCodigoA()
                    if continuar2==True:
                        mycursor = mydb.cursor()
                        sql = "UPDATE articulos SET codigo = '"+str(self.codigoNuevo)+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit()

                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigoNuevo)+"%'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        for ind in myresultado:
                            print("\x1b[0;36m"+"\n================================================================================")
                            print("> EL CODIGO DEL ARTICULO "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                            print("================================================================================\n\n")
                        
                    time.sleep(3)
                    return self.modificarArticulo() 

                elif opcion == ("2"):   # 2. MODIFICAR EL NOMBRE DEL ARTICULO
                    limpioPantalla()
                    print("\x1b[0;36m"+"================================================================================")
                    print("                       INGRESE EL NOMBRE NUEVO         ")
                    print("================================================================================\n")
                    self.nombreNuevo = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE articulos SET nombre = '"+self.nombreNuevo+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\x1b[0;36m"+"\n================================================================================")
                        print("> EL NOMBRE DEL ARTICULO "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarArticulo()
                        
                elif opcion == ("3"):   # 3. MODIFICAR LA CATEGORIA
                    limpioPantalla()
                    print("\x1b[0;36m"+"================================================================================")
                    print("                        INGRESE LA CATEGORIA NUEVA         ")
                    print("================================================================================\n")
                    self.categoriaNueva = input("> ")
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE articulos SET categoria = '"+self.categoriaNueva+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\x1b[0;36m"+"\n================================================================================")
                        print("> LA CATEGORIA DEL ARTICULO "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarArticulo()

                elif opcion == ("4"):   # 4. MODIFICAR PRECIO
                    limpioPantalla()
                    print("\x1b[0;36m"+"================================================================================")
                    print("                         INGRESE EL PRECIO NUEVO           ")
                    print("================================================================================\n")
                    self.precioNuevo = self.validar.verificarPrecio()
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE articulos SET precio = '"+str(self.precioNuevo)+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\x1b[0;36m"+"\n================================================================================")
                        print("> EL PRECIO DEL ARTICULO "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    
                    time.sleep(3)
                    return self.modificarArticulo()

                elif opcion == ("5"):   # 5. MODIFICAR STOCK
                    limpioPantalla()
                    print("\x1b[0;36m"+"================================================================================")
                    print("                            INGRESE EL STOCK          ")
                    print("================================================================================\n")
                    self.stockNuevo = self.validar.verificarStock()
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE articulos SET stock = '"+str(self.stockNuevo)+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print("\n================================================================================")
                        print("> EL STOCK DE "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                        print("================================================================================\n\n")
                    time.sleep(3)
                    return self.modificarArticulo()

                elif opcion == ("6"):   # 6.  MODIFICAR DNI DEL PROVEEDOR DEL ARTICULO
                    limpioPantalla()
                    print("\x1b[0;36m"+"================================================================================")
                    print("                    INGRESE EL DNI DEL PROVEEDOR NUEVO          ")
                    print("================================================================================\n")
                    self.proveedorNuevo = self.validar.validarIngresoDocumento()
                    continuar=self.validar.validarExistenciaDocumentoP()
                    if continuar==True:
                        mycursor = mydb.cursor()
                        sql = "UPDATE articulos SET dniProveedor = '"+str(self.proveedorNuevo)+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        mydb.commit()

                        sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        for ind in myresultado:
                            print("\x1b[0;36m"+"\n================================================================================")
                            print("> EL DNI DEL PROVEEDOR DEL ARTICULO "+ str(ind[1]).upper() + " SE MODIFICO CORRECTAMENTE.")
                            print("================================================================================\n\n")
                            time.sleep(3)
                    else:
                        print("\n================================================================================")
                        print("> NO PUDO ENCONTRARSE EL PROVEEDOR, PRIMERO DEBERA REGISTRARLO.")
                        print("================================================================================\n\n")
                        time.sleep(3)
                        return self.modificarArticulo()

                elif opcion == ("7"):   # 7. MODIFICAR TODOS LOS DATOS DEL ARTICULO
                    limpioPantalla()
                    
                    print("================================================================================")
                    print("                             MODIFICAR ARTICULO                 ")
                    print("================================================================================\n")
                    self.codigoviejo=self.codigo
                    self.codigo = self.validar.validarIngresoCodigo()
                    continuar=self.validar.validarInexistenciaCodigoA()
                    if continuar==True:

                        self.nombre = input("> NOMBRE: ")
                        self.categoria = input("> CATEGORIA: ")
                        self.precio = self.validar.verificarPrecio()
                        self.stock = self.validar.verificarStock()
                        self.proveedor = self.validar.validarIngresoDocumento()
                        continuar2=self.validar.validarExistenciaDocumentoP()
                    
                        if continuar2==True:
                            mycursor = mydb.cursor()
                            sql = "INSERT INTO articulos (codigo, nombre, categoria, precio, stock, dniProveedor) VALUES (%s, %s, %s, %s,%s, %s)"
                            val = (str(self.codigo), self.nombre, self.categoria, self.precio, self.stock,self.proveedor)
                            mycursor.execute(sql, val)
                            mydb.commit()

                            mycursor = mydb.cursor()
                            sql = "DELETE FROM articulos WHERE codigo LIKE '%"+str(self.codigoviejo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit()

                            if mycursor.rowcount > 0:
                                print("\x1b[0;36m"+"\n================================================================================")
                                print("> EL ARTICULO", (self.nombre).upper() ,"SE REGISTRO CORRECTAMENTE.")
                                print("================================================================================\n\n")
                                time.sleep(3)
                            else:
                                print("\n================================================================================")
                                print("ERROR AL CARGAR EL ARTICULO.")
                                print("================================================================================\n\n")
                                time.sleep(3)
                        else:
                                print("\n================================================================================")
                                print("ERROR AL CARGAR EL ARTICULO.")
                                print("================================================================================\n\n")
                                time.sleep(3)
                    else:
                        print("\n================================================================================")
                        print("> NO PUDO ENCONTRARSE EL ARTICULO, PRIMERO DEBERA REGISTRARLO.")
                        print("================================================================================\n\n")
                        time.sleep(3)
                        return self.modificarArticulo()

        elif opcion == ("8"):   # 8. ATRAS
            Articulos()

        else:                   # SE INGRESARON MAL LOS DATOS
            print("\x1b[0;36m"+"================================================================================")
            print("> ERROR, OPCION INVALIDA.")
            print("================================================================================\n\n")
            return self.modificarArticulo()

    def eliminarArticulo(self):  # ELIMINAR ARTICULO
        limpioPantalla()
        print("\x1b[0;36m"+"================================================================================")
        print("                               ELIMINAR ARTICULO           ")
        print("================================================================================\n")
        self.codigo=self.validar.validarIngresoCodigo()
        self.validar.validarExistenciaCodigoA()
        print("\n================================================================================\n\n")

        mycursor = mydb.cursor()
        sql = "DELETE FROM articulos WHERE codigo LIKE '%"+str(self.codigo)+"%'"
        mycursor.execute(sql)
        mydb.commit()
        
        if mycursor.rowcount > 0:
            print("\x1b[0;36m"+"\n================================================================================")
            print("> EL ARTICULO CON CODIGO ", self.codigo ,"SE ELIMINO CORRECTAMENTE.")
            print("================================================================================\n\n")

        else:
            print("\x1b[0;36m"+"\n================================================================================")
            print("> ERROR AL ELIMINAR EL ARTICULO.")
            print("================================================================================\n\n")

        time.sleep(3)
        Articulos()
#--------------------------------------------------------------------------------------------------------------------------

class Ventas(Articulos):   #---------------------------------- S E C C I O N   V E N T A S --------------------------------
    def __init__(self):   # MOSTRAR MENU VENTAS
        self.fecha= datetime.datetime.now()
        self.codigoFecha=int(self.fecha.strftime("%d%m%Y%H%M%S"))
        self.validar= Validaciones()

    def carrito(self):   # MOSTRAR CARRITO
        self.total=0

        #------------------------------------  C A R R I T O  --------------------------------------------------------
        print("\x1b[0;31m"+"================================================================================")
        print("               N U M E R O   D E   C O M P R A: "+str(self.codigoFecha))
        print("================================================================================")
        print("{0:^16}{1:^8}{2:^30}{3:^5} {4:^8} {5:^8}".format("COMPRA NUMERO","CODIGO","PRODUCTO","CANTIDAD","PRECIO", "TOTAL"))  
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM compra where codigoVenta LIKE'%"+str(self.codigoFecha)+"%'")
        for ind in mycursor:
            self.total=self.total + ind[5]
            print("{0:^16}{1:^8}{2:^30}{3:^7}  {4:^8} {5:^8}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind [5]))
        print("\n================================================================================")
        print("TOTAL: $ "+str(self.total))
        print("================================================================================")
        
    def articulosStock(self):   # MOSTRAR ARTICULOS DISPONIBLES 
        print("\x1b[0;36m"+"================================================================================")
        print("                                    S T O C K           ")
        print("================================================================================\n")
        print("{0:^10} {1:^29} {2:^15} {3:^5} {4:^5} {5:^10}".format("CÓDIGO","ARTICULO","CATEGORIA","PRECIO","STOCK","PROVEEDOR")) 
        print("================================================================================\n")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM articulos")

        for ind in mycursor:
            if int(ind[4])>0:
                print ("{0:^10} {1:^30} {2:^15} {3:^5} {4:^5} {5:^10}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind[5]))
        print("================================================================================\n")

    def opcionesCompra(self):
        limpioPantalla()
        print("\x1b[0;31m"+"================================================================================")
        print("                    E M I T I R   F A C T U R A   P A R A        ")
        print("================================================================================\n")
        print("                 ==========================================")
        print("                 |           1. CONSUMIDOR FINAL          |")       
        print("                 ==========================================")
        print("                 ==========================================")
        print("                 |          2. CLIENTE REGISTRADO         |")
        print("                 ==========================================")
        print("                 ==========================================")
        print("                 |           3. REGISTRAR CLIENTE         |")
        print("                 ==========================================")
        print("                 ==========================================")
        print("                 |                 4. ATRAS               |")
        print("                 ==========================================")
        print("\n================================================================================")
        self.opcion= input("> ")

        if self.opcion == "1":
            self.tipoCliente=99999999
            return self.compra(self.tipoCliente)

        if self.opcion == "2":
            self.tipoCliente=self.validar.validarIngresoDocumento()
            continuar=self.validar.validarExistenciaDocumentoC()
            if continuar ==True:
                return self.compra(self.tipoCliente)
            else:
                print("")
                return 


        elif self.opcion == "3":
            return

        elif self.opcion == "4":
            return 

    def compra(self,cliente):   # REALIZA UNA COMPRA        
        limpioPantalla()
        self.tipoCliente=cliente
        comprar =True
        while comprar == True:
            limpioPantalla()
            self.articulosStock()  ### MUESTRO STOCK DISPONIBLE. PIDO CODIGO Y CANTIDAD ⬇
            self.carrito()
            print("================================================================================")
            print("                 ==========================================")
            print("                 |           1. AÑADIR ARTICULOS          |")       
            print("                 ==========================================")
            print("                 ==========================================")
            print("                 |           2. QUITAR ARTICULOS          |")
            print("                 ==========================================")
            print("                 ==========================================")
            print("                 |           3. FINALIZAR COMPRA          |")
            print("                 ==========================================")
            print("                 ==========================================")
            print("                 |           4. CANCELAR COMPRA           |")
            print("                 ==========================================")
            print("================================================================================")
            self.opcion= input("> ")
            print("================================================================================")
            
            if self.opcion == "1":
                self.codigo= self.validar.validarIngresoCodigo()
                continuar= self.validar.validarExistenciaCodigoA()
                if continuar== True:
                    continuar2= self.validar.validarExistenciaCodigoCompra()
                    if continuar2 == True:
                        self.cantidad= self.validar.validarCantidad()
                        print("================================================================================")
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()

                        for ind in myresultado:
                            if int(self.cantidad) > 0 and int(self.cantidad) <= int(ind[4]):
                                self.resta=int(ind[4])-int(self.cantidad)
                                sql = "UPDATE articulos SET stock = '"+str(self.resta)+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                                mycursor.execute(sql)
                                mydb.commit()                    ### REEMPLAZO EL STOCK EN LA TABLA ARTICULOS ^
                            elif int(self.cantidad) > int(ind[4]):
                                print("================================================================================")
                                print("> NO HAY SUFICIENTE STOCK DISPONIBLE, EL STOCK DISPONIBLE ES DE: "+ str(ind[4]))
                                print("================================================================================\n\n") 
                                time.sleep(3)
                                return self.compra(self.tipoCliente)   
                        
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM compra WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        for ind in myresultado:
                            self.cantidadNueva=int(ind[3])+int(self.cantidad)
                            self.totalNuevo= int(ind[4])*int(self.cantidadNueva)

                            sql = "UPDATE compra SET cantidad = '"+str(self.cantidadNueva)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit() 

                            sql = "UPDATE compra SET precioT = '"+str(self.totalNuevo)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit() 
                            return self.compra(self.tipoCliente)
                            
                    elif continuar2 == False:
                        self.cantidad= self.validar.validarCantidad()
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()

                        for ind in myresultado:
                            if int(self.cantidad) > 0 and int(self.cantidad) <= int(ind[4]): ### FILTRO QUE SEA MAYOR A 0 Y SI HAY ESA CANTIDAD EN STOCK
                                self.resta=int(ind[4])-int(self.cantidad) ### RESTO LA CANTIDAD A COMPRAR DEL STOCK
                                self.codigoArt = ind[0]
                                self.producto = ind[1]
                                self.precioU = ind[3]
                                self.precioT = int(self.cantidad) * self.precioU

                                sql = "UPDATE articulos SET stock = '"+str(self.resta)+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                                mycursor.execute(sql)
                                mydb.commit()                    ### REEMPLAZO EL STOCK EN LA TABLA ARTICULOS ^

                                mycursor = mydb.cursor()
                                sql = "INSERT INTO compra (codigoVenta, codigoArt, producto, cantidad, precioU, precioT) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (str(self.codigoFecha), self.codigoArt, self.producto, self.cantidad, self.precioU, self.precioT)
                                mycursor.execute(sql, val)
                                mydb.commit()                    ### COPIO LOS DATOS EN LA TABLA VENTAS ^
                            elif int(self.cantidad) > int(ind[4]):
                                print("================================================================================")
                                print("> NO HAY SUFICIENTE STOCK DISPONIBLE, EL STOCK DISPONIBLE ES DE: "+ str(ind[4]))
                                print("================================================================================\n\n")
                                time.sleep(3)
                        return self.compra(self.tipoCliente)
                return self.compra(self.tipoCliente)

            elif self.opcion == "2":
                print("================================================================================")
                print("                            ELIMINAR ARTICULO           ")
                print("================================================================================")
                self.codigo= self.validar.validarIngresoCodigo()
                continuar=self.validar.validarExistenciaCodigoA()
                if continuar== True:
                    continuar3= self.validar.validarExistenciaCodigoCompra()
                    if continuar3 == True:
                        self.cantidad= self.validar.validarCantidad()
                            
                        mycursor = mydb.cursor()
                        mycursor.execute("SELECT * FROM compra WHERE codigoArt LIKE '%"+str(self.codigo)+"%'")
                        
                        for ind in mycursor:
                            cantidadtotal= int(ind[3])
                            preciounidad= int(ind[4])
                            preciototal= int(ind[5]) - (preciounidad * int(self.cantidad))


                        if self.cantidad < cantidadtotal:
                            self.cantidadComprar= cantidadtotal-self.cantidad
                            self.total=self.total-(preciounidad * int(self.cantidad))
                            mycursor = mydb.cursor()
                            sql = "UPDATE compra SET cantidad = '"+str(self.cantidadComprar)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit()
                            mycursor = mydb.cursor()
                            sql = "UPDATE compra SET precioT = '"+str(preciototal)+"' WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit()
                            mycursor = mydb.cursor()
                            mycursor.execute("SELECT * FROM articulos WHERE codigo LIKE '%"+str(self.codigo)+"%'")
                            
                            for ind in mycursor:
                                self.stock= int(ind[4])+int(self.cantidad)
                                
                            mycursor = mydb.cursor()
                            sql = "UPDATE articulos SET stock = '"+str(self.stock)+"' WHERE codigo LIKE '%"+str(self.codigo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit()


                        elif self.cantidad == cantidadtotal:
                            self.total=self.total-preciototal
                            mycursor = mydb.cursor()
                            sql = "DELETE FROM compra WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit()
                        
                            mycursor = mydb.cursor()
                            sql = "DELETE FROM compra WHERE codigoArt LIKE '%"+str(self.codigo)+"%'"
                            mycursor.execute(sql)
                            mydb.commit()
                            
                            print("\n================================================================================")
                            print("> ",mycursor.rowcount, " ARTICULO ELIMINADO.")
                            print("================================================================================\n\n")
                            comprar = True
                        else:
                            print("\n================================================================================")
                            print("> LA CANTIDAD INGRESADA ES MAYOR A LA QUE FIGURA EN EL CARRITO.")
                            print("================================================================================\n\n")
                            time.sleep(3)

                        return self.compra(self.tipoCliente)

                    elif continuar3 == False:
                        print("\n================================================================================")
                        print("> EL ARTICULO NO SE ENCUENTRA EN EL CARRITO.")
                        print("================================================================================\n\n")
                        time.sleep(3)
                        return self.compra(self.tipoCliente)

            elif self.opcion == "3":

                mycursor = mydb.cursor()
                sql = "SELECT * FROM compra"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()

                for ind in myresultado:
                    self.dato0= ind[0]   
                    self.dato1= ind[1] 
                    self.dato2= ind[2] 
                    self.dato3= ind[3] 
                    self.dato4= ind[4] 
                    self.dato5= ind[5] 

                    mycursor2 = mydb.cursor()
                    sql2 = "INSERT INTO facturacion (codigoVenta, codigoArt, producto, cantidad, precioU, precioT) VALUES (%s, %s, %s, %s, %s, %s)"
                    val2 = (self.dato0, self.dato1, self.dato2, self.dato3, self.dato4, self.dato5)
                    mycursor2.execute(sql2, val2)

                mycursor = mydb.cursor()
                sql = "DELETE FROM compra WHERE codigoVenta LIKE '%"+str(self.codigoFecha)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                return self.facturacion()

            elif self.opcion == "4":
                self.compraArt=[]
                self.compraCant=[]
                
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM compra")
                for ind in mycursor:
                    self.compraArt.append(ind[1])
                    self.compraCant.append(ind[3])

                for codigoarticulo in self.compraArt:
                    mycursor = mydb.cursor()
                    mycursor.execute("SELECT * FROM articulos WHERE codigo LIKE '%"+str(codigoarticulo)+"%'")
                    
                    for ind in mycursor:
                        self.stock= ind[4] + int(self.compraCant[0])
                    
                    mycursor = mydb.cursor()
                    sql = "UPDATE articulos SET stock = '"+str(self.stock)+"' WHERE codigo LIKE '%"+str(codigoarticulo)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()

                    mycursor = mydb.cursor()
                    sql = "DELETE FROM compra WHERE codigoArt LIKE '%"+str(codigoarticulo)+"%'"
                    mycursor.execute(sql)
                    mydb.commit()
                    self.compraCant.pop(0)
                else:
                    print("================================================================================")
                    print("COMPRA CANCELADA CON EXITO.") 
                    print("================================================================================\n\n")
                time.sleep(3)
                return
                    
            
            else: 
                print("================================================================================")
                print("> OPCION INCORRECTA")
                print("================================================================================\n\n")
                time.sleep(3)
                return self.compra(self.tipoCliente)

    def facturacion(self):   # EMITE UNA FACTURA CON LOS DATOS DEL LOCAL, CLIENTE, Y PRODUCTOS COMPRADOS. ###
        self.totalfactura=0
        print("\x1b[0;31m"+"================================================================================")
        print("                                F A C T U R A  ")
        print("================================================================================\n")
        print("KIOSCO")
        print("NUMERO DE COMPRA: "+str(self.codigoFecha))
        print("FECHA Y HORA: "+str(self.fecha.strftime("%d/%m/%Y/ %H:%M:%S")))
        print("DNI CLIENTE: "+str(self.tipoCliente))
        print("\n================================================================================")
        print("{0:^16}{1:^8}{2:^30}{3:^5} {4:^8} {5:^8}".format("COMPRA NUMERO","CODIGO","PRODUCTO","CANTIDAD","PRECIO", "TOTAL"))  
        print("================================================================================\n")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM facturacion where codigoVenta LIKE'%"+str(self.codigoFecha)+"%'")
        for ind in mycursor:
            self.totalfactura= self.totalfactura + ind[5]
            print("{0:^16}{1:^8}{2:^30}{3:^7}  {4:^8} {5:^8}".format(ind[0] , ind[1] , ind[2], ind[3], ind[4], ind [5]))
        print("================================================================================\n")
        print("\n================================================================================")
        print("TOTAL: "+str(self.totalfactura))
        print("================================================================================")

        mycursor = mydb.cursor()
        sql = "INSERT INTO ventas (codigoVenta, dniCliente, total) VALUES (%s, %s, %s)"
        val = (str(self.codigoFecha), str(self.tipoCliente), str(self.totalfactura))
        mycursor.execute(sql, val)
        mydb.commit()  
        time.sleep(10)
        limpioPantalla() 
        
    def listaVentas(self):   # MUESTA EL HISTORIAL DE VENTAS
        limpioPantalla()
        print("\x1b[0;31m"+"================================================================================")
        print("                                 V E N T A S                                    ")
        print("================================================================================\n")
        print("                 ==========================================")
        print("                 |      1. MOSTRAR TODAS LAS VENTAS       |")       
        print("                 ==========================================")
        print("                 ==========================================")
        print("                 |     2. BUSCAR POR NUMERO DE COMPRA     |")
        print("                 ==========================================")
        print("                 ==========================================")
        print("                 |      3. BUSCAR POR DNI DE CLIENTE      |")
        print("                 ==========================================")
        print("                 ==========================================")
        print("                 |                4. ATRAS                |")
        print("                 ==========================================")
        print("================================================================================")
        self.opcion=input("> ")
        repet= True
        while repet == True:
            if self.opcion == "1":
                limpioPantalla()
                self.total=0
                print("\x1b[0;31m"+"================================================================================")
                print("                                 V E N T A S                                    ")
                print("================================================================================\n")
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM ventas")    
                myresultado = mycursor.fetchall()
                print("================================================================================\n")
                print("{0:^15}{1:^15}{2:^15}".format("CODIGO VENTA","DNI CLIENTE","TOTAL"))  
                print("================================================================================\n")
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM ventas")
                for ind in mycursor:
                    self.total= self.total + ind[2]
                    print("{0:^15} {1:^15} {2:^15}".format(ind[0] , ind[1] , ind[2]))
                print("\n================================================================================")
                print("TOTAL RECAUDADO: "+str(self.total))
                print("================================================================================")
                print(" > PRESIONE ENTER PARA VOLVER.")
                input(" > ")
                return self.listaVentas()  
                
            elif self.opcion == "2":
                self.total=0
                limpioPantalla()
                print("\x1b[0;31m"+"================================================================================")
                print("                                 V E N T A S                                    ")
                print("================================================================================\n")
                self.codigoCompra= self.validar.validarExistenciaPedido()
                print("================================================================================\n")
                if self.codigoCompra==True:
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM ventas where codigoVenta = '"+self.codigoCompra+"' "
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    print("================================================================================\n")
                    print("{0:^15}{1:^15}{2:^15}".format("CODIGO VENTA","DNI CLIENTE","TOTAL"))  
                    print("================================================================================\n")
                    for ind in myresultado:
                        self.total= self.total + ind[2]
                        print("{0:^15} {1:^15} {2:^15}".format(ind[0] , ind[1] , ind[2]))
                    print("\n================================================================================")
                    print(" > PRESIONE ENTER PARA VOLVER.")
                    input(" > ")
                    return self.listaVentas()  
                else:
                    print("\n================================================================================")
                    print(" > NO SE ENCONTRO LA COMPRA.")
                    print("\n================================================================================")
                    time.sleep(3)
                    return self.listaVentas()  


            elif self.opcion == "3":
                limpioPantalla()
                print("\x1b[0;31m"+"================================================================================")
                print("                                 V E N T A S                                    ")
                print("================================================================================\n")
                self.documento= self.validar.validarIngresoDocumento()
                continuar= self.validar.validarExistenciaDocumentoC()
                if continuar==True:
                    mycursor = mydb.cursor()
                    sql = "SELECT * FROM ventas where dniCliente = '"+self.documento+"' "
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    print("================================================================================\n")
                    print("{0:^15}{1:^15}{2:^15}".format("CODIGO VENTA","DNI CLIENTE","TOTAL"))  
                    print("================================================================================\n")
                    for ind in myresultado:
                        self.total= self.total + ind[2]
                        print("{0:^15} {1:^15} {2:^15}".format(ind[0] , ind[1] , ind[2]))
                    print("\n================================================================================")
                    print(" > PRESIONE ENTER PARA VOLVER.")
                    input(" > ")
                    return self.listaVentas() 


            elif self.opcion == "4":
                return

            else:
                print("> OPCION INCORRECTA, VUELVA A INTENTAR.")
                print("================================================================================\n")
                time.sleep(3)
                return self.listaVentas()          
#--------------------------------------------------------------------------------------------------------------------------

class Validaciones:   #---------------------------------- S E C C I O N   V A L I D A C I O N E S -------------------------
#   VALIDACIONES DOCUMENTO / TELEFONO / CORREO ------------------------------------  
    def validarIngresoDocumento(self):
        self.documento  = input("> DNI: ")
        while True:
            try:
                self.documento = int(self.documento) 
                longitud = (len(str(self.documento)))
                if longitud <= 8 and longitud >= 7 :
                    return str(self.documento)
                else:
                    print("\n================================================================================")
                    print("> DNI INCORRECTO, INGRESE 7 U 8 NUMEROS.")
                    print("================================================================================\n")
                    return self.validarIngresoDocumento()
            except ValueError:
                print("\n================================================================================")
                print("> DNI INCORRECTO, INGRESE SOLO NUMEROS.") 
                print("================================================================================\n")
                return self.validarIngresoDocumento()

    def verificarCorreo(self):
        self.mail=input("> MAIL: ")
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        self.esmail= re.match(expresion_regular, self.mail)
        if self.esmail == None:
            print("\n================================================================================")
            print("> MAIL INCORRECTO.") 
            print("================================================================================\n")
            return self.verificarCorreo()
        else:
            return self.mail

    def verificarTelefono(self):
        self.telefono  = input("> TELEFONO: ")
        while True:
            try:
                self.telefono = int(self.telefono)
                return self.telefono
            except ValueError:
                print("\n================================================================================")
                print("> TELEFONO INCORRECTO, INGRESE SOLO NUMEROS.") 
                print("================================================================================\n")
                return self.verificarTelefono()
    
    def verificarPrecio(self):
        self.num  = input("> PRECIO: ")
        while True:
            try:
                self.num = int(self.num)
                return self.num
            except ValueError:
                print("\n================================================================================")
                print("> INGRESE SOLO NUMEROS.") 
                print("================================================================================\n")
                return self.verificarPrecio()

    def verificarStock(self):
        self.num  = input("> STOCK: ")
        while True:
            try:
                self.num = int(self.num)
                return self.num
            except ValueError:
                print("\n================================================================================")
                print("> INGRESE SOLO NUMEROS.") 
                print("================================================================================\n")
                return self.verificarStock()

    def validarCantidad(self):
        self.cantidad  = input("> CANTIDAD: ")
        while True:
            try:
                self.cantidad = int(self.cantidad)
                return self.cantidad
            except ValueError:
                print("\n================================================================================")
                print("> CANTIDAD INCORRECTA, INGRESE SOLO NUMEROS.") 
                print("================================================================================\n")
                return self.validarCantidad()
#----------------------------------------------------------------------------------
#   VALIDACIONES CODIGO -----------------------------------------------------------  
    def validarIngresoCodigo(self):
        self.codigo  = input("> CODIGO: ")
        while True:
            try:
                self.codigo = int(self.codigo) 
                longitud = (len(str(self.codigo)))
                if longitud == 8:
                    return str(self.codigo)
                else:
                    print("\n================================================================================")
                    print("> CODIGO INCORRECTO, INGRESE 8 NUMEROS.")
                    print("================================================================================\n")
                    return self.validarIngresoCodigo()
            except ValueError:
                print("\n================================================================================")
                print("> CODIGO INCORRECTO, INGRESE SOLO NUMEROS.") 
                print("================================================================================\n")
                return self.validarIngresoCodigo()

    def validarIngresoCodigoVenta(self):
        self.codigo  = input("> CODIGO: ")
        while True:
            try:
                self.codigo = int(self.codigo) 
                longitud = (len(str(self.codigo)))
                if longitud == 14:
                    return str(self.codigo)
                else:
                    print("\n================================================================================")
                    print("> CODIGO INCORRECTO, INGRESE 14 NUMEROS.")
                    print("================================================================================\n")
                    return self.validarIngresoCodigoVenta()
            except ValueError:
                print("\n================================================================================")
                print("> CODIGO INCORRECTO, INGRESE SOLO NUMEROS.") 
                print("================================================================================\n")
                return self.validarIngresoCodigoVenta()
#----------------------------------------------------------------------------------
#   VALIDACIONES CODIGO ARTICULOS -------------------------------------------------
    def validarInexistenciaCodigoA(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.codigo) == ind[0]:
                print("\n================================================================================")
                print("> EL ARTICULO YA EXISTE.")
                print("================================================================================\n\n")
                time.sleep(3)
                limpioPantalla()
                return False
        else:
            return True
               
    def validarExistenciaCodigoA(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM articulos where codigo LIKE '%"+str(self.codigo)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.codigo) == ind[0]:
                return True
        else:
            print("\n================================================================================")
            print("> EL ARTICULO NO EXISTE.")
            print("================================================================================\n\n")
            time.sleep(3)
            limpioPantalla()
            return False

    def validarExistenciaCodigoCompra(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM compra where codigoArt LIKE '%"+str(self.codigo)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.codigo) == ind[1]:
                return True
        else:
            return False

    def validarExistenciaCodigoPedido(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM pedido where codigoArt LIKE '%"+str(self.codigo)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.codigo) == ind[2]:
                return True
        else:
            return False
    
    def validarExistenciaPedido(self):
        print(self.codigo)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM pedidosrealizados where numeroPedido LIKE '%"+str(self.codigo)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.codigo) == ind[0]:
                return True
        else:
            return False

#----------------------------------------------------------------------------------
#   VALIDACIONES DOCUMENTO PROVEEDORES --------------------------------------------  
    def validarInexistenciaDocumentoP(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.documento) == ind[0]:
                print("\n================================================================================")
                print("> EL PROVEEDOR YA EXISTE.")
                print("================================================================================\n\n")
                
                time.sleep(3)
                limpioPantalla()
                return False
        else:
            return True
                
    def validarExistenciaDocumentoP(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM proveedores where dni LIKE '%"+str(self.documento)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.documento) == ind[0]:
                return True
        else:
            print("\n================================================================================")
            print("> EL PROVEEDOR NO EXISTE.")
            print("================================================================================\n\n")
            time.sleep(3)
            return  False
#----------------------------------------------------------------------------------
#   VALIDACIONES DOCUMENTO CLIENTES -----------------------------------------------  
    def validarInexistenciaDocumentoC(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.documento) == ind[0]:
                print("\n================================================================================")
                print("> EL CLIENTE YA EXISTE")
                print("================================================================================\n\n")
                time.sleep(3)
                return False
        else:
            return True
                
    def validarExistenciaDocumentoC(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM clientes where dni LIKE '%"+str(self.documento)+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()

        for ind in myresultado:
            if int(self.documento) == ind[0]:
                return True
        else:
            print("\n================================================================================")
            print("> EL CLIENTE NO EXISTE")
            print("================================================================================\n\n")
            time.sleep(3)
            return False
#--------------------------------------------------------------------------------------------------------------------------



#------------------------------------ I N I C I O -------------------------------------#

menu=Inicio()

#--------------------------------------------------------------------------------------#
#--------------------------------------- BASE DE DATOS --------------------------------#
"""
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE kiosco")
"""
#--------------------------------------------------------------------------------------#
#-------------------------------------- TABLA PROVEEDORES -----------------------------#
"""mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE proveedores (dni INT PRIMARY KEY, nombre VARCHAR(255), direccion VARCHAR(255), telefono INT, mail VARCHAR(255), situacionIva VARCHAR(255))")

#-------------------------------------------------------------------------------------#
#-------------------------------------- TABLA CLIENTES -------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE clientes (dni INT PRIMARY KEY, apellidoNombre VARCHAR(255), direccion VARCHAR(255), telefono INT, mail VARCHAR(255), situacionIva VARCHAR(255))")

#-------------------------------------------------------------------------------------#
#-------------------------------------- TABLA ARTICULOS ------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE articulos (codigo INT PRIMARY KEY, nombre VARCHAR(255), categoria VARCHAR(255), precio INT, stock INT, dniProveedor INT)")

#------------------------------------------------------------------------------------#
#-------------------------------------- TABLA FACTURACION --------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE facturacion (codigoVenta BIGINT, codigoArt INT, producto VARCHAR(255), cantidad INT, precioU INT, precioT INT)")

#------------------------------------------------------------------------------------#
#-------------------------------------- TABLA COMPRA --------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE compra (codigoVenta BIGINT, codigoArt INT, producto VARCHAR(255), cantidad INT, precioU INT, precioT INT)")

#------------------------------------------------------------------------------------#
#---------------------------------- TABLA DEVOLUCION --------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE devoluciones (fecha BIGINT, codigoArt INT, nombreArt VARCHAR(255), cantidad INT, motivo VARCHAR(255))")

#------------------------------------------------------------------------------------#
#-------------------------------------- TABLA VENTAS --------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE ventas (codigoVenta BIGINT PRIMARY KEY, dniCliente INT, total INT)")

#------------------------------------------------------------------------------------#
#------------------------------------- TABLA PEDIDOS --------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE pedido (numeroPedido BIGINT, proveedor INT, codigoArt INT, nombreItem VARCHAR(255), cantidadItem INT, precio INT, total INT)")

#------------------------------------------------------------------------------------#
#-------------------------- TABLA PEDIDOS REALIZADOS --------------------------------#
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE pedidosrealizados (numeroPedido BIGINT, proveedor INT, codigoArt INT, nombreItem VARCHAR(255), cantidadItem INT, precio INT, total INT)")
"""
#------------------------------------------------------------------------------------#
#-------------------------------------- LISTA ARTICULOS -----------------------------#
"""mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
sql = "INSERT INTO articulos (codigo, nombre, categoria, precio, stock, dniProveedor) VALUES (%s, %s, %s,%s, %s,%s)"
val = [
    ('86888688','Coca-Cola 500ml','Bebidas','100','20','30567279'),
    ('49242949','Levite Manzana 500ml','Bebidas','100','20','30567279'),
    ('56893654','Levite Naranja 500ml','Bebidas','100','20','30567279'),
    ('54755475','Agua s/g 500ml','Bebidas','100','20','30567279'),
    ('12452587','Oreo','Galletitas','80','20','56214893'),
    ('57558754','Sonrisas','Galletitas','80','20','56214893'),
    ('54578857','Pepitos','Galletitas','80','20','56214893'),
    ('75428545','Aguila 300g','Chocolates','200','20','78445210'),
    ('54552145','Block 1kg','Chocolates','50','20','78445210'),
    ('55455785','Milka 200g','Chocolates','200','20','78445210'),
    ('54753265','Aguila x3','Alfajores','80','20','44807224'),
    ('54724152','Terrabusi x3','Alfajores','80','20','44807224'),
    ('54755996','Oreo x3','Alfajores','80','20','44807224'),
    ('54755485','Milka x3','Alfajores','80','20','44807224'),
    ('54365285','Lays 75g','Snacks','150','20','55786432'),
    ('56985655','Doritos 75g','Snacks','150','20','55786432'),
    ('56755655','Rueditas 50g','Snacks','150','20','55786432'),
    ('56898555','Palitos 50g','Snacks','150','20','55786432'),]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Fueron insertados.")"""
#-----------------------------------------------------------------------------------#
#----------------------------------- LISTA PROVEEDORES -----------------------------#
"""mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database = "kiosco"
)
mycursor = mydb.cursor()
sql = "INSERT INTO proveedores (dni, nombre, direccion, telefono, mail, situacionIva) VALUES (%s, %s, %s,%s, %s,%s)"
val = [
    ('30567279','Proveedor Bebidas','calle falsa 123','1554565326','proveedorbebidas@gmail.com','registrado'),
    ('44807224','Proveedor Alfajores','calle falsa 123','1554565326','proveedoralfajores@gmail.com','registrado'),
    ('55786432','Proveedor Snacks','calle falsa 123','1554565326','proveedorsnacks@gmail.com','registrado'),
    ('56214893','Proveedor Galletitas','calle falsa 123','1554565326','proveedorgalletitas@gmail.com','registrado'),
    ('78445210','Proveedor de Chocolates','calle falsa 123','1554565326','proveedorchocolates@gmail.com','registrado')]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Fueron insertados.")"""
#-----------------------------------------------------------------------------------#



