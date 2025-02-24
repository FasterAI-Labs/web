from fasthtml.common import *
from monsterui.all import *
from config import COMPANY_NAME
from datetime import datetime

def create_footer_link_group(title, links):
    return DivVStacked(
        H4(title, cls="text-sm font-semibold text-gray-400 mb-4"),
        *[A(text, href=link, 
            cls="text-sm text-gray-500 hover:text-orange-500 transition-colors duration-200"
          ) for text, link in links],
        cls="space-y-2"
    )

def create_footer():
    FOOTER_LINKS = {
        'Company': [
            ("About", "/about"),
            ("Contact Us", "/contact")
        ],
        'Resources': [
            ("Documentation", "https://fasterai-labs.github.io/fasterai/quickstart.html"),
            ("Blog", "/blog"),
        ],
        'Legal': [
            ("Privacy Policy", "/privacy"),
            ("Cookie Settings", "/cookies"),
        ]
    }

    SOCIAL_ICONS = [
        ("twitter", "https://twitter.com/fasterai"),
        ("github", "https://github.com/FasterAI-Labs"),
    ]

    return Container(
        Container(
            Div(
                DivFullySpaced(
                    DivVStacked(
                        H3(COMPANY_NAME, cls="text-lg font-bold text-gray-400"),
                    ),
                    DivHStacked(
                        *[A(UkIcon(icon, ratio=1.2), 
                            href=link,
                            cls="text-gray-400 hover:text-orange-500 transition-colors duration-200"
                          ) for icon, link in SOCIAL_ICONS],
                        cls="space-x-6"
                    )
                ),
                Hr(cls="my-8 border-gray-800"),
                DivFullySpaced(
                    *[create_footer_link_group(title, links) 
                      for title, links in FOOTER_LINKS.items()],
                    cls="grid grid-cols-1 md:grid-cols-3 gap-8"
                ),
                DivCentered(
                    P(f"© {datetime.now().year} {COMPANY_NAME}. All rights reserved.", 
                      cls="text-sm text-gray-600 mt-8")
                ),
                cls='space-y-4 py-12'
            ),
            cls='px-6 mx-auto',
            style={
                "max-width": "1200px",
            }
        ),
        cls="w-full",
        style={
            "min-width": "100%",
        }
    )