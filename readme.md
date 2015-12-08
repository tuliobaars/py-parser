# Zeelo

[DEPRECATED] Architecture:
I was thinking in create a Python script in the root folder of this project called "zeelo.py". In order to crawl all links related to the given company, the user should provide the company name to "zeelo.py". This script will call the Scrapy crawler and the crawler will do his job returning a JSON with items. Each item has a `reference` and a `link` - the first one is the complete reference that the [search engine] uses to classify it ("23/07/2014 - RI HAPPY BRINQUEDOS S.A. E SUBSIDIARIAS - pág. 49 \nEMPRESARIAL - PUBLICACOES - BALANCO", for example) and the last one is the link for the PDF.

Interesting links:
	- [About the project](https://hackpad.com/Zeelo-Apax-DF-Analyzer-8u5aC8ARMe5)
	- [Search Engine (the page to be crawled)](http://balancos.imprensaoficial.com.br/Condiario.asp)
	- [Example of summary](http://diariooficial.imprensaoficial.com.br/nav_v4/index.asp?c=3&e=20151202&p=1)

Interesting tools:
	- [Selenium (Very famous)](http://selenium-python.readthedocs.org/)
	- [Splinter](https://splinter.readthedocs.org/en/latest/)
	- [PhantomJS](http://phantomjs.org/)