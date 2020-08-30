$ sudo apt update
$ sudo apt install postgresql postgresql-contrib postgis

$ sudo -i -u postgres
$ psql

#### LOCAL
# CREATE USER iguzman WITH PASSWORD 'iguzman';
# CREATE DATABASE iguzman WITH OWNER iguzman;
# GRANT ALL PRIVILEGES ON DATABASE iguzman TO iguzman;
# \c iguzman;
# create extension postgis;


#### QA
# CREATE USER iguzman_qa WITH PASSWORD 'password';
# CREATE DATABASE iguzman_qa WITH OWNER iguzman_qa;
# GRANT ALL PRIVILEGES ON DATABASE iguzman_qa TO iguzman_qa;
# \c iguzman_qa;
# create extension postgis;


#### STAGING
# CREATE USER iguzman_staging WITH PASSWORD 'password';
# CREATE DATABASE iguzman_staging WITH OWNER iguzman_staging;
# GRANT ALL PRIVILEGES ON DATABASE iguzman_staging TO iguzman_staging;
# \c iguzman_staging;
# create extension postgis;


#### MASTER
# CREATE USER iguzman_master WITH PASSWORD 'password';
# CREATE DATABASE iguzman_master WITH OWNER iguzman_master;
# GRANT ALL PRIVILEGES ON DATABASE iguzman_master TO iguzman_master;
# \c iguzman_master;
# create extension postgis;

$ export db_name=iguzman_qa && \
  export db_user=iguzman_qa && \
  export db_password=password && \
  python manage.py createsuperuser

$ export db_name=iguzman_staging && \
  export db_user=iguzman_staging && \
  export db_password=password && \
  python manage.py createsuperuser

$ export db_name=iguzman_master && \
  export db_user=iguzman_master && \
  export db_password=password && \
  python manage.py createsuperuser
