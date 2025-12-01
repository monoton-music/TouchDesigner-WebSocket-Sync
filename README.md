# TouchDesigner-WebSocket-Sync

Bidirectional parameter sync between TouchDesigner and web browser via WebSocket.

Tested with TouchDesigner 2025.31550

## Structure

```
├── td/                          # TouchDesigner scripts
│   ├── parexec1.py              # Broadcasts parameter changes to WebSocket clients
│   └── webserver1_callbacks.py  # Handles HTTP/WebSocket requests
├── server/                      # Web client files
│   └── index.html               # Slider UI
└── example.toe                  # Example TouchDesigner project
```

## Usage

1. Clone this repository and keep the folder structure as-is
2. Open `example.toe` in TouchDesigner
3. The Web Browser COMP in TD may not work properly. If so, open http://localhost:9980 in your browser instead

## Setup (for custom projects)

1. Create a `webserver1` (Web Server DAT) with port (e.g. 9980)
2. Create a `param` (Base COMP) with custom parameter `Value` (Float, 0-1)
3. Create a `parexec1` (Parameter Execute DAT) watching `param`, enable "Values Changed"
4. Set callbacks path to `td/webserver1_callbacks.py` in Web Server DAT
5. Set script path to `td/parexec1.py` in Parameter Execute DAT
6. Open http://localhost:9980 in browser

## Protocol

**TD -> Web:**
```json
{ "type": "valueChange", "name": "Value", "value": 0.5 }
```

**Web -> TD:**
```json
{ "type": "setValue", "name": "Value", "value": 0.5 }
```
