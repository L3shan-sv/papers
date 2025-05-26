import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.models.author import Author

# Create and save a new author
a1 = Author(name="Kweku Smoke")
a1.save()
print("Saved:", a1)

# Find by ID
found = Author.find_by_id(a1.id)
print("Found by ID:", found)

# Find by name
found_by_name = Author.find_by_name("Kweku Smoke")
print("Found by name:", found_by_name)

from lib.models.magazine import Magazine

# Create and save a new magazine
m1 = Magazine(name="Tech Today", category="Technology")
m1.save()
print("Saved:", m1)

# Find by ID
found_mag = Magazine.find_by_id(m1.id)
print("Found by ID:", found_mag)

# Find by name
found_mag_name = Magazine.find_by_name("Tech Today")
print("Found by name:", found_mag_name)

# Find by category
found_by_cat = Magazine.find_by_category("Technology")
print("Found by category:", found_by_cat)

from lib.models.article import Article

# Create a new article (using existing author and magazine ids)
article1 = Article(title="The Future of AI", author_id=a1.id, magazine_id=m1.id)
article1.save()
print("Saved:", article1)

# Find article by ID
found_article = Article.find_by_id(article1.id)
print("Found by ID:", found_article)

# Find articles by title
found_by_title = Article.find_by_title("The Future of AI")
print("Found by title:", found_by_title)

# Find articles by author
articles_by_author = Article.find_by_author(a1.id)
print("Articles by author:", articles_by_author)

# Find articles by magazine
articles_by_mag = Article.find_by_magazine(m1.id)
print("Articles by magazine:", articles_by_mag)
