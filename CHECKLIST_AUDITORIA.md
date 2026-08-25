# Checklist de Auditoría (Control de Integridad)

**Rol:** Control de Integridad
**Issue relacionado:** #4

Este checklist debe verificarse **antes de aprobar cualquier merge a `main`**.

## Controles obligatorios

- [ ] **Revisión por PR**: todo cambio pasa por Pull Request, nunca push directo a `main` (excepto la línea base inicial).
- [ ] **Referencia a issue**: el PR incluye `Closes #N` y los commits referencian `(#N)`.
- [ ] **Sin secretos**: no se suben credenciales reales; solo `.env.example` con valores de ejemplo.
- [ ] **Sin archivos sueltos**: no se incluyen archivos temporales, cachés (`__pycache__/`, `.pytest_cache/`) ni binarios innecesarios.
- [ ] **Pruebas en verde**: si el cambio afecta código, `pytest tests/` debe pasar al 100% antes del merge.
- [ ] **Documentación actualizada**: si el cambio afecta comportamiento, se actualiza el README o el doc correspondiente.
- [ ] **Convención de commits respetada**: `tipo: descripción (#issue)` (ver `docs/TRAZABILIDAD.md`).
- [ ] **Verificación de artefactos**: en un release, el tag coincide con el contenido real de `main` en ese punto (no hay commits post-tag sin nueva versión).

## Excepción documentada de este proyecto

Por tratarse de un ejercicio individual que simula los roles de un equipo, la revisión cruzada (aprobación de un segundo integrante) se documenta mediante comentarios de revisión (`review type: COMMENT`) en lugar de un `APPROVE`, ya que GitHub no permite auto-aprobar el propio Pull Request. Esta limitación se deja registrada aquí para no simular evidencia falsa.

## Responsable

Control de Integridad (issue #4) — valida este checklist en cada PR antes del merge.
