import flet
from flet import Page, ElevatedButton


def main(page: Page):
    b1 = ElevatedButton(text="Tıkla", tooltip="Açıklama")
    page.controls.append(b1)
    page.update()


# flet.app(target=main)
flet.app(target=main, port=8080, view=flet.WEB_BROWSER)
