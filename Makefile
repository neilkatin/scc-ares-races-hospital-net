

HospitalNetScript.html: HospitalNetScript.jinja

%.html: %.jinja
	pipenv run ./jinja_run.py --template $< --output $@
