import json

def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

with open("docs.json",) as read_file:
	data = json.load(read_file, object_hook=as_complex)

def check_microapi(microapi, data):
	if microapi:
		if microapi in data['microapi']:
			documentation = data['microapi'][microapi]
			return "Success"
		else:
			return "Microapi is not in Database"
	else:
		return "Invalid Entry"

#print(check_microapi('commentss', data))