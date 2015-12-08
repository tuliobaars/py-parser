# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Company(scrapy.Item):
	company_name = scrapy.Field()

# class ZeeloItem(scrapy.Item):
# 	""" 

# 	"""
#     # We need to store the complete reference given by the search engine. Each PDF has a unique reference.
#     # 
#     # Example when we're inside of "RI HAPPY BRINQUEDOS S.A. E SUBSIDIARIAS" page:
#     # 23/07/2014 - RI HAPPY BRINQUEDOS S.A. E SUBSIDIARIAS - pág. 49 \nEMPRESARIAL - PUBLICACOES - BALANCO 
#     reference = scrapy.Field() 

#     # The link for the referenced PDF.
#     link = scrapy.Field()

#     pass
