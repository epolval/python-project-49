install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
	
package-uninstall:
	python3 -m pip uninstall hexlet-code
	
lint:
	poetry run ruff check

lint-fix:
	poetry run ruff check --fix

calc:
	poetry run brain-calc

even:
	poetry run brain-even

gcd:
	poetry run brain-gcd

prime:
	poetry run brain-prime

progression:
	poetry run brain-progression
