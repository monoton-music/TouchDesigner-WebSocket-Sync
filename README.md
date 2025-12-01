# TouchDesigner-WebSocket-Sync

Bidirectional parameter sync between TouchDesigner and web browser via WebSocket.

## Structure

```
├── td/                          # TouchDesigner scripts
│   ├── parexec1.py              # Broadcasts parameter changes to WebSocket clients
│   └── webserver1_callbacks.py  # Handles HTTP/WebSocket requests
├── server/                      # Web client files
│   └── index.html               # Slider UI
└── example.toe                  # Example TouchDesigner project
```

## Setup

1. Open `example.toe` in TouchDesigner
2. Create a `webserver1` (Web Server DAT) with port (e.g. 9980)
3. Create a `param` (Base COMP) with custom parameter `Value` (Float, 0-1)
4. Create a `parexec1` (Parameter Execute DAT) watching `param`, enable "Values Changed"
5. Set callbacks path to `td/webserver1_callbacks.py` in Web Server DAT
6. Set script path to `td/parexec1.py` in Parameter Execute DAT
7. Open `http://localhost:9980` in browser

## Protocol

**TD -> Web:**
```json
{ "type": "valueChange", "name": "Value", "value": 0.5 }
```

**Web -> TD:**
```json
{ "type": "setValue", "name": "Value", "value": 0.5 }
```
