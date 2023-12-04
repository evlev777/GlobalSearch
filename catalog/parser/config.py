import os


SERVER_NAME = os.getenv("SERVER_NAME")
PORT = os.getenv("PORT")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")


def create_sql_query(user_str: str) -> str:
    sql_query = f"""
    SELECT [DOC_ID]
      ,[REFRESH]
      ,[SORT1]
      ,[SORT2]
      ,[SORT3]
      ,[ERES]
      ,[UID]
      ,[CRDATE]
      ,[IRI]
      ,[TITLE]
      ,[DOCTYPE]
    FROM [A_Met_Book].[dbo].[DOCREF] where TITLE like '%{user_str}%'
    """
    return sql_query
