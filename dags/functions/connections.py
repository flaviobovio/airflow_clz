def ms_sql(database=''):
    """ Connection parameters for the Microsoft SQL Server

    Args:
        database (str, optional): Database schema, Defaults to ''

    Returns:
        dict: Connection parameters
    """

    connection_string = {
        'server': '192.168.2.111',
        'user': 'am',
        'password': 'dl',
        'database': database,
        'tds_version': '7.0'
    }    

    return connection_string


def my_sql(database=''):
    """ Connection parameters for the MySQL Server

    Args:
        database (str, optional): Database schema, Defaults to ''

    Returns:
        dict: Connection parameters
    """
    connection_string = {
        'server': '192.168.2.106',
        'user': 'airflow',
        'password': 'airflow',
        'database': database,
    }    

    return connection_string

