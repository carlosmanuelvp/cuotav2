import flet as ft


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
        multiline=False,
        min_lines=1,
        max_lines=1,
        validation_func=None,
        error_text=None,
        text_size=None,
        on_change=None,
    ):
        super().__init__()
        # eventos
        self.on_blur = self._on_blur_handler
        self._user_on_blur = on_blur
        self._validation_func = validation_func

        # variables
        self.text_size = text_size
        self.multiline = multiline
        self.min_lines = min_lines
        self.max_lines = max_lines
        self.height = height
        self.disabled = disable
        self.focused_color = ft.Colors.INDIGO_500
        self.suffix_icon = suffix_icon
        self.password = password
        self.label = label
        self.hint_text = hint_text
        self.hint_style = ft.TextStyle(color=ft.Colors.GREY_500)
        self.prefix_icon = prefix_icon
        self.error_style = ft.TextStyle(color=ft.Colors.RED_400)
        self.error_text = error_text
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
        self.on_change = on_change

    def _on_blur_handler(self, e):
        if self._validation_func:
            is_valid = self._validation_func(self.value)
            if not is_valid:
                self.error_border_color = ft.colors.RED_400
                self.update()
            else:
                self.error_border_color = None
                self.error_text = None
                self.update()

        if self._user_on_blur:
            self._user_on_blur(e)
