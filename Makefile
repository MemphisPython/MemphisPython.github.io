html:
	pelican -s settings.py content

clean:
	rm -rf output

deploy:
	make html; source ~/.rackspace_brad && cd output && swiftcontainer mempy && swiftupload .
