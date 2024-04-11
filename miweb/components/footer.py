import reflex as rx
def footer() -> rx.Component:
    return rx.vstack(
        rx.text("© 2024 Raul Contreras"),
    )