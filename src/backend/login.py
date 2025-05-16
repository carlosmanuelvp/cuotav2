from get_cuota import obtener_cuota


datos = obtener_cuota("carlosmvp", "Contreras28.0e0")
if datos:
    print("Datos:", datos)
