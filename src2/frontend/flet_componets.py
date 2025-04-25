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


class CustomContainer(ft.Container):
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


class CustomTextField(ft.TextField):
    def __init__(
        self,
        label,
        hint_text=None,
        prefix_icon=None,
        error_style=None,
        width=250,
        password=False,
        bgcolor="white",
        border_radius=10,
        suffix_icon=None,
        height=None,
        can_reveal_password=False,
        disable=False,
        on_blur=None,
        disabled=False,
    ):
        super().__init__()
        # meventos
        self.on_blur = on_blur
        # varibales

        self.height = height
        self.disabled = disable
        self.focused_color = ft.Colors.INDIGO_500
        self.suffix_icon = suffix_icon
        self.password = password
        self.label = label
        self.hint_text = hint_text
        self.hint_style = ft.TextStyle(color=ft.Colors.GREY_500)
        self.prefix_icon = prefix_icon
        self.error_style = error_style
        self.border_color = ft.Colors.GREY_400
        self.border_radius = 10
        self.width = width
        self.bgcolor = ft.Colors.WHITE
        self.text_style = ft.TextStyle(color=ft.Colors.BLACK)
        self.border_radius = border_radius
        self.cursor_color = ft.Colors.BLACK
        self.bgcolor = bgcolor
        self.focused_color = ft.Colors.BLACK54
        self.text_size = 14
        self.can_reveal_password = can_reveal_password

    class CustomCheckbox(ft.Checkbox):
        def __init__(
            self,
            is_error=None,
            color=None,
            label="",
            value=False,
            disabled=False,
            fill_color=None,
            check_color=None,
            width=None,
        ):
            super().__init__()
            self.active_color = ft.Colors.INDIGO_500
            self.is_error = is_error
            self.label = label
            self.value = value
            self.disabled = disabled
            self.fill_color = fill_color
            self.check_color = check_color
            self.width = width

            self.scale = 1.0
            self.tooltip = None


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
