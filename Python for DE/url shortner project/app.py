from flask import Flask, request, redirect, render_template, abort
import random
import string

from models import (
    get_all_url,
    insert_url,
    init_db,
    get_url,
    delete_url_by_code,
    increment_visit_count
)


app = Flask(__name__)

# Initialize database
init_db()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Display all URLs and create a new short URL.
    """

    if request.method == "POST":
        original_url = request.form.get("url")

        # Validate URL input
        if not original_url:
            return "URL is required", 400

        # Generate a unique short code
        short_code = generate_short_code()

        # Store URL in database
        insert_url(original_url, short_code)

        # Redirect back to homepage
        return redirect("/")

    # Get all stored URLs
    all_urls = get_all_url()

    return render_template(
        "index.html",
        all_urls=all_urls
    )


@app.route("/<short_code>")
def redirect_to_url(short_code):
    """
    Redirect the user from the short URL
    to the original URL.
    """

    url_data = get_url(short_code)

    if not url_data:
        abort(404)

    # Increase visit count
    increment_visit_count(short_code)

    # Redirect to original URL
    return redirect(url_data["original_url"])


@app.route("/delete/<short_code>", methods=["POST"])
def delete_url(short_code):
    """
    Delete a shortened URL.
    """

    delete_url_by_code(short_code)

    return redirect("/")


@app.route("/about")
def about():
    """
    About page.
    """

    return "This is an amazing Python learning journey."


if __name__ == "__main__":
    app.run(debug=True)