# Parameter Execute DAT callbacks
# Broadcasts parameter changes to all connected WebSocket clients

import json

def onValueChange(par, prev):
	return

def onValuesChanged(changes):
	"""
	Called at end of frame with a list of parameter changes.
	Broadcasts each change to all connected WebSocket clients as JSON.
	"""
	webserver = op('webserver1')
	if not webserver:
		return

	for c in changes:
		par = c.par
		# Build JSON message with parameter name and current value
		msg = {
			'type': 'valueChange',
			'name': par.name,
			'value': par.eval()
		}
		msg_json = json.dumps(msg)

		# Send to all connected WebSocket clients
		for client in webserver.webSocketConnections:
			webserver.webSocketSendText(client, msg_json)

def onPulse(par):
	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
