# Reminder Application

## Overview

The **Reminder Application** is a Python-based tool designed to help you stay organized by displaying timely notifications. Whether you need interval-based reminders or specific time-based alerts, this application ensures you never miss important tasks or breaks. It integrates seamlessly with the Windows system tray, allowing you to manage the application effortlessly.

## Features

- **Interval-Based Reminders**: Receive random motivational messages at regular intervals.
- **Time-Based Reminders**: Get fixed messages at specific times of the day.
- **System Tray Integration**: Run the application in the background with a convenient system tray icon.
- **Customizable Configuration**: Easily modify reminders and schedules through a `config.json` file.
- **Logging**: Comprehensive logging for monitoring application behavior and troubleshooting.
- **Standalone Executable**: Package the application into a single executable for easy distribution.

## Table of Contents

1. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
   - [Installing Dependencies](#installing-dependencies)
2. [Configuration](#configuration)
   - [Understanding `config.json`](#understanding-configjson)
   - [Sample `config.json`](#sample-configjson)
3. [Usage](#usage)
   - [Running the Application](#running-the-application)
   - [Packaging into an Executable](#packaging-into-an-executable)
4. [Troubleshooting](#troubleshooting)
   - [Common Issues and Solutions](#common-issues-and-solutions)
5. [Logging](#logging)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)
9. [Acknowledgements](#acknowledgements)

---

## Installation

### Prerequisites

Before setting up the Reminder Application, ensure you have the following installed on your system:

- **Python 3.6 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually included with Python).

### Setting Up a Virtual Environment

It's recommended to use a virtual environment to manage your project's dependencies. This ensures that your project's libraries don't interfere with other Python projects on your system.

1. **Create a Virtual Environment**

   Open your terminal or command prompt and navigate to your project directory. Then, run:

   ```bash
   python -m venv venv
   ```

   This command creates a new virtual environment named `venv`.

2. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     .\venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   After activation, your terminal prompt will be prefixed with `(venv)` indicating that the virtual environment is active.

### Installing Dependencies

The application relies on several Python libraries. These can be installed using the provided `requirements.txt` file.

1. **Create `requirements.txt`**

   Create a file named `requirements.txt` in your project directory with the following content:

   ```plaintext
   win10toast==0.9
   pystray==0.17.3
   Pillow==9.5.0
   schedule==1.1.0
   ```

2. **Install Dependencies**

   With the virtual environment activated, run:

   ```bash
   pip install -r requirements.txt
   ```

   This command installs all the necessary libraries specified in `requirements.txt`.

   **Note:** If you prefer not to use `requirements.txt`, you can install the libraries individually:

   ```bash
   pip install win10toast pystray Pillow schedule
   ```

---

## Configuration

### Understanding `config.json`

The `config.json` file is the heart of the Reminder Application. It defines the reminders, their messages, and the scheduling details. By modifying this file, you can customize what messages are displayed and when they appear.

### Sample `config.json`

Below is a sample `config.json` to get you started:

```json
{
  "reminders": [
    {
      "message": [
        "We first make our habits, and then our habits make us.",
        "The important work of moving the world forward does not wait to be done by perfect men.",
        "To dare is to lose one's footing momentarily. Not to dare is to lose oneself.",
        "Action speaks louder than words.",
        "Confidence is not about being loud; it's about being present and comfortable in your own space.",
        "True confidence comes from knowledge and experience, not from theatrical displays of power.",
        "To walk confidently into any room, first command yourself; the rest will follow.",
        "Confidence grows when we dare to step beyond our comfort zones and embrace new challenges.",
        "The cadence of your speech can be as powerful as the words you choose—control the pace, and you control the room.",
        "Confidence isn't a trait we're born with; it's a skill we can nurture and develop over time.",
        "Taking time to respond shows control and confidence; don't rush your answers or actions.",
        "Even the most subtle gestures, like a steady gaze or smooth movement, can convey a powerful sense of confidence.",
        "When we are confident, we convey our message once—clearly and effectively—without the need to convince.",
        "Master your environment and your presence, and you will naturally project the confidence you seek."
      ],
      "interval_minutes": 30
    },
    {
      "message": "You did great today! Now, take a break, write down what you did, think about your next steps, and get ready to exercise.",
      "time": ["11:50", "15:10", "17:10"]
    }
  ]
}
```

### Configuration Parameters

- **message**: The content to display as a reminder.
  - **List of Strings**: For interval-based reminders that show a random message from the list.
  - **Single String**: For fixed time-based reminders.
- **interval_minutes**: (Optional) Specifies the interval in minutes for interval-based reminders.
- **time**: (Optional) A list of times in `HH:MM` 24-hour format for time-based reminders.

### Customization

- **Adding New Reminders**: Add a new object to the `reminders` array with the desired configuration.
- **Modifying Existing Reminders**: Edit the `message`, `interval_minutes`, or `time` fields as needed.
- **Removing Reminders**: Delete the respective object from the `reminders` array.

---

## Usage

### Running the Application

With the virtual environment activated and dependencies installed, you can run the application using Python:

```bash
python main.py
```

**Behavior:**

1. **Confirmation Dialog**: Upon launching, a dialog will display the loaded configuration. Confirm to start the reminder system.
2. **System Tray Icon**: After confirmation, a system tray icon will appear.
3. **Notifications**: Reminders will pop up based on the schedule defined in `config.json`.
4. **Exiting the Application**: Right-click the system tray icon and select "Exit" to terminate the application gracefully.

### Packaging into an Executable

To distribute the application without requiring users to install Python and dependencies, you can package it into a standalone executable using `PyInstaller`.

#### Steps:

1. **Ensure PyInstaller is Installed**

   ```bash
   pip install pyinstaller
   ```

2. **Prepare an Icon (Optional)**

   If you want a custom icon for your executable and system tray, prepare a `.ico` file (e.g., `icon.ico`) and place it in the script directory.

3. **Run PyInstaller**

   Open your terminal or command prompt, navigate to the directory containing your `main.py` and `config.json`, and execute:

   ```bash
   pyinstaller --onefile --noconsole --icon=icon.ico --add-data "config.json;." --hidden-import=win10toast --collect-all win10toast main.py
   ```

   **Parameters Explained:**

   - `--onefile`: Packages everything into a single executable.
   - `--noconsole`: Hides the console window.
   - `--icon=icon.ico`: Sets the icon for the executable (optional).
   - `--add-data "config.json;."`: Includes `config.json` in the same directory as the executable.
     - **Note**: On **Windows**, use a semicolon `;` to separate source and destination. On **macOS/Linux**, use a colon `:`.
   - `--hidden-import=win10toast`: Ensures `win10toast` is included.
   - `--collect-all win10toast`: Collects all data related to `win10toast`.

4. **Locate the Executable**

   After running PyInstaller, the executable will be located in the `dist` folder within your project directory.

5. **Test the Executable**

   - **Run the Executable**:
     - Double-click the executable to launch the application.
     - A confirmation dialog should appear displaying the loaded configuration.
     - Upon confirmation, the system tray icon should appear.
     - Reminders should pop up as per the schedule defined in `config.json`.
     - Right-clicking the tray icon should present an "Exit" option to terminate the application.
   
   - **Check the Log File**:
     - Ensure that `reminder.log` is created in the same directory as the executable.
     - Open `reminder.log` to verify that all actions are logged correctly and that there are no errors.

---

## Troubleshooting

### Common Issues and Solutions

#### 1. **Application Exits Immediately**

**Symptoms**: The executable closes right after launching without any notifications or system tray icon.

**Solutions**:

- **Missing Dependencies**: Ensure that all dependencies are included during packaging. Use the `--hidden-import` flag for any missing packages like `win10toast`.
- **Check `config.json` Inclusion**: Verify that `config.json` is included with the executable using the `--add-data` flag.
- **Review Log File**: Open `reminder.log` to identify any errors during startup.
- **Run Without `--noconsole`**: Temporarily remove the `--noconsole` flag to see real-time error messages.

#### 2. **Notifications Not Appearing**

**Symptoms**: The application runs, but no notifications pop up as scheduled.

**Solutions**:

- **Check Notification Settings**: Ensure that Windows notifications are enabled for your application.
- **Verify Scheduling**: Double-check the `config.json` for correct `interval_minutes` and `time` formats.
- **Review Log File**: Look for any errors related to displaying notifications.

#### 3. **System Tray Icon Missing**

**Symptoms**: After running the application, no system tray icon appears.

**Solutions**:

- **Ensure `pystray` and `Pillow` Are Included**: Verify that these libraries are installed and included during packaging.
- **Check Log File**: Look for errors related to the system tray icon.
- **Icon Creation**: Ensure that the `create_image` function correctly creates an icon.

#### 4. **Errors Related to `win10toast` Not Found**

**Symptoms**: Errors like `DistributionNotFound: The 'win10toast' distribution was not found and is required by the application`.

**Solutions**:

- **Explicitly Include `win10toast`**: Use `--hidden-import=win10toast` and `--collect-all win10toast` in the PyInstaller command.
- **Ensure Correct Installation**: Verify that `win10toast` is installed in your environment.
- **Check Virtual Environment**: Ensure PyInstaller is running in the same environment where `win10toast` is installed.

#### 5. **Log File Not Created**

**Symptoms**: No `reminder.log` file is found after running the application.

**Solutions**:

- **Check Write Permissions**: Ensure that the application has permission to write to its directory.
- **Logging Configuration**: Verify that logging is correctly set up in the script.

### Viewing Logs

Logs are saved in the `reminder.log` file in the same directory as the executable or script. Review this file for detailed information about the application's operation and any errors encountered.

---

## Logging

The application uses Python's built-in `logging` module to record its operations and any errors that occur. All log entries are written to the `reminder.log` file, which is located in the same directory as the executable or script.

### Log Levels

- **INFO**: General information about the application's operations (e.g., loading configuration, scheduling reminders).
- **WARNING**: Indications of potential issues (e.g., invalid message formats).
- **ERROR**: Critical issues that prevent the application from functioning correctly (e.g., missing dependencies, errors during notification display).

### Example Log Entries

```
2024-04-27 12:00:00,000 - INFO - Application started.
2024-04-27 12:00:00,100 - INFO - Attempting to load configuration file.
2024-04-27 12:00:00,200 - INFO - Configuration file loaded successfully.
2024-04-27 12:00:00,300 - INFO - Displaying configuration confirmation dialog.
2024-04-27 12:00:05,500 - INFO - User confirmed to start the reminder system.
2024-04-27 12:00:05,600 - INFO - Starting reminder scheduler.
2024-04-27 12:00:05,700 - INFO - Setting up random message reminders.
2024-04-27 12:00:05,800 - INFO - Scheduled reminder every 30 minutes.
2024-04-27 12:00:05,900 - INFO - Setting up fixed message reminders.
2024-04-27 12:00:06,000 - INFO - Scheduled reminder daily at 11:50.
2024-04-27 12:00:06,100 - INFO - Scheduled reminder daily at 15:10.
2024-04-27 12:00:06,200 - INFO - Scheduled reminder daily at 17:10.
2024-04-27 12:00:06,300 - INFO - Scheduler thread started.
2024-04-27 12:00:06,400 - INFO - System tray thread started.
```

---

## Contributing

Contributions are welcome! If you'd like to improve the Reminder Application, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page.
2. **Create a New Branch**: 

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Changes**: Implement your changes in the new branch.
4. **Commit Your Changes**:

   ```bash
   git commit -m "Add Your Feature Description"
   ```

5. **Push to GitHub**:

   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Create a Pull Request**: Navigate to your forked repository on GitHub and click "Compare & pull request."

Please ensure that your contributions adhere to the project's coding standards and include appropriate documentation and tests where applicable.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions, issues, or suggestions, feel free to reach out:

- **Email**: your.email@example.com
- **GitHub**: [YourGitHubUsername](https://github.com/YourGitHubUsername)

---

## Acknowledgements

- [win10toast](https://pypi.org/project/win10toast/)
- [pystray](https://pypi.org/project/pystray/)
- [Pillow](https://pypi.org/project/Pillow/)
- [schedule](https://pypi.org/project/schedule/)
- [PyInstaller](https://www.pyinstaller.org/)

---

## Screenshots

*Include screenshots of the confirmation dialog, system tray icon, and a sample notification to give users a visual understanding of the application.*

---

## Future Enhancements

- **GUI for Configuration**: Develop a user-friendly interface to manage reminders without editing `config.json`.
- **Cross-Platform Support**: Extend support to other operating systems like macOS and Linux.
- **Advanced Scheduling**: Implement more complex scheduling options, such as recurring reminders on specific days.
- **Customization Options**: Allow users to customize notification titles, durations, and icons.

---

Thank you for using the Reminder Application! We hope it helps you stay organized and productive.