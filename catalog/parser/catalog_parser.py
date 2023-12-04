from typing import List
import pymssql
from .config import create_sql_query, SERVER_NAME, PORT, USER_NAME, PASSWORD


def catalog_parser(user_str: str) -> List:

    try:
        with pymssql.connect(
            server=SERVER_NAME,
            port=PORT,
            user=USER_NAME,
            password=PASSWORD,
            database='A_Met_Book',
            as_dict=True
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(create_sql_query(user_str))
            list_db = cursor.fetchall()
            catalog_api = []

            for item in list_db:
                catalog_api.append({
                    'year': item.get('SORT1').split('/')[0],
                    'author': item.get('SORT2').split('/')[0].title(),
                    'title': item.get('TITLE'),
                    'url': f'https://books.bsuir.by/MegaPro/UserEntry?Action=FindDocs&ids={item.get("DOC_ID")}'
                })

            return catalog_api
    except AttributeError:
        return []
