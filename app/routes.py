from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Nhựt đã đến với thế giới này !"
