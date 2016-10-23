import re

def delete_content(pfile):
    pfile.seek(0)
    pfile.truncate()

def write_to_file(contact_type):
	for item in contact_type:
		f.write('%s\n' % item)
		
with open('contact.csv', 'r+') as f:
		lines = str(f.readlines())
		lines_email = list(set(re.findall(r'[\w\.-]+@[\w\.-]+', lines)))
		lines_phone = list(set(re.findall(r'\(?\b[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}\b', lines)))
		delete_content(f)
		f.write('PHONE NUMBERS:\n')
		write_to_file(lines_phone)
		f.write('\nEMAILS:\n')
		write_to_file(lines_email)



