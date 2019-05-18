#!/usr/bin/env python2.7
import sys

def doNop(data, s):
	s = s.split(':')
	try:
		s[0] = int(s[0], 16)
	except:
		print '"'+s[0]+'" is not a valid hexadecimal file address.'
		exit(4)

	n = 1
	if len(s) == 2:
		try:
			n = int(s[1])
		except:
			print '"'+s+'" is not a valid decimal number of bytes to nop.'
			exit(5)
	elif len(s) > 2:
		print 'Too many colons!'
		exit(6)

	for i in range(n):
		try:
			data[s[0]+i] = '\x90'
			print 'Nopped address', hex(s[0]+i)
		except:
			print 'Whoops, the address to NOP is greater than the file size.'
			exit(9)
	return

def doWrite(data, s):
	s = s.split('=')
	try:
		s[0] = int(s[0], 16)
	except:
		print '"'+s[0]+'" is not a valid hexadecimal file address.'
		exit(4)

	if len(s) != 2:
		print 'Invalid use of write function.'
		exit(7)

	try:
		s[1] = s[1].decode('hex')
	except:
		print '"'+s[1]+'" is not an hexadecimal list of opcodes.'
		exit(8)

	for i in range(len(s[1])):
		try:
			data[s[0]+i] = s[1][i]
			print 'Wrote', hex(ord(s[1][i])), 'to address', hex(s[0]+i)
		except:
			print 'Whoops, the address to write is greater than the file size.'
			exit(9)
	return
	

if __name__ == '__main__':
	print 'M O P P E R'
	print '\tReady to overwrite?\n'

	if len(sys.argv) != 3:
		print 'Usage:', sys.argv[0], '[file] "[command1];[command2];..."'
		exit(1)

	try:
		with open(sys.argv[1], 'rb') as f:
			data = [i for i in f.read()]
	except:
		print 'Could not open file "'+sys.argv[1]+'".'
		exit(2)

	print 'Loaded', len(data), 'bytes from "'+sys.argv[1]+'".\n'
	
	commands = sys.argv[2].split(';')
	for i in commands:
		if len(i) == 0:
			continue

		if i[0] == 'N':
			doNop(data, i[1:])
		elif i[0] == 'W':
			doWrite(data, i[1:])
		else:
			print 'Unknown command:', i[0]
			exit(3)
	with open('MOPPED_'+sys.argv[1], 'wb') as f:
		f.write(''.join(data))
