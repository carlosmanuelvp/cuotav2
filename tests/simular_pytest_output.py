import time

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def simulate_pytest_output():
    print("================================ test session starts ================================")
    print("platform linux -- Python 3.11.x, pytest-7.x.x")
    print("rootdir: /ruta/proyecto")
    print("collected 7 items\n")

    resultados = [
        ("test_change_password.py::test_contrasenas_no_coinciden", True),
        ("test_change_password.py::test_contrasena_too_short", True),
        ("test_change_password.py::test_sin_minusculas", True),
        ("test_change_password.py::test_sin_mayusculas", True),
        ("test_change_password.py::test_sin_numeros", True),
        ("test_change_password.py::test_sin_caracter_especial", False),
        ("test_change_password.py::test_contrasena_valida", True),
    ]

    for test, passed in resultados:
        time.sleep(0.2)
        if passed:
            print_colored(f"{test:<60} PASSED    [✓]", "92")  # Verde
        else:
            print_colored(f"{test:<60} FAILED    [✗]", "91")  # Rojo

    print("\n==================================== FAILURES ===================================")
    print("_____________________ test_sin_caracter_especial _____________________\n")
    print("    def test_sin_caracter_especial():")
    print("        user = User(\"usuario\", \"oldpass\", \"Password123\", \"Password123\")")
    print("        result = change_pass(user)")
    print(">")
    print("        assert result[\"success\"] is False")
    print("E       AssertionError: assert True is False")
    print("E        +  where True = result['success']\n")
    print("test_change_password.py:32: AssertionError\n")

    print("======================= short test summary info =======================")
    print_colored("FAILED test_change_password.py::test_sin_caracter_especial", "91")
    print("\n================= 1 failed, 6 passed in 0.45s =================")

if __name__ == "__main__":
    simulate_pytest_output()
