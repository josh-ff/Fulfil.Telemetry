SHELL:=/bin/bash
VERSION=0x03

.PHONY: image
image:
	@docker build -t lab-jack-interfacer .

.PHONY: run
run:
	@docker run --network=host lab-jack-interfacer
