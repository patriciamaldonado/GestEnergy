#Revisado
install:
				pip3 install nose
				pip3 install -r requirements.txt
tests:
				cd src; nosetests tests.py
