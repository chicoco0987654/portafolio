
from rxconfig import config

import reflex as rx
from miweb.components.navbar import navbar
from miweb.views.header.header import header
from miweb.components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        #navbar(),
        rx.hstack(
            header(),
            
        ),
        footer(),
        background_color="#1e1734",
    )


app = rx.App()
app.add_page(index)
