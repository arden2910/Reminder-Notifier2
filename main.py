import json
import os
import sys
import random
import threading
import time
import logging
from datetime import datetime
from tkinter import Tk, messagebox

from win10toast import ToastNotifier
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import schedule

# Configuration and log file paths
CONFIG_FILE = 'config.json'
LOG_FILE = 'reminder.log'

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# Initialize ToastNotifier
toaster = ToastNotifier()

# Event to signal scheduler thread to stop
stop_event = threading.Event()


def load_config():
    logging.info("Attempting to load configuration file.")
    if not os.path.exists(CONFIG_FILE):
        show_error(f"Configuration file '{CONFIG_FILE}' does not exist.")
        logging.error(f"Configuration file '{CONFIG_FILE}' does not exist.")
        sys.exit(1)
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        if 'reminders' not in config:
            raise ValueError("Invalid configuration: 'reminders' key not found.")
        logging.info("Configuration file loaded successfully.")
        return config
    except json.JSONDecodeError as e:
        show_error(f"Error parsing {CONFIG_FILE}: {e}")
        logging.error(f"Error parsing {CONFIG_FILE}: {e}")
        sys.exit(1)
    except Exception as e:
        show_error(f"Error loading configuration: {e}")
        logging.error(f"Error loading configuration: {e}")
        sys.exit(1)


def show_error(message):
    root = Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror("Error", message)
    root.destroy()


def display_confirmation(config):
    logging.info("Displaying configuration confirmation dialog.")
    root = Tk()
    root.withdraw()  # Hide the main window

    config_str = json.dumps(config, indent=2, ensure_ascii=False)

    confirm = messagebox.askyesno(
        "Confirm Configuration",
        f"The following configuration has been loaded:\n\n{config_str}\n\nDo you want to start the reminder system?"
    )

    root.destroy()
    if confirm:
        logging.info("User confirmed to start the reminder system.")
        return True
    else:
        logging.info("User canceled the reminder system.")
        return False


def show_notification(message):
    positive_attributes = [
        "Proactive", "Focused", "Wise", "Adaptable", "Inclusive",
        "Explorer", "Strategist", "Artist",
        "Mentor", "Professional Expert", "Solution Architect", "Leader", "CTO",
        "Planner", "Implementer", "Athlete", "Mountaineer",
    "Joyful", "Content", "Grateful", "Calm", "Energetic",
    "Optimistic", "Empowered", "Confident", "Inspired", "Peaceful"
    ]
    try:
        logging.info(f"Displaying notification: {message}")
        toaster.show_toast(
            random.choice(positive_attributes),
            message,
            duration=10,  # Duration in seconds
            threaded=True
        )
    except Exception as e:
        logging.error(f"Error displaying notification: {e}")


def schedule_reminders(config):
    logging.info("Starting reminder scheduler.")
    for reminder in config['reminders']:
        message = reminder.get('message')
        if isinstance(message, list):
            message_func = lambda m=message: show_notification(random.choice(m))
            logging.info("Setting up random message reminders.")
        elif isinstance(message, str):
            message_func = lambda m=message: show_notification(m)
            logging.info("Setting up fixed message reminders.")
        else:
            logging.warning("Invalid message format in configuration.")
            continue

        if 'interval_minutes' in reminder:
            interval = reminder['interval_minutes']
            schedule.every(interval).minutes.do(message_func)
            logging.info(f"Scheduled reminder every {interval} minutes.")

        if 'time' in reminder:
            times = reminder['time']
            for t in times:
                try:
                    schedule.every().day.at(t).do(message_func)
                    logging.info(f"Scheduled reminder daily at {t}.")
                except schedule.ScheduleValueError:
                    logging.error(f"Invalid time format: {t}. Expected HH:MM in 24-hour format.")

    while not stop_event.is_set():
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            logging.error(f"Scheduler encountered an error: {e}")
            time.sleep(1)
    logging.info("Scheduler thread has been stopped.")


def create_image():
    # Create an image for the system tray icon
    width = 64
    height = 64
    color1 = "blue"
    color2 = "white"

    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        [(width // 2, 0), (width, height // 2)],
        fill=color2
    )
    dc.rectangle(
        [(0, height // 2), (width // 2, height)],
        fill=color2
    )

    return image


def on_exit(icon, item):
    logging.info("User selected to exit the application.")
    icon.stop()
    stop_event.set()  # Signal the scheduler thread to stop


def setup_tray():
    menu = (item('Exit', on_exit),)
    icon = pystray.Icon("ReminderApp", create_image(), "Reminder App", menu)
    try:
        icon.run()
    except Exception as e:
        logging.error(f"System tray icon encountered an error: {e}")


def main():
    logging.info("Application started.")
    config = load_config()
    if display_confirmation(config):
        # Start scheduler in a separate thread
        scheduler_thread = threading.Thread(target=schedule_reminders, args=(config,))
        scheduler_thread.start()
        logging.info("Scheduler thread started.")

        # Setup system tray in the main thread
        setup_tray()
        logging.info("System tray has been closed.")

        # Wait for the scheduler thread to finish
        scheduler_thread.join()
        logging.info("Application has exited gracefully.")
    else:
        logging.info("User chose not to start the reminder system.")
        sys.exit(0)


if __name__ == "__main__":
    main()
