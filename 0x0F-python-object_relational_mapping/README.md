0x0F. Python - Object-relational mapping

<<<<<<< HEAD
Requirements

    MySQL server version 8.0 installed on Ubuntu 20.04
    Module MySQLdb
    Module SQLAlchemy

Scripts

    0-select_states.py: a script that connects to a MySQL server running on localhost at port 3306 and lists all states from the database hbtn_0e_0_usa.
    1-filter_states.py: a script that connects to a MySQL server running on localhost at port 3306 and lists all states with a name starting with N from the database hbtn_0e_0_usa.
    2-my_filter_states.py: a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
    3-my_safe_filter_states.py: a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. This script uses MySQLdb to prevent SQL injection attacks.
    4-cities_by_state.py: a script that lists all cities from the database hbtn_0e_4_usa.
    5-filter_cities.py: a script that takes in the name of a state as an argument and lists all cities of that state from the database hbtn_0e_4_usa.
    model_state.py: a Python file that contains the class definition of a State and an instance Base = declarative_base().
    7-model_state_fetch_all.py: a script that lists all State objects from the database hbtn_0e_6_usa.
    8-model_state_fetch_first.py: a script that prints the first State object from the database hbtn_0e_6_usa.
    9-model_state_filter_a.py: a script that lists all State objects that contain the letter 'a' in their name from the database hbtn_0e_6_usa.
    10-model_state_my_get.py: a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
    11-model_state_insert.py: a script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
    12-model_state_update_id_2.py: a script that changes the name of a State object from the database hbtn_0e_6_usa.
    13-model_state_delete_a.py: a script that deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.

Usage

All scripts should be run in the following format:

css

./[script_name.py] [mysql_username] [mysql_password] [database_name]


=======
This project focuses on the integration of two powerful technologies: databases and Python. In the first part, we will utilize the MySQLdb module to establish a connection with a MySQL database and execute SQL queries. In the second part, we will employ SQLAlchemy, an Object-Relational Mapper (ORM), to interact with the database using Python code instead of writing direct SQL queries. The goal is to abstract the storage details and provide a seamless way to manipulate objects without worrying about the underlying database implementation.
>>>>>>> d0153b2e63bb8ca337d081e9fc239d935850cc38
