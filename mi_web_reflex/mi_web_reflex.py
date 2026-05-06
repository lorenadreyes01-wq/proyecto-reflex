import reflex as rx

class The100State(rx.State):
 
    user_status: str = "MIEMBRO DEL ARCA (Estación Alfa)"
    location_text: str = "Coordenadas: Órbita Terrestre"
    badge_color: str = "sky"
    text_color: str = "#f1f5f9"
    bg_style: str = "linear-gradient(to right, #1e293b 0%, #334155 100%)"
    

    is_on_earth: bool = False
    is_confetti: bool = False

    def claim_the_earth(self):
        self.is_on_earth = True
        self.is_confetti = True
        self.user_status = "¡TERRESTRE (GROUNDER) / Trikru!"
        self.location_text = "Ubicación: Bosque (Cerca de Polis)"
        self.badge_color = "grass" # Verde selva
        self.text_color = "white"
        self.bg_style = "url('https://images.unsplash.com/photo-1549241400-096802c67618?q=80&w=2000&auto=format&fit=crop'), linear-gradient(to top, #111827 0%, #1c1c1c 100%)"
        self.bg_position = "center"
        self.bg_size = "cover"

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
     
            rx.heading(
                "THE 100: SURVIVAL LOG",
                size="9",
                weight="bold",
                color="#00D2FF", # Cyan estilo Sci-Fi
                font_family="Monospace",
                padding_top="1em"
            ),
            
            rx.text(
                "REGISTRO DE SUPERVIVENCIA DEL ARCA",
                color_secondary="gray",
                font_size="1.2em",
                letter_spacing="2px"
            ),

            rx.divider(border_color="#00D2FF", border_width="2px", width="80%"),
            
            rx.vstack(
                rx.text("Estatus del Usuario:", color="#8d8d8d"),
                rx.badge(
                    The100State.user_status,
                    size="3",
                    variant="soft",
                    color_scheme=The100State.badge_color,
                    border_radius="full",
                ),
                rx.text(The100State.location_text, font_size="1.1em", color="#f1f5f9"),
                spacing="4",
                align="center",
                background="#1c1c1c",
                padding="2em",
                border_radius="15px",
                box_shadow="0 0 15px rgba(0,210,255,0.2)",
            ),

            rx.button(
                "¡RECLAMAR LA TIERRA!",
                on_click=The100State.claim_the_earth,
                size="4",
                radius="full",
                color_scheme="grass",
                background="linear-gradient(to bottom, #4ade80, #166534)",
                _hover={
                    "transform": "scale(1.05)",
                    "background": "linear-gradient(to bottom, #86efac, #15803d)",
                },
                box_shadow="0px 5px 15px rgba(0,255,100,0.3)",
            ),
            
            rx.cond(
                The100State.is_confetti,
                rx.particle_confetti(),
            ),

            spacing="7",
            align="center",
            width="80%",
            max_width="700px",
            padding="3em",
            border_radius="25px",
            background_image="url('https://images.unsplash.com/photo-1549241400-096802c67618?q=80&w=2000&auto=format&fit=crop')" if The100State.is_on_earth else "",
            background="#1c1c1c",
            border="1px solid #00D2FF" if not The100State.is_on_earth else "1px solid green",
            transition="all 1s ease-in-out", # Transición suave
        ),
        height="100vh",
        background_image="url('https://images.unsplash.com/photo-1549241400-096802c67618?q=80&w=2000&auto=format&fit=crop')" if The100State.is_on_earth else "",
        background=The100State.bg_style, # Fondo dinámico
        transition="all 1s ease-in-out",
    )

app = rx.App()
app.add_page(index, title="The 100 Survival Log")