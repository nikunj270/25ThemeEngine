# 25ThemeEngine

Qt dashboard application built with `PySide6` and `QT-PyQt-PySide-Custom-Widgets`.

## What it does

- Loads the main window from generated UI modules in `src/`
- Applies theme settings from `json-styles/style.json`
- Connects to an OPC UA endpoint through the `Extra/` worker stack
- Logs process values to SQLite and CSV helpers under `Logger/`

## Main entry points

- `main.py` starts the application window
- `Extra/exopc.py` connects UI widgets to live OPC updates
- `Extra/opcua_client.py` manages the background OPC UA client thread
- `Logger/` and `Alarm/` contain persistence helpers

## Run locally

```bash
pip install -r requirements.txt
python main.py
```

## Notes

- The active OPC implementation is the `Extra/` package.
- Generated UI files in `src/` are tied to the `.ui` files in `ui/`.
