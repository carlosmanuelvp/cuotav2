import time
import random

# Colores ANSI
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
CYAN = "\033[96m"
BOLD = "\033[1m"

# Resultados simulados: (nombre de test, pasó o no)
test_results = [
    ("test_passwords_do_not_match", False),
    ("test_password_too_short", False),
    ("test_missing_lowercase", False),
    ("test_missing_uppercase", False),
    ("test_missing_number", False),
    ("test_missing_special_char", False),
    ("test_valid_password", True),
]

# Encabezado estilo pytest
print(f"{BOLD}============================= test session starts ============================={RESET}")
print("platform linux -- Python 3.11.8, pytest-8.1.1, pluggy-1.4.0")
print("rootdir: /home/user/project")
print("collected 7 items\n")

# Barra de progreso con estado
passed = 0
failed = 0
symbols = []

for name, success in test_results:
    time.sleep(random.uniform(0.1, 0.25))  # Simula tiempo aleatorio por test
    if success:
        symbols.append(f"{GREEN}.{RESET}")
        passed += 1
    else:
        symbols.append(f"{RED}F{RESET}")
        failed += 1

print("".join(symbols) + "\n")

# Detalles por test
for name, success in test_results:
    if success:
        print(f"tests/test_change_password.py::{name} {GREEN}PASSED{RESET}")
    else:
        print(f"tests/test_change_password.py::{name} {RED}FAILED{RESET}")

# Mensajes de error simulados
print("\n" + f"{RED}=================================== FAILURES ==================================={RESET}")

for name, success in test_results:
    if not success:
        print(f"\n{BOLD}{RED}___________________________ {name} ___________________________{RESET}")
        print(f"{CYAN}tests/test_change_password.py{RESET}: AssertionError")

# Resumen final
print("\n" + "=" * 79)
print(f"{GREEN if failed == 0 else RED}== {passed} passed, {failed} failed in 0.83s =={RESET}")

if failed:
    print(f"\n{RED}FAILED{RESET} test suite")
else:
    print(f"\n{GREEN}All tests passed successfully!{RESET}")
