#!/usr/bin/env python
""" Find all companies for a given search term.

This script gets all valid companies for a given search term.
For example, if we're willing to search companies within the name
"Brinquedo" in it we'll get the following results:

	# BRINQUEDOS BANDEIRANTE
	# BRINQUEDOS BANDEIRANTE S.A.
	# BRINQUEDOS BANDEIRANTE S/A
	# BRINQUEDOS MIMO S/A
	# GIGAFORT DISTRIBUIDORA DE BRINQUEDOS S.A.
	# GROW JOGOS E BRINQUEDOS
	# GROW JOGOS E BRINQUEDOS S.A.
	# GROW JOGOS E BRINQUEDOS S/A
	# GULLIVER S.A. MANUFATURA DE BRINQUEDOS
	# GULLIVER S/A MANUFATURA DE BRINQUEDOS

Note that some of them are indeed the same but with another fantasy 
name. In this case we can note three different companies that certainly 
are the same:

	# BRINQUEDOS BANDEIRANTE
	# BRINQUEDOS BANDEIRANTE S.A.
	# BRINQUEDOS BANDEIRANTE S/A

Take care with that - with great power comes great responsibility.

@author: Fernando Paladini <paladini@lisha.ufsc.br>
"""
from splinter import Browser

# Global variables
base_url = 'http://balancos.imprensaoficial.com.br/Condiario.asp'
search_term = 'Brinquedo'
companies_found = []

# Visiting the page
browser = Browser()
browser.visit(base_url)
browser.fill('txtNome_Empresa', search_term)
browser.find_by_name('pesquisar').click()

# Finding the companies with the given search term
def cleanup_everything(x):
	return x.find_by_tag('a')

companies_found = browser.find_by_xpath('//div[@class="pB17"]')[0].find_by_tag('tr')[1].find_by_tag('tr')[0:-3]
companies_found = ( cleanup_everything(x) for x in companies_found )

for p in companies_found:
	print(p.value + "\n" + p['href'] + "\n")

browser.quit()
