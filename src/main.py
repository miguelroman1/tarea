import flet as ft
from controllers.TareaControllers import TareaController
from controllers.UserController import AuthController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            #caso 1: login
            page.add(ft.Text("Caso 1"))
            page.views.append(LoginView(page, auth_ctrl))

            #caso 2: dashboard
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))

        #caso de seguridad: Si algo falla, mostrar texto de error
        if not page.views:
            page.views.append(
                ft.View("/",[ft.Text("Error: Ruta no encontrada o vista vacia")])
            )

        page.update()

    page.on_route_change = route_change
    page.go("/")



def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()