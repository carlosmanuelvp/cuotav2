import pytest

# Simulación de prueba exitosa
def test_success():
    """Simula un caso donde la prueba pasa correctamente"""
    assert True, "Este es un caso de prueba exitoso."

# Simulación de fallo esperado
@pytest.mark.xfail(reason="Este fallo es esperado para demostrar cómo se maneja.")
def test_expected_fail():
    """Simula un caso de prueba que fallará de forma controlada."""
    assert False, "Este fallo es esperado."

# Simulación de caso omitido
@pytest.mark.skip(reason="Este test está siendo omitido de forma intencional.")
def test_skipped():
    """Simula un caso que se salta por una razón específica."""
    assert True, "Este test ha sido omitido."

# Simulación de fallo
def test_fail():
    """Simula un fallo de prueba para mostrar cómo pytest lo maneja."""
    assert False, "Este test debería fallar para mostrar la salida."

# Caso de prueba con una excepción
def test_raise_exception():
    """Simula el lanzamiento de una excepción en una prueba."""
    with pytest.raises(ValueError):
        raise ValueError("Esto es una excepción simulada.")

# Simulación de un resultado con una condición específica
def test_condition_fail():
    """Simula un fallo basado en una condición."""
    num = 3
    assert num == 4, f"Se esperaba 4, pero obtuvimos {num}"

# Caso con una advertencia
@pytest.mark.warning
def test_warning():
    """Simula el caso de una advertencia durante la ejecución."""
    import warnings
    warnings.warn("Este es un caso de prueba con advertencia.")

# Caso con parámetros (simula varios casos en un solo test)
@pytest.mark.parametrize("input_data, expected", [(5, 10), (3, 6), (7, 14)])
def test_multiplication(input_data, expected):
    """Simula un test parametrizado para comprobar resultados."""
    assert input_data * 2 == expected, f"Se esperaba {expected} pero obtuvimos {input_data * 2}"
