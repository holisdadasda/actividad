precios=[2500,3000,1500,5000]

for precio in precios:
    descuento = precio * 0.10
    nuevo_precio = precio - descuento
    print("nuevo precio: ", nuevo_precio)