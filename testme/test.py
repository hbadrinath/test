#/usr/bin/env python
import nose

def grt_wrld():
	return "Hello World!!" 

def test_grtwrld():
	assert grt_wrld() == "Hello World!!" 
	assert __name__ != '__main__'

#def test_all():
#	print "SKN SKN SKN SKN SKN SKN SKN SKN SKN SKN SKN SKN"
#	nose.main()

if __name__ == '__main__':
	print "[Error] cant run directly from command line"
