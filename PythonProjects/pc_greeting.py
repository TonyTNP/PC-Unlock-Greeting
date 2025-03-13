import datetime
import random
import os
import getpass

# Get the current username
username = getpass.getuser()

# Generate a time-based greeting
hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good morning"
elif 12 <= hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# Personalized messages
messages = [
    f"{greeting}, Engineer {username}! Time to conquer the day! 🚀",
    f"{greeting}, Engineer {username}! Make today great! 🌟",
    f"{greeting}, Engineer {username}! Stay focused and productive! 💡",
    f"{greeting}, Engineer {username}! Hope you have an amazing day! 😃",
    f"{greeting}, Engineer {username}! Keep coding and keep learning! 🖥️"
]

# Select a random message
message = random.choice(messages)

# Display in console
print(message)

# Show Windows Toast Notification
powershell_command = f'''
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
$toastXml = New-Object Windows.Data.Xml.Dom.XmlDocument
$toastXml.LoadXml('<toast><visual><binding template="ToastGeneric"><text>{message}</text></binding></visual></toast>')
$toast = [Windows.UI.Notifications.ToastNotification]::new($toastXml)
$notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("PC Greeting")
$notifier.Show($toast)
'''

# Execute PowerShell command for toast notification
try:
    os.system(f'powershell -Command "{powershell_command}"')
except Exception as e:
    print(f"Notification error: {e}")
