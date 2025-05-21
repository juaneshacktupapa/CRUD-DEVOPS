a = [
    [100, "Ruperto", 5],
    [200, "Araminta", 35],
    [300, "Pompilio", 50]
]

class ProductoCRUD:
    def __init__(m):
        m.productos = a
    def listar(m):
        if not m.productos:
            print("No hay productos para mostrar.\n")
            return
        for producto in m.productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
        print()

    def buscar_por_codigo(m, id_producto):
        for producto in m.productos:
            if producto[0] == id_producto:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
                return
        print("Producto no encontrado.\n")

    def eliminar(m, id_producto):
        for producto in m.productos:
            if producto[0] == id_producto:
                m.productos.remove(producto)
                print("Producto eliminado.\n")
                return
        print("Producto no encontrado.\n")

    def actualizar(m, id_producto, actualizar_nombre, actualizar_precio):
        for producto in m.productos:
            if producto[0] == id_producto:
                producto[1] = actualizar_nombre
                producto[2] = actualizar_precio
                print("Producto actualizado.\n")
                return
        print("Producto no encontrado.\n")

    def insertar(m, id_producto, nombre, precio):
        # Verificar si el ID ya existe
        for producto in m.productos:
            if producto[0] == id_producto:
                print("El ID ya existe. Intente con otro ID.\n")
                return        
        m.productos.append([id_producto, nombre, precio])
        print("Producto insertado.\n")

def menu():
    crud = ProductoCRUD()
    while True:
        print("1. Listar productos")
        print("2. Buscar producto por código ID")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Insertar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crud.listar()
        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto: "))
            crud.buscar_por_codigo(id_producto)
        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            crud.eliminar(id_producto)
        elif opcion == "4":
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            actualizar_nombre = input("Ingrese el nuevo nombre: ")
            actualizar_precio = float(input("Ingrese el nuevo precio: "))
            crud.actualizar(id_producto, actualizar_nombre, actualizar_precio)
        elif opcion == "5":
            id_producto = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            crud.insertar(id_producto, nombre, precio)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
