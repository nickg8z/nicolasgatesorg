# Nick Gates – Personal Site

This is my personal website.  
It’s intentionally simple: just static HTML and CSS, no frameworks or databases.

The site has four main sections:

- **About** – who I am and what I do
- **Publications** – my published articles and op-eds
- **Blog** – my own writing, published here instead of on social media
- **Contact** – email, Matrix, and my PGP key

---

## Blog Helper Script

There’s a small Python script in `/scripts` called `add_post.py` that makes it easier to add new blog posts.

- Write your post in Markdown (`.md` file).
- Run:
  ```bash
  python scripts/add_post.py your-post.md
  ```

* The script will:

  - Convert your Markdown into an HTML file inside `/blog/`
  - Update `blog.html` with a new link to the post

This keeps the site completely static, while giving me a quick way to add posts without manually editing HTML each time.

---

## Forking

Feel free to fork this repo and adapt it for your own personal site.
The design is deliberately minimal so you can:

- Use it as a simple personal homepage
- Run it as your own “self-hosted social media”
- Extend it however you want

---

## License

Do whatever you want with it.
