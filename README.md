# selenium-python-dummy

#vscode python
1.extension : python | code runner

2.install linter

3.add create virtual env, ".venv"

DNID1084L01:sample_python muksidini$ python3 -m venv .venv
DNID1084L01:sample_python muksidini$ source .venv/bin/activate

4.install selenium
	pip3 install -U selenium
	pip3 install webdriver-manager
	pip3 install behave
	
5.run

# run all tests
behave

# run the scenarios in a feature file
behave features/web.feature

# run all tests that have the @duckduckgo tag
behave --tags @duckduckgo

# run all tests that do not have the @unit tag
behave --tags ~@unit

# run all tests that have @basket and either @add or @remove
behave --tags @basket --tags @add,@remove
