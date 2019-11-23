
'''
CONVERT RANDOM NUMBER FILES
Jeff Thompson | 2019 | jeffreythompson.org

A utility to convert the original random number files on
Marsaglia's CD-ROM, which are in binary format, to digits
between 0-9. The resulting files will be about 50MB each,
so they are not included in this repo. To convert them,
change the input filename below and run this script.

'''

import os, struct

input_filename = 'bits.01'
input_folder =   'CD-ROM'
output_folder =  'RandomDigits'

print 'getting random digits from file...'
digits = []
with open(os.path.join(input_folder, input_filename), 'rb') as f:
	value = f.read(4)
	while value != '':
		try:
			value = f.read(4)
			value = struct.unpack('<L', value)[0]
			for digit in str(value):
				digits.append(digit)
		except:
			break
print '- unpacked ' + str(len(digits)) + ' digits'
print '- sample: ' + ', '.join([str(i) for i in digits[0:10]])
print '- digit counts:'
for i in range(0,10):
	print '  - ' + str(i) + ': ' + str(digits.count(str(i)))

print '\n' + 'saving digits to file...'
output_filename = input_filename + '.txt'
if (not os.path.exists(output_folder)):
	os.mkdir(output_folder)
with open(os.path.join(output_folder, output_filename), 'w') as f:
	for digit in digits:
		f.write(digit + '\n')
print '- done'

