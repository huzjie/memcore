PY ?= python3

.PHONY: doctor add eval test build run clean

doctor:
	$(PY) -m memcore doctor

add:
	$(PY) -m memcore add "$(CONTENT)" --force

eval:
	$(PY) -m memcore eval

serve:
	$(PY) -m memcore serve --host 0.0.0.0 --port 8080

test:
	$(PY) -m pytest -q

build:
	docker build -t memcore:latest .

run:
	docker run --rm -p 8080:8080 memcore:latest

clean:
	rm -rf build dist *.egg-info .pytest_cache
