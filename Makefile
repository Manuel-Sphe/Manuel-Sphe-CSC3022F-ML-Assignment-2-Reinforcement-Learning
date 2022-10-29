insatll: venv
	. venv/bin/activate; python3 -m pip install --upgrade pip;pip3 install -Ur req.txt
venv:
	test -d venv || python3 -m venv venv

clean:
	rm -rf venv
	#find -iname "*.pyc" -delete
run1:
	. venv/bin/activate; python3 src/Scenario1.py

run2:
	. venv/bin/activate; python3 src/Scenario2.py

