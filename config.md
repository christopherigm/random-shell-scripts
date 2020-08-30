$ sudo apt update
$ sudo apt upgrade
$ sudo passwd root
$ sudo apt install openssh-server upstart supervisor htop ufw python3

$ sudo groupadd developers
$ groups
$ sudo adduser USERNAME
$ sudo adduser --system --no-create-home USERNAME
$ usermod -m -d /newhome/username USERNAME
$ sudo adduser USERNAME sudo
$ sudo adduser USERNAME GROUPNAME
$ sudo userdel USERNAME
$ sudo nano /etc/sudoers
    > USERNAME    ALL=(ALL:ALL) ALL
$ export LC_ALL=C

-------------------------------------------
$ ssh-keygen -t rsa -C "christopher.guzman.monsalvo@gmail.com"
$ ssh-keygen -t rsa
$ cat ~/.ssh/id_rsa.pub

$ ssh-copy-id user@host.com
$ sudo nano /etc/ssh/sshd_config
    > PermitRootLogin without-password
$ reload ssh OR sudo service ssh restart

$ sudo nano ~/.bashrc
    > alias python=python3
$ . ~/.bashrc
-------------------------------------------

#Node & NPM
$ sudo apt install npm
$ sudo npm install ansi npm -g
$ sudo mkdir /usr/local/node
//https://nodejs.org/es/download/current/
$ wget https://nodejs.org/dist/v9.3.0/node-v9.3.0-linux-x64.tar.xz
$ sudo mv node-v8.4.0-linux-x64 /usr/local/node/
$ sudo mv /usr/bin/nodejs /usr/bin/nodejs2
$ sudo ln -s /usr/local/node/node-v8.4.0-linux-x64/bin/node /usr/bin/nodejs
$ sudo ln -s /usr/local/node/node-v8.4.0-linux-x64/bin/node /usr/bin/node
$ sudo npm i bower gulp -g

#DB
$ sudo apt install mysql-server
$ sudo apt install postgresql postgresql-contrib
$ sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
$ sudo apt-get update
$ sudo apt-get install postgis
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
$ echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
$ sudo apt update
$ sudo apt install -y mongodb-org
$ sudo systemctl enable mongod.service
$ sudo service mongod start

#Web Servers
$ sudo apt install nginx
$ sudo apt install apache2
$ sudo a2enmod rewrite
$ sudo a2enmod ssl
$ sudo apt install curl
$ sudo apt install php php-cli php-mcrypt libapache2-mod-php php-mysql
$ sudo apt-get install php-xml
$ sudo apt-get install php-mbstring
$ sudo apt-get install php-curl

#Python & VirtualEnvs
$ sudo apt install libpq-dev python-dev python3-dev build-essential python-setuptools postgresql-server-dev-all python-psyc opg2


$ sudo apt install python3-distutils
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo pip install django-admin-tools virtualenv virtualenvwrapper


$ sudo pip install django-admin-tools
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
$ sudo pip install --upgrade youtube_dl
$ sudo pip install gunicorn

$ sudo nano ~/.bashrc
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
$ . ~/.bashrc



------------------------------------------- MySQL
$ mysql -h localhost -u root -p
> password: *****
mysql> use mysql;
mysql> SET PASSWORD FOR 'user'@'hostname' = PASSWORD('new-password');
mysql> FLUSH PRIVILEGES;

mysql> CREATE USER 'user'@'localhost' IDENTIFIED BY 'password'
mysql> GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> DROP USER 'user’@‘localhost';
-------------------------------------------

------------------------------------------- POSTGRESQL
$ sudo su - postgres
$ psql
# \connect DBNAME
# \dt
# CREATE USER root PASSWORD 'root';
# CREATE DATABASE sample WITH OWNER root;
# GRANT ALL PRIVILEGES ON DATABASE sample TO root;
# DROP DATABASE sample;

$ sudo su - postgres
$ pg_dump postgres > postgres_db.bak
$ createdb -T template0 restored_database
$ psql restored_database < database.bak

https://www.digitalocean.com/community/tutorials/how-to-backup-postgresql-databases-on-an-ubuntu-vps
-------------------------------------------

------------------------------------------- PostGIS
$ sudo su - postgres
$ psql -d DATABASE_NAME
DATABASE_NAME=# CREATE EXTENSION postgis;
DATABASE_NAME=# SELECT PostGIS_version();

# https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postgis-on-ubuntu-14-04
-------------------------------------------

=========================================================

------------------------------------------- Backup & Restore MongoDB
$ sudo mongodump --db newdb

$ sudo mkdir /var/backups/mongobackups
$ sudo mongodump --db newdb --out /var/backups/mongobackups/`date +"%m-%d-%y"`
$ sudo crontab -e
    > 3 3 * * * mongodump --out /var/backups/mongobackups/`date +"%m-%d-%y"`
$ sudo mongorestore --db newdb --drop /var/backups/mongobackups/01-20-16/newdb/
# https://www.digitalocean.com/community/tutorials/how-to-back-up-restore-and-migrate-a-mongodb-database-on-ubuntu-14-04
-------------------------------------------


