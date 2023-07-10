class Carrito:
    def __init__ (self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, inventario):
        id = str(inventario.Id_juego)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "inventario_id": inventario.Id_juego,
                "nombre": inventario.nombre_juego,
                "acumulado": float(inventario.valor),
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += float(inventario.valor)
        self.guardar_carrito()

    def sumar(self, inventario):
        id = str(inventario.Id_juego)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += float(inventario.valor)
            self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, inventario):
        id = str(inventario.Id_juego)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, inventario):
        id = str(inventario.Id_juego)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= float(inventario.valor)
            if self.carrito[id]["cantidad"] <= 0:self.eliminar(inventario)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
