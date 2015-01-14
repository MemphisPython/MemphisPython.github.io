html:
	pelican -o site -s settings.py content

clean:
	rm -rf site
