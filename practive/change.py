import flet as ft
import re

def main(page: ft.Page):
    page.title = "Cambiar Contraseña"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600

    # Input fields
    current_password_field = ft.TextField(
        label="Contraseña actual",
        password=True,
        can_reveal_password=True,
        width=300
    )
    new_password_field = ft.TextField(
        label="Nueva Contraseña",
        password=True,
        can_reveal_password=True,
        width=300
    )
    confirm_new_password_field = ft.TextField(
        label="Confirmar Nueva Contraseña",
        password=True,
        can_reveal_password=True,
        width=300
    )

    # Validation feedback texts
    feedback_current_match = ft.Text("", color=ft.colors.RED_ACCENT_700, size=12)
    feedback_new_match = ft.Text("", color=ft.colors.RED_ACCENT_700, size=12)
    feedback_length = ft.Text("✗ 8 caracteres", color=ft.colors.RED_ACCENT_700, size=12)
    feedback_uppercase = ft.Text("✗ letra mayúscula", color=ft.colors.RED_ACCENT_700, size=12)
    feedback_lowercase = ft.Text("✗ minúscula", color=ft.colors.RED_ACCENT_700, size=12)
    feedback_digit = ft.Text("✗ número", color=ft.colors.RED_ACCENT_700, size=12)
    feedback_special = ft.Text("✗ carácter especial", color=ft.colors.RED_ACCENT_700, size=12)
    success_message = ft.Text("", color=ft.colors.GREEN_ACCENT_700, size=14, weight=ft.FontWeight.BOLD)

    # Special characters for validation
    special_characters = r'[!@#$%^&*(),.?":{}|<>]'

    def validate_password(e):
        current_password = current_password_field.value
        new_password = new_password_field.value
        confirm_new_password = confirm_new_password_field.value

        # Reset feedback texts
        feedback_current_match.value = ""
        feedback_new_match.value = ""
        feedback_length.value = "✗ 8 caracteres"
        feedback_uppercase.value = "✗ letra mayúscula"
        feedback_lowercase.value = "✗ minúscula"
        feedback_digit.value = "✗ número"
        feedback_special.value = "✗ carácter especial"
        success_message.value = ""

        feedback_length.color = ft.colors.RED_ACCENT_700
        feedback_uppercase.color = ft.colors.RED_ACCENT_700
        feedback_lowercase.color = ft.colors.RED_ACCENT_700
        feedback_digit.color = ft.colors.RED_ACCENT_700
        feedback_special.color = ft.colors.RED_ACCENT_700

        is_valid = True

        # Validation 1: New password cannot be same as current
        if new_password == current_password and new_password != "":
            feedback_current_match.value = "La nueva contraseña no puede ser igual a la actual."
            is_valid = False

        # Validation 2: New password and confirmation must match
        if new_password != confirm_new_password and confirm_new_password != "":
            feedback_new_match.value = "La nueva contraseña y la confirmación no coinciden."
            is_valid = False

        # Validation 3: New password complexity
        if new_password: # Only validate complexity if new password is not empty
            # Length
            if len(new_password) >= 8:
                feedback_length.value = "✓ 8 caracteres"
                feedback_length.color = ft.colors.GREEN_ACCENT_700
            else:
                is_valid = False

            # Uppercase
            if any(char.isupper() for char in new_password):
                feedback_uppercase.value = "✓ letra mayúscula"
                feedback_uppercase.color = ft.colors.GREEN_ACCENT_700
            else:
                is_valid = False

            # Lowercase
            if any(char.islower() for char in new_password):
                feedback_lowercase.value = "✓ minúscula"
                feedback_lowercase.color = ft.colors.GREEN_ACCENT_700
            else:
                is_valid = False

            # Digit
            if any(char.isdigit() for char in new_password):
                feedback_digit.value = "✓ número"
                feedback_digit.color = ft.colors.GREEN_ACCENT_700
            else:
                is_valid = False

            # Special character
            if re.search(special_characters, new_password):
                feedback_special.value = "✓ carácter especial"
                feedback_special.color = ft.colors.GREEN_ACCENT_700
            else:
                is_valid = False
        else: # If new password is empty, all complexity checks fail
             is_valid = False


        # If all validations pass
        if is_valid and current_password and new_password and confirm_new_password:
             success_message.value = "¡Contraseña cambiada con éxito!"
        elif not current_password or not new_password or not confirm_new_password:
             # Don't show success if fields are empty, even if complexity checks pass
             pass # Keep success message empty
        else:
             success_message.value = "" # Clear success message if any validation fails


        page.update()

    # Change password button
    change_password_button = ft.ElevatedButton(
        "Cambiar Contraseña",
        on_click=validate_password
    )

    page.add(
        ft.Column(
            [
                current_password_field,
                feedback_current_match,
                new_password_field,
                confirm_new_password_field,
                feedback_new_match,
                ft.Column([
                    feedback_length,
                    feedback_uppercase,
                    feedback_lowercase,
                    feedback_digit,
                    feedback_special,
                ], spacing=2),
                change_password_button,
                success_message
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

if __name__ == "__main__":
    ft.app(target=main)