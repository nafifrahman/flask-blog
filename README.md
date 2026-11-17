# Flask Blog Application

A beginner Flask project built for my Masterschool assignment.

## Features

- Display all blog posts
- Add a new blog post
- Update an existing post
- Delete a post
- Like a post
- Save changes in a JSON file

## Technologies

- Python
- Flask
- HTML and Jinja templates
- CSS
- JSON

## Run locally

1. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Start the application:

   ```bash
   python app.py
   ```

3. Open http://127.0.0.1:5000 in your browser.

On Codio, use `python3 app.py`.

## Project structure

```text
flask-blog/
├── app.py
├── blog_posts.json
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── add.html
    └── update.html
```

## Notes

Posts are stored in `blog_posts.json`. Adding, updating, deleting,
or liking a post changes that file.

This application is a learning project and runs in Flask debug mode
for local development.