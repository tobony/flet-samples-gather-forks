import flet as ft

def main(page: ft.Page):
    page.title = "Draggable VerticalDivider example"            
    
    def move_vertical_divider(e: ft.DragUpdateEvent):
        c.width += e.delta_x
        page.update()

    c = ft.Container(
                    bgcolor=ft.colors.ORANGE_300,
                    alignment=ft.alignment.center,
                    width=100,
                    #expand=1,
                )
    page.add(ft.Row(controls=
            [
                c,
                ft.GestureDetector(
                    content=ft.VerticalDivider(),
                    on_pan_update=move_vertical_divider),
                ft.Container(
                    bgcolor=ft.colors.BROWN_400,
                    alignment=ft.alignment.center,
                    expand=1,
                ),
            ],
            spacing=0,
            width=400,
            height=400
        )
    )
ft.app(target=main)            
