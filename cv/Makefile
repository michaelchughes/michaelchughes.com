# Makefile to build PDF and Markdown resume from YAML.
#
# Brandon Amos <http://bamos.io> and Ellis Michael <http://ellismichael.com>

TEMPLATES=$(shell find templates -type f)

BUILD_DIR=build
TEX=$(BUILD_DIR)/resume.tex
PDF=$(BUILD_DIR)/resume.pdf
MD=$(BUILD_DIR)/resume.md

.PHONY: all clean

all: pdf markdown
markdown: $(MD)
pdf: $(PDF)
tex: $(TEX)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(TEX): $(BUILD_DIR)
	python generate.py -b publications.yaml resume.yaml --latex

$(MD): $(BUILD_DIR)
	python generate.py -b publications.yaml resume.yaml --markdown

# Try quite mode... if it fails run in verbose mode
$(PDF): $(TEX)
	latexmk -pdf -cd- -quiet -silent -jobname=$(BUILD_DIR)/resume $(BUILD_DIR)/resume || latexmk -pdf -cd- -verbose -jobname=$(BUILD_DIR)/resume $(BUILD_DIR)/resume
	# Clean up unnecessary files -c 
	latexmk -silent -c -cd $(BUILD_DIR)/resume

clean:
	rm -rf $(BUILD_DIR)
