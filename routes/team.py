from fasthtml.common import *
from monsterui.all import *
from app import rt
from components.menu import create_menu
from components.footer import create_footer
from components.layout import create_layout

def create_team_section():
    """Create a section displaying team member cards in a grid layout"""
    team_members = [
        {
            "name": "Nathan Hubens",
            "role": "Founder & CEO",
            "image": "static/imgs/team/profile.jpg",
            "social": {
                "twitter": "https://x.com/HubensN",
                "linkedin": "https://www.linkedin.com/in/hubensn/",
                "github": "https://github.com/nathanhubens"
            }
        },
        # Add more team members here
    ]

    return Section(
        Div(
            H2("Our Team", cls="text-3xl font-bold text-center text-neutral-100"),
            P("Meet the people behind FasterAI", 
              cls="text-center text-neutral-400 mt-4 mb-16"),
            Div(
                *[create_team_card(member) for member in team_members],
                cls="grid grid-cols-1 md:grid-cols-3 gap-8"
            ),
            cls="max-w-7xl mx-auto px-6 py-24"
        ),
        cls=""
    )


def create_team_card(member):
    social_links = Div(
        A(UkIcon("twitter", height=16), href=member["social"]["twitter"], 
          cls="text-neutral-500 hover:text-orange-400"),
        A(UkIcon("linkedin", height=16), href=member["social"]["linkedin"], 
          cls="text-neutral-500 hover:text-orange-400"),
        A(UkIcon("github", height=16), href=member["social"]["github"], 
          cls="text-neutral-500 hover:text-orange-400"),
        cls="flex gap-4 mt-2 relative z-10"
    )
    
    return Div(
        Div(
            Img(src=member["image"], 
                cls="w-20 h-20 rounded-full ring-2 ring-neutral-800 ring-offset-4 ring-offset-neutral-900 relative z-10"),
            cls="shrink-0"
        ),
        Div(
            H3(member["name"], cls="text-lg font-medium text-white"),
            P(member["role"], cls="text-orange-500 text-sm mt-1"),
            social_links,
            cls="ml-6 relative z-10"
        ),
        cls="""
            flex items-center p-6 bg-neutral-800/40 backdrop-blur-sm rounded-xl border border-neutral-700
            transform-gpu perspective-1000 relative cursor-pointer
            transition-transform duration-75
            [transform-style:preserve-3d]
            [&>*]:[transform-style:preserve-3d]
        """,
        onmousemove="""
            const rect = this.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = (y - centerY) / 60;
            const rotateY = (centerX - x) / 60;
            
            this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.005, 1.005, 1.005)`;
            this.style.transition = 'none';
        """,
        onmouseleave="""
            this.style.transition = 'transform 150ms ease-out';
            this.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        """
    )

@rt
def team():
    return Container(
        Div(
            #Div(cls="absolute inset-0", 
            #    style="background: radial-gradient(circle at bottom center, rgb(24, 24, 24) 0%, rgb(0, 0, 0) 100%)"),
            Div(
                create_menu(),
                Main(
                    create_team_section(),
                    cls="pt-16 pb-24"
                ),
                cls="relative z-10"
            ),
            cls="relative w-full"
        ),
        create_footer(),
        cls=""
    ) 