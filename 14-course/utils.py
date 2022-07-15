import sqlite3
from errors_classes import ValueNotInAuditoryRange

DB_PATH = "netflix.db"


def to_title_case(string):
    return str(string).title()


def validate_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        return e

    return conn


def create_cursor():
    conn = validate_connection(DB_PATH)
    with conn as connection:
        cursor = connection.cursor()

    return cursor


def get_dict_by_title(title):
    cur = create_cursor()
    select_query = """SELECT `title`, `country`, `release_year`, `listed_in`, `description`
                    FROM netflix
                    where `title` LIKE ?
                    ORDER BY `release_year` DESC
                    """
    cur.execute(select_query, ('%' + title + '%',))

    full_result = cur.fetchone()
    title = full_result[0]
    country = full_result[1]
    release_year = full_result[2]
    genre = full_result[3]
    description = full_result[4].rstrip()
    dict_by_title = {
        "title": title,
        "country": country,
        "release_year": release_year,
        "genre": genre,
        "description": description
    }

    return dict_by_title


def get_dict_by_year_range(from_year, to_year):
    cur = create_cursor()
    select_query = """SELECT `title`, `release_year`
                        FROM netflix
                        where `release_year` between ? and ?
                        LIMIT 20
                        """
    cur.execute(select_query, (from_year, to_year))

    full_result = cur.fetchall()
    dict_list = []
    for line in full_result:
        title = line[0]
        year = line[1]
        title_dict = {
            "title": title,
            "year": year
        }
        dict_list.append(title_dict)
    return dict_list


# def validate_and_create_auditory_list(auditory) -> list:
#     """Функция принимает аудиторию и возвращает соответствующий набор рейтингов"""
#
#     children = ["G", "G", "G"]
#     family = ["G", "PG", "PG-13"]
#     adult = ["R", "NC-17", None]
#     if auditory == "children":
#         auditory = children
#     elif auditory == "family":
#         auditory = family
#     elif auditory == "adult":
#         auditory = adult
#     else:
#         raise ValueNotInAuditoryRange("Нет такого рейтинга!")
#     return auditory


def validate_and_create_auditory_list(auditory) -> list:
    rate_system = {
        'children': ['G', 'G', 'G'],
        'family': ['G', 'PG', 'PG-13'],
        'adult': ['R', 'NC-17', 'R']
    }
    for key, value in rate_system.items():
        if auditory == key:
            return value
        elif auditory not in rate_system:
            raise ValueNotInAuditoryRange("Нет такого рейтинга!")


def generate_placeholder(items):
    """Создает последовательность вопросиков"""

    return ",".join(["?"] * len(items))


def get_dict_by_auditory(auditory):
    auditory = validate_and_create_auditory_list(auditory)
    cur = create_cursor()
    select_query = "SELECT  title, `rating`, `description` " \
                   "FROM netflix " \
                   "where `rating` IN (" + generate_placeholder(auditory) + ") LIMIT 50"

    cur.execute(select_query, auditory)

    full_result = cur.fetchall()
    dict_list = []
    for line in full_result:
        title = line[0]
        rating = line[1]
        description = line[2].rstrip()

        rating_dict = {
            "title": title,
            "rating": rating,
            "description": description
        }
        dict_list.append(rating_dict)
    return dict_list


def get_recent_dict_by_genre(genre):
    """Получаем список свежих фильмов по жанру"""

    cur = create_cursor()
    select_query = """SELECT  title, `description`
                      FROM netflix
                      where `listed_in` LIKE (?)
                      ORDER BY `release_year` DESC
                      LIMIT 10
    """
    cur.execute(select_query, ('%' + genre + '%',))
    full_result = cur.fetchall()
    dict_list = []
    for line in full_result:
        title = line[0]
        description = line[1].rstrip()
        genre_dict = {
            "title": title,
            "description": description,
        }
        dict_list.append(genre_dict)
    return dict_list


def get_actors(one, two):
    """Функция принимает имена двух актеров и возвращает список тех, кто играет с ними в паре больше 2 раз"""

    cur = create_cursor()
    actors_query = """
        SELECT "cast"
        FROM netflix
        WHERE "cast" LIKE ? AND "cast" LIKE ?
        """
    cur.execute(actors_query, ('%' + one + '%', '%' + two + '%'))
    full_result = cur.fetchall()
    list_of_actors = []
    for line in full_result:
        for actor in line:
            list_of_actors.append(actor)
    new = ', '.join(list_of_actors)
    new_list = new.split(', ')

    result = set()
    for actor in new_list:
        num = new_list.count(actor)
        if actor != one and actor != two and num > 2:
            result.add(actor)

    return result


def type_year_genre(type, release_year, genre):
    """Функция принимает тип, год и жанр фильмы и возвращает фильмы"""

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    type_query = """
    SELECT `title`, `description`
    FROM netflix
    WHERE `type` LIKE ?
    AND `release_year` LIKE ?
    AND `listed_in` LIKE ?
    """
    cur.execute(type_query, ("%" + type + "%", "%" + release_year + "%", "%" + genre + "%"))
    executed_type = cur.fetchall()
    con.close()
    return executed_type

