# sam build corre este archivo dentro de src/ y pasa ARTIFACTS_DIR.
# Instala wheels manylinux para el runtime de Lambda (python3.13) sin importar
# la version de Python de la maquina que compila.
PYTHON ?= python3
LAMBDA_PYTHON ?= 3.13
LAMBDA_ABI ?= cp313
LAMBDA_PLATFORM ?= manylinux2014_x86_64

build-OrchestratorFunction build-SimulatorFunction build-AggregatorFunction:
	mkdir -p "$(ARTIFACTS_DIR)"
	$(PYTHON) -m pip install -r requirements-lambda.txt -t "$(ARTIFACTS_DIR)" \
		--platform $(LAMBDA_PLATFORM) \
		--python-version $(LAMBDA_PYTHON) \
		--implementation cp \
		--abi $(LAMBDA_ABI) \
		--only-binary=:all: \
		--no-cache-dir
	cp -r engine lambdas "$(ARTIFACTS_DIR)/"
