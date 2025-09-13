import db

def menu():
    while True:
        print("\n📚 Mini Bibliotekssystem")
        print("1. Visa alla böcker")
        print("2. Lägg till en bok")
        print("3. Sök böcker")
        print("4. Uppdatera en bok")
        print("5. Ta bort en bok")
        print("6. Avsluta")

        choice = input("Välj ett alternativ (1-6): ")

        if choice == "1":
            books = db.view_books()
            print("\nAlla böcker:")
            for b in books:
                print(b)

        elif choice == "2":
            title = input("Titel: ")
            author = input("Författare: ")
            year = input("År: ")
            isbn = input("ISBN: ")
            db.add_book(title, author, year, isbn)
            print("✅ Bok tillagd!")

        elif choice == "3":
            title = input("Titel (lämna tomt om ej relevant): ")
            author = input("Författare: ")
            year = input("År: ")
            isbn = input("ISBN: ")
            results = db.search_books(title, author, year, isbn)
            print("\nSökresultat:")
            for r in results:
                print(r)

        elif choice == "4":
            book_id = input("ID på boken att uppdatera: ")
            title = input("Ny titel: ")
            author = input("Ny författare: ")
            year = input("Nytt år: ")
            isbn = input("Nytt ISBN: ")
            db.update_book(book_id, title, author, year, isbn)
            print("✅ Bok uppdaterad!")

        elif choice == "5":
            book_id = input("ID på boken att ta bort: ")
            db.delete_book(book_id)
            print("🗑️ Bok borttagen!")

        elif choice == "6":
            print("👋 Avslutar programmet...")
            break
        else:
            print("❌ Ogiltigt val, försök igen.")

if __name__ == "__main__":
    db.connect()
    menu()
