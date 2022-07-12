import sqlite3
from errors_classes import ValueNotInAuditoryRange
import cursor as cursor
import family as family

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


def validate_rating(auditory):
    children = ["G", None, None]
    family = ["G", "PG", "PG-13"]
    adult = ["R", "NC-17", None]
    if auditory == "children":
        auditory = children
    elif auditory == "family":
        auditory = family
    elif auditory == "adult":
        auditory = adult
    else:
        raise ValueNotInAuditoryRange("Нет такого рейтинга!")
    return auditory


def get_dict_by_rating(auditory):
    auditory = validate_rating(auditory)
    cur = create_cursor()
    select_query = """SELECT  title, `rating`, `description`
                            FROM netflix
                            where `rating` = ? or rating = ? or rating = ?
                            LIMIT 50
                            """
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
