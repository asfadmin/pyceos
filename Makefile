KSY := $(wildcard src/*)
OUT_DIR := pyceos
PY := $(KSY:src/%.ksy=$(OUT_DIR)/%.py)

.DEFAULT_GOAL := all
.PHONY: all
all:
	ksc --target python --python-package . --outdir $(OUT_DIR) $(KSY)
	black -q $(PY)

.PHONY: lint
lint:
	black --check $(PY)
