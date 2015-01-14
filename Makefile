html:
	pelican -o html -s settings.py content

clean:
	rm -rf html
