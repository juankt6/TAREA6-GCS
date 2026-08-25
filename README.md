# TAREA6-GCS — Auditoría de Configuración + Release Controlado

Proyecto integrador: **Módulo de Inventario INFIEC (simulado)**, usado como caso de estudio
para aplicar auditoría de configuración (física y funcional), trazabilidad, control de
integridad y un release controlado, según la Semana 6 de Gestión de la Configuración de
Software (GCS).

## Descripción del proyecto

Simula una función crítica del sistema de inventario de **INFIEC Cía. Ltda.**: la
actualización de existencias (`stock`), validando que no se permitan valores negativos
que dejarían inconsistente la base de datos del ERP.

## Estructura del repositorio

```
TAREA6-GCS/
├── src/                  # Código fuente del módulo de inventario
├── tests/                # Pruebas de validación (evidencia de auditoría funcional)
├── docs/                 # Documentación de auditoría y trazabilidad
├── scripts/              # Scripts de entrega/despliegue
├── .github/workflows/    # Pipeline simple de build/test (CI)
├── CHECKLIST_AUDITORIA.md
├── DOC_ENTREGA.md
└── .env.example
```

## Instalación y ejecución

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m pytest tests/ -v
```

## Roles del equipo (Semana 6)

| Rol | Responsable | Evidencia |
|---|---|---|
| Auditor Físico (Config Items) | juankt6 | Issue + PR de estructura/documentación |
| Auditor Funcional (Requisitos) | juankt6 | Issue + checklist + evidencia de prueba |
| Gestor de Trazabilidad | juankt6 | Plantilla de PR + referencias cruzadas |
| Gestor de Release | juankt6 | Release vX.Y.Z + notas |
| Control de Integridad | juankt6 | CHECKLIST_AUDITORIA.md |
| Entrega/Despliegue | juankt6 | DOC_ENTREGA.md + workflow CI |

## Licencia

Ver [LICENSE](LICENSE).
