# Definerer klassen "Book" til at representer en bog
class Book:
    # En konstrukt metode til at initialisere en ny bog
    def __init__(self, book_id, title, author, copies):
        # Initialiser attributterne for bogen
        self.book_id = book_id # Bogens ID
        self.title = title # Bogens title
        self.author = author # Bogens forfatter
        self.copies = copies # Antal af kopier af bogen

    # Metode til at vise informationer om bogen i en string
    def display_info(self):
        #Returner en string, der inkluderer alle bogens informationer i et læsbart format
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

# Definerer klassen "Medlemmer" til at representer en medlem
class Member:
    # En konstrukt metode til at initialisere en ny medlem
    def __init__(self, member_id, name):
        # Initialiser attributterne for bogen
        self.member_id = member_id # Medlem ID
        self.name = name # Medlem navn
        self.borrowed_books = [] # En tom liste, der vil vise antallet af bøger som medlem har lånt

    # Metode til at vise informationer om medlem i en string
    def display_info(self):
        #Returner en string, der inkluderer alle medlem informationer i et læsbart format
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

    # Metode til at låne en medlem låner en bog
    def borrow_book(self, book):
        #Tjekker om der er en kopi af bogen
        if book.copies > 0:
            # Hvis ja, tilføj bogen til listen af lånte bøger
            self.borrowed_books.append(book)
            # Reducer antallet af kopier af bogen
            book.copies -= 1
            # Returner en besked om, at medlem har lånt bogen
            return f"{self.name} borrowed {book.title}."
        # Hvis bogen ikke har nogle kopier, returner at der ikke er nogle tilgængelig
        return "Book not available."

    # Metode til at returnere en bog
    def return_book(self, book):
        # Tjekker om medlem har lånt bogen
        if book in self.borrowed_books:
            # Hvis ja, fjerner bogen fra listen af lånte bøger
            self.borrowed_books.remove(book)
            # Øger antallet af bogens kopi
            book.copies += 1
            # Returner en besked om, at medlem har returner bogen
            return f"{self.name} returned {book.title}."
        # Hvis medlem ikke har lånt bogen, returner at bogen ikke er lånt
        return "Book not borrowed."

# Definerer klassen "Biblioteket" til at representer biblioteket
class Library:
    # En konstrukt metode der initialiserer bøger, til bøger og medlemmer
    def __init__(self):
        # Initialiser attributterne for "tomme" bøger
        self.books = {} # Gemmer bøger med book_id som nøgle
        self.members = {} # Gemmer medlemmer med member_id som nøgle

    # Tilføjer en bog til biblioteket
    def add_book(self, book):
        self.books[book.book_id] = book
    
    # Fjerner en bog fra biblioteket baseret på book_id
    def remove_book(self, book_id):
        return self.books.pop(book_id, "Book not found.")

    # Opdaterer information om en bog
    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id in self.books:
            if title:
                self.books[book_id].title = title # Opdaterer titel hvis givet
            if author:
                self.books[book_id].author = author # Opdaterer forfatter hvis givet
            if copies is not None:
                self.books[book_id].copies = copies # Opdaterer antal eksemplarer hvis givet
            return "Book updated."
        return "Book not found."
    
    # Tilføjer et medlem til biblioteket
    def add_member(self, member):
        self.members[member.member_id] = member

    # Fjerner et medlem fra biblioteket baseret på member_id
    def remove_member(self, member_id):
        return self.members.pop(member_id, "Member not found.")

    # Opdaterer information om et medlem
    def update_member(self, member_id, name=None):
        if member_id in self.members:
            if name:
                self.members[member_id].name = name
            return "Member updated."
        return "Member not found."

    # Udleverer en bog til et medlem (bog udlånes)
    def issue_book(self, book_id, member_id):
        if book_id in self.books and member_id in self.members:
            return self.members[member_id].borrow_book(self.books[book_id])
        return "Book or Member not found."

    # Modtager en bog retur fra et medlem (bog afleveres)
    def return_book(self, book_id, member_id):
        if book_id in self.books and member_id in self.members:
            return self.members[member_id].return_book(self.books[book_id])
        return "Book or Member not found."

    # Viser information om alle bøger i biblioteket
    def display_books(self):
        return [book.display_info() for book in self.books.values()]

    # Viser information om alle medlemmer i biblioteket
    def display_members(self):
        return [member.display_info() for member in self.members.values()]
    

