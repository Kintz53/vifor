class Library:
    library = None
    def __init__(self):
        self.__books = []

    @classmethod
    def get_instance(cls):
        if cls.library == None:
            cls.library = Library()
        return cls.library

    @property
    def books(self):
        return self.__books

    def setNewBook(self, book):
        self.__books.append(book)

    def delBook(self, book):
        self.__books.remove(book)


class Book:
    take=False
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @title.setter
    def title(self, newtitle):
        self.__title = newtitle



    @author.setter
    def author(self, newauthor):
        self.__author = newauthor

    def __eq__(self, other):
        return (self.__title == other.__title and self.__author == other.__author)


class User:
    def __init__(self, pseudo):
        self.__pseudo = pseudo
        self.__borrowedBooks = []

    @property
    def pseudo(self):
        return self.__pseudo
    def borrowBook(self, indexBook):
        library = Library.get_instance()
        if library.books[indexBook:indexBook + 1]:
            self.__borrowedBooks.append(library.books[indexBook])

    def readBook():
        pass


class Menu():
    Library = Library().get_instance()

    def __init__(self,user1):
        self.user=user1

    def menu_choix(self):
        print("--------------------------Menu-----------------------------")
        print("-------------tapper 1 pour recuper un livre----------------")
        print('-------------tapper 2 pour ajouter un livre----------------')
        print('-------------tapper 3 supprimer le livre-------------------')
        print('---------------tapper 4 rendre le livre--------------------')
        print('--------------tapper 5 Modifier un livre ------------------')
        print('-------------tapper 6 pour Quitter le menu ----------------')
        a = int(input())
        match a:
            case 1:
                self.menu_recupe()
            case 2:
                self.menu_add()
    def menu_recupe(self):
        livres_disponibles = [
            (index, i) for index, i in enumerate(Library().get_instance().books) if not i.take
        ]
        for index, i in enumerate(Library().get_instance().books):
            if not i.take:
                print(f"Il reste le livre {i.title} écrit par {i.author} avec l'index {index}")
        if len(livres_disponibles)!=0:
            print('Quel livre voulez vous prendre ? ')
            a=input()
            a=int(a)
            user.borrowBook(a)
            Library().get_instance().books[a].take=True
            self.menu_choix()
        else:
            print('Pas de livre de dispo ! ')
            self.menu_choix()

    def menu_add(self):
        titre=input('donner le titre du livre')
        auteur=input('Donner l auteur du livre')
        book=Book(titre,auteur)
        Library().get_instance().books.append(book)
        self.menu_choix()

nom=input('Donner votre nom : ')
user=User(nom)
menu = Menu(user)
menu.menu_choix()