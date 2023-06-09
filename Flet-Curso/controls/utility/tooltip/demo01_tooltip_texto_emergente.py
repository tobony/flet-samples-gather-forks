import math

import flet as flt
from flet import *


def main(page: Page):
    page.title = "Tooltip"

    page.add(
        Tooltip(
            message='This is a tooltip',
            content=Text('Hover to see tooltip'),
            padding=20,
            border_radius=10,
            text_style=TextStyle(size=20, color=colors.WHITE),
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=alignment.Alignment(0.8, 1),
                colors=[
                    "0xff1f005c",
                    "0xff5b0060",
                    "0xff870160",
                    "0xffac255e",
                    "0xffca485c",
                    "0xffe16b5c",
                    "0xfff39060",
                    "0xffffb56b",
                ],
                tile_mode=GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            )
        )
    )


if __name__ == "__main__":
    flt.app(target=main)
