from typing import Callable
from nicegui import ui, app
from src.state.card_search import search, get_card_types
from src.ui.grid import grid


def header():
    with ui.header().classes("bg-gray-900 text-white p-4 font-bold text-xl"):
        ui.label("Card Explorer").classes("text-center")

def search_bar(search_query: str, search_amount: int, handle_search: Callable):
    with ui.column().classes("w-full"):
        with ui.row().classes("bg-white flex w-full p-6 shadow-md items-center gap-4"):
            search_input = ui.input(value=search_query,placeholder="Search for cards...").props("filled dense").classes("flex-1 min-w-0")
            result_limit = ui.select(["10", "25", "50", "100"], value=str(search_amount)).props("rounded dense").classes("w-24")
            ui.button("Search", icon="search", on_click=lambda: handle_search(search_input.value, int(result_limit.value))).props("color=primary")

def scrollable_selector(items: dict[str, bool], handle_selected_types: Callable):
    with ui.scroll_area():
        for item, is_checked in items.items():
            ui.checkbox(item, value=is_checked, on_change=lambda e: handle_selected_types(e)).props("rounded").classes("mb-2")
@ui.refreshable
def filters(cards_filters: dict[str, bool], handle_selected_types: Callable):
    ui.label("Card Type").classes("font-bold text-lg mb-2")
    scrollable_selector(cards_filters, handle_selected_types)
    ui.separator()
    ui.label("Card Attribute").classes("mt-4 font-medium")
    attributes = ["Light", "Dark", "Earth", "Fire", "Water", "Wind", "Divine"]
    scrollable_selector({attr: False for attr in attributes}, handle_selected_types)
    ui.separator()
    ui.label("Card Level").classes("mt-1 font-medium")
    with ui.row().classes("w-full text-center items-center justify-between"):
        ui.label('1')
        ui.slider(min=1, max=12, value=4).props('label-always').classes("w-2/3")
        ui.label('12').classes("text-center")

@ui.refreshable
def content(cards_types: list[str], handle_checkbox_change: Callable):
    cards, set_cards = ui.state([])
    search_amount, set_search_amount = ui.state(10)
    search_query, set_search_query = ui.state('')

    async def update_search_results(query: str, limit: int):
        try:
            search_amount = limit
            search_query = query
            set_search_query(search_query)
            set_search_amount(search_amount)
            selected = [t for t, val in cards_types.items() if val]
            results = await search(query, limit, selected)
        except Exception as e:
            ui.notify(f"Error: {e}", color="negative")
            return
        ui.notify(f"Found {len(results)} result(s)", color="info")
        set_cards(results)
        grid.refresh(results)
    
    # ui.timer(0,get_cards_types,once=True)
    ui.dark_mode()
    ui.query("body").classes("bg-gray-100")
    with ui.row().classes("flex w-full p-10 mr-10 gap-6"):
        search_bar(search_query, search_amount, update_search_results)
        with ui.row().classes("flex w-full"):
            with ui.column().classes("flex-2 w-1/6 bg-white p-4 rounded shadow-md h-fit mt-0"):
                filters(cards_types, handle_checkbox_change)
            with ui.column().classes("flex-1 px-4h-fit mt-0"):
                grid(cards)

def footer():
    with ui.footer().classes("bg-gray-900 text-white p-4 text-center"):
        with ui.row().classes("flex justify-center items-center gap-2"):
            ui.label("Made by Richard Nunes. Source code available at").classes("text-sm")
            ui.link("GitHub", "https://github.com/richlpn/YugiohExplorer")

@ui.page('/')
async def page():
    if "cards_types" not in app.storage.user:
        app.storage.user.cards_types = {x: False for x in await get_card_types()}
    
    cards_types = app.storage.user.cards_types
    def handle_checkbox_change(event):
        card_type = event.sender.text
        app.storage.user.cards_types[card_type] = event.sender.value
        ui.notify(f"Checkbox changed: {card_type} is {'checked' if event.sender.value else 'unchecked'}")
    header()
    content(cards_types, handle_checkbox_change)
    footer()
ui.run(storage_secret="Secret key", title="YuGiOh Card Search")
