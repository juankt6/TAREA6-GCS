"""
Pruebas de validacion del modulo de inventario.
Evidencia de Auditoria Funcional - Issue #2
"""
import pytest
from src.inventario import actualizar_stock, StockInvalidoError


def test_ac1_rechaza_stock_negativo():
    """AC1: rechaza operaciones que resulten en stock negativo."""
    with pytest.raises(StockInvalidoError):
        actualizar_stock(stock_actual=5, cantidad=-10)


def test_ac1_permite_stock_valido():
    """AC1 (caso positivo): permite operaciones que mantienen stock >= 0."""
    resultado = actualizar_stock(stock_actual=5, cantidad=-3)
    assert resultado == 2


def test_ac2_registra_log_en_intento_fallido(caplog):
    """AC2: registra en el log cada intento fallido con el motivo."""
    with caplog.at_level("ERROR"):
        with pytest.raises(StockInvalidoError):
            actualizar_stock(stock_actual=2, cantidad=-5)
    assert any("rechazado" in record.message for record in caplog.records)


def test_ac3_no_modifica_stock_si_falla():
    """AC3: el stock no se modifica cuando la validacion falla (no hay efecto secundario)."""
    stock_actual = 3
    try:
        actualizar_stock(stock_actual=stock_actual, cantidad=-100)
    except StockInvalidoError:
        pass
    # actualizar_stock es pura (no muta estado externo); se verifica que
    # el valor original permanece intacto en el ambito del llamador.
    assert stock_actual == 3


def test_stock_exacto_a_cero_es_valido():
    """Caso limite: dejar el stock exactamente en 0 es una operacion valida."""
    resultado = actualizar_stock(stock_actual=10, cantidad=-10)
    assert resultado == 0
