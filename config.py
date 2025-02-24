from fasthtml.common import *
from monsterui.all import *
from datetime import datetime

# Theme configuration
THEME_COLOR = Theme.orange

# Content configurations
COMPANY_NAME = "FasterAI"
COMPANY_TAGLINE = "Smaller. Faster. Open."

# Create a regular navigation for non-index pages
NAV_LINKS = (
    A("Pricing", href="/pricing", subnav=[
        A("Enterprise", href="/pricing#enterprise"),
        A("Starter", href="/pricing#starter"),
    ]),
    A("Resources", href="#", subnav=[
        A("Documentation", href="/docs"),
        A("Blog", href="/blog"),
        A("Help Center", href="/help")
    ])
)