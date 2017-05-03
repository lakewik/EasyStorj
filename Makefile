.PHONY: all clean run

VENV := venv
MAIN := main.py

PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python

all run: $(VENV) $(MAIN)
	$(PYTHON) $(MAIN)

clean:
	@ rm -rf $(VENV)

$(VENV): requirements.txt
	virtualenv --system-site-packages -p python2 $(VENV)
	$(PIP) install -r $<