# Hovedfunktionen, hvor programmet starter
def main():
    # Opretter et nyt bibliotek-objekt
    library = Library()

    while True:
        # Udskriver menuen til brugeren
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book")
        print("4. Add Member")
        print("5. Remove Member")
        print("6. Update Member")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Display Books")
        print("10. Display Members")
        print("11. Exit")
        
        # Spørger brugeren om et valg
        choice = input("Enter choice: ")

        # Tilføj en ny bog
        if choice == "1":
            book_id = input("Enter book ID: ") # Beder om bogens ID
            title = input("Enter title: ") # Beder om titel
            author = input("Enter author: ") # Beder om forfatter
            copies = int(input("Enter copies: ")) # Beder om antal eksemplarer
            library.add_book(Book(book_id, title, author, copies)) # Tilføjer bogen til biblioteket

        # Fjern en bog
        elif choice == "2":
            book_id = input("Enter book ID to remove: ") # Beder om ID på bogen der skal fjernes
            print(library.remove_book(book_id)) # Fjerner og viser resultatet

        # Opdater en bog
        elif choice == "3":
            book_id = input("Enter book ID to update: ") # Beder om bogens ID
            title = input("Enter new title (or leave blank): ") or None # Ny titel, eller None
            author = input("Enter new author (or leave blank): ") or None # Ny forfatter, eller None
            copies = input("Enter new copies (or leave blank): ") # Nye eksemplarer, eller None
            copies = int(copies) if copies else None
            print(library.update_book(book_id, title, author, copies)) # Udfører opdatering

        # Tilføj nyt medlem
        elif choice == "4":
            member_id = input("Enter member ID: ") # Opretter medlems ID
            name = input("Enter name: ") # Medlems navn
            library.add_member(Member(member_id, name)) # Tilføjer medlem

        # Fjern medlem
        elif choice == "5":
            member_id = input("Enter member ID to remove: ") # ID på medlem der skal fjernes
            print(library.remove_member(member_id)) # Fjerner og viser resultat

        # Opdater medlem
        elif choice == "6":
            member_id = input("Enter member ID to update: ") # ID på medlem
            name = input("Enter new name (or leave blank): ") or None # Nyt navn eller None
            print(library.update_member(member_id, name)) # Opdaterer medlem

        # Udlån en bog
        elif choice == "7":
            book_id = input("Enter book ID to issue: ") # ID på bog der skal udlånes
            member_id = input("Enter member ID: ") # ID på medlem der låner
            print(library.issue_book(book_id, member_id)) # Gennemfører udlån

        # Modtag en bog retur
        elif choice == "8":
            book_id = input("Enter book ID to return: ") # ID på bog der returneres
            member_id = input("Enter member ID: ") # ID på medlem der returner
            print(library.return_book(book_id, member_id)) # Gennemfører returnering

        # Vis alle bøger i biblioteket
        elif choice == "9":
            print("Books in library:")
            for book in library.display_books():
                print(book) # Udskriver info om hver bog

        # Vis alle medlemmer i biblioteket
        elif choice == "10":
            print("Members in library:")
            for member in library.display_members():
                print(member) # Udskriver info om hvert medlem

        # Afslut programmet
        elif choice == "11":
            print("Exiting...")
            break # Stopper while-løkken og afslutter programmet

        # Hvis brugerens input ikke er gyldigt
        else:
            print("Invalid choice, please try again.")

# Sikrer at main() kun kører når filen køres direkte
if __name__ == "__main__":
    main()
