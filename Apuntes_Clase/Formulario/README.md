# Registro de Estudiantes con Flet (Python)



## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un formulario de registro de estudiantes utilizando la librería Flet en Python.

El formulario permite capturar información académica y personal del estudiante, aplicando validaciones para garantizar la integridad de los datos ingresados antes de procesarlos.

El proyecto está basado en la tarea original del formulario proporcionado en clase y fue mejorado agregando validaciones adicionales y controles interactivos.



## Tecnologías Utilizadas

- Python
- Flet
- Expresiones Regulares (re)



## Funcionalidades Implementadas

- Validación de campos vacíos.
- Validación de formato de correo electrónico.
- Validación de nombre (solo letras y espacios).
- Validación de número de control (solo números).
- Uso de control Dropdown para selección de carrera.
- Uso de control Dropdown para selección de semestre.
- Uso de control RadioGroup para selección de género.
- Visualización de datos en ventana modal (AlertDialog) después de enviar correctamente el formulario.
- Uso de SnackBar para mostrar advertencias.



## Explicación del Código

1. Importaciones

```python
import flet as ft
import re
```

flet: Permite crear la interfaz gráfica.

re: Se utiliza para validar el formato del correo y el nombre mediante expresiones regulares.

2. Función Principal
```
def main(page: ft.Page):
```

Es la función que construye toda la aplicación.
Recibe como parámetro la página principal donde se agregan los controles visuales.


3. Configuración de la Página

```page.title = "Registro de Estudiantes - Topicos Avanzados"
page.bgcolor = "#FDFBE3"
page.padding = 30
page.theme_mode = ft.ThemeMode.LIGHT
page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
```
Se configuran:
- Título de la ventana
- Color de fondo
- Espaciado interno
- Modo claro
- Alineación centrada

4. Campos de Entrada

Se utilizan controles TextField para capturar:

Nombre

Número de control

Email

Ejemplo:

```txt_nombre = ft.TextField(
    label="Nombre", 
    border_color="#4D2A32", 
    hint_text="Solo letras"
)
```

5. Controles Implementados
Dropdown Carrera

Permite seleccionar una carrera entre tres opciones.

```dd_carrera = ft.Dropdown(
    label="Carrera",
    options=[
        ft.dropdown.Option("Ingenieria en Sistemas"),
        ft.dropdown.Option("Ingenieria Civil"),
        ft.dropdown.Option("Ingenieria Industrial"),
    ]
)
```
Dropdown Semestre

Genera automáticamente los valores del 1 al 10:

```dd_semestre = ft.Dropdown(
    label="Semestre",
    options=[ft.dropdown.Option(str(i)) for i in range(1, 11)]
)
```
RadioGroup Género
Permite seleccionar una única opción.

```radio_genero = ft.RadioGroup(
    content=ft.Row([
        ft.Radio(value="Masculino", label="Masculino"),
        ft.Radio(value="Femenino", label="Femenino"),
        ft.Radio(value="Otro", label="Otro")
    ])
)
```

Validaciones Implementadas
Las validaciones se ejecutan en la función:

```
def validar_y_enviar(e):
```

1. Validación de Campos Vacíos
Se verifica que ningún campo esté vacío:

```
if not nom or not con or not ema or not car or not sem or not gen:
```
Si algún campo está vacío, se muestra un SnackBar de advertencia y no se permite continuar.


2. Validación de Nombre

Solo permite letras, espacios y caracteres acentuados:

```
re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nom)
```

3. Validación de Número de Control

Se valida que solo contenga números:


```
con.isdigit()
```

4. Validación de Email
   
Se valida mediante expresión regular:

```
re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", ema)
```
Visualización de Datos
Si todas las validaciones se cumplen, se muestra una ventana modal (AlertDialog) con los datos capturados:

```
dlg_datos = ft.AlertDialog(...)
```

El contenido del diálogo se actualiza dinámicamente con la información ingresada por el usuario.


## Ejecución del Proyecto

1. Instalar dependencias

```
pip install flet
```

O usando requirements.txt:

```
pip install -r requirements.txt
```

2. Ejecutar la aplicación
```
python main.py
```

## Código funcionando
<img width="1571" height="877" alt="image" src="https://github.com/user-attachments/assets/7a892ef9-bb9a-4143-a019-6cfd5b0518e0" />

<img width="1562" height="858" alt="image" src="https://github.com/user-attachments/assets/67ba9965-d25b-48d5-98ae-acd7afd8c2f5" />


<img width="1563" height="877" alt="image" src="https://github.com/user-attachments/assets/d06dd43e-2c0b-4e5b-9227-3ab907adbd8e" />



Si se envia con campos vacíos muestra la siguiente advertencia:
<img width="1567" height="878" alt="image" src="https://github.com/user-attachments/assets/43896fee-0348-45de-98c6-dca536eb5320" />

## Conclusión 

Este proyecto permite aplicar conceptos fundamentales de desarrollo de interfaces gráficas con Python, validación de datos y manejo de eventos.

Desde mi punto de vista, este ejercicio es importante porque simula el funcionamiento de formularios reales utilizados en sistemas académicos o administrativos. Las validaciones implementadas evitan errores comunes y mejoran la experiencia del usuario.

El uso de controles como Dropdown y RadioGroup hace que la interfaz sea más organizada y profesional, además de reforzar el aprendizaje sobre componentes interactivos en Flet.
