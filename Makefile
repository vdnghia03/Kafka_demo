include .env

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	make down && make up

to_psql:
	docker exec -ti wh_postgres psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
