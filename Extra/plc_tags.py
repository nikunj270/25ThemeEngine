########################################################################
## PLC Tag Definitions — Siemens OPC UA Server
########################################################################
## Replace the placeholder node_id values with your actual PLC node IDs.
## Namespace index (ns=X) and node ID format (s= for string, i= for integer)
## depend on your PLC's OPC UA server configuration.
##
##

########################################################################

PLC_TAGS = {
    # Dashboard circular progress bars
    "Memory": {
        "node_id": "ns=4;s=DB1.DBD0",
        "type": float,
        "label": "Memory Used",
        "scale": 1.0,       # multiply raw value by this
        "offset": 0,       # add this after scaling
    },
    "Disk": {
        "node_id": "ns=4;s=DB1.DBD4",
        "type": float,
        "label": "Disk Used",
        "scale": 1.0,
        "offset": 0,
    },
    "CPU": {
        "node_id": "ns=4;s=DB1.DBD8",
        "type": float,
        "label": "CPU Used",
        "scale": 1.0,
        "offset": 0,
    },
    "Network": {
        "node_id": "ns=4;s=DB1.DBD12",
        "type": float,
        "label": "Network",
        "scale": 1.0,
        "offset": 0,
    },

    # Dashboard linear progress bars
    "Loading": {
        "node_id": "ns=4;s=DB1.DBD16",
        "type": float,
        "label": "Loading",
        "scale": 1.0,
        "offset": 0,
    },
    "Processing": {
        "node_id": "ns=4;s=DB1.DBD20",
        "type": float,
        "label": "Processing",
        "scale": 1.0,
        "offset": 0,
    },
    "DataSync": {
        "node_id": "ns=4;s=DB1.DBD24",
        "type": float,
        "label": "Data Sync",
        "scale": 1.0,
        "offset": 0,
    },
    "FileUpload": {
        "node_id": "ns=4;s=DB1.DBD28",
        "type": float,
        "label": "File Upload",
        "scale": 1.0,
        "offset": 0,
    },
}

# OPC UA connection settings
OPCUA_ENDPOINT = "opc.tcp://192.168.30.15:4840"  # <-- Replace with your PLC's IP
OPCUA_SECURITY_MODE = "none"                    # "none", "sign", or "sign_and_encrypt"
OPCUA_CONNECT_TIMEOUT = 10                      # seconds
OPCUA_SUBSCRIPTION_INTERVAL = 500               # milliseconds between updates
