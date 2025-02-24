from .about import about
from .team import team
from .index import index
from .blog import blog

from fasthtml.common import *
from monsterui.all import *
from config import COMPANY_NAME, NAV_LINKS
from app import rt

def create_page_layout(title, subtitle, content):
    return Container(
        NavBar(
            *NAV_LINKS,
            brand=A(
                DivLAligned(Img(src="imgs/logo.png", height=40, width=40), H3(COMPANY_NAME)),
                href="/",  
                cls="uk-navbar-item uk-logo"
            ),
            sticky=True,
            cls="uk-navbar-transparent uk-position-top",
            #style={"z-index": "980"}  # Added z-index to ensure dropdowns appear above content
        ),
        Container(
            DivCentered(
                H1(title),
                Subtitle(subtitle),
                cls='py-12'
            ),
            content,
            cls=ContainerT.xl,
            style={"padding-top": "80px"}
        )
    )