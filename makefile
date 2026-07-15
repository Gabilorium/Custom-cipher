.PHONY: encoder decoder test clean specific_encoder_test specific_decoder_test list_tests help

help:
	@echo "make alphabet                         - generate the cipher alphabet"
	@echo "make encoder FILE=...                 - encode a file (omit FILE for interactive mode)"
	@echo "make decoder FILE=...                 - decode a file (omit FILE for interactive mode)"
	@echo "make list_tests                       - lists all the posible tests"
	@echo "make test                             - run the automated test suite"
	@echo "make specific_encoder_test TEST=...   - run encoder tests matching TEST"
	@echo "make specific_decoder_test TEST=...   - run decoder tests matching TEST"
	@echo "make clean                            - remove generated files"

clean:
	rm -f alphabet.json
	rm -rf __pycache__ cipher/__pycache__ alphabet_generator/__pycache__ Tests/__pycache__
	rm -rf .pytest_cache

encoder: alphabet.json
	python3 -m cipher.encoder $(FILE)

decoder: alphabet.json
	python3 -m cipher.decoder $(FILE)

test: alphabet.json
	python3 -m pytest -v

specific_encoder_test: alphabet.json
	python3 -m pytest Tests/test_encoder.py -k "$(TEST)"

specific_decoder_test: alphabet.json
	python3 -m pytest Tests/test_decoder.py -k "$(TEST)"

alphabet.json: alphabet_generator/generator.py cipher/rules.py
	python3 -m alphabet_generator.generator

list_tests:
	@echo "------DECODER TESTS------"
	@python3 -m pytest Tests/test_decoder.py --collect-only -q | awk -F"::" '{print $$2}'
	@echo "------ENCODER TESTS------"
	@python3 -m pytest Tests/test_encoder.py --collect-only -q | awk -F"::" '{print $$2}'