from fasthtml.common import *
from monsterui.all import *

def create_menu():
    """Create a fixed navigation bar that's consistent across all pages"""
    nav_structure = [
        {
            "label": "Features",
            "items": [
                ("Compressor", "/compress", "sliders"),
                ("Benchmark", "/benchmark", "chart-bar"),
            ]
        },
        {
            "label": "Resources",
            "items": [
                ("Blog", "/blog", "file-text"),
                ("Documentation", "https://fasterai-labs.github.io/fasterai/quickstart.html", "book"),
            ]
        },
        {
            "label": "About",
            "items": [
                ("Our Team", "/team", "users"),
                ("The Company", "/about", "building"),
            ]
        }
    ]

    # Create navigation items with dropdowns
    nav_items = []
    for nav in nav_structure:
        dropdown_items = Div(
            *[
                A(
                    DivHStacked(
                        UkIcon(icon, height=16, cls="text-orange-500"),
                        Span(label, cls="ml-2"),
                        cls="px-4 py-2 hover:bg-neutral-700/40 rounded-md w-full"
                    ),
                    href=link,
                    cls="text-neutral-200 transition-colors duration-200 block"
                )
                for label, link, icon in nav["items"]
            ],
            cls="absolute top-full mt-2 py-2 w-48 bg-neutral-800/40 backdrop-blur-md rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 ease-in-out border border-neutral-700"
        )
        
        nav_items.append(
            Div(
                Div(
                    nav["label"],
                    UkIcon("chevron-down", height=16, 
                          cls="ml-1 transition-transform duration-200 group-hover:rotate-180 transform-gpu"),
                    cls="flex items-center cursor-pointer px-4 py-2"
                ),
                dropdown_items,
                cls="relative group text-neutral-300 hover:text-orange-500 transition-colors duration-200"
            )
        )

    # Create the navigation bar
    return Nav(
        Div(
            # Logo/Brand section and Navigation links grouped together
            DivHStacked(
                A(
                    Img(src="/static/imgs/logo/logo.png", width=40, height=40,
                        cls="transition-transform duration-200 hover:scale-95 transform-gpu"),
                    Span("FasterAI", cls="pl-4"),
                    href="/",
                    cls="flex items-center text-xl font-bold text-neutral-100 hover:text-orange-500 transition-colors duration-200"
                ),
                # Navigation links with dropdowns - moved closer to company name
                Div(*nav_items, cls="hidden md:flex items-center space-x-2 ml-8"),
                cls="flex items-center"  # Changed to just flex and items-center
            ),
            # Contact Us button in its own container
            A("Contact Us", 
              href="mailto:contact@fasterai.com",
              cls="bg-orange-500 hover:bg-orange-600 text-sm px-4 py-2 rounded text-white ml-auto transition-all duration-200 hover:shadow-inner hover:-translate-y-0.5 active:-translate-y-0.5 transform-gpu"),  # Added ml-auto
            cls="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between"
        ),
        cls="w-full fixed top-0 left-0 border-b border-neutral-700 z-50 backdrop-blur-md bg-neutral-900/40"  # Lightened border and background
    )