import flet as ft

# Use of GestureDetector for with on_pan_update event for dragging card
# Absolute positioning of controls within stack

def main(page: ft.Page):

    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_update=drag,
        left=0,
        top=0,
        animate_position=1000,
        content=ft.Container(bgcolor=ft.colors.GREEN, width=70, height=100),
    )    

    page.add(ft.Stack(controls=[card], width=1000, height=500))

ft.app(target=main)
