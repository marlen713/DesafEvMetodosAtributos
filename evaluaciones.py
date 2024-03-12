
from pizza import Pizza

# Punto 5a
print(Pizza.ingredientes_carne)
print(Pizza.ingredientes_vegetales)
print(Pizza.tipos_masa)

# Punto 5b
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Punto 5c
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# Punto 5d
print(f"Ingredientes vegetales: {mi_pizza.ingrediente_vegetal1}, {mi_pizza.ingrediente_vegetal2}")
print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
print(f"Tipo de masa: {mi_pizza.tipo_masa}")
print(f"¿Es una pizza válida? {mi_pizza.es_valida}")

# Punto 5e
print(f"¿Es la clase {Pizza} una pizza válida? ")