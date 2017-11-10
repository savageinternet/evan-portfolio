all: npm less pyth copy

npm: package.json
	npm install

less: npm
	mkdir -p build/css
	./node_modules/less/bin/lessc less/style.less build/css/style.css

pyth: requirements.txt htmlize.py
	pip install -r requirements.txt
	python htmlize.py

copy: pyth less
	cp -r google2ef4f2b4bcd33bf5.html favicon.ico fonts img js robots.txt build

run: copy
	cd build && python -m http.server

clean:
	rm -r build/*
