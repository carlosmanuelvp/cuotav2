import flet as ft
from models import AppStatus as app_status

# from frontend.views.login_vies import
from frontend.title_bar import create_titlebar
from frontend.views.login_views import LoginViewPage
from frontend.views.main_view import MainView


class MainController:
    def __init__(self, page: ft.Page):
        self.page = page

        self.configure_view()
        self.build_ui()

    def configure_view(self):
        self.page.window.width = 330
        self.page.window.height = 595
        self.page.padding = 0
        self.title_bar_buttons_hidden = True
        self.title_bar_hidden = True
        self.page.window.title_bar_hidden = True
        self.page.window.title_bar_buttons_hidden = True
        self.page.window.frameless = False
        self.page.bgcolor = ft.Colors.BROWN_50

    def build_ui(self):
        self.main_login_view = LoginViewPage(page=self.page)
        self.main_view = MainView(page=self.page)
        if app_status.is_login:
            self.page.add(create_titlebar(self.page), self.main_view.build_ui())

        else:
            self.page.add(create_titlebar(self.page), self.main_login_view.build_ui())

    # self.main_view = MainViewPage(page=self.page)
    # self.page.add(create_titlebar(self.page), self.main_view.build_ui())
