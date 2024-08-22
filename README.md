**  Instalación AIRFLOW   **

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html



**  Dar acceso a la Base de MySQL desde el contenedor  **
1) Ensure MySQL is Listening on All Interfaces:

Check if MySQL is configured to listen to external connections.
Open /etc/mysql/my.cnf or /etc/mysql/mysql.conf.d/mysqld.cnf and ensure the bind-address is set to 0.0.0.0
[mysqld]
bind-address = 0.0.0.0

2) Allow MySQL User to Connect Remotely:

Ensure your MySQL user is allowed to connect from any host (%). You can run the following in MySQL:

You will need to add the IP address of each system that you want to grant access to, and then grant privileges:
CREATE USER 'root'@'ip_address' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'ip_address';

If you see %, well then, there's another problem altogether as that is "any remote source". 
If however you do want any/all systems to connect via root, use the % wildcard to grant access:
CREATE USER 'root'@'%' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';

Finally, reload the permissions, and you should be able to have remote access:
FLUSH PRIVILEGES;


** Microsoft SQL Server **
# usar tds_version='7.0' en string connection

import pymssql
conn = pymssql.connect(server='192.168.2.111', user='am', password='dl', database='omicronvt', tds_version='7.0')


