from fasthtml.common import *
from monsterui.all import *
from app import rt
from components.layout import create_layout

@rt
def compress():
    content = Main(
        Section(
            Div(
                DivCentered(
                    H1("Model Compressor", cls="text-4xl font-bold text-center"),
                    P("Compress your models with our interactive demo", 
                      cls="text-xl text-gray-500 mt-4 text-center"),
                    Div(
                        Iframe(
                            src="https://nathan12-compressor.hf.space",
                            cls="w-[1200px] h-[800px] mt-12 rounded-xl border border-neutral-700 bg-neutral-800/40 backdrop-blur-md",
                            frameborder="0"
                        ),
                        cls="mx-auto"
                    ),
                    cls="py-24"
                ),
                cls="max-w-9xl mx-auto px-12"
            ),
            cls="w-full"
        ),
        cls="pt-16 pb-24"
    )
    return create_layout(content) 