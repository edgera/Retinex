

all:
	docker build -t dongb5/retinex .

run:
	mkdir -p results 
	docker run --rm -it -w=/retinex \
		-v $(shell pwd)/data:/data:ro \
		-v $(shell pwd)/results:/results \
		dongb5/retinex 
