import reflex as rx
def navbar() -> rx.Component:
    return rx.hstack(
        rx.link("Home", href="/",color="#5bfeee"),
        rx.link("About", href="/about",color="#5bfeee"),
        rx.link("Contact", href="/contact",color="#5bfeee"),
        rx.link("Proyects", href="/proyects",color="#5bfeee"),
        background="linear-gradient(rgba(253, 53, 140, 0.8),rgba(253, 53, 140, 0))",
        width="100%",
        height="65px",
        padding="1%",
        justify="between"
    )