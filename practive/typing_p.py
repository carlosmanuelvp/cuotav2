LoginView="erw"

def setup_views(self):
        self.views = {
            "login": LoginView(self.page),
            "dashboard": DashboardView(self.page),
            #"ajustes": AjustesView(self.page, self),
           # "historial": HistorialView(self.page, self),
           # "ayuda": AyudaView(self.page, self),
        }

        self.stack = ft.Stack(expand=True)

        for key, view in self.views.items():
            container = CustomControllerBasePage(
                content=view.build_ui(),


            )
