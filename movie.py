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

   def play (self, step=1):
       self.play_number += step

   def play_random(self):
       self.play_number += random.randint(1,100)

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

#definiujemy funkcję której wywołanie spowoduje zwiększenie liczby oglądniętych odcinków losowego serialu, filmu
def generate_views(temp_list): 
    temp_list[random.randint(0, len(temp_list)-1)].play_random()
    return temp_list

#definiujemy funkcje która zwróci nam listę filmów posortowaną alfabetycznie
def get_movie(list):
    temp_list = []
    for i in range (len(list)):
        if isinstance(list[i],Series) is False:
            temp_list.append(list[i])
    list = sorted(temp_list, key=lambda title: title.title)
    return list

#definiujemy funkcje która zwróci nam listę seriali posortowaną alfabetycznie
def get_series(list):
    temp_list = []
    for i in range (len(list)):
        if isinstance(list[i],Series) is True:
            temp_list.append(list[i])
    list = sorted(temp_list, key=lambda title: title.title)
    return list

#definiujemy funkcję wyszukiwania filmów/seriali
def search(list):
    movie_to_search = input("Wpisz nazwe szukanego filu lub serialu: ")
    for i in range(len(list)):
        if movie_to_search == list[i].title:
            print(f"Film/serial został znaleziony w bazie danych. Znajduje się na pozycji:  {i+1}. {list[i]}")
            return
    print(f"Filmu/Serialu {movie_to_search} nie znaleziono w bazie danych")

#definiujemy funkcję która powtórzy nam operację generowania oglądnięć filmów/seriali określoną ilość razy
def repeat_generate_views(num_of_repeat,list):
    for i in range(num_of_repeat):
        generate_views(list)

#Funkcja która ma nam zwrócić listę top 3 seriali/filmów
def top_titles(list):
    temp_list=[]
    list = sorted(list, key=lambda i: i.play_number)
    temp_list.append(list[-1])
    temp_list.append(list[-2])
    temp_list.append(list[-3])
    return temp_list

#dodatkowa funkcja która generuje losowo ilości seriali oraz ich epizodów oraz sezonów
def generate_full_series(temp_s_and_m_list):
    number_of_series = random.randint(3, 4)
    for i in range (number_of_series):
        series_title = fake.catch_phrase()
        series_release_year = fake.year()
        series_category = random_category()
        numb_of_seasons = random.randint(2, 4)
        number_of_epizodes = random.randint(4, 9)
        for j in range(numb_of_seasons):
            for k in range(number_of_epizodes):
                    temp_s_and_m_list.append(Series(title=series_title ,release_year=series_release_year ,category=series_category , season_number=j+1 ,epizode_number=k+1))
    return temp_s_and_m_list

#______________Początek głównego programu___________________
#użytkownik definiuje czy chce stworzyć wizytówki biznesowe czy prywatne
if __name__ == "__main__":
    print("Biblioteka filmów")

# losowo generujemy dowolną ilość filmów (pomięzy 10 a 20) i dodajemy do listy
    mov_ser_base_list = []
    for i in range(random.randint(10, 20)):
        mov_ser_base_list.append(Movies(title=fake.city() ,release_year=fake.year() ,category=random_category() ))

#wywołujemy funkcję odpowiedzialną za generowanie seriali
    mov_ser_base_list = generate_full_series(mov_ser_base_list)

#wywołanie funkcji która doda losową ilość  odtworzeę (miedzy 1 a 100) dla losowego filu/serialu
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