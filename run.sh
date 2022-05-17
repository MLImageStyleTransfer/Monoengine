python3.9 -m venv venv

./venv/bin/pip install -r requirements.txt

cd ./app/database

sudo docker-compose up -d

cd ../../

./venv/bin/python runner.py
