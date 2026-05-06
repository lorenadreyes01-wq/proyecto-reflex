import reflex as rx

class The100State(rx.State):
    # Variables de estado
    user_status: str = "SISTEMA DEL ARCA: EN ÓRBITA"
    location: str = "Sector: Espacio Exterior"
    on_earth: bool = False
    
    # Colores y Estilos dinámicos
    theme_color: str = "#00D2FF" # Cyan para el espacio
    bg_style: str = "linear-gradient(to bottom, #0f172a, #1e293b)"

    def bajar_a_la_tierra(self):
        self.on_earth = True
        self.user_status = "¡SURVIVOR: TERRESTRE!"
        self.location = "Sector: Tierra (Bosque)"
        self.theme_color = "#4ade80" # Verde para la tierra
        # Cambiamos el fondo a uno más oscuro/selvático
        self.bg_style = "linear-gradient(to top, #052e16, #14532d)"

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Título principal
            rx.heading(
                "THE 100: SURVIVAL LOG",
                size="9",
                color=The100State.theme_color,
                font_family="Monospace",
                transition="all 0.5s ease",
            ),
            
            # Texto de bienvenida
            rx.text(
                "Protocolo de Supervivencia Activado",
                color="gray",
                font_size="1.1em",
            ),

            # Tarjeta de Información
            rx.vstack(
                rx.badge(
                    The100State.user_status,
                    variant="soft",
                    color_scheme="sky" if not The100State.on_earth else "grass",
                    size="3",
                ),
                rx.text(The100State.location, font_weight="bold"),
                spacing="3",
                align="center",
                background="#111827",
                padding="2em",
                border_radius="lg",
                border=f"1px solid {The100State.theme_color}",
            ),

            # Botón Interactivo (Requisito)
            rx.button(
                "¡BAJAR A LA TIERRA!",
                on_click=The100State.bajar_a_la_tierra,
                size="4",
                color_scheme="grass",
                # Efecto visual al pasar el mouse
                _hover={"transform": "scale(1.1)", "transition": "0.3s"},
                disabled=The100State.on_earth,
            ),

            # Condicional Creativo: Mensaje de éxito con animación
            rx.cond(
                The100State.on_earth,
                rx.text(
                    "¡BIENVENIDA A CASA, LORENA!",
                    font_size="1.5em",
                    color="#4ade80",
                    animation="bounce 1s infinite",
                    font_weight="bold",
                ),
            ),

            spacing="6",
            align="center",
            padding="4em",
            border_radius="25px",
            background="#0f172a",
            box_shadow="0 0 20px rgba(0,0,0,0.5)",
        ),
        height="100vh",
        background=The100State.bg_style,
        transition="all 1s ease",
    )

app = rx.App()
app.add_page(index, title="The 100 Survival")