import requests

BASE_URL = "https://openlibrary.org/search.json"

read_books = []

def search_book(title):
    params = {
        "title": title
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        books = data["docs"][:5]  # Get first 5 results
        
        for i, book in enumerate(books):
            book_title = book.get("title", "Unknown Title")
            author = book.get("author_name", ["Unknown Author"])[0]
            print(f"{i+1}. {book_title} by {author}")
        
        return books
    else:
        print("Error connecting to API.")
        return []

def add_to_read(book):
    title = book.get("title", "Unknown Title")
    author = book.get("author_name", ["Unknown Author"])[0]
    
    read_books.append({
        "title": title,
        "author": author
    })
    
    print(f"Added '{title}' to your read list.")



