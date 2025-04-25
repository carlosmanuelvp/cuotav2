import flet as ft


class CustomElevatedButton(ft.ElevatedButton):
    def __init__(
        self,
        content,
        text=None,
        icon=None,
        on_click=None,
        disabled=False,
        bgcolor=None,
        color=None,
        width=50,
        height=50,
        size=15,
        style=ft.ButtonStyle(shape=ft.CircleBorder(), bgcolor="#1976D2", padding=15),
    ):
        super().__init__()
        self.content = content
        self.text = text
        self.icon = icon
        self.style = style
        self.on_click = on_click
        self.disabled = disabled
        self.bgcolor = bgcolor
        self.color = color
        self.width = width
        self.height = height

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            elevation=3,
        )
        self.tooltip = None
