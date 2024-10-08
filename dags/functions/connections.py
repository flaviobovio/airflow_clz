def ms_sql(database=''):
    """ Connection parameters for the Microsoft SQL Server

    Usage example: 
        import pymssql

        from functions.connections import ms_sql

        conn = pymssql.connect(**ms_sql())

    Args:
        database (str, optional): Database schema, Defaults to ''

    Returns:
        dict: Connection parameters
    """

    connection_string = {
        'server': '192.168.1.100', # Your Server IP
        'user': 'user1',
        'password': 'pwd1',
        'database': database,
        'tds_version': '7.0'
    }    

    return connection_string


def my_sql(database=''):
    """ Connection parameters for the MySQL Server

    Usage example: 
        import pymysql

        from functions.connections import my_sql
        
        conn = pymssql.connect(**my_sql())

    Args:
        database (str, optional): Database schema, Defaults to ''

    Returns:
        dict: Connection parameters
    """
    connection_string = {
        'host': '192.168.1.150', # Your Server IP
        'user': 'airflow',
        'password': 'airflow',
        'database': database,
    }    

    return connection_string

