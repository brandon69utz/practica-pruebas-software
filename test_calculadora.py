
import pytest

from calculadora import (
    sumar, restar, multiplicar, dividir
)


def test_sumar_positivos():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-2, -3) == -5


def test_dividir_exactamente():
    assert dividir(10, 2) == 5


def test_dividir_decimal():
    assert dividir(7, 2) == 3.5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_restar():
    assert restar(8, 3) == 5


def test_restar_negativos():
    assert restar(-5, -2) == -3


def test_multiplicar_negativos():
    assert multiplicar(-3, 4) == -12


def test_dividir_cero_entre_numero():
    assert dividir(0, 5) == 0


def test_dividir_texto():
    with pytest.raises(ValueError):
        dividir("diez", 2)
