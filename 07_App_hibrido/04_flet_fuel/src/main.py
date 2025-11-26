import flet as ft


def main(page: ft.Page):
    page.title = "App Flex Fuel"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    gasolina = ft.TextField(
        label="Preço da Gasolina",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    etanol = ft.TextField(
        label="Preço do Etanol",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Melhor abastecer com:"),
        content=ft.Text(size=20, weight="bold"),
        actions=[ft.TextButton("OK", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("FLEX FUEL", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            # expand=True,
        ),
        ft.ResponsiveRow(
            [ 
                ft.Container(gasolina, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(etanol, col={"sm": 6, "md": 4, "xl": 2}),
            ]
        )
    )


ft.app(main)
