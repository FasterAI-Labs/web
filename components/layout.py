from fasthtml.common import *
from monsterui.all import *
from components.menu import create_menu
from components.footer import create_footer

def create_layout(content):
    """Create a consistent layout wrapper for all pages"""
    return Container(
        Div(
            create_menu(),
            Div(
                content,
                cls="relative z-10"
            ),
            create_footer(),
            cls="min-h-screen w-full"
        ),
        cls="bg-gradient-to-b from-neutral-800 to-neutral-950 min-w-full min-h-screen"
    ) 