from fasthtml.common import *
from monsterui.all import *
from config import THEME_COLOR

# Theme configuration
THEME_COLOR = Theme.orange
APP_CONFIG = {
    'hdrs': THEME_COLOR.headers(highlightjs=True),
    'live': True,
    'static_dir': "imgs",
    'body_cls': "bg-neutral-900 text-white",
    'head': """
        <link rel="icon" type="image/png" href="/static/imgs/logo/logo.png">
        <style>
            body {
                background: linear-gradient(to bottom, rgb(23, 23, 23) 0%, rgb(17, 17, 17) 100%);
            }
        </style>
    """
}

# Create app instance
THEME_COLOR.light = True
app, rt = fast_app(**APP_CONFIG)