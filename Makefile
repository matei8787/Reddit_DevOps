prod_up:
	docker-compose -f docker-compose.prod.yml up --build --force-recreate

dev_up:
	docker-compose -f docker-compose.dev.yml up --build --force-recreate

stage_up:
	docker-compose -f docker-compose.stage.yml up --build --force-recreate


prod_down:
	docker-compose -f docker-compose.prod.yml down -v

stage_down:
	docker-compose -f docker-compose.stage.yml down -v

dev_down:
	docker-compose -f docker-compose.dev.yml down -v

prod_restart:
	docker-compose -f docker-compose.prod.yml down -v
	docker-compose -f docker-compose.prod.yml up --build

dev_restart:
	docker-compose -f docker-compose.dev.yml down -v
	docker-compose -f docker-compose.dev.yml up --build

stage_restart:
	docker-compose -f docker-compose.stage.yml down -v
	docker-compose -f docker-compose.stage.yml up --build

prod_kill:
	docker-compose -f docker-compose.prod.yml down -v --remove-orphans

dev_kill:
	docker-compose -f docker-compose.dev.yml down -v --remove-orphans

stage_kill:
	docker-compose -f docker-compose.stage.yml down -v --remove-orphans

prod_python:
	docker-compose -f docker-compose.prod.yml exec web python ./bugtracker/manage.py migrate --no-input
	docker-compose -f docker-compose.prod.yml exec web python ./bugtracker/manage.py collectstatic --no-input

dev_python:
	docker-compose -f docker-compose.dev.yml exec web python ./bugtracker/manage.py migrate --no-input
	docker-compose -f docker-compose.dev.yml exec web python ./bugtracker/manage.py collectstatic --no-input