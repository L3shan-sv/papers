import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
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

def test_save_and_find_magazine():
    mag = Magazine(name="Science Monthly", category="Science")
    mag.save()

    found = Magazine.find_by_id(mag.id)
    assert found.name == "Science Monthly"

    found_by_name = Magazine.find_by_name("Science Monthly")
    assert found_by_name.id == mag.id

    found_by_category = Magazine.find_by_category("Science")
    assert len(found_by_category) >= 1

def test_magazine_relationships():
    mag = Magazine(name="News Today", category="News")
    mag.save()

    a1 = Author(name="Writer A")
    a2 = Author(name="Writer B")
    a1.save()
    a2.save()

    a1.add_article(mag, "Headline One")
    a2.add_article(mag, "Headline Two")

    contributors = mag.contributors()
    assert len(contributors) == 2

    titles = mag.article_titles()
    assert "Headline One" in titles
    assert "Headline Two" in titles

def test_magazine_contributing_authors():
    mag = Magazine(name="Exclusive Mag", category="Lifestyle")
    mag.save()

    a1 = Author(name="Contributor X")
    a2 = Author(name="Contributor Y")
    a1.save()
    a2.save()

    a1.add_article(mag, "Title 1")
    a1.add_article(mag, "Title 2")
    a1.add_article(mag, "Title 3")
    a2.add_article(mag, "Another Title")

    contributing = mag.contributing_authors()
    assert len(contributing) == 1
    assert contributing[0].name == "Contributor X"
