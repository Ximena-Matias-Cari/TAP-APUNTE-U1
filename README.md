# TAP-APUNTE-U1
# Apuntes de Clase: Programación de Interfaces Gráficas
## Unidad I: Interfaz Gráfica de Usuario (GUI)

Este repositorio contiene la investigación documental y ejemplos prácticos de la Unidad I, centrados en el uso del framework **Flet** (basado en Flutter) para Python.

---

### 1.1 Creación de interfaz gráfica para usuarios
En el ecosistema de Flet, la creación de una interfaz no se basa en el dibujo manual de píxeles, sino en la construcción de un **Árbol de Controles**. 

* **Estructura Base:** Toda aplicación inicia con una función `main(page: ft.Page)`. La instancia `page` actúa como el contenedor raíz de la aplicación.
* **Controles (Widgets):** Los elementos visuales se denominan "Controls". Para que un control sea visible, debe ser agregado al árbol de la página mediante `page.add()` o `page.controls.append()`.
* **Layout Dinámico:** Flet utiliza un sistema de diseño flexible. Los componentes se organizan principalmente mediante:
    * `Column`: Alineación vertical.
    * `Row`: Alineación horizontal.
    * `Container`: Para aplicar márgenes, rellenos y colores de fondo.



---

### 1.2 Tipos de eventos
Los eventos son señales que el sistema envía cuando ocurre una interacción. En Flet, los eventos están vinculados a las propiedades que comienzan con el prefijo `on_`.

| Tipo de Evento | Propiedad en Flet | Descripción |
| :--- | :--- | :--- |
| **Acción** | `on_click` | Se dispara al presionar un botón o elemento interactivo. |
| **Cambio** | `on_change` | Se activa cuando el valor de un input (TextField, Checkbox) varía. |
| **Teclado** | `on_keyboard_event` | Captura teclas presionadas de forma global en la página. |
| **Ventana** | `on_resize` | Detecta cuando el usuario cambia el tamaño de la aplicación. |
| **Enfoque** | `on_focus` / `on_blur` | Se dispara cuando un elemento gana o pierde la atención del cursor. |

---

### 1.3 Manejo de eventos
El manejo de eventos se realiza mediante funciones de **Callback**. Una función de callback se ejecuta automáticamente cuando el evento ocurre.

* **El objeto `ControlEvent`:** Cada vez que se dispara un evento, Flet pasa un objeto que contiene información sobre el evento (quién lo disparó, coordenadas, datos ingresados, etc.).
* **Sincronización (`page.update`):** A diferencia de otros frameworks, Flet requiere que notifiques a la página cuando has realizado cambios en el estado de los controles para que estos se rendericen en la pantalla.

> **Regla de oro:** Modificar una propiedad (ej. `text.value = "Nuevo"`) no cambia la pantalla hasta que se ejecuta `page.update()`.

---

### 1.4 Manejo de componentes gráficos de control
Los componentes son los bloques de construcción de la GUI. Se categorizan según su funcionalidad:

1.  **Componentes de Entrada:** * `TextField`: Para captura de texto.
    * `Dropdown`: Listas desplegables.
    * `ElevatedButton`: Botones con relieve para acciones principales.
2.  **Componentes de Visualización:** * `Text`: Para etiquetas y párrafos.
    * `Icon`: Iconografía de Material Design.
    * `Image`: Renderizado de imágenes locales o URL.
3.  **Componentes de Contenedor:** * `ListView`: Para listas largas que requieren scroll.
    * `Stack`: Para encimar elementos (uno sobre otro).
    * `Card`: Contenedores con sombra y bordes redondeados para agrupar información.



---

## Bibliografía

* Flet. (2024). *Flet fundamentals: Getting started*. Recuperado de https://flet.dev/docs/guides/python/getting-started
* Flet. (2024). *Reference: KeyboardEvent*. Recuperado de https://flet.dev/docs/controls/page#on_keyboard_event
* Google. (s. f.). *Material Design 3 Components*. Recuperado de https://m3.material.io/components
* Scribbr. (2026). *Generador de citas APA*. https://www.scribbr.es/citar/generador/
