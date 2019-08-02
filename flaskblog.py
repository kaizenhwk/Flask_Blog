from flask import Flask, escape, request, render_template

app = Flask(__name__)

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