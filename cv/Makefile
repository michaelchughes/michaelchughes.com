# Makefile to build PDF and Markdown resume from YAML.
# 
# Acks
# ----
# Brandon Amos <http://bamos.io> and Ellis Michael <http://ellismichael.com>

TEMPLATES=$(shell find templates -type f)

BUILD_DIR=build
TEX=$(BUILD_DIR)/resume.tex
PDF=$(BUILD_DIR)/resume.pdf
MD=$(BUILD_DIR)/resume.md

YAML=$(BUILD_DIR)/publications_journal.yaml $(BUILD_DIR)/publications_workshop.yaml $(BUILD_DIR)/publications_conference.yaml $(BUILD_DIR)/publications_highlight.yaml $(BUILD_DIR)/publications_preprint.yaml $(BUILD_DIR)/publications_underreview.yaml

.PHONY: all clean

markdown: $(MD)
pdf: $(PDF)
tex: $(TEX)

all: $(PDF) $(MD)
	cp $(BUILD_DIR)/resume.pdf ../content/papers/MichaelCHughes_CurriculumVitae.pdf
	cp $(BUILD_DIR)/resume.md ../content/pages/cv.md

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(TEX): $(BUILD_DIR) $(YAML) generate.py ../.git/logs/HEAD
	python generate.py -b publications.yaml resume.yaml --latex

$(MD): $(BUILD_DIR) $(YAML) generate.py ../.git/logs/HEAD
	python generate.py -b publications.yaml resume.yaml --markdown

# Try quite mode... if it fails run in verbose mode
$(PDF): $(TEX)
	latexmk -pdf -cd- -quiet -silent -jobname=$(BUILD_DIR)/resume $(BUILD_DIR)/resume || latexmk -pdf -cd- -verbose -jobname=$(BUILD_DIR)/resume $(BUILD_DIR)/resume
	# Clean up unnecessary files -c 
	latexmk -silent -c -cd $(BUILD_DIR)/resume

clean:
	rm -rf $(BUILD_DIR)

$(BUILD_DIR)/publications_journal.yaml: $(BUILD_DIR) publications.yaml
	grep -B4 -A2 "venuetype: journal" publications.yaml | sed -e 's/--//g' > $(BUILD_DIR)/publications_journal.yaml;

$(BUILD_DIR)/publications_conference.yaml: $(BUILD_DIR) publications.yaml
	grep -B4 -A2 "venuetype: conference" publications.yaml | sed -e 's/--//g' > $(BUILD_DIR)/publications_conference.yaml;

$(BUILD_DIR)/publications_workshop.yaml: $(BUILD_DIR) publications.yaml
	grep -B4 -A2 "venuetype: workshop" publications.yaml | sed -e 's/--//g' > $(BUILD_DIR)/publications_workshop.yaml;

## BY DISPLAYTYPE

$(BUILD_DIR)/publications_highlight.yaml: $(BUILD_DIR) publications.yaml
	grep -B7 "displaytype: highlight" publications.yaml | sed -e 's/--//g' > $(BUILD_DIR)/publications_highlight.yaml;

$(BUILD_DIR)/publications_preprint.yaml: $(BUILD_DIR) publications.yaml
	grep -B7 "displaytype: preprint" publications.yaml | sed -e 's/--//g' > $(BUILD_DIR)/publications_preprint.yaml;

$(BUILD_DIR)/publications_underreview.yaml: private_content/publications_underreview.yaml
	grep -B7 "displaytype: underreview" private_content/publications_underreview.yaml | sed -e 's/--//g' > $(BUILD_DIR)/publications_underreview.yaml;

	
