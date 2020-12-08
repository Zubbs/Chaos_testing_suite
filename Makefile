all:
	docker-compose up --build -d
	pipenv install
	pipenv run python job_manager.py

