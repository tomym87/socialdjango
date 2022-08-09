ls
cd ..
ls
pwd
exit
ls
pwd
mkdir env
ls
python3 -m venv /home/tomy/env/md
source ~/env/md/bin/activate
ls
git clone https://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@github.com/tomym87/djangotwitter.git
ls
ls djangotwitter/
sudo mv djangotwitter/social_project ../
usermod -aG sudo tomy\
usermod -aG sudo tomy
sudo usermod -aG sudo tomy
deactivate
su root
ls
sudo mv djangotwitter/social_project ../
ls
ls djangotwitter/
cd ..
ls
sudo mv social_project /home/tomy/
ls
cd tomy/
ls
ls env/
source ~/env/md/bin/activate
ls
cd djangotwitter/
ls
pip install -r requirements.txt
cdc ..
cd ..
ls
clear
ls
ls social_project
ls
pwd
ls env/
ls
cd social_project/
ls
python manage.py runserver 0.0.0.0:8000
sudo apt-get install python3.8-dev
sudo apt-get install gcc
pip install uwsgi
sudo nano test.py
ls
uwsgi --http :8000 --wsgi-file test.py
ls
uwsgi --http :8000 --module social_project.uwsgi
uwsgi --http :8000 --module social_project.wsgi
sudo apt-get install nginx
sudo nano /etc/nginx/sites-available/social_project.conf
sudo nano uwsgi_params
sudo ln -s /etc/nginx/sites-available/social_project.conf /etc/nginx/sites-enabled/
nano social_project/settings.py 
python manage.py collectstatic
ls
ls media
sudo /etc/nginx/init.d/nginx restart
nginx
sudo /etc/init.d/nginx restart
uwsgi --socket social_project.sock --module social_project.wsgi --chmod-socket=666
sudo nano social_project_uwsgi.ini
uwsgi --ini social_project_uwsgi.ini
ps aux
ls /home/tomy/
cd /home/tomy/env/md/
mkdir vassals
sudo ln -s /home/tomy/social_project/social_project_uwsgi.ini /home/tomy/env/md/vassals/
sudo reboot
