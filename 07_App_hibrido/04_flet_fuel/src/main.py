import flet as ft
import os 

def main(page: ft.Page):
    # Definindo a cor de fundo da página como AMARELO
    page.bgcolor = ft.Colors.YELLOW 
    
    # ... (restante da função calcular_combustivel permanece o mesmo)
    def calcular_combustivel(e):
        if not gasolina.value:
            gasolina.error_text = "Valor da gasolina não pode ficar vazio."
            gasolina.update()
            return 
        if not etanol.value:
            etanol.error_text = "Valor do etanol não pode ficar vazio."
            etanol.update()
            return 

        gasolina.error_text = ""
        etanol.error_text = ""
        gasolina.update()
        etanol.update()

        try:
            gasolina_val = float(gasolina.value.replace(",", "."))
            etanol_val = float(etanol.value.replace(",", "."))
            resultado = "Gasolina" if (gasolina_val * 0.7) < etanol_val else "Etanol"
            dlg_modal.content.value = resultado

            page.open(dlg_modal)  
            page.update()
        except ValueError:
            gasolina.error_text = "Entrada inválida. Use números."
            etanol.error_text = "Entrada inválida. Use números."
            page.update()
                
    page.title = "App Flex Fuel"
    page.scroll = "adaptive"
    
    # --- Alteração aqui: Adicionando bgcolor branco aos TextFields ---
    gasolina = ft.TextField(
        label="Preço da Gasolina",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER,
        bgcolor=ft.Colors.WHITE, # Fundo branco para a caixa de input
    )
    etanol = ft.TextField(
        label="Preço do Etanol",
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=calcular_combustivel,
        bgcolor=ft.Colors.WHITE, # Fundo branco para a caixa de input
    )
    # ---------------------------------------------------------------

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Melhor abastecer com:"),
        content=ft.Text(size=40,color="red", weight="bold"), 
        actions=[ft.TextButton("OK", on_click=lambda e:page.close(dlg_modal))],
        actions_alignment=ft.MainAxisAlignment.END
    )

    botao_imagem_calcular = ft.Container(
        content=ft.Image(
            src="calcular_icon.png", 
            width=100, 
            height=100,
            fit=ft.ImageFit.CONTAIN
        ),
        on_click=calcular_combustivel, 
        padding=ft.padding.all(10),
        tooltip="Calcular melhor combustível"
    )
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Álcool ou Gasolina?", size=30, weight="bold", color=ft.Colors.BLACK), 
                alignment=ft.alignment.center,
                padding=ft.padding.all(20
            ),)
        ),
        ft.ResponsiveRow(
            [ 
                ft.Container(gasolina, col={"sm": 6, "md": 4, "xl": 2}),
                ft.Container(etanol, col={"sm": 6, "md": 4, "xl": 2}),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
       ),
       ft.Row(
           [
               ft.Container(
                   botao_imagem_calcular,
                    padding=30                      
               )
           ],
           alignment=ft.MainAxisAlignment.CENTER
       )
    )

ft.app(target=main, assets_dir="assets")