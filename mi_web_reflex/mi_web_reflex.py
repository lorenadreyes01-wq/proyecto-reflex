"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# Definimos el Estado para que el botón sea interactivo
class State(rx.State):
    saludo: str = "¡Bienvenida a mi primera página web!"

    def actualizar_texto(self):
        self.saludo = "¡El botón funciona! Proyecto completado con éxito."

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # 1. Título principal
            rx.heading("Proyecto de Informática: Reflex", size="9", color_scheme="indigo"),
            
            # 2. Texto de bienvenida (que cambiará al pulsar el botón)
            rx.text(State.saludo, font_size="1.5em", font_weight="bold"),
            
            # 3. Botón interactivo
            rx.button(
                "Presiona para interactuar", 
                on_click=State.actualizar_texto,
                size="3",
                color_scheme="grass"
            ),
            
            spacing="5",
            align="center",
            padding="2em",
            box_shadow="lg",
            border_radius="15px",
            bg="white",
        ),
        height="100vh",
        background="linear-gradient(to top, #dfe9f3 0%, white 100%)",
    )

app = rx.App()
app.add_page(index)
