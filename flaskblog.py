from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '77f13060df47c6b4c5b3b2697aa27606'

posts = [
    {
        'author': 'Mafuzur Matin',
        'title': 'Blog post 1',
        'content': 'Post 1 content',
        'date_posted': 'August 02, 2019'
    },
    {
        'author': 'Mafuzur Matin',
        'title': 'Blog post 2',
        'content': 'Post 2 content',
        'date_posted': 'August 01, 2019'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

if __name__ == '__main__':
    app.run(debug=True)