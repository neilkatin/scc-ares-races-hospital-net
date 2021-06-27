SCC ARES/RACES Hospital Net Documents
=====================================


This repository holds scripts for the Santa Clara County ARES (Amature Radio Emergency Service)/RACES (Radio Ameteur Civil Emergency Service) group.

It holds the scripts we use to use our weekly radio nets.

The Hospital Net Script uses [jinja2](https://jinja.palletsprojects.com/en/3.0.x/) as the templating language.
There is a small python program (jinja_run.py) and a Makefile used to expand the template nto an html file.

The environment was build and tested using python 3.8.  It assumes you have gnu make and pipenv installed.

To set up the environment and expand the template:

```shell
pipenv --python 3.8             # set up the python virtual environment
pipenv update
make                            # expand the script template
```

The generated file uses the ```writing-mode: sideways-lr;``` CSS command; this seems to only work on Firefox,
so to generate the PDF document print using that browser.

