#!/usr/bin/env bash

# This script deletes the database hbtn_0c_0 in the MySQL server

mysql -uroot -p -e "DROP DATABASE IF EXISTS hbtn_0c_0;"