------------------------------------------- SUPERVISOR
$ sudo nano /usr/local/bin/long.sh
#!/bin/bash
while true
do
	# Echo current date to stdout
	echo `date`
	# Echo 'error!' to stderr
	echo 'error!' >&2
	sleep 1
done

$ sudo chmod +x /usr/local/bin/long.sh

$ sudo nano /etc/supervisor/conf.d/long_script.conf
[program:long_script]
#directory=/home/user/
command=/usr/local/bin/long.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/long.err.log
stdout_logfile=/var/log/long.out.log

$ sudo supervisorctl reread
$ sudo supervisorctl update
$ tail /var/log/long.out.log

$ sudo supervisorctl status
$ sudo supervisorctl stop <name>
$ sudo supervisorctl start <name>
$ sudo supervisorctl restart <name>

# https://serversforhackers.com/c/monitoring-processes-with-supervisord
# https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps
-------------------------------------------

------------------------------------------- FIREWALL UFW
$ sudo ufw status
$ sudo ufw allow ssh
$ sudo ufw allow 22/tcp
$ sudo ufw allow 80/tc
$ sudo ufw deny 80/tcp
$ sudo ufw delete allow ssh
$ sudo ufw delete allow 80/tcp
$ sudo ufw status numbered
$ ufw app list
# https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server
-------------------------------------------

------------------------------------------- PIP INSTALL REQUIRIMENTS
$ pip install -r requiriments.txt
$ pip freeze -l > requiriments.txt
-------------------------------------------

------------------------------------------- VIRTUALENV
$ workon
$ mkvirtualenv -p /usr/bin/python3 sample
$ rmvirtualenv <name>
$ python manage.py collectstatic
$ gunicorn --bind 0.0.0.0:8080 --workers 3 --reload webservices_intertours.wsgi
-------------------------------------------

------------------------------------------- EJECUTAR DJANGO CON GUNICORN
gunicorn --bind 0.0.0.0:8000 -w 1 --reload APP_NAME.wsgi:application
-------------------------------------------

------------------------------------------- SUPERVISOR GUNICORN
[program:solefi]
command=/home/christopher/.virtualenvs/solefi/bin/gunicorn --bind 0.0.0.0:4001 --workers 1 --reload  webpage.wsgi:application
directory=/var/www/apps/solefi/webpage/
autostart=true
autorestart=true
stderr_logfile=/var/log/apps/solefi/error.log
stdout_logfile=/var/log/apps/solefi/output.log
-------------------------------------------

------------------------------------------- NGINX GZIP
$ sudo nano /etc/nginx/nginx.conf
gzip on;
gzip_disable "msie6";

gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_buffers 16 8k;
gzip_http_version 1.1;
gzip_min_length 256;
gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/vnd.ms-fontobject application/x-font-ttf font/opentype image/svg+xml image/x-icon image/svg+xml;

#https://www.digitalocean.com/community/tutorials/how-to-add-the-gzip-module-to-nginx-on-ubuntu-14-04
-------------------------------------------


------------------------------------------- NGINX DJANGO
server {
  listen   80;

  server_name solefi.vaggustudios.com solefi.com.mx www.solefi.com.mx;

  location /static/ {
    autoindex on;
    expires 30d;
    add_header Vary Accept-Encoding;
    access_log off;
    alias /var/www/apps/solefi/webpage/static/;
  }

  location / {
    proxy_pass http://127.0.0.1:4001/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_cache_bypass $http_upgrade;
  }
}
-------------------------------------------


------------------------------------------- CERTIFICADOS SSL
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx
$ sudo apt-get install python-certbot-apache
$ sudo certbot --apache -d example.com -d www.example.com
$ sudo certbot --nginx -d example.com -d www.example.com
$ sudo service nginx restart
$ sudo service apahce2 restart
$ sudo crontab -e
    > 15 3 * * * /usr/bin/certbot renew --quiet
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04
# https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04
-------------------------------------------

------------------------------------------- ATOM
$ sudo apm install atom-beautify
-------------------------------------------

------------------------------------------- RASPBERRY
# To Share Wifi - Ethernet Connetion
$ nm-connection-editor
# Get IP
$ sudo dhclient -r
# Enable SSH Interface
$ sudo raspi-confi
    > Interfacing Options -> SSH -> YES -> OK
$ sudo apt-get install python3

$ sudo raspi-config

$ sudo apt-get install software-properties-common
$ sudo apt-get install postgis
$ sudo apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
$ sudo pip install Pillow

# https://rhnvrm.github.io/2016-08-07-share-wifi-via-ethernet-gnome-3-20/
# https://www.cyberciti.biz/faq/howto-linux-renew-dhcp-client-ip-address/
-------------------------------------------

------------------------------------------- IPTABLES
$ sudo iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
# https://unix.stackexchange.com/questions/136190/iptables-rule-to-allow-incoming-ssh-connections
-------------------------------------------


------------------------------------------- Wordpress
$ chmod 777 -R wp-content
$ nano wp-config.php
    > define('FS_METHOD', 'direct');
-------------------------------------------



https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn
https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04
https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps


export let NODEJS_SERVER_URL = "http://127.0.0.1:8000";
export let BACKEND_URL = "http://intertours-dev.southcentralus.cloudapp.azure.com/";
