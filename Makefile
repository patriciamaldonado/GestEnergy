.PHONY: install tests tests_api start-heroku start stop restart delete show
#revisado
install: #instalamos dependencias
	pip3 install nose
	npm install -g n
	npm install -g pm2
	node -v
	pm2 -v
	pip3 install -r requirements.txt

tests: # ejecutamos tests unitarios
	nosetests tests/test_clientes.py -v

tests_api: #ejecutamos tests de integración para la api
	nosetests tests/test_api.py -v

start-heroku: #para el despliegue en heroku
	gunicorn src.main:app -b 0000:$(PORT)

start: #inicio del servicio añadiendo un alias
	pm2 start 'gunicorn src.main:app -b 0000:5000 -w 2' --name "api"

stop: # paramos el servicio
	pm2 stop api

restart: # reiniciamos el servicio
	pm2 restart api

delete: #eliminamos el servicio de la lista de procesos
	pm2 delete api

show: #Obtenemos más detalles sobre nuestro proceso
	pm2 show api
