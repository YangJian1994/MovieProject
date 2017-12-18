from flask import Flask, render_template, request, redirect, url_for
import config
from exts import db
from models import Recommend, Action, Fiction, War, Love, Funny

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/detail/<name>', methods=['GET','POST'])
def detail(name):
    page = request.args.get('page', 1, type=int)
    if name == 'recommend':
        pagination = Recommend.query.paginate(page, per_page=20, error_out=True)
    elif name == 'action':
        pagination = Action.query.paginate(page, per_page=20, error_out=True)
    elif name == 'fiction':
        pagination = Fiction.query.paginate(page, per_page=20, error_out=True)
    elif name == 'war':
        pagination = War.query.paginate(page, per_page=20, error_out=True)
    elif name == 'love':
        pagination = Love.query.paginate(page, per_page=20, error_out=True)
    elif name == 'funny':
        pagination = Funny.query.paginate(page, per_page=20, error_out=True)
    else:
        return '404'
    datas = pagination.items
    print(page)
    return render_template('detail.html', name=name, datas=datas, pagination=pagination)


if __name__ == '__main__':
    app.run(debug=True)
