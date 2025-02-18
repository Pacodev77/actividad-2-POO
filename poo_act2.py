# Programación Orientada a Objetos
# Alumno: Francisco Ruiz.  Matrícula: 82859
# Coach: Gustavo Alfredo Valdés González

class Carro:
    def __init__(self, marca, modelo, color, costo):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.costo = costo  # Almacenar el costo como número

    def __str__(self):
        return f"\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nCosto: ${self.costo:.2f}\n" # Formatear el costo aquí

    def get_costo(self):
        return self.costo  # Retornar el costo

# Crear objetos (costos como números)
carro1 = Carro("Toyota", "Corolla", "Beige", 245000.00)
carro2 = Carro("Ford", "Malibu", "Negro", 180000.00)
carro3 = Carro("Jeep", "Renegade", "Gris", 325000.00)

cars = [carro1, carro2, carro3]

for car in cars:
    print(car)  # Imprime la información del carro, incluyendo el costo
    precio = car.get_costo()  # Obtiene el costo
    print("-" * 20)
   
   



