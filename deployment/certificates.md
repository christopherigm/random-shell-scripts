------------------------------------------- CERTIFICADOS SSL
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx

$ sudo certbot --nginx -d db.qa.iguzman.com.mx -d db.staging.iguzman.com.mx -d db.iguzman.com.mx
$ sudo service nginx restart

$ sudo crontab -e
    > 15 3 * * * /usr/bin/certbot renew --quiet
