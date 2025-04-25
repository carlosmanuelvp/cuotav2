import flet as ft


class CustomControllerBasePage(ft.Container):
    def __init__(
        self,
        content,
        alignment=None,
        padding=8,
        margin=0,
        border=None,
        border_radius=None,
        width=None,
        height=None,
        visible=True,
    ):
        super().__init__()
        self.content = content
        self.alignment = alignment
        self.padding = padding
        self.margin = margin

        self.border = border
        self.border_radius = border_radius
        self.width = width
        self.height = height
        self.expand = True
        self.visible = visible
