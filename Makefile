
install:
	pip3 install nose
	pip3 install -r requirements.txt

tests:
	cd src; nosetests tests.py

tests_api:
	cd src; nosetests testapi.py

start: #inicio del servicio añadiendo un alias
	pm2 start 'gunicorn main:app -b 0000:5000 -w 2' --name "api"

stop: # paramos el servicio
	pm2 stop api

restart: # reiniciamos el servicio
	pm2 restart api

delete: #eliminamos el servicio de la lista de procesos
	pm2 delete api

show: #Obtenemos más detalles sobre nuestro proceso
	pm2 show api
