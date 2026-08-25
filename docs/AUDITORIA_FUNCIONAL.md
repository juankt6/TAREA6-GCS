# Auditoría Funcional de Requisitos

**Rol:** Auditor Funcional (Requisitos)
**Issue relacionado:** #2

## Requisito validado

El módulo `src/inventario.py` debe rechazar cualquier operación que deje el stock en un valor negativo.

## Criterios de aceptación y resultado

| # | Criterio | Prueba automatizada | Resultado |
|---|---|---|---|
| AC1 | Rechaza operaciones que resulten en stock negativo | `test_ac1_rechaza_stock_negativo` | ✅ PASSED |
| AC1b | Permite operaciones válidas (stock >= 0) | `test_ac1_permite_stock_valido` | ✅ PASSED |
| AC2 | Registra en log cada intento fallido | `test_ac2_registra_log_en_intento_fallido` | ✅ PASSED |
| AC3 | No modifica el stock cuando la validación falla | `test_ac3_no_modifica_stock_si_falla` | ✅ PASSED |
| Extra | Caso límite: stock exacto en 0 es válido | `test_stock_exacto_a_cero_es_valido` | ✅ PASSED |

## Evidencia de ejecución

`5 passed in 0.02s` — ver captura: `docs/evidencia_pruebas_funcionales.png`

## Conclusión

El requisito se cumple en su totalidad. Los 3 criterios de aceptación definidos en el issue #2 quedan verificados con evidencia automatizada y reproducible (`pytest tests/ -v`).
