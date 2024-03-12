
class Pizza:
    ingredientes_carne = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_masa = ["tradicional", "delgada"]

    def _init_(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def realizar_pedido(self):
        self.ingrediente_proteico = input("Ingresa el ingrediente proteico: ")
        self.ingrediente_vegetal1 = input("Ingresa el primer ingrediente vegetal: ")
        self.ingrediente_vegetal2 = input("Ingresa el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingresa el tipo de masa (tradicional/delgada): ")

        if self.validar_pedido():
            self.es_valida = True

    def validar_pedido(self):
        return (self.validar_elemento(self.ingrediente_proteico, self.ingredientes_carne) and
                self.validar_elemento(self.ingrediente_vegetal1, self.ingredientes_vegetales) and
                self.validar_elemento(self.ingrediente_vegetal2, self.ingredientes_vegetales) and
                self.validar_elemento(self.tipo_masa, self.tipos_masa))