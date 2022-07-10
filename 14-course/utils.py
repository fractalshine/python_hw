import sqlite3


def to_title_case(string):
    return str(string).title()


def create_connection(db_file):
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


def get_dict_by_title(conn, title):
    cursor = conn.cursor()
    title_upper = to_title_case(title)
    select_query = """SELECT `title`, `country`, `release_year`, `listed_in`, `description`
                    FROM netflix
                    where title = ?"""
    cursor.execute(select_query, (title_upper,))

    full_result = cursor.fetchall()
    title = full_result[0][0]
    country = full_result[0][1]
    release_year = full_result[0][2]
    genre = full_result[0][3]
    description = full_result[0][4]
    dict_by_title = {
        "title": title,
        "country": country,
        "release_year": release_year,
        "genre": genre,
        "description": description
    }

    return dict_by_title


def main():
    database = "netflix.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print(get_dict_by_title(conn, "american son"))


if __name__ == '__main__':
    main()
