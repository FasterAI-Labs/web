from fasthtml.common import *
from monsterui.all import *
from app import rt
from config import COMPANY_NAME, COMPANY_TAGLINE
from utils import create_section
from components.menu import create_menu
from components.footer import create_footer
from components.layout import create_layout

def create_about_section():
    """Create the about page sections"""
    return Div(
        create_section(
            DivCentered(
                H1("About " + COMPANY_NAME, 
                   cls="text-4xl font-bold mb-6"),
                P("Our mission is to democratize AI by making it faster, smaller, and more accessible.",
                  cls="text-xl text-gray-600 max-w-3xl mx-auto"),
            ),
        ),
        
        create_section(
            Grid(
                DivVStacked(
                    H2("Our Mission", cls="text-2xl font-bold mb-4"),
                    P("We're on a mission to revolutionize AI deployment by creating tools that make models smaller and faster without compromising on performance. We believe that efficient AI should be accessible to everyone.",
                      cls="text-gray-300"),
                ),
                DivVStacked(
                    H2("Our Vision", cls="text-2xl font-bold mb-4"),
                    P("A future where AI is not just powerful, but sustainable and accessible. Where companies of all sizes can deploy state-of-the-art AI without massive computational resources.",
                      cls="text-gray-300"),
                ),
                cols_sm=1,
                cols_md=2,
                cls="gap-12"
            )
        ),
        
        create_section(
            H2("Our Values", cls="text-3xl font-bold text-center mb-12"),
            Grid(
                Card(
                    DivVStacked(
                        UkIcon("unlock", cls="text-orange-500", ratio=1.5),
                        H3("Transparency", cls="text-xl font-bold mt-4 mb-2"),
                        P("We believe in open source and sharing knowledge with the community.",
                          cls="text-gray-300"),
                    ),
                    cls="p-6 bg-neutral-900"
                ),
                Card(
                    DivVStacked(
                        UkIcon("users", cls="text-orange-500", ratio=1.5),
                        H3("Community First", cls="text-xl font-bold mt-4 mb-2"),
                        P("Built by developers, for developers, with the community at heart.",
                          cls="text-gray-300"),
                    ),
                    cls="p-6 bg-neutral-900"
                ),
                Card(
                    DivVStacked(
                        UkIcon("star", cls="text-orange-500", ratio=1.5),
                        H3("Excellence", cls="text-xl font-bold mt-4 mb-2"),
                        P("Committed to delivering the highest quality tools and solutions.",
                          cls="text-gray-300"),
                    ),
                    cls="p-6 bg-neutral-900"
                ),
                cols_sm=1,
                cols_md=3,
                cls="gap-6"
            )
        ),
        cls="max-w-7xl mx-auto px-6 w-full"
    )

@rt
def about():
    return Container(
        Div(
            #Div(cls="absolute inset-0", 
            #    style="background: radial-gradient(circle at bottom center, rgb(24, 24, 24) 0%, rgb(0, 0, 0) 100%)"),
            Div(
                create_menu(),
                Main(
                    create_about_section(),
                    cls="pt-16 pb-24"
                ),
                cls="relative z-10"
            ),
            cls="relative w-full"
        ),
        create_footer(),
        cls=""
    )