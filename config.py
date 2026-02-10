import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

DEFAULT_CONFIG = {
    "wake_word": "alexa",
}

def load_config():

    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}. Using defaults.")
        return DEFAULT_CONFIG

def save_config(config_data):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config_data, f, indent=4) # indent makes it readable
    except Exception as e:
        print(f"Error saving config: {e}")

def update_wake_word(new_model):
    config = load_config()
    config["wake_word"] = new_model
    save_config(config)
    print(f"✅ Configuration updated: Wake Word set to '{new_model}'")