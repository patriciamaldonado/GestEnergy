
install:
	pip3 install -r requirements.txt
tests:
	cd src; nosetests tests.py
