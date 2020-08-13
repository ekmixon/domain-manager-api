.PHONY: all help build logs loc up stop down

# make all - Default Target. Does nothing.
all:
	@echo "Flask helper commands."
	@echo "For more information try 'make help'."

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: build = build all containers
build:
	docker-compose build

# target: app logs - Runs flask logs in the terminal
logs:
	 docker attach --sig-proxy=false dm-api

# target: loc - Count lines of code.
loc:
	 loc src

# target: up - Run local web server.
up:
	 docker-compose up -d

# target: stop - Stop all docker containers
stop:
	docker-compose stop

# target: down - Remove all docker containers
down:
	docker-compose down

# target: shell - python shell within container
shell:
	docker exec -it dm-api python3