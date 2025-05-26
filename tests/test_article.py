import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_article_crud():
    author = Author(name="Author Test")
    magazine = Magazine(name="Mag Test", category="Test")
    author.save()
    magazine.save()

    article = Article(title="Test Article", author_id=author.id, magazine_id=magazine.id)
    article.save()

    found = Article.find_by_id(article.id)
    assert found.title == "Test Article"

    by_title = Article.find_by_title("Test Article")
    assert any(a.id == article.id for a in by_title)

def test_find_by_author_and_magazine():
    author = Author(name="Finder")
    magazine = Magazine(name="Finder Mag", category="General")
    author.save()
    magazine.save()

    article = Article(title="Find Me", author_id=author.id, magazine_id=magazine.id)
    article.save()

    by_author = Article.find_by_author(author.id)
    assert len(by_author) == 1

    by_mag = Article.find_by_magazine(magazine.id)
    assert len(by_mag) == 1
