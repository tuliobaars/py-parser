#!/usr/bin/env python
""" A simple test using splinter.

Not important, just a simple test using splinter.

@author Fernando Paladini <paladini@lisha.ufsc.br>
"""
from splinter import Browser

browser = Browser()
browser.visit('http://www.google.com')
browser.fill('q', 'splinter')
button = browser.find_by_name('btnG')
button.click()

if browser.is_text_present('splinter.readthedocs.org'):
	print('Yes, found it! :)')
else:
	print('No, didn\'t find it :/ ')

browser.quit()

