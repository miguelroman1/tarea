import flet as ft

def LoginView(page: ft.Page, auth_controller):
    
    email_input = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.PERSON,
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL,
        border_color="lightBlueAccent"
    )
    
    pass_input = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.KEY,
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10,
        border_color="lightBlueAccent"
    )
    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()

    login_button = ft.ElevatedButton(
        "Iniciar sesión",
        width=250,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_400,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    pass_input.on_submit = login_click
    
    registro = ft.ElevatedButton(
        "Registrarme",
        width=200,
        on_click=lambda _: page.go("/registro"),
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Login"),
            bgcolor="lightBlueAccent",
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al Sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    ft.TextButton(
                        "Crear una cuenta nueva",
                        on_click=lambda _: page.go("/registro")
                    )
                    
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )