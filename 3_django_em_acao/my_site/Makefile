SHELL := /bin/bash

NO_COLOR=\x1b[0m
OK_COLOR=\x1b[32;01m
INFO_COLOR=\x1b[1;36m

ERROR_COLOR=\x1b[31;01m
WARN_COLOR=\x1b[33;01m

install_dependencies:
	@echo -e "$(INFO_COLOR)Installing Project Dependencies$(NO_COLOR)"
	@pip install -r ../requirements.txt
	@echo -e "$(OK_COLOR)All dependencies installed[OK]$(NO_COLOR)"
setup:
	@$(MAKE) install_dependencies
	@python3 manage.py migrate
	@echo -e "$(OK_COLOR)Django tables created and applied[OK]$(NO_COLOR)"
	@python3 manage.py makemigrations
	@echo -e "$(OK_COLOR)Apps tables created [OK]$(NO_COLOR)"
	@python3 manage.py migrate
	@echo -e "$(OK_COLOR)Apps tables applied [OK]$(NO_COLOR)"
	@echo -e "$(OK_COLOR)Setup done [OK]$(NO_COLOR)"
run:
	@python3 manage.py runserver
test:
	@python3 manage.py test $(app)
app:
	@python3 manage.py startapp $(name)
	@echo -e "$(OK_COLOR)App $(name) created [OK]$(NO_COLOR)"
packages:
	@pip freeze
clear:
	@find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@find . -path "*/migrations/*.pyc"  -delete
	@rm -rf db.sqlite3
	@echo -e "$(OK_COLOR)Database and migrations removed [OK]$(NO_COLOR)"
dep:
	@echo -e "$(INFO_COLOR)Installing Project Dependencies$(NO_COLOR)"
	@pip3 install -r ../requirements.txt
	@echo -e "$(OK_COLOR)All dependencies installed[OK]$(NO_COLOR)"
adm:
	@echo -e "$(INFO_COLOR)Creating Adm user$(NO_COLOR)"
	@python3 manage.py createsuperuser
	@echo -e "$(OK_COLOR)Super User was created[OK]$(NO_COLOR)"
migrations:
	@echo -e "$(OK_COLOR)Doing makemigrations[OK]$(NO_COLOR)"
	@python3 manage.py makemigrations
migrate:
	@echo -e "$(OK_COLOR)Doing migrate[OK]$(NO_COLOR)"
	@python3 manage.py migrate
