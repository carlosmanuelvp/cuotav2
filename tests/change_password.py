def cambiar_contrasena():
    print("=== Cambiar Contraseña - Cuota UCI ===")

    usuario = input("Ingrese su nombre de usuario: ")
    contrasena_actual = input("Ingrese su contraseña actual: ")
    nueva_contrasena = input("Ingrese la nueva contraseña: ")
    confirmar_contrasena = input("Confirme la nueva contraseña: ")

    # Validaciones básicas
    if nueva_contrasena != confirmar_contrasena:
        print("❌ Las contraseñas no coinciden. Intente nuevamente.")
        return

    if nueva_contrasena == contrasena_actual:
        print("❌ La nueva contraseña no puede ser igual a la actual.")
        return

    # Aquí se simularía una llamada real a una API o backend para validar el cambio
    print(f"✅ Contraseña del usuario '{usuario}' cambiada con éxito.")

# Simulación del test
if __name__ == "__main__":
    cambiar_contrasena()
