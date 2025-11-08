# Alarm Clock & Reminder App

A beginner-friendly Python project that lets you set, view, edit, and delete multiple alarms and reminders. Works in both Jupyter Notebook and VS Code.

## Features
- Set multiple alarms/reminders with custom messages
- View all scheduled alarms
- Edit or delete alarms
- Alarms trigger with sound alert or printed message
- Supports 12-hour and 24-hour time formats
- Optional: Save alarms to file, snooze, repeat reminders

## File Structure
- `AlarmClock_ReminderApp.ipynb` — Step-by-step Jupyter Notebook version
- `AlarmClock_ReminderApp.py` — Final Python script for VS Code/terminal
- `AlarmClock_ReminderApp_NEXT_STEPS.md` — Optional add-ons and upgrade ideas
- `alarms.json` — Stores alarms for persistence (created automatically)

## How to Run

### In Jupyter Notebook
1. Open `AlarmClock_ReminderApp.ipynb` in Jupyter or VS Code.
2. Run each cell in order and follow the instructions.
3. Use the menu to set, view, edit, and delete alarms.

### In VS Code / Terminal
1. Open a terminal in the project folder.
2. Run:
   ```
   python AlarmClock_ReminderApp.py
   ```
3. Use the CLI menu to interact with alarms.

## Requirements
- Python 3.7+
- For sound alerts:
  - Windows: `winsound` (built-in)
  - Other OS: Install `playsound` (`pip install playsound`)

## Optional Enhancements
See `AlarmClock_ReminderApp_NEXT_STEPS.md` for ideas:
- GUI (Tkinter)
- Desktop notifications
- Custom alarm sounds
- Advanced repeat options
- Mobile app version
- Cloud sync
- Unit tests

## License
MIT License

---

**Enjoy building and customizing your Alarm Clock & Reminder App!**