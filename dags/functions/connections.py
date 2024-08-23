def ms_sql(database=''):

    connection_string = {
        'server': '192.168.2.111',
        'user': 'am',
        'password': 'dl',
        'database': database,
        'tds_version': '7.0'
    }    

    return connection_string