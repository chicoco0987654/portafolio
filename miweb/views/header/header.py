import reflex as rx
from miweb.views.links.links import links

def header() -> rx.Component:
    return rx.hstack(
        rx.box(
          rx.vstack(
            rx.avatar(src="https://media.licdn.com/dms/image/D4E03AQF-vftiPEpfRg/profile-displayphoto-shrink_800_800/0/1705319047780?e=1718236800&v=beta&t=nlXw5CPUXgMlY_8GgglTgDx7Iej86T5pyFAWuS71ZKI",
                  name="Raul Contreras",
                  size="8",
                  border_radius="50%",
                  box_shadow=("0 0 5px #fff",
                            "0 0 10px #fff",
                            "0 0 20px #fff",
                            "0 0 30px #0ff",),
                    margin_top="10%",
                    margin_left="15%",
                  ),
                  rx.text("Raul Contreras",
                          color="white",
                          font_size="30px",
                          font_weight="bold",
                          font_family="consolas",
                          position_X="center",
                          margin_left="5%",
                          ),
            ) ,
            background_color="black",
            border_radius="15px",
            #fd358c
            box_shadow=("0 0 5px #fd358c",
                        "0 0 10px #fd358c",
                        "0 0 20px #fd358c",
                        "0 0 40px #fd358c",
                        "0 0 80px #fd358c",
                        "0 0 90px #fd358c",
                        "0 0 100px #fd358c",
                        "0 0 150px #fd358c"
            ),
            height="auto",
            width="200px",
            margin_left="10%",
        )
        ,
        
        rx.box(
            rx.text("""Hola soy Raul Contreras, soy estudiante de ingenieria civil en computacion e informatica en la Universidad mayor, me gusta la programacion y la tecnologia,
                     me gusta aprender cosas nuevas y me gusta la musica, soy de Santiago, Chile.""",
                     ),
            background_color="black",
            color="white",
            width="40%",
            margin="10%",
            padding="5%",
            box_shadow=("0 0 5px #fff",
                "0 0 10px #fff",
                "0 0 20px #fff",
                "0 0 40px #0ff",
                "0 0 80px #0ff",
                "0 0 90px #0ff",
                "0 0 100px #0ff",
                "0 0 150px #0ff"),
                border_radius="15px",
                text_align="justify",
                
        ),
        justify="between",
        max_height="500px",
        margin_top="15%",
    )
