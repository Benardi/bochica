run:
	scrapy crawl brasil_elpais -o ./output/results.json

export:
	python ./utils/format_output.py ./output/results.json ./output/result.csv
