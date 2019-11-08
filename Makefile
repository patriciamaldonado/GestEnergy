
install: #instalamos dependencias
	pip3 install nose
	npm install -g n
	npm install -g pm2
	node -v
	pm2 -v
	pip3 install -r requirements.txt

tests: # ejecutamos tests unitarios
	cd src; nosetests tests.py

tests_api: #ejecutamos tests de integración para la api
	cd src; nosetests testapi.py

start-heroku: #para el despliegue en heroku
	cd src; gunicorn main:app -b 0000:$(PORT)

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
