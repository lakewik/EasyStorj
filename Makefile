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
	virtualenv -p python2 $(VENV)
	$(PIP) install -r $<
	ln -s /usr/lib/python2.7/dist-packages/PyQt4 $(VENV)/lib/python2.7/site-packages/
	ln -s /usr/lib/python2.7/dist-packages/sip.*so $(VENV)/lib/python2.7/site-packages/
