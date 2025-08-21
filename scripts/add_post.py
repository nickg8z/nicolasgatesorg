import os
import sys
import datetime
import markdown

# Paths
BLOG_DIR = "blog"
BLOG_INDEX = "blog.html"
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header>
    <h1>{title}</h1>
    <nav>
      <a href="index.html">About</a>
    <a href="thoughts.html">Publications</a>
      <a href="blog.html">Blog</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>
  <main>
    <article>
      <h2>{title}</h2>
      <p><em>Published {date}</em></p>
      {content}
    </article>
  </main>
</body>
</html>
"""


def add_post(md_file):
    # Read Markdown
    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(text, extensions=["fenced_code", "tables"])

    # Extract title (first line of markdown or filename)
    first_line = text.strip().splitlines()[0]
    title = (
        first_line.replace("#", "").strip()
        if first_line.startswith("#")
        else os.path.splitext(os.path.basename(md_file))[0]
    )

    # Date
    date = datetime.date.today().strftime("%B %d, %Y")

    # Build final HTML
    html = TEMPLATE.format(title=title, date=date, content=html_content)

    # Save HTML file in /blog
    filename = title.lower().replace(" ", "-") + ".html"
    filepath = os.path.join(BLOG_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Created {filepath}")

    # Update blog index
    link_html = (
        f'      <li><a href="blog/{filename}">{title}</a> <span>— {date}</span></li>\n'
    )
    with open(BLOG_INDEX, "r+", encoding="utf-8") as f:
        content = f.readlines()
        for i, line in enumerate(content):
            if "<ul>" in line:  # find list start
                content.insert(i + 1, link_html)
                break
        f.seek(0)
        f.writelines(content)
    print(f"✅ Updated {BLOG_INDEX} with new link")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_post.py post.md")
    else:
        add_post(sys.argv[1])
