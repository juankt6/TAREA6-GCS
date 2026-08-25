# Documento de Entrega

**Rol:** Entrega/Despliegue
**Issue relacionado:** #5

## Pasos de entrega controlada

1. **Desarrollo**: cada cambio se hace en una rama derivada de un issue (`tipo/nombre-corto`).
2. **Validación local**: ejecutar `python3 -m pytest tests/ -v` antes de abrir el PR.
3. **Pull Request**: abrir PR hacia `main`, completar la plantilla (`.github/PULL_REQUEST_TEMPLATE.md`) y el checklist de `CHECKLIST_AUDITORIA.md`.
4. **CI automático**: el workflow `.github/workflows/ci.yml` ejecuta las pruebas automáticamente en cada push y PR contra `main`. El merge solo debe aprobarse si el pipeline está en verde.
5. **Revisión cruzada**: al menos un integrante adicional revisa el PR (en este ejercicio individual, se documenta como comentario de revisión).
6. **Merge a main**: una vez aprobado y con CI en verde, se fusiona a `main` (línea base).
7. **Release**: cuando todos los issues estén cerrados, el Gestor de Release crea el tag y las release notes (ver issue #6).

## Evidencia de ejecución del pipeline

El workflow se activa automáticamente en GitHub Actions con cada push/PR a `main`. Ver pestaña **Actions** del repositorio: 
`https://github.com/juankt6/TAREA6-GCS/actions`

## Cómo validar localmente

```bash
git clone https://github.com/juankt6/TAREA6-GCS.git
cd TAREA6-GCS
pip install -r requirements.txt
python3 -m pytest tests/ -v
```

Resultado esperado: `5 passed`.
