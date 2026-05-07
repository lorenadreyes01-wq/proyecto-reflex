# The 100: Survival Log - Reflex Web Project

Este proyecto es una aplicación web interactiva inspirada en la serie **"The 100"**, desarrollada para la asignatura de Informática. Utiliza el framework **Reflex** para crear una experiencia de usuario reactiva utilizando únicamente Python.

## Requisitos Previos

Para ejecutar este proyecto, necesitas tener instalado:
* **Python 3.10** (Versión estable recomendada para Reflex).
* **Poetry** (Gestor de dependencias y entornos virtuales).

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/lorenadreyes01-wq/proyecto-reflex.git](https://github.com/lorenadreyes01-wq/proyecto-reflex.git)
   cd mi-web-reflex

   Configurar el entorno con Poetry:

2. **Configurar el entorno con Poetry:**
   ```bash
   poetry env use python3.10
   poetry install
   Activar el entorno virtual
   ```

3. **Activar el entorno virtual:**
   ```bash
   poetry env activate
   ```

# Ejecución
Para iniciar el servidor de desarrollo y ver la página en tu navegador:
```bash
poetry run reflex run
La aplicación estará disponible en: http://localhost:3000
```

# Lógica del Proyecto (Basado en The 100)
La aplicación demuestra el uso de Programación Reactiva:

**Estado dinámico:** El usuario inicia como "Miembro del Arca" en un entorno oscuro y metálico.

**Interacción:** Al presionar el botón "¡BAJAR A LA TIERRA!", el estado (rx.State) actualiza los colores, textos y fondos simultáneamente.

**Animaciones:** Implementación de renderizado condicional con animaciones de tipo bounce para celebrar la llegada a la Tierra.
