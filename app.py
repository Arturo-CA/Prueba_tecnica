# Diccionarios iniciales
productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
stock = {1: 50, 2: 45, 3: 30, 4: 15}

def list_products():
    print("========================================")
    print("Lista de Productos:")
    print("========================================")
    for id in productos:
        print(f"{id} \t {productos[id]} \t {precios[id]:.2f} \t {stock[id]}")
    print("========================================")

def get_option(prompt, tipo=int):
    while True:
        try:
            return tipo(input(prompt))
        except ValueError:
            print(f"Por favor, ingrese un valor válido de tipo {tipo.__name__}.")

def add_product():
    nuevo_id = max(productos.keys()) + 1 if productos else 1
    nombre = input("Ingrese el nombre del nuevo producto: ")
    precio = get_option("Ingrese el precio del nuevo producto: ", float)
    cantidad_stock = get_option("Ingrese el stock del nuevo producto: ", int)
    
    productos[nuevo_id] = nombre
    precios[nuevo_id] = precio
    stock[nuevo_id] = cantidad_stock
    print(f"Producto '{nombre}' agregado con éxito.")

def delete_product():
    id_eliminar = get_option("Ingrese el ID del producto a eliminar: ")
    if id_eliminar in productos:
        nombre = productos.pop(id_eliminar)
        precios.pop(id_eliminar)
        stock.pop(id_eliminar)
        print(f"Producto '{nombre}' eliminado.")
    else:
        print("ID no encontrado.")

def update_product():
    id_actualizar = get_option("Ingrese el ID del producto a actualizar: ")
    if id_actualizar in productos:
        nombre = input(f"Ingrese el nuevo nombre del producto (actual: {productos[id_actualizar]}): ") or productos[id_actualizar]
        precio = get_option(f"Ingrese el nuevo precio del producto (actual: {precios[id_actualizar]}): ", float) or precios[id_actualizar]
        cantidad_stock = get_option(f"Ingrese el nuevo stock del producto (actual: {stock[id_actualizar]}): ", int) or stock[id_actualizar]
        
        productos[id_actualizar] = nombre
        precios[id_actualizar] = precio
        stock[id_actualizar] = cantidad_stock
        print(f"Producto '{id_actualizar}' actualizado.")
    else:
        print("ID no encontrado.")

def menu():
    opciones = {
        1: add_product,
        2: delete_product,
        3: update_product,
        4: lambda: print("Saliendo del programa.")
    }
    
    while True:
        list_products()
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
        opcion = get_option("Elija opción: ")

        if opcion in opciones:
            if opcion == 4:
                opciones[opcion]()
                break
            else:
                opciones[opcion]()
        else:
            print("Opción no válida. Intentelo nuevamente.")

if __name__ == "__main__":
    menu()
