# Calculadora

Inicio de una interfaz de calculadora en Python

Este proyecto corresponde al desarrollo inicial de una calculadora utilizando Python y la librería Flet. 
El objetivo es crear la interfaz gráfica de la calculadora e implementar botones que permitan mostrar los números presionados en un área de texto mediante el evento on_click.

Instalación de Flet
Para el desarrollo de la interfaz se utiliza la librería Flet, la cual se instala desde Git Bash. 
Primero se crea una carpeta para el proyecto:

```
mkdir calculadora
cd calculadora
```

Posteriormente, se crea y activa un entorno virtual:
```
py -m venv .venv  
source .venv/Scripts/activate
```
Una vez activado el entorno virtual, se instala Flet:
```
pip install flet
```
Para comprobar que la instalación fue correcta se utiliza el siguiente comando:
```
flet --version
```
Desarrollo de la interfaz de la calculadora

Se importa la librería Flet y se define la función principal del programa:
```
```python
import flet as ft
```

Después de crear la dependencia aislada de Flet, se abre Visual Studio Code en la carpeta del proyecto previamente creada. Dentro de esta carpeta se encuentra el archivo principal donde se importa la librería Flet y se desarrolla la interfaz gráfica de la calculadora.

Inicialmente, se importa la librería necesaria y se define la función principal del programa:
```
import flet as ft

def main(page: ft.Page):
```
La función main recibe como parámetro un objeto page, el cual representa la ventana principal de la aplicación.

Configuración de la ventana
```
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20
```

En esta parte se establecen las características de la ventana:
- El título que se mostrará en la barra superior.
- El ancho y alto de la ventana.
- El espacio interno entre los elementos y el borde de la ventana.

Área de visualización (display)

Posteriormente, se crea el área donde se mostrarán los números que el usuario presione en la calculadora.
```

    display = ft.Container(
        content=ft.Text("0", size=30),
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
    )
```

Aquí se utiliza un Container que contiene un texto inicial con el valor 0.
Este contenedor funciona como la pantalla de la calculadora y se le asignan propiedades como color de fondo, tamaño, alineación del texto hacia la derecha y bordes redondeados.

Evento on_click de los botones

A continuación, se define la función que se ejecutará cuando se presione un botón.
```
    # FUNCION DEL CLICK
    def agregar_numero(e):
        valor = e.control.data

        if valor == "AC":
            display.content.value = "0"
        else:
            if display.content.value == "0":
                display.content.value = valor
            else:
                display.content.value += valor

        page.update()

```
Esta función recibe un evento (e) que contiene la información del botón presionado.
El valor del botón se obtiene mediante e.control.data.

Si el valor es "AC", el contenido del display se reinicia y se muestra 0, eliminando cualquier número previamente ingresado.

Si el botón presionado es un número:

Si el display contiene "0", este se reemplaza por el número presionado.

En caso contrario, el número se concatena al valor existente.

Finalmente, se utiliza page.update() para actualizar la interfaz y reflejar los cambios en pantalla.

Creación del contenedor de botones
```
    grid = ft.GridView(
        runs_count=3,
        spacing=10,
        run_spacing=10,
        width=210,
        height=220,
        expand=False
    )
```

El GridView permite organizar los botones en forma de cuadrícula, definiendo el número de columnas, el espacio entre ellos y el tamaño del área.

Botones numéricos
```
    numeros = ["1", "2", "3"]
```
Implementación del botón AC (borrar)

Para permitir borrar el contenido mostrado en el área de texto de la calculadora, se agregó un botón con la etiqueta “AC” (All Clear). Este botón tiene la función de reiniciar el valor del display a 0 cuando es presionado.

El botón AC se incluye dentro del mismo arreglo de botones numéricos, asignándole como dato (data) el valor "AC", lo que permite identificarlo dentro de la función que maneja el evento on_click.
```

numeros = ["7","8","1","AC"]
```

Se crea una lista con los números que tendrá la calculadora en esta etapa.
```
    for n in numeros:
        grid.controls.append(
            ft.ElevatedButton(
                text=n,
                data=n,
                on_click=agregar_numero,
                height=50
            )
        )

```
Cada botón:

- Muestra un número.

- Envía su valor mediante data.

- Ejecuta la función agregar_numero al hacer clic.

De esta manera, al presionar cualquier botón, el número correspondiente aparece en el display.

Organización final de la interfaz
```
    layout_principal = ft.Column(
        controls=[
            display,
            grid
        ],
        tight=True
    )

```
Se utiliza una columna para organizar la pantalla de la calculadora en dos partes principales:

El display.

Los botones.

Mostrar la aplicación
```
    page.add(layout_principal)
    page.update()

ft.app(target=main)
```

Finalmente, se agregan los elementos a la página y se ejecuta la aplicación.
La instrucción ft.app(target=main) permite que el programa se ejecute y se muestre la ventana de la calculadora.

Resultado final

Al ejecutar el programa, se visualiza una calculadora básica con tres botones numéricos.
Cada vez que el usuario presiona un botón, el número seleccionado se muestra en el área de texto, demostrando el funcionamiento del evento on_click y la actualización dinámica de la interfaz.

<img width="375" height="427" alt="image" src="https://github.com/user-attachments/assets/4afbc376-4936-42bb-9848-faee172b4a60" />
