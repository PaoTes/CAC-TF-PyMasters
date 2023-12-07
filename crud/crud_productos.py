import mysql.connector

class Producto:
    def __init__(self,id, nombre, descripcion, marca, precio, imagen):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.precio = precio
        self.imagen = imagen

class CRUDProductos:
    def __init__(self):
        # Modifica las credenciales según tu configuración de MySQL
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='api_db',
            port=3306
        )
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS api_productos(
                                id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                nombre VARCHAR(100) NOT NULL,
                                descripcion VARCHAR(200) NOT NULL,
                                marca VARCHAR(20)NOT NULL,
                                precio FLOAT NOT NULL,
                                imagen VARCHAR(200)
                            )''')
        self.connection.commit()

    def insert_producto(self, producto):
        self.cursor.execute('''INSERT INTO api_productos (
                               nombre, descripcion, marca, precio,imagen
                             ) VALUES (%s, %s, %s, %s, %s)''',
                            (producto.nombre, producto.descripcion, producto.marca, producto.precio, producto.imagen
                            ))
        self.connection.commit()

    def mostrar_productos(self):
        self.cursor.execute('''SELECT * FROM api_productos''')
        return self.cursor.fetchall()

    def buscar_producto(self, id):
        self.cursor.execute('''SELECT * FROM api_productos WHERE id = %s''', (id,))
        return self.cursor.fetchall()

    def actualizar_producto(self, id, nuevos_valores):
        update_query = "UPDATE api_productos SET "
        update_params = []
        for key, value in nuevos_valores.items():
            update_query += f"{key} = %s, "
            update_params.append(value)
        update_query = update_query.rstrip(", ") + " WHERE id = %s"
        update_params.append(id)
        self.cursor.execute(update_query, tuple(update_params))
        self.connection.commit()
        
    def borrar_producto(self, id):
        producto = self.buscar_producto(id)
        if producto:
            self.cursor.execute('''DELETE FROM api_productos WHERE id = %s''', (id,))
            self.connection.commit()


def mostrar_menu():
    print("==== MENÚ ====")
    print("1. Agregar Producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar Producto por Id")
    print("4. Actualizar Producto")
    print("5. Eliminar Producto")
    print("6. Salir")

crud = CRUDProductos()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción: ")
        marca = input("Ingrese la marca ( AMD / INTEL): ")
        precio = float(input("Ingrese el precio del producto: "))
        imagen = input("Ingrese la URL de la imagen: ")
        

        producto = Producto( nombre, descripcion, marca, precio, imagen)
        crud.insert_producto(producto)
        print("Producto agregado correctamente.")

    elif opcion == "2":
        productos = crud.mostrar_productos()
        for producto in productos:
           print("\n")
           
           prod_t= '''Id: {}\nNombre: {}\nDescripcion: {}\nMarca: {}\nUrl Imagen: {}\nPrecio: {}\n'''.format(*producto)
           print(prod_t)
           print("*"*100)
           #print(producto)

    elif opcion == "3":
        id = int(input("Ingrese el Id del producto a buscar: "))
        productos = crud.buscar_producto(id)
        for producto in productos:
            print("\n")
           
            prod_t= '''Id: {}\nNombre: {}\nDescripcion: {}\nMarca: {}\nUrl Imagen: {}\nPrecio: {}\n'''.format(*producto)
            print(prod_t)
            print("*"*100)

    elif opcion == "4":
        id = int(input("Ingrese el Id del Producto a actualizar: "))
        producto = crud.buscar_producto(id)
    
        if producto:
            producto_actualizar = producto[0]
            print("Ingrese los nuevos valores (deje en blanco para mantener los valores existentes):")
            nombre = input("Nuevo Nombre: ")
            descripcion = input("Nueva descripción: ")
            marca = input("Nueva Marca: ")
            precio = float(input("Ingrese el nuevo precio: "))
            imagen = input("Nueva Url de la imagen: ")

            nuevos_valores = {}

            if nombre:
                nuevos_valores['nombre'] = nombre
            if descripcion:
                nuevos_valores['descripcion'] = descripcion
            if marca:
                nuevos_valores['marca'] = marca
            if precio:
                nuevos_valores['precio'] = precio
            if imagen:
                nuevos_valores['imagen'] = imagen

            crud.actualizar_producto(id, nuevos_valores)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    elif opcion == "5":
        id = int(input("Ingrese el ID del producto a eliminar: "))
        if id:
            confirmacion = input(f"¿Está seguro de eliminar el producto con id  '{id}'? (S/N): ")
            if confirmacion.upper() == "S":
                crud.borrar_producto(id)
                print("Producto borrado correctamente.")
            else:
                print("El producto no se eliminó.")

    elif opcion == "6":
        print("Saliendo del sistema: Sesión Finalizada")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
