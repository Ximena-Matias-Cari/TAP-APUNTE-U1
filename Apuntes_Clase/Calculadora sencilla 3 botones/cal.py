import flet as ft

def main(page: ft.Page):

    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    # DISPLAY
    display = ft.Container(
        content=ft.Text("0", size=30),
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
    )

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

    # GRID DE BOTONES
    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=210,
        height=220,
        expand=False
    )

    # BOTONES
    numeros = ["1", "2", "3", "AC"]

    for n in numeros:
        grid.controls.append(
            ft.ElevatedButton(
                content=ft.Text(n, size=16),
                data=n,
                on_click=agregar_numero,
                height=50
            )
        )

    # LAYOUT PRINCIPAL
    layout_principal = ft.Column(
        controls=[
            display,
            grid
        ],
        tight=True
    )

    page.add(layout_principal)
    page.update()

ft.app(target=main)
