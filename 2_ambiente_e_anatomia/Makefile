NO_COLOR=\x1b[0m
OK_COLOR=\x1b[32;01m
INFO_COLOR=\x1b[1;36m

ERROR_COLOR=\x1b[31;01m
WARN_COLOR=\x1b[33;01m
MAKEFILE_DIR=$(shell pwd)

env:
	@echo -e "$(INFO_COLOR)Virtualenv setup$(NO_COLOR)"
	@virtualenv --python=python3.7 semcomp_env	
	@echo -e "$(OK_COLOR)Virtualenv OK$(NO_COLOR)"
req:
	@echo -e "$(INFO_COLOR)Installing requirements$(NO_COLOR)"
	@pip install -r requirements.txt	
	@echo -e "$(OK_COLOR)Requirements OK$(NO_COLOR)"
project:
	@echo -e "$(INFO_COLOR)Creating project$(NO_COLOR)"
	@django-admin.py startproject $(name)
	@echo -e "$(OK_COLOR)Project $(name) OK$(NO_COLOR)"\
