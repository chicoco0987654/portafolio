import reflex as rx

def links() ->  rx.Component:
    return rx.vstack(
        rx.button("instagram", href="https://www.instagram.com/r._el_chicoco/"),
        rx.button("linkedin", href="https://www.linkedin.com/in/raul-contreras-3b1b0b1a0/"),
        height="150%",
        
    )