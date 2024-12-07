# Library Management System

# Variables to hold data
books = []  # List of books (tuples)
book_details = {}  # Dictionary to store book details with ISBN as key

# Function to display the menu
def display_menu():
    
    print("\nLibrary Management System")
    print("-" * 30)
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Book by ISBN")
    print("4. Exit")

# Add a book function
def add_book():
    isbn = input("Enter ISBN: ")
    if isbn in book_details:
        print("❗ This book already exists in the library.")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = input("Enter Publication Year: ")

    # Store book as a tuple and add it to the list
    book = (isbn, title, author, year)
    books.append(book)
    # Add details to the dictionary
    book_details[isbn] = {"Title": title, "Author": author, "Year": year}
    print("✅ Book added successfully!")

# View all books
def view_books():
    if not books:
        print("❗ No books in the library.")
        return

    print("\nList of Books:")
    print("-" * 30)
    for book in books:
        print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")

# Search a book by ISBN
def search_book():
    isbn = input("Enter ISBN to search: ")
    if isbn in book_details:
        print("\nBook Details:")
        for key, value in book_details[isbn].items():
            print(f"{key}: {value}")
    else:
        print("❌ Book not found.")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # Switch statement alternative (Python 3.10+ supports match-case)
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print("📚 Exiting the Library Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
