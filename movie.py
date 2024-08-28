#Import niezbednych bibliiotek
from faker import Faker
import random
import datetime
fake = Faker()

#definicja klasy movie na podstawie której bedą tworzone instancje dla filmów
class Movies:
    def __init__(self, title, release_year, category):
        self.title = title
        self.release_year = release_year
        self.category = category
        #zmienna
        self.play_number = 0

    def play(self, step=1):
        self.play_number += step

    def __str__(self):
        return f"{self.title} {self.release_year} Play number: {self.play_number}"

#definicja klasy series na podstawie której bedą tworzone instancje dla seriali
class Series(Movies):
    def __init__(self, season_number, epizode_number, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.epizode_number = epizode_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.epizode_number:02d} Play number: {self.play_number}"

# definiujemy funkcje która bedzie nadawała losowe katergorie filmom lub serialom ze zdefiniowanej listy
def random_category():
    return random.choice( ["Action", "Thriller", "Horror", "Sci-Fi", "Documentary", "Romance comedy", "Romance comedy" ] )

#definiujemy funkcje która zwróci nam listę filmów posortowaną alfabetycznie
def get_movie(funct_list):
    funct_list = list_sorting(reco_class_type(funct_list,Movies))
    return funct_list

#definiujemy funkcje która zwróci nam listę seriali posortowaną alfabetycznie
def get_series(funct_list):
    funct_list = list_sorting(reco_class_type(funct_list,Series))
    return funct_list

def list_sorting(funct_list):
    return sorted(funct_list, key=lambda title: title.title)

#definiujemy funkcję która rozpoznaje które instancje to seriale a które to filmy i zwraca odpowiedznią listę do funkcji get_series lub get_movie
def reco_class_type(funct_list,type_of_class):
    temp_list=[]
    for i in range(len(funct_list)):
        if type(funct_list[i]) is type_of_class:
            temp_list.append(funct_list[i])
    return temp_list

#definiujemy funkcję wyszukiwania filmów/seriali
def search(funct_list):
    movie_to_search = input("Wpisz nazwe szukanego filu lub serialu: ")
    for i in range(len(funct_list)):
        if movie_to_search == funct_list[i].title:
            print(f"Film/serial został znaleziony w bazie danych. Znajduje się na pozycji:  {i+1}. {list[i]}")
            return
    print(f"Filmu/Serialu {movie_to_search} nie znaleziono w bazie danych")

#definiujemy funkcję która powtórzy nam operację generowania oglądnięć filmów/seriali określoną ilość razy
def repeat_generate_views(num_of_repeat,temp_list):
    for i in range(num_of_repeat):
        generate_views(temp_list)

#definiujemy funkcję której wywołanie spowoduje zwiększenie liczby oglądniętych odcinków losowego serialu, filmu
def generate_views(temp_list): 
    num_of_plays = random.randint(1,100)
    random_list_element = temp_list[random.randint(0, len(temp_list)-1)]
    for i in range(num_of_plays):
        random_list_element.play()

#Funkcja która ma nam zwrócić listę top 3 seriali/filmów
def top_titles(funct_list):
    funct_list = sorted(funct_list, key=lambda i: i.play_number)
    funct_list.reverse()
    return funct_list

def generate_full_series():
    temp_series_list=[]
    number_of_series = random.randint(2, 3)
    for i in range(number_of_series):
        series_title = fake.catch_phrase()
        series_release_year = fake.year()
        series_category = random_category()
        numb_of_seasons = random.randint(2, 4)
        number_of_epizodes = random.randint(3, 6)
        for j in range(numb_of_seasons):
            for k in range(number_of_epizodes):
                temp_series_list.append(Series(title=series_title ,release_year=series_release_year ,category=series_category , season_number=j+1 ,epizode_number=k+1))
    return temp_series_list


#______________Początek głównego programu___________________
#użytkownik definiuje czy chce stworzyć wizytówki biznesowe czy prywatne
if __name__ == "__main__":
    print("Biblioteka filmów")
    mov_ser_base_list =[]

#losowo generujemy dowolną ilość filmów (pomięzy 5 a 10) i dodajemy do listy filmów
    mov_base_list = []
    for i in range(random.randint(5, 10)):
        mov_base_list.append(Movies(title=fake.city() ,release_year=fake.year() ,category=random_category() ))

#Listę całkowitą z filmami i serialami rozszeszamy najpierw o wygenerowane filmy, a nastepnie o wygenerowane seriale
    mov_ser_base_list.extend(mov_base_list)
    mov_ser_base_list.extend(generate_full_series())

#wywołanie funkcji która doda losową ilość  odtworzeń (miedzy 1 a 100) dla losowego filmu/serialu
    repeat_generate_views(10, mov_ser_base_list)

#wyświetlamy pełną listę seriali i filmów dla przejrzystowści działania programu
    print("All Movies & Series in database")
    for i in range(len(mov_ser_base_list)):
        print(i+1, " ", mov_ser_base_list[i])

#wyświetlamy wszytskie filmy posortowane pod względem nazwy
    sorted_series_movie = get_movie(mov_ser_base_list)
    print("Movies only, sorted by title:")
    for i in range(len(sorted_series_movie)):
        print(i+1, " ", sorted_series_movie[i])

#wyświetlamy wszytskie seriale posortowane pod względem nazwy
    sorted_series_movie = get_series(mov_ser_base_list)
    print("Series only, sorted by title:")
    for i in range(len(sorted_series_movie)):
        print(i+1, " ", sorted_series_movie[i])

#Wyświetlamy top 3 seriale lub filmy z dzisiejszego dnia
    top_tiles = top_titles(mov_ser_base_list)
    print(f"Najpopularniejsze filmy i seriale dnia {datetime.datetime.now().strftime("%d")}.{datetime.datetime.now().strftime("%m")}.{datetime.datetime.now().strftime("%y")} \n 1.{top_tiles[0]}\n 2.{top_tiles[1]} \n 3.{top_tiles[2]}")
 
# Uruchamiamy funkcję wyszukiwania danego serialu/filmu w naszej bazie danych
    search(mov_ser_base_list)