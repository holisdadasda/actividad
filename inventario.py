class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

class SistemaInventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self):
        codigo = input("Codigo: ")
        if codigo == "":
            print("El codigo no puede estar vacio")
            return
        for p in self.productos:
            if p.codigo == codigo:
                print("Ya existe un producto con ese codigo")
                return
        nombre = input("Nombre: ")
        if nombre == "":
            print("El nombre no puede estar vacio")
            return
        precio_str = input("Precio: ")
        if precio_str == "":
            print("El precio no puede estar vacio")
            return
        precio = float(precio_str)
        if precio < 0:
            print("El precio no puede ser negativo")
            return
        cantidad_str = input("Cantidad: ")
        if cantidad_str == "":
            print("La cantidad no puede estar vacia")
            return
        cantidad = int(cantidad_str)
        if cantidad < 0:
            print("La cantidad no puede ser negativa")
            return
        categoria = input("Categoria: ")
        if categoria == "":
            print("La categoria no puede estar vacia")
            return
        nuevo = Producto(codigo, nombre, precio, cantidad, categoria)
        self.productos.append(nuevo)
        print("Producto registrado correctamente")

    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos registrados")
            return
        for p in self.productos:
            print("Codigo:", p.codigo)
            print("Nombre:", p.nombre)
            print("Precio:", p.precio)
            print("Cantidad:", p.cantidad)
            print("Categoria:", p.categoria)
            print("---")

    def buscar_producto(self):
        print("1. Buscar por codigo")
        print("2. Buscar por nombre")
        opcion = input("Opcion: ")
        if opcion == "1":
            codigo = input("Ingrese el codigo: ")
            for p in self.productos:
                if p.codigo == codigo:
                    print("Codigo:", p.codigo)
                    print("Nombre:", p.nombre)
                    print("Precio:", p.precio)
                    print("Cantidad:", p.cantidad)
                    print("Categoria:", p.categoria)
                    return
            print("Producto no encontrado")
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            for p in self.productos:
                if p.nombre.lower() == nombre.lower():
                    print("Codigo:", p.codigo)
                    print("Nombre:", p.nombre)
                    print("Precio:", p.precio)
                    print("Cantidad:", p.cantidad)
                    print("Categoria:", p.categoria)
                    return
            print("Producto no encontrado")
        else:
            print("Opcion invalida")

    def actualizar_producto(self):
        codigo = input("Ingrese el codigo del producto a actualizar: ")
        for p in self.productos:
            if p.codigo == codigo:
                precio_str = input("Nuevo precio: ")
                if precio_str == "":
                    print("El precio no puede estar vacio")
                    return
                precio = float(precio_str)
                if precio < 0:
                    print("El precio no puede ser negativo")
                    return
                cantidad_str = input("Nueva cantidad: ")
                if cantidad_str == "":
                    print("La cantidad no puede estar vacia")
                    return
                cantidad = int(cantidad_str)
                if cantidad < 0:
                    print("La cantidad no puede ser negativa")
                    return
                categoria = input("Nueva categoria: ")
                if categoria == "":
                    print("La categoria no puede estar vacia")
                    return
                p.precio = precio
                p.cantidad = cantidad
                p.categoria = categoria
                print("Producto actualizado correctamente")
                return
        print("Producto no encontrado")

    def eliminar_producto(self):
        codigo = input("Ingrese el codigo del producto a eliminar: ")
        for i in range(len(self.productos)):
            if self.productos[i].codigo == codigo:
                self.productos.pop(i)
                print("Producto eliminado correctamente")
                return
        print("Producto no encontrado")

    def calcular_total_inventario(self):
        total = 0
        for p in self.productos:
            total = total + (p.precio * p.cantidad)
        print("Valor total del inventario:", total)

    def mostrar_agotados(self):
        hay_agotados = False
        for p in self.productos:
            if p.cantidad == 0:
                print("Codigo:", p.codigo)
                print("Nombre:", p.nombre)
                print("Categoria:", p.categoria)
                print("---")
                hay_agotados = True
        if hay_agotados == False:
            print("No hay productos agotados")

    def guardar_archivo(self):
        archivo = open("inventario.txt", "w")
        for p in self.productos:
            archivo.write("Codigo: " + p.codigo + "\n")
            archivo.write("Nombre: " + p.nombre + "\n")
            archivo.write("Precio: " + str(p.precio) + "\n")
            archivo.write("Cantidad: " + str(p.cantidad) + "\n")
            archivo.write("Categoria: " + p.categoria + "\n")
            archivo.write("---\n")
        archivo.close()
        print("Inventario guardado en inventario.txt")


sistema = SistemaInventario()

while True:
    print("")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular total del inventario")
    print("7. Mostrar productos agotados")
    print("8. Guardar en archivo")
    print("9. Salir")
    print("")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        sistema.registrar_producto()
    elif opcion == "2":
        sistema.mostrar_productos()
    elif opcion == "3":
        sistema.buscar_producto()
    elif opcion == "4":
        sistema.actualizar_producto()
    elif opcion == "5":
        sistema.eliminar_producto()
    elif opcion == "6":
        sistema.calcular_total_inventario()
    elif opcion == "7":
        sistema.mostrar_agotados()
    elif opcion == "8":
        sistema.guardar_archivo()
    elif opcion == "9":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida")
