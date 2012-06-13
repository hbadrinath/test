#/usr/bin/env python

def grt_wrld():
	return "Hello World!!" 

def test_grtwrld():
	assert grt_wrld() == "Hello World!!" 
	assert __name__ != '__main__'

if __name__ == '__main__':
	print "[Error] cant run directly from command line"

