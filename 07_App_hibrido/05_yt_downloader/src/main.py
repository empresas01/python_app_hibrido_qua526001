import flet as ft
from pytubefix import YouTube

import os
import threading


def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/youtube.png"


    # cria as pastas caso não existam
    caminho_videos = "videos"
    caminho_audios = "audios"
    os.makedirs(caminho_videos, exist_ok=True)
    os.makedirs(caminho_audios, exist_ok=True)

    # componentes da interface gráfica
    titulo = ft.Textfield(
        label="Cole a URL do video do YouTube aqui",
        width=400,
        border_radius=10
    )

    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets", "youtube.png")
    logo_cabecalho = ft.Image(src=logo_path, width=300, height=200)

    # componente para mostrar informações do video
    video_info = ft.container(
        content=ft.Column([]),
        visible=False,
        padding=10,
        border_radius=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        width=400
    )

    # barra de progresso
    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.Colors.BLUE,
        bgcolor=ft.Colors.BLUE_GREY_50
    )


    status_text = ft.Text(
        "",
        color=ft.Colors.BLACK,
        size=14,
        text_align=ft.TextAlign.CENTER
    )

    # nistrar as informações do video na interface
    def mostrar_info_video(yt):
        try:
            # Limpa o container
            video_info.content.controls.clear()

            # adicionar informações do video
            video_info.content.controls.extend(
                [
                    ft.Text(f"Título: {yt.title}", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Canal: {yt.author}", size=12),
                    ft.Text(f"Duração: {yt.length/60}:{yt.length%60:02d}",size=12),
                    ft.Text(f"Views: {yt.views}", size=12),
                ]
            )
            
            video_info.visible = True
            page.update()

        except Exception as e:
            status_text.value = f"Erro ao obter informações do vídeo: {str(e)}"
            status_text.color = ft.Colors.RED
            page.update()

    # função para baixar o video
    def baixar_video(e):
        if not url.value.strip():
            status_text.value = "Por favor, insira uma URL válida."
            status_text.color = ft.Colors.ORANGE
            page.update()
            return
        
        def download_thread():
            try:
                progress_bar.visible = True
                status_text.value = "Baixando vídeo..."
                status_text.color = ft.Colors.BLUE
                page.update()

                # cria objeto do youtube
                yt = YouTube(url.value.strip())

                # mostra as informações do video
                mostrar_info_video(yt)

                # iniciar o download
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=caminho_videos)

                progress_bar.visible = False
                status_text.value = "Download concluído!"
                status_text.color = ft.Colors.GREEN
                page.update()

            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro ao baixar vídeo: {str(e)}"
                status_text.color = ft.Colors.RED
                page.update()
    page.add(
        ft.SafeArea(
            ft.Container(
                
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
