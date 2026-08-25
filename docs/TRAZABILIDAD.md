# Convención de Trazabilidad

**Rol:** Gestor de Trazabilidad
**Issue relacionado:** #3

## Convención de mensajes de commit

Formato: `tipo: descripción breve (#issue)`

Tipos permitidos:
- `feat`: nueva funcionalidad
- `fix`: corrección de errores
- `docs`: cambios de documentación
- `chore`: tareas de mantenimiento/config
- `test`: pruebas
- `ci`: pipeline / integración continua

Ejemplo: `feat: agregar validacion de stock negativo (#2)`

## Cadena de trazabilidad exigida

Todo cambio debe poder rastrearse: **Issue → Branch → Commit(s) → PR → Merge (main) → Release**.

Reglas:
1. Cada branch nace de un issue: `tipo/nombre-corto` (ej. `audit/config-fisica`, `feature/trazabilidad`).
2. Cada commit referencia el issue con `(#N)`.
3. Cada PR usa `Closes #N` en la descripción para cerrar el issue automáticamente al hacer merge.
4. Cada release enumera los issues y PR incluidos (ver `CHANGELOG` en las release notes).

## Plantilla de PR

Ver [`.github/PULL_REQUEST_TEMPLATE.md`](../.github/PULL_REQUEST_TEMPLATE.md), aplicada automáticamente a todo PR nuevo.
