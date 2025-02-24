from fasthtml.common import *
from monsterui.all import *


def create_section(*children, title=None, subtitle=None, **kwargs):
    """Create a consistent section with optional title and subtitle"""
    content = []
    if title:
        header = DivCentered(
            H2(title, cls="text-3xl font-bold"),
            P(subtitle, cls="text-gray-500 mt-2") if subtitle else None,
            cls="mb-12"
        )
        content.append(header)
    
    content.extend(children)
    
    return Section(
        Div(
            *content,
            cls="max-w-7xl mx-auto px-6 py-16"
        ),
        cls="w-full",
        **kwargs
    )