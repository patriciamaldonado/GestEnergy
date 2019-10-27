
install:
	pip3 install nose
	pip3 install -r requirements.txt

tests:
	cd src; nosetests test.py

tests_api:
	cd src; nosetests testapi.py

start:
	pm2 start 'gunicorn main:app -b 0000:5000 -w 2' --name "api"

stop:
	pm2 stop api
