from fasthtml.common import *
from monsterui.all import *
from app import rt
from config import COMPANY_NAME, COMPANY_TAGLINE
from utils import create_section
from components.menu import create_menu
from components.footer import create_footer
from components.layout import create_layout

# Features configuration
FEATURES = [
    {
        "icon": "rocket",
        "title": "Lightning Fast",
        "emphasis": "3x",
        "description": "faster inference on any hardware without compromising accuracy"
    },
    {
        "icon": "shrink",
        "title": "Minimal Footprint",
        "emphasis": "90%",
        "description": "smaller models with production-ready performance"
    },
    {
        "icon": "leaf",
        "title": "Eco-Friendly",
        "emphasis": "75%",
        "description": "reduction in carbon footprint with our AI solutions"
    },
    {
        "icon": "users",
        "title": "Community-Driven",
        "emphasis": "100%",
        "description": "open-source with full transparency"
    },
]

def create_hero_section():
    return Section(
        Div(
            DivCentered(
                H1(COMPANY_TAGLINE, 
                   cls="text-6xl font-bold text-center text-white"),
                P("Transform your AI models with production-ready optimization", 
                  cls="text-xl text-gray-500 max-w-3xl mx-auto mt-6"),
                DivHStacked(
                    A(Button("Get Started", 
                           cls="uk-button uk-button-primary bg-orange-500 hover:bg-orange-600 transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5"),
                      href="https://github.com/fasterai",
                      target="_blank"),
                    A(Button("View Documentation",
                           cls="uk-button uk-button-default bg-neutral-700/90 hover:bg-neutral-600 transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5"),
                      href="https://fasterai-labs.github.io/fasterai/quickstart.html"),
                    cls="space-x-4 flex justify-center mt-8"
                ),
                cls="py-20"
            ),
            cls="max-w-4xl mx-auto px-6"
        ),
        cls="w-full mt-16"
    )

def create_installation_section():
    return Section(
        Div(
            DivCentered(
                P("Get started in seconds", 
                  cls="text-lg text-neutral-400 font-medium mb-4"),
                Div(
                    Div(
                        Code("pip install fasterai",
                            cls="text-neutral-100 font-mono text-lg"),
                        Button(
                            Div(
                                UkIcon("copy"),
                                id="copyIcon",
                                cls="block"
                            ),
                            Div(
                                UkIcon("check"),
                                id="checkIcon",
                                cls="hidden text-green-500"
                            ),
                            cls="ml-4 text-neutral-400 hover:text-orange-500 transition-colors",
                            onclick="""
                                navigator.clipboard.writeText('pip install fasterai');
                                document.getElementById('copyIcon').classList.add('hidden');
                                document.getElementById('copyIcon').classList.remove('block');
                                document.getElementById('checkIcon').classList.add('block');
                                document.getElementById('checkIcon').classList.remove('hidden');
                                setTimeout(() => {
                                    document.getElementById('copyIcon').classList.add('block');
                                    document.getElementById('copyIcon').classList.remove('hidden');
                                    document.getElementById('checkIcon').classList.add('hidden');
                                    document.getElementById('checkIcon').classList.remove('block');
                                }, 2000);
                            """
                        ),
                        cls="flex items-center justify-between px-6 py-3 bg-neutral-800/40 rounded-lg border border-neutral-700"
                    ),
                    cls="flex items-center justify-center"
                ),
                cls="py-12"
            ),
            cls="max-w-4xl mx-auto px-6"
        ),
        cls="w-full"
    )

def create_feature_card(icon, title, emphasis, description):
    return Card(
        DivVStacked(
            UkIcon(icon, 
                  cls="text-orange-500 transition-transform duration-75 transform-gpu relative z-10",
                  ratio=1.5),
            H3(title, cls="text-lg font-semibold relative z-10"),
            P(
                Span(emphasis, cls="text-2l font-bold text-orange-500"),
                " ",
                Span(description, cls="text-gray-500 text-sm"),
                cls="mt-2 relative z-10"
            ),
            cls="text-center p-6 relative z-10"
        ),
        cls="""
            group hover:shadow-lg transition-transform duration-75 shadow-md bg-neutral-800/40 backdrop-blur-md 
            transform-gpu perspective-1000 relative cursor-pointer
            hover:shadow-[0_10px_20px_rgba(240,80,0,0.15)]
            [transform-style:preserve-3d]
            [&>*]:[transform-style:preserve-3d]
            border border-neutral-700
        """,
        onmousemove="""
            const rect = this.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;
            
            this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
            this.style.transition = 'none';
        """,
        onmouseleave="""
            this.style.transition = 'transform 150ms ease-out';
            this.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        """
    )

@rt
def index():
    content = Div(
        Main(
            create_hero_section(),
            create_section(
                Grid(
                    *[create_feature_card(**feature) for feature in FEATURES],
                    cols_sm=1,
                    cols_md=2,
                    cols_lg=4,
                    cls="gap-6"
                ),
                title="",
                id="features-section"
            ),
            create_installation_section(),
            cls="pt-16 pb-24"
        ),
        cls="relative z-10"
    )
    return create_layout(content)