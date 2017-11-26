from flask import Flask, render_template
from flask_flatpages import FlatPages
import utils


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'


app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route('/')
def index():
    return render_template(
        'index.html',
        pages=pages,
        time=utils.get_push_time()
    )


@app.route('/<path:path>/')
def page(path):
    current_page = pages.get_or_404(path)
    return render_template(
        'post.html',
        page=current_page,
        time=utils.get_push_time()
    )


if __name__ == '__main__':
    app.debug = True
    app.run()
