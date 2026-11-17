import json
import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BLOG_POSTS_FILE = "blog_posts.json"


def load_posts():
    """Read blog posts from the JSON file."""
    if not os.path.exists(BLOG_POSTS_FILE):
        return []

    with open(BLOG_POSTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    """Save blog posts to the JSON file."""
    with open(BLOG_POSTS_FILE, "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


def fetch_post_by_id(post_id):
    """Return the blog post with the given ID, or None."""
    posts = load_posts()

    for post in posts:
        if post["id"] == post_id:
            return post

    return None


@app.route("/")
def index():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        posts = load_posts()

        if posts:
            new_id = max(post["id"] for post in posts) + 1
        else:
            new_id = 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content,
            "likes": 0
        }

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        posts = load_posts()

        for current_post in posts:
            if current_post["id"] == post_id:
                current_post["author"] = request.form.get("author")
                current_post["title"] = request.form.get("title")
                current_post["content"] = request.form.get("content")
                break

        save_posts(posts)

        return redirect(url_for("index"))

    return render_template("update.html", post=post)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    posts = load_posts()
    updated_posts = []

    for post in posts:
        if post["id"] != post_id:
            updated_posts.append(post)

    save_posts(updated_posts)

    return redirect(url_for("index"))


@app.route("/like/<int:post_id>")
def like(post_id):
    posts = load_posts()

    for post in posts:
        if post["id"] == post_id:
            post["likes"] += 1
            break

    save_posts(posts)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)