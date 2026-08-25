"""
Módulo de Inventario INFIEC (simulado)
Gestiona la actualización de existencias del ERP.
"""
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("inventario_infiec")


class StockInvalidoError(ValueError):
    """Se lanza cuando una operación dejaría el stock en un valor negativo."""
    pass


def actualizar_stock(stock_actual: int, cantidad: int) -> int:
    """
    Actualiza el stock de un producto.

    Args:
        stock_actual: cantidad actual en inventario.
        cantidad: cantidad a sumar (positiva) o restar (negativa).

    Returns:
        El nuevo stock resultante.

    Raises:
        StockInvalidoError: si la operación resulta en stock negativo.
    """
    nuevo_stock = stock_actual + cantidad

    if nuevo_stock < 0:
        logger.error(
            "Intento de dejar stock negativo rechazado: stock_actual=%s, cantidad=%s",
            stock_actual, cantidad
        )
        raise StockInvalidoError(
            f"Operación rechazada: el stock no puede ser negativo "
            f"(actual={stock_actual}, cambio={cantidad})"
        )

    logger.info("Stock actualizado correctamente: %s -> %s", stock_actual, nuevo_stock)
    return nuevo_stock
