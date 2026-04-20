import flet as ft

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(label="Email", width=350, border_radius=10)
    pass_input = ft.TextField(label="Password", width=350, border_radius=10, password=True, can_reveal_password=True)
    
    def login_click(e):
    if not email_input.value or not pass_input.value:
        page.snac_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
        page.Snack_bar.open = True
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
            
    return ft.View(
        route = "/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )