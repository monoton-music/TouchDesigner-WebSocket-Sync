# Web Server DAT callbacks
# Serves static files and handles WebSocket communication for parameter sync

import json
import os

def onHTTPRequest(dat, request, response):
	"""
	Serves static files from the 'server' directory.
	Defaults to index.html for root path requests.
	"""
	uri = request['uri']

	# Default to index.html for root
	if uri == '/' or uri == '':
		uri = '/index.html'

	# Build full path to requested file
	file_path = uri.lstrip('/')
	full_path = os.path.join(project.folder, 'server', file_path)

	if os.path.exists(full_path) and os.path.isfile(full_path):
		try:
			# Determine content type based on file extension
			content_type = 'text/plain'
			if file_path.endswith('.html'):
				content_type = 'text/html'
			elif file_path.endswith('.css'):
				content_type = 'text/css'
			elif file_path.endswith('.js'):
				content_type = 'application/javascript'
			elif file_path.endswith('.json'):
				content_type = 'application/json'

			# Read and return file contents
			with open(full_path, 'r', encoding='utf-8') as f:
				content = f.read()

			response['statusCode'] = 200
			response['statusReason'] = 'OK'
			response['content-type'] = content_type
			response['data'] = content
		except Exception as e:
			response['statusCode'] = 500
			response['statusReason'] = 'Internal Server Error'
			response['data'] = f'Error: {str(e)}'
	else:
		response['statusCode'] = 404
		response['statusReason'] = 'Not Found'
		response['data'] = f'File not found: {uri}'

	return response

def onWebSocketOpen(dat, client, uri):
	"""
	Called when a new WebSocket client connects.
	Sends the current parameter value to sync the client immediately.
	"""
	target = op('param')
	if target and hasattr(target.par, 'Value'):
		msg = {
			'type': 'valueChange',
			'name': 'Value',
			'value': target.par.Value.eval()
		}
		dat.webSocketSendText(client, json.dumps(msg))

def onWebSocketClose(dat, client):
	return

def onWebSocketReceiveText(dat, client, data):
	"""
	Called when a WebSocket message is received from a client.
	Parses JSON and updates the target parameter if message type is 'setValue'.
	"""
	try:
		msg = json.loads(data)
		if msg.get('type') == 'setValue':
			name = msg.get('name')
			value = msg.get('value')

			# Update the target operator's parameter
			target = op('param')
			if target and hasattr(target.par, name):
				setattr(target.par, name, float(value))
	except Exception as e:
		debug(f'WebSocket error: {e}')

def onWebSocketReceiveBinary(dat, client, data):
	return

def onWebSocketReceivePing(dat, client, data):
	dat.webSocketSendPong(client, data=data)

def onWebSocketReceivePong(dat, client, data):
	return

def onServerStart(dat):
	return

def onServerStop(dat):
	return
