#Views de pruebas

from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
	
	return HttpResponse('Hello, world! {now}'.format(
		now = datetime.now().strftime('%d %b %Y - %H:%M hrs')
	))

def sorted_integers(request):
	numbers = [int (i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	data = {
	'status': 'ok',
	'numbers': sorted_ints,
	'message': 'Integers sort successfully.'
	}
	#import pdb; pdb.set_trace()
	return HttpResponse(
		json.dumps(data, indent=4), 
		content_type='application/json'
	)

def say_hi(request, name, age):
	# import pdb; pdb.set_trace()
	if age < 12:
		message = 'Sorry {}, You are not allowed here'.format(name)
	else:
		message = 'Hello, {}! Welcome to PlatziGram'.format(name)

	return HttpResponse(message)