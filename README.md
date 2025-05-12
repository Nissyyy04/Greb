
# GrebLogger

GrebLogger is a lightweight Python-based tool that captures visitor metadata via a Flask webserver, logs it locally, and dispatches details to a Discord channel. It uses ngrok for tunneling, offers a CLI for configuration, and securely stores settings in a platform-agnostic JSON config.

---

## Features

- **Visitor Tracking**  
  Captures IP, real IP (via X-Forwarded-For), platform, browser, version, language, and raw User-Agent on each HTTP request.

- **Local Logging**  
  Persists each visitor’s metadata to timestamped files in a `grabs/` directory.

- **Discord Notifications**  
  Sends an embed via Discord Webhook for every new visitor, tagging `@everyone`.

- **Tunneling**  
  Automatically spins up an ngrok tunnel (region: EU) to expose your local Flask server.

- **Interactive CLI**  
  Configure webhook URL and redirect target through a curses-style menu, with live feedback and ASCII art banners.

- **Cross-Platform Config**  
  Uses a `Config` class that stores settings in `~/Documents/GrebLogger/config.json`.

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Nissyyy04/Greb.git
   cd Greb
   ```

2. **Create a virtual environment & install deps**

   ```bash
   python -m venv venv
   source venv/bin/activate   # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

---

## Configuration

All settings persist in your Documents folder:

* **Discord Webhook** (`webhook`)
* **Redirect URL** (`redirect_url`)

You can change them via the CLI menu or manually edit:

```
~/Documents/GrebLogger/config.json
```

---

## Usage

1. **Run the main menu**

   ```bash
   python main.py
   ```

2. **Main Menu**

   * **Change Discord Webhook**
   * **Change Redirect URL**
   * **Start Greb Logger**
   * **Exit**

3. **Visitor Flow**

   * Users hit the auto generated ngrok link; metadata is logged and sent to Discord.
   * Visitor is redirected to your configured URL.

---

## Project Structure

```
.
├── app.py          # Flask server & ngrok integration
├── main.py         # Async CLI with banners and menu
├── shared.py       # Imports and exposes config & constants
├── data/           # Config module
│   ├── __init__.py # Config class for JSON persistence
├── grabs/          # Auto-generated visitor log files
└── requirements.txt
```

---

## Contributing

Contributions, issues, and feature requests are welcome. Please fork the repo and open a PR.

---

## License

This project is released under the MIT License.
