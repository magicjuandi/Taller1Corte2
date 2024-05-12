def buscar_vuelos(origen, destino, fecha):
    return ["Vuelo A", "Vuelo B", "Vuelo C"]

def reserva_asiento(vuelo, asiento):
    return True  


def pago(valor):
    return True  


def reservar_vuelo_completo(origen, destino, fecha, asiento):
    vuelos_disponibles = buscar_vuelos(origen, destino, fecha)
    if vuelos_disponibles:
        vuelo_seleccionado = vuelos_disponibles[0] 
        if reserva_asiento(vuelo_seleccionado, asiento):
            if pago(100): 
                return "Reserva exitosa."
            else:
                return "Fallo en el procesamiento del pago."
        else:
            return "Fallo en la reserva del asiento."
    else:
        return "No hay vuelos disponibles para esa ruta y fecha"

def main():
    origen = input("Ingrese el origen: ")
    destino = input("Ingrese el destino: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    asiento = input("Ingrese el número de asiento deseado: ")

    resultado = reservar_vuelo_completo(origen, destino, fecha, asiento)
    print(resultado)

if __name__ == "__main__":
    main()
