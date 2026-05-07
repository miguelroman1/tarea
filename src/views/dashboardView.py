import flet as ft

def DashboardView(page, tarea_controller):
    user = page.user_data
    
    if not user:
        page.go("/")
        return
    
    page.controls.clear()
    page.title = f"Dashboard - {user['nombre']}"
    
    # Crear componentes
    titulo = ft.Text(f"Bienvenido, {user['nombre']}", size=24, weight="bold")
    txt_titulo = ft.TextField(label="Nueva Tarea", width=300)
    btn_agregar = ft.ElevatedButton("Agregar", bgcolor=ft.Colors.GREEN_400)
    lista_tareas = ft.Column()
    
    def refresh():
        lista_tareas.controls.clear()
        user_id = user.get('id_usuario') or user.get('id')
        
        try:
            tareas = tarea_controller.obtener_lista(user_id)
            for t in tareas:
                lista_tareas.controls.append(
                    ft.Container(
                        content=ft.Text(f"• {t['titulo']}"),
                        padding=5,
                        border=ft.border.all(1, ft.Colors.GREY_400),
                        border_radius=5,
                        margin=5
                    )
                )
        except Exception as e:
            lista_tareas.controls.append(ft.Text(f"Error: {e}", color="red"))
        
        page.update()
    
    def add_task(e):
        if txt_titulo.value:
            tarea_controller.guardar_nueva(
                user['id_usuario'], 
                txt_titulo.value, 
                "", 
                "media", 
                "trabajo"
            )
            txt_titulo.value = ""
            refresh()
    
    btn_agregar.on_click = add_task
    
    # Agregar todo a la página
    page.add(
        titulo,
        ft.Row([txt_titulo, btn_agregar]),
        ft.Divider(),
        ft.Text("Mis Tareas:", size=18, weight="bold"),
        lista_tareas,
        ft.Divider(),
        ft.ElevatedButton("Cerrar sesión", on_click=lambda _: page.go("/"))
    )
    
    refresh()
    page.update()