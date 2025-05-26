import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_save_and_find_author():
    author = Author(name="John Doe")
    author.save()
    assert author.id is not None

    found = Author.find_by_id(author.id)
    assert found.name == "John Doe"

    found_by_name = Author.find_by_name("John Doe")
    assert found_by_name.id == author.id

def test_author_article_relationship():
    author = Author(name="Jane Smith")
    author.save()

    mag = Magazine(name="Health Weekly", category="Health")
    mag.save()

    article = author.add_article(mag, "Healthy Living")
    assert article.id is not None
    assert article.title == "Healthy Living"

    articles = author.articles()
    assert len(articles) == 1
    assert articles[0].title == "Healthy Living"

def test_author_magazine_and_topic_areas():
    author = Author(name="Alex Writer")
    author.save()

    mag1 = Magazine(name="Tech World", category="Technology")
    mag2 = Magazine(name="Nature Daily", category="Science")
    mag1.save()
    mag2.save()

    author.add_article(mag1, "AI in 2025")
    author.add_article(mag2, "Climate Change 101")

    magazines = author.magazines()
    assert len(magazines) == 2
    topics = author.topic_areas()
    assert "Technology" in topics
    assert "Science" in topics
