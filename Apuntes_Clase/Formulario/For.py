import flet as ft
import re

def main(page: ft.Page):
    page.title = "Registro de Estudiantes - Topicos Avanzados"
    page.bgcolor = "#FDFBE3"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Campos de entrada ---
    txt_nombre = ft.TextField(
        label="Nombre", 
        border_color="#4D2A32", 
        hint_text="Solo letras"
    )
    txt_control = ft.TextField(
        label="Numero de control", 
        border_color="#4D2A32",
        keyboard_type=ft.KeyboardType.NUMBER,
        hint_text="Solo numeros"
    )
    txt_email = ft.TextField(
        label="Email", 
        border_color="#4D2A32",
        hint_text="ejemplo@correo.com"
    )

    dd_carrera = ft.Dropdown(
        label="Carrera",
        border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Ingenieria en Sistemas"),
            ft.dropdown.Option("Ingenieria Civil"),
            ft.dropdown.Option("Ingenieria Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 11)]
    )

    radio_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino"),
            ft.Radio(value="Femenino", label="Femenino"),
            ft.Radio(value="Otro", label="Otro")
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    # --- Funciones de control ---

    def cerrar_dialogo(e):
        dlg_datos.open = False
        page.update()

    dlg_datos = ft.AlertDialog(
        title=ft.Text("Datos Recogidos"),
        actions=[
            ft.TextButton("Cerrar", on_click=cerrar_dialogo),
        ],
    )

    def validar_y_enviar(e):
        # Limpiar errores previos
        txt_nombre.error_text = None
        txt_control.error_text = None
        txt_email.error_text = None
        
        # Captura de valores
        nom = txt_nombre.value.strip() if txt_nombre.value else ""
        con = txt_control.value.strip() if txt_control.value else ""
        ema = txt_email.value.strip() if txt_email.value else ""
        car = dd_carrera.value
        sem = dd_semestre.value
        gen = radio_genero.value

        # 1. Validacion de campos vacios
        if not nom or not con or not ema or not car or not sem or not gen:
            # Crear y mostrar SnackBar inmediatamente
            snack = ft.SnackBar(
                content=ft.Text("Advertencia: No se puede dejar espacios vacios"),
                bgcolor=ft.Colors.RED_700,
            )
            page.overlay.append(snack)
            snack.open = True
            page.update()
            return

        # 2. Validacion de Nombre (letras y espacios)
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nom):
            txt_nombre.error_text = "No se permiten numeros ni simbolos"
            page.update()
            return

        # 3. Validacion de Control (solo numeros)
        if not con.isdigit():
            txt_control.error_text = "Solo se permiten numeros"
            page.update()
            return

        # 4. Validacion de Email
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", ema):
            txt_email.error_text = "Correo invalido"
            page.update()
            return

        # 5. Si todo es correcto, mostrar Dialogo
        dlg_datos.content = ft.Text(
            f"Nombre: {nom}\n"
            f"Control: {con}\n"
            f"Email: {ema}\n"
            f"Carrera: {car}\n"
            f"Semestre: {sem}\n"
            f"Genero: {gen}"
        )
        page.overlay.append(dlg_datos)
        dlg_datos.open = True
        page.update()

    # --- Boton ---
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar Datos", color="white"),
        bgcolor="#4D2A32",
        width=400,
        on_click=validar_y_enviar
    )

    # --- Layout ---
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("REGISTRO DE ESTUDIANTE", size=25, weight="bold", color="#4D2A32"),
                txt_nombre,
                txt_control,
                txt_email,
                ft.Row([dd_carrera, dd_semestre], spacing=10),
                ft.Text("Genero:", weight="bold", color="#4D2A32"),
                radio_genero,
                btn_enviar
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
            padding=20,
            bgcolor="white",
            border_radius=10,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK12)
        )
    )

ft.app(target=main)
