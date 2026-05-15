precios=[2500,3000,1500,5000]

for precio in precios:
    if precio < 2000:
        print("barato: ", precio)
    elif precio <= 4000:
        print("medio: ", precio )
        