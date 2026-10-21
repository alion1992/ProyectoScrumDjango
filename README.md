# Proyecto Django — Scrum

## 1. Descripción

Este proyecto es una aplicación desarrollada con **Django** para gestionar información relacionada con un sistema Scrum.

Incluye modelos para:

- **Programador:** nombre y apellido.
- **Proyecto:** nombre del proyecto.
- **Sprint:** fechas de inicio y fin, y proyecto asociado.
- **Tarea:** nombre, fechas, estado, sprint y programador asignados.
- **Etiqueta:** etiquetas que pueden asociarse a varias tareas.

## 2. Requisitos previos

Antes de empezar, necesitas tener instalado:

- [Python](https://www.python.org/downloads/).
- [Git](https://git-scm.com/downloads).
- Un editor de código, como [PyCharm](https://www.jetbrains.com/pycharm/) o [Visual Studio Code](https://code.visualstudio.com/).

Comprueba que Python está instalado abriendo una terminal y ejecutando:

```bash
python --version
```

Si el comando no funciona, prueba:

```bash
python3 --version
```

Comprueba también que Git está instalado:

```bash
git --version
```

## 3. Clonar el repositorio

Abre una terminal y sitúate en la carpeta donde quieras guardar el proyecto.

Ejecuta el siguiente comando, sustituyendo la URL por la dirección real del repositorio de GitHub:

```bash
git clone URL_DEL_REPOSITORIO
```

Por ejemplo, si la URL del repositorio es `https://github.com/USUARIO/DjangoProject1.git`:

```bash
git clone https://github.com/USUARIO/DjangoProject1.git
```

Entra en la carpeta del proyecto:

```bash
cd DjangoProject1
```

## 4. Crear el entorno virtual

Un entorno virtual permite instalar las dependencias del proyecto sin afectar a otros proyectos de Python.

### macOS y Linux

```bash
python3 -m venv .venv
```

### Windows

```powershell
python -m venv .venv
```

## 5. Activar el entorno virtual

### macOS y Linux

```bash
source .venv/bin/activate
```

### Windows — CMD

```cmd
.venv\Scripts\activate.bat
```

### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando el entorno esté activado, normalmente aparecerá `(.venv)` al principio de la línea de la terminal.

**Importante:** activa el entorno virtual cada vez que abras una nueva terminal para trabajar en el proyecto.

## 6. Instalar las dependencias

Comprueba que estás en la carpeta raíz del proyecto, donde se encuentra `requirements.txt`.

Actualiza `pip`:

```bash
python -m pip install --upgrade pip
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

Este comando instalará Django y las demás librerías indicadas en el archivo `requirements.txt`.

## 7. Acceder a la carpeta de Django

En este repositorio, el proyecto Django está dentro de la carpeta `ejemplo`.

Entra en ella:

```bash
cd ejemplo
```

Comprueba que estás en la carpeta correcta:

```bash
ls
```

En Windows también puedes utilizar:

```powershell
dir
```

Deberías encontrar el archivo `manage.py` y las carpetas de las aplicaciones del proyecto.

## 8. Aplicar las migraciones

Django utiliza las migraciones para crear y actualizar las tablas de la base de datos.

Ejecuta:

```bash
python manage.py migrate
```

Este comando creará las tablas necesarias en la base de datos SQLite local.

**Nota:** la base de datos original no se incluye en el repositorio. Cada alumno tendrá su propia base de datos local.

## 9. Comprobar que Django funciona

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

Si todo funciona correctamente, aparecerá un mensaje indicando que el servidor está disponible en una dirección similar a esta:

```text
http://127.0.0.1:8000/
```

Abre esa dirección en tu navegador.

Para detener el servidor, pulsa `Ctrl + C` en la terminal.

## 10. Comandos habituales

| Acción | Comando |
|---|---|
| Activar el entorno en macOS/Linux | `source .venv/bin/activate` |
| Instalar dependencias | `python -m pip install -r requirements.txt` |
| Crear migraciones tras modificar modelos | `python manage.py makemigrations` |
| Aplicar migraciones | `python manage.py migrate` |
| Iniciar el servidor | `python manage.py runserver` |
| Comprobar errores del proyecto | `python manage.py check` |

## 11. Solución de problemas

### Error: `No module named django`

Comprueba que el entorno virtual está activado y ejecuta:

```bash
python -m pip install -r requirements.txt
```

### Error: no se encuentra `manage.py`

Comprueba que has entrado en la carpeta `ejemplo`:

```bash
cd ejemplo
```

### Error al ejecutar las migraciones

Ejecuta primero:

```bash
python manage.py check
```

Lee el mensaje de error y comprueba que las migraciones del proyecto están presentes en las carpetas `migrations` de las aplicaciones.

### El puerto 8000 está ocupado

Puedes iniciar el servidor en otro puerto:

```bash
python manage.py runserver 8001
```

En ese caso, accede a `http://127.0.0.1:8001/`.

---

## 12. Flujo de trabajo recomendado

Cuando trabajes con el proyecto:

1. Abre el proyecto en tu editor.
2. Activa el entorno virtual.
3. Entra en la carpeta `ejemplo`.
4. Modifica el código necesario.
5. Si modificas los modelos, genera las migraciones y aplícalas.
6. Ejecuta el servidor y comprueba los cambios.

¡Ya tienes el entorno preparado para trabajar con Django!
