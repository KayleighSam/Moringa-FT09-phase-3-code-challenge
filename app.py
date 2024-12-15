from flask import Flask, render_template, request, redirect, url_for
from models.author import Author
from models.magazine import Magazine
from models.article import Article

# Initialize Flask app
app = Flask(__name__)

# Route to display the data
@app.route('/')
def index():
    # Fetch all data from models
    authors = Author.list_all()
    magazines = Magazine.list_all()
    articles = Article.list_all()

    # Pass the data to the template
    return render_template('index.html', authors=authors, magazines=magazines, articles=articles)

# Route to add a new author
@app.route('/add-author', methods=['POST'])
def add_author():
    name = request.form['name']
    if name:
        Author.create(name)
    return redirect(url_for('index'))

# Route to add a new magazine
@app.route('/add-magazine', methods=['POST'])
def add_magazine():
    name = request.form['name']
    category = request.form['category']
    if name and category:
        Magazine.create(name, category)
    return redirect(url_for('index'))

# Route to add a new article
@app.route('/add-article', methods=['POST'])
def add_article():
    author_id = request.form['author_id']
    magazine_id = request.form['magazine_id']
    title = request.form['title']
    if author_id and magazine_id and title:
        Article.create(author_id, magazine_id, title)
    return redirect(url_for('index'))

# Route to delete an author
@app.route('/delete-author/<int:id>', methods=['GET'])
def delete_author(id):
    Author.delete(id)
    return redirect(url_for('index'))

# Route to delete a magazine
@app.route('/delete-magazine/<int:id>', methods=['GET'])
def delete_magazine(id):
    Magazine.delete(id)
    return redirect(url_for('index'))

# Route to delete an article
@app.route('/delete-article/<int:id>', methods=['GET'])
def delete_article(id):
    Article.delete(id)
    return redirect(url_for('index'))

# Route to update an author
@app.route('/update-author/<int:id>', methods=['POST'])
def update_author(id):
    new_name = request.form['name']
    if new_name:
        Author.update(id, new_name)
    return redirect(url_for('index'))

# Route to update a magazine
@app.route('/update-magazine/<int:id>', methods=['POST'])
def update_magazine(id):
    new_name = request.form['name']
    new_category = request.form['category']
    if new_name and new_category:
        Magazine.update(id, new_name, new_category)
    return redirect(url_for('index'))

# Route to update an article
@app.route('/update-article/<int:id>', methods=['POST'])
def update_article(id):
    new_title = request.form['title']
    new_author_id = request.form['author_id']
    new_magazine_id = request.form['magazine_id']
    if new_title and new_author_id and new_magazine_id:
        Article.update(id, new_author_id, new_magazine_id, new_title)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
