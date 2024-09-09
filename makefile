all:
	@echo "make db			- Start postgres container"
	@echo "make app			- Start app container"
	@echo "make devenv      - install enviroment python3.12"
	@echo "make compose     - build and run app, db services"
	@exit 0

devenv: clean
	rm -rf env
	# создаем новое окружение
	apt-get install python3-venv
	python3.12 -m venv env
	env/bin/python3.12 -m pip install pip --upgrade
	env/bin/python3.12 -m pip install wheel
	# ставим зависимости
	env/bin/python3.12 -m pip install -r requirements.txt

redis:
	docker stop redis-container || true
	docker compose run -d -p 6379:6379 --name redis-container

app:
	docker stop backend-container || true
	docker compose run -d -p 8002:8002 --name backend-container

compose:
	docker compose up --build -d