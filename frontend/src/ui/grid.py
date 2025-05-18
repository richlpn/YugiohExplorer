
from nicegui import ui
from src.schema.card import Card

@ui.refreshable
def grid(items: list["Card"]):
    results_container = ui.row().classes("flex-wrap items-stretch justify-start gap-6 w-full")
    results_container.clear()
    for card in items:
        with results_container:
            with ui.card().classes("w-72 shadow-md hover:shadow-lg transition-shadow duration-300"):
                ui.image(card.image_url[-1].image_url_small).classes("w-full object-cover")
                with ui.card_section():
                    ui.label(card.name).classes("font-bold text-lg")
                    ui.label(card.desc).classes("text-sm text-gray-700 line-clamp-2")