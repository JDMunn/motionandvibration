CWD=$(shell pwd)
ENV=$(CWD)/env

default: dev $(ENV)

$(ENV):
	virtualenv -p python3 $(ENV)
	$(ENV)/bin/pip install -r requirements.txt


clean:
	rm -Rf $(ENV) || true
	make -C app/static clean

dev:
	make -C app/static dev

prod:
	make -C app/static prod


check:
	PYTHONPATH=$(CWD) $(ENV)/bin/python -m unittest discover app/

run: $(ENV) prod
	rm app/static/js/app_bundle.js; browserify app/static/js/app.js > app/static/js/app_bundle.js; \
	    $(ENV)/bin/gunicorn -b 0.0.0.0:8082 --chdir app api:app --log-level debug

