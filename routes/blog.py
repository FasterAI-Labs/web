from fasthtml.common import *
from monsterui.all import *
from app import rt
from components.menu import create_menu
from components.footer import create_footer
from components.layout import create_layout
from pathlib import Path


# Blog posts configuration
BLOG_POSTS = [
    {
        "title": "Optimizing Large Language Models for Production",
        "date": "March 15, 2024",
        "preview": "Learn how to reduce your LLM's size while maintaining performance...",
        "author": "Nathan Hubens",
        "read_time": "5 min read",
        "image": "static/imgs/blog/kseniya-lapteva-l75mCsy2Kcc-unsplash.jpg",
        "url": "/blog/llm"
    },
    {
        "title": "Getting Started with Model Compression",
        "date": "March 10, 2024",
        "preview": "A beginner's guide to implementing model compression techniques...",
        "author": "Nathan Hubens",
        "read_time": "4 min read",
        "image": "static/imgs/blog/kseniya-lapteva-vWRKuMKdVaE-unsplash.jpg",
        "url": "/blog/compression"
    },
    {
        "title": "Case Study: 3x Faster Inference in Production",
        "date": "March 5, 2024",
        "preview": "How Company X achieved 3x faster inference using FasterAI...",
        "author": "Nathan Hubens",
        "read_time": "6 min read",
        "image": "static/imgs/blog/kseniya-lapteva-ZL8UKfJ1wtQ-unsplash.jpg",
        "url": "/blog/case-study"
    },
    {
        "title": "Case Study: 3x Faster Inference in Production",
        "date": "March 5, 2024",
        "preview": "How Company X achieved 3x faster inference using FasterAI...",
        "author": "Nathan Hubens",
        "read_time": "6 min read",
        "image": "static/imgs/blog/kseniya-lapteva-fYAbU-yaDlg-unsplash.jpg",
        "url": "/blog/case-study"
    },
]

def create_blog_card(title, date, preview, author, read_time, image, url):
    # Print the URL for debugging
    print(f"Creating card with URL: {url}")
    return A(
        Card(
            DivVStacked(
                Img(src=image, alt=title, cls="w-full h-64 object-cover rounded-t-lg relative z-10"),
                DivVStacked(
                    Span(date, cls="text-sm text-orange-500"),
                    H3(title, cls="text-xl font-semibold mt-2"),
                    P(preview, cls="text-gray-500 mt-2 text-sm"),
                    Div(
                        Span(author, cls="text-sm text-neutral-400"),
                        Span("•", cls="mx-2 text-neutral-600"),
                        Span(read_time, cls="text-sm text-neutral-400"),
                        cls="mt-4"
                    ),
                    cls="p-8 relative z-10"
                ),
                cls="h-full relative z-10"
            ),
            cls="""
                group hover:shadow-lg transition-transform duration-75 shadow-md bg-neutral-800/40 backdrop-blur-md w-[350px]
                transform-gpu perspective-1000 relative cursor-pointer
                [transform-style:preserve-3d]
                [&>*]:[transform-style:preserve-3d]
                border border-neutral-700
            """
        ),
        href=url,
        cls="block hover:no-underline",
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

def read_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

@rt("/blog/{filepath:path}")
async def blog_post(filepath: str):  # str is a built-in type, no import needed
    try:
        print(f"Requested filepath: {filepath}")
        safe_filepath = filepath.strip('/')
        full_path = Path("content/blog") / f"{safe_filepath}.md"
        print(f"Looking for file at: {full_path}")
        print(f"Current working directory: {Path.cwd()}")
        
        # Check if file exists
        if not full_path.exists():
            print(f"File does not exist at {full_path}")
            # Try to list files in the directory to debug
            blog_dir = Path("content/blog")
            if blog_dir.exists():
                print("Files in content/blog directory:")
                for file in blog_dir.glob("*.md"):
                    print(f"- {file}")
            else:
                print("content/blog directory does not exist!")
            return "404 - Blog post not found", 404
        
        content = read_markdown_file(full_path)
        return render_blog_post(render_md(content))
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return "404 - Blog post not found", 404
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {str(e)}", 500

@rt
def blog():
    content = Main(
        Section(
            Div(
                DivCentered(
                    H1("Blog", cls="text-4xl font-bold text-center"),
                    P("Latest insights, tutorials, and updates from our team", 
                      cls="text-xl text-gray-500 mt-4 text-center"),
                    Div(
                        *[create_blog_card(**post) for post in BLOG_POSTS],
                        cls="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-12 mt-16 justify-items-center"
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

def render_blog_post(content):
    return Container(
        Div(
            create_menu(),
            Div(
                Div(cls="absolute inset-0", 
                    style="background: radial-gradient(circle at top center, rgba(60, 60, 60, 1) -50%, rgba(0, 0, 0, 0) 50%)"),
                Div(
                    Main(
                        Section(
                            Div(
                                DivCentered(
                                    Div(
                                        content,
                                        cls="prose prose-invert max-w-none"
                                    ),
                                    cls="py-20"
                                ),
                                cls="max-w-4xl mx-auto px-6"
                            ),
                            cls="w-full"
                        ),
                        cls="pt-16 pb-24"
                    ),
                    cls="relative z-10"
                ),
                cls="relative w-full min-h-screen"
            ),
            create_footer(),
            cls="bg-black"
        )
    )