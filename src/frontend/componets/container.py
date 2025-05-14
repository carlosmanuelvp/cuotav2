import flet as ft


class   CustomContainer(ft.Container):
    def __init__(
        self,
        content,
        gradient=None,
        visible=True,
        padding=8,
        margin=0,
        bgcolor=None,
        border=None,
        border_radius=None,
        width=None,
        height=None,
        expand=False,
        alignment=None,
        opacity=None,
    ):
        super().__init__()

        self.expand = expand
        self.gradient = gradient
        self.content = content
        self.alignment = alignment
        self.padding = padding
        self.margin = margin
        self.bgcolor = bgcolor
        self.border = border
        self.border_radius = border_radius
        self.width = width
        self.height = height
        self.expand = False
        self.visible = visible
        self.opacity = opacity
