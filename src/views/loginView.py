import flet as ft

def LoginView(page: ft.Page):
    email_input = ft.TextField(label="Email", width=350, border_radius=10)
    pass_inpot = ft.TextField(label="Password", width=350, border_radius=10, password=True, can_reveal_password=True)
    
    def login_click(e):
        user, msg = auth_controller.login(email_input.value, pass_inpot.value)
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
    return ft.view("/", [
        
    ))