from fasthtml.common import *
from monsterui.all import *
from config import COMPANY_NAME, NAV_LINKS
from app import rt

@rt('/pricing') 
def pricing():
    pricing_plans = [
        {
            "name": "Starter",
            "price": "Free Forever",
            "period": "",
            "description": "Perfect for trying out FasterAI",
            "features": [
                "Basic model optimization",
                "Community support",
                "1 project",
                "Basic analytics"
            ]
        },
        {
            "name": "Enterprise",
            "price": "Custom",
            "period": "",
            "description": "For large organizations",
            "features": [
                "Custom solutions",
                "Dedicated support",
                "SLA guarantee",
                "On-premise deployment",
                "Custom integrations",
                "Training workshops"
            ]
        }
    ]

    def create_pricing_card(plan):
        return Card(
            DivVStacked(
                DivCentered(
                    DivVStacked(
                        H3(plan["name"], cls="uk-card-title"),
                        DivHStacked(
                            H2(plan["price"], cls="text-primary"),
                            Span(plan["period"], cls=TextT.muted),
                            cls="uk-flex uk-flex-middle"
                        ),
                        P(plan["description"], cls=TextT.muted),
                        cls="space-y-3"
                    ),
                ),
                DividerLine(),
                Div(
                    *[DivHStacked(
                        UkIcon("check", cls='text-orange-500', style={"width": "20px", "margin-right": "8px"}),
                        P(feature, style={"margin": "0"}),
                        cls="uk-flex uk-flex-left"
                    ) for feature in plan["features"]],
                    cls="space-y-2 uk-margin-medium",
                    style={"text-align": "left", "padding-left": "16px"}
                ),
                DivCentered(
                    Button(
                        "Get Started" if plan["name"] != "Enterprise" else "Contact Sales",
                        href="/contact",
                        cls=ButtonT.primary,
                        style={"width": "100%"}
                    )
                ),
                cls="space-y-6"
            ),
            cls="uk-card-hover",
            style={"max-width": "300px", "margin": "0 auto"}  # Added margin auto for centering
        )

    pricing_content = Container(
        Grid(
            *[create_pricing_card(plan) for plan in pricing_plans],
            cols_md=2,
            cols_lg=2,
            cls="uk-grid-match uk-grid-medium uk-flex-center",  # Added uk-flex-center class
            style={"gap": "2rem"}
        ),
        cls=ContainerT.sm,
        style={"margin": "0 auto"}  # Added margin auto for centering
    )

    return create_page_layout(
        "Simple, transparent pricing",
        "Choose the plan that's right for you",
        pricing_content
    )