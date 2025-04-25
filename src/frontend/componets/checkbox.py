import flet as ft


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
