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

    def actualizar_producto(self, producto):
        self.cursor.execute('''UPDATE api_productos SET
                            nombre = %s,  descripcion = %s, marca = %s,
                            precio = %s, imagen = %s
                            WHERE id = %s''',
                        (producto.nombre, producto.descripcion, producto.marca, producto.precio, producto.imagen
                         ))
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
    print("3. Buscar Producto por Nombre")
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
            print(producto)

    elif opcion == "3":
        id = int(input("Ingrese el Id del producto a buscar: "))
        productos = crud.buscar_producto(id)
        for producto in productos:
            print(producto)

    elif opcion == "4":
        id = int(input("Ingrese la palabra clave de la ley a actualizar: "))
        producto = crud.buscar_producto(id)
        if productos:
            producto_actualizar = producto[0]
            print("Ingrese los nuevos valores (deje en blanco para mantener los valores existentes):")
            nombre = input("Nuevo número de normativa: ")
            descripcion = input("Nueva descripción: ")
            marca = input("Nuevo órgano legislativo: ")
            precio = float(input("Ingrese el nuevo precio: "))
            imagen = input("Nueva Url de la imagen: ")
    

        if nombre:
            producto_actualizar.nombre = nombre
        if descripcion:
            producto_actualizar.descripcion = descripcion
        if marca:
            producto_actualizar.marca = marca
        if precio:
            producto_actualizar.precio = precio
        if imagen:
           producto_actualizar.imagen = imagen
        

        crud.actualizar_producto(producto_actualizar)
        print("Producto actualizado correctamente.")

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
