#!/usr/bin/env python
""" Find all PDFs for a specific company.

This script will find all PDFs for a (very) specific company. If the
search term is ambigous, then the website will return more than 
one company. For example, if you search for "BRINQUEDOS BANDEIRANTE",
than the website will return the following results:

	# BRINQUEDOS BANDEIRANTE
	# BRINQUEDOS BANDEIRANTE S.A.
	# BRINQUEDOS BANDEIRANTE S/A

It's almost certain that these three companies are the same, but their
database have a lot of inconsistencies and things like that can happen. 
For now we don't have a clear solution for that, so this script assumes
that we only have one company for a given term. WE ALWAYS GET THE 
FIRST COMPANY FROM THE RESULTS, REMEMBER THAT. We're ignoring if 
there's more than one company for the same term (and this can happen, 
as you can see at 'test2_find_company.py').

-----------------------

Summarizing, the algorithm is somewhat like that:
	1. Search the website for the "search_term" term.
	2. Get the first company returned for the given term.
	3. Go to the company page and extract PDFs links.
	4. Parse each link, extract the correct param and concatenate
		with the URL for download. Add to "pdfs" list.
	5. Done. 

@author Fernando Paladini <paladini@lisha.ufsc.br>
"""
from splinter import Browser
import urlparse

# Global variables.
base_url = 'http://balancos.imprensaoficial.com.br/Condiario.asp'
base_pdf_url = 'http://document.imprensaoficial.com.br/'
search_term = 'Brinquedo'
pdfs = []

# Visiting the page.
browser = Browser()
browser.visit(base_url)
browser.fill('txtNome_Empresa', search_term)
browser.find_by_name('pesquisar').click()

# Finding the first company with the given search term.
company = browser.find_by_xpath('//div[@class="pB17"]')[0].find_by_tag('tr')[1].find_by_tag('tr')
company = company[0].find_by_tag('a') # this may raise an exception, take care.
print("\n[ " + company.value + " ]")

# Goind to the next page parse the PDFs from the company.
company.click()
pdfs_found = browser.find_by_name('Publicacao').find_by_tag('table')[0].find_by_tag('a')

# Extracting PDFs urls and storing it inside the list.
for pdf in pdfs_found:
	parsed = urlparse.urlparse(pdf['href'])
	url = base_pdf_url + urlparse.parse_qs(parsed.query)['imagem'][0]
	print(url)
	pdfs.append([pdf.value, url])

print('')
browser.quit()
