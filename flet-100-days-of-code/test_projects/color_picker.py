import flet as ft
import colorsys

WIDTH = 10
HEIGHT = 10
SQUARE_SIZE = 40
CIRCLE_SIZE = SQUARE_SIZE*2

class CustomColorPicker(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.content = ft.Column()
        self.generate_color_matrix(hue=0)
        self.on_dismiss=lambda e: print("Dialog dismissed!")
    
    def generate_color_matrix(self, hue):
        def rgb2hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255.0), int(rgb[1]*255.0), int(rgb[2]*255.0))
        
        selected_color = ft.Text("#0a0a0a")
        color_matrix = ft.Stack(
            height=HEIGHT*SQUARE_SIZE+CIRCLE_SIZE, 
            width=WIDTH*SQUARE_SIZE+CIRCLE_SIZE
            )
        self.content.controls = []
        #colors.controls = []

        def pick_color(e):
            circle.top = e.control.top + SQUARE_SIZE/2 - CIRCLE_SIZE/2
            circle.left = e.control.left + SQUARE_SIZE/2 - CIRCLE_SIZE/2
            circle.content.bgcolor = e.control.bgcolor
            circle.update()
            selected_color.value = e.control.bgcolor
            selected_color.update()

        for j in range (0, HEIGHT):
            for i in range (0, WIDTH):
                #color = rgb2hex(colorsys.hsv_to_rgb(i/WIDTH,  1, 1 * (HEIGHT - j + 1) / HEIGHT))
                color = rgb2hex(colorsys.hsv_to_rgb(hue,  (i) /WIDTH, 1 * (HEIGHT - j) / HEIGHT))
                color_matrix.controls.append(ft.Container(
                    height=SQUARE_SIZE, 
                    width=SQUARE_SIZE, 
                    bgcolor=color, 
                    on_click=pick_color,
                    top = j*SQUARE_SIZE+CIRCLE_SIZE/2,
                    left = i*SQUARE_SIZE+CIRCLE_SIZE/2  ))

        def find_color(x, y):
            for color_square in color_matrix.controls[:-1]:
                #if (control.top < x and control.top > x-SQUARE_SIZE) and (control.left < y and control.left > y-SQUARE_SIZE):
                if x > color_square.top and x < color_square.top + SQUARE_SIZE and y > color_square.left and y < color_square.left + SQUARE_SIZE:
                    return color_square.bgcolor
            return 'blue'

        def on_pan_end(e: ft.DragEndEvent):
            e.control.content.bgcolor = find_color(x = e.control.top + CIRCLE_SIZE/2, y = e.control.left + CIRCLE_SIZE/2)
            e.control.update()
            selected_color.value = e.control.content.bgcolor
            selected_color.update()
        
        def on_pan_update(e: ft.DragUpdateEvent):
            
            e.control.top = max(0, e.control.top + e.delta_y)
            e.control.left = max(0, e.control.left + e.delta_x)
            e.control.update()

        circle = ft.GestureDetector(
            top = HEIGHT*SQUARE_SIZE,
            left = 0,
            on_pan_update=on_pan_update,
            on_pan_end=on_pan_end,
            content=ft.Container(
            width=CIRCLE_SIZE,
            height=CIRCLE_SIZE,
            bgcolor='#0a0a0a',
            border_radius=SQUARE_SIZE*5,
            border=ft.border.all(width=2, color='white')))

        color_matrix.controls.append(circle)
        
        
        self.content.controls.append(color_matrix)
        self.content.controls.append(selected_color)
        #self.update()


def main(page: ft.Page):
    
    color_picker = CustomColorPicker()
    page.dialog = color_picker

    def open_color_picker(e):
        color_picker.open = True
        page.update()
    
    page.add(ft.IconButton(icon=ft.icons.BRUSH, on_click=open_color_picker))
    
ft.app(target=main)