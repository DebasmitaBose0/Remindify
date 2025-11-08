"""
Alarm Clock & Reminder App (Beginner-Friendly Python Script)
Run this script in VS Code or any Python IDE.
"""
import datetime
import time
import threading
import json
try:
    import winsound
except ImportError:
    winsound = None
try:
    from playsound import playsound
except ImportError:
    playsound = None

alarms = []
ALARM_FILE = 'alarms.json'

def parse_time_input(time_str, time_format='24'):
    try:
        if time_format == '12':
            return datetime.datetime.strptime(time_str, '%I:%M %p').time()
        else:
            return datetime.datetime.strptime(time_str, '%H:%M').time()
    except ValueError:
        return None

def format_time(dt_time, time_format='24'):
    if time_format == '12':
        return dt_time.strftime('%I:%M %p')
    else:
        return dt_time.strftime('%H:%M')

def is_valid_time(time_str, time_format='24'):
    return parse_time_input(time_str, time_format) is not None

def create_alarm_dict(time_obj, message, repeat='once', status='active'):
    return {
        'time': time_obj.strftime('%H:%M'),
        'message': message,
        'repeat': repeat,
        'status': status,
        'snooze_until': None
    }

def set_alarm():
    print('--- Set a New Alarm ---')
    time_format = input('Choose time format (12/24): ').strip()
    if time_format not in ['12', '24']:
        print('Invalid format. Defaulting to 24-hour.')
        time_format = '24'
    time_str = input('Enter alarm time (e.g., 08:30 PM or 20:30): ').strip()
    if not is_valid_time(time_str, time_format):
        print('Invalid time format.')
        return
    time_obj = parse_time_input(time_str, time_format)
    message = input('Enter alarm message: ').strip()
    repeat = input('Repeat? (once/daily/interval in minutes): ').strip()
    if repeat.isdigit():
        repeat = int(repeat)
    alarm = create_alarm_dict(time_obj, message, repeat)
    alarms.append(alarm)
    print('Alarm set successfully!')

def view_alarms():
    print('--- Scheduled Alarms ---')
    if not alarms:
        print('No alarms set.')
        return
    print(f"{'Index':<6}{'Time':<8}{'Message':<20}{'Repeat':<10}{'Status':<10}")
    for idx, alarm in enumerate(alarms):
        print(f"{idx:<6}{alarm['time']:<8}{alarm['message']:<20}{str(alarm['repeat']):<10}{alarm['status']:<10}")

def edit_alarm():
    view_alarms()
    if not alarms:
        return
    try:
        idx = int(input('Enter index of alarm to edit: '))
        alarm = alarms[idx]
    except (ValueError, IndexError):
        print('Invalid index.')
        return
    new_time = input(f"Enter new time (current: {alarm['time']}) or press Enter to keep: ").strip()
    if new_time:
        if is_valid_time(new_time, '24'):
            alarm['time'] = parse_time_input(new_time, '24').strftime('%H:%M')
        else:
            print('Invalid time format. Keeping old time.')
    new_msg = input(f"Enter new message (current: {alarm['message']}) or press Enter to keep: ").strip()
    if new_msg:
        alarm['message'] = new_msg
    print('Alarm updated!')

def delete_alarm():
    view_alarms()
    if not alarms:
        return
    try:
        idx = int(input('Enter index of alarm to delete: '))
        alarms.pop(idx)
        print('Alarm deleted!')
    except (ValueError, IndexError):
        print('Invalid index.')

def play_sound():
    print('Playing alarm sound...')
    if winsound:
        winsound.Beep(1000, 1000)
    elif playsound:
        try:
            playsound('alarm.wav')
        except Exception:
            print('Sound file not found or error playing sound.')
    else:
        print('No sound library available.')

def trigger_alarm(alarm):
    print(f"\n⏰ ALARM! {alarm['message']} ({alarm['time']})")
    play_sound()
    snooze = input('Snooze? (y/n): ').strip().lower()
    if snooze == 'y':
        mins = input('Snooze for 5 or 10 minutes? (5/10): ').strip()
        if mins in ['5', '10']:
            next_time = (datetime.datetime.now() + datetime.timedelta(minutes=int(mins))).time()
            alarm['snooze_until'] = next_time.strftime('%H:%M')
            alarm['status'] = 'active'
            print(f"Alarm snoozed until {alarm['snooze_until']}")

def check_alarms():
    now = datetime.datetime.now().strftime('%H:%M')
    for alarm in alarms:
        if alarm['status'] == 'active':
            if alarm.get('snooze_until'):
                if datetime.datetime.now().strftime('%H:%M') == alarm['snooze_until']:
                    trigger_alarm(alarm)
                    alarm['snooze_until'] = None
            elif alarm['time'] == now:
                trigger_alarm(alarm)
                if alarm['repeat'] == 'once':
                    alarm['status'] = 'inactive'
                elif alarm['repeat'] == 'daily':
                    pass
                elif isinstance(alarm['repeat'], int):
                    next_time = (datetime.datetime.now() + datetime.timedelta(minutes=alarm['repeat'])).time()
                    alarm['time'] = next_time.strftime('%H:%M')

def save_alarms():
    with open(ALARM_FILE, 'w') as f:
        json.dump(alarms, f)
    print('Alarms saved to file.')

def load_alarms():
    global alarms
    try:
        with open(ALARM_FILE, 'r') as f:
            alarms = json.load(f)
        print('Alarms loaded from file.')
    except (FileNotFoundError, json.JSONDecodeError):
        alarms = []

def alarm_monitor():
    while True:
        check_alarms()
        time.sleep(30)

def start_alarm_monitor():
    t = threading.Thread(target=alarm_monitor, daemon=True)
    t.start()

def main_menu():
    load_alarms()
    while True:
        print('\n--- Alarm Clock & Reminder App ---')
        print('1. Set Alarm')
        print('2. View Alarms')
        print('3. Edit Alarm')
        print('4. Delete Alarm')
        print('5. Save & Exit')
        choice = input('Choose an option (1-5): ').strip()
        if choice == '1':
            set_alarm()
        elif choice == '2':
            view_alarms()
        elif choice == '3':
            edit_alarm()
        elif choice == '4':
            delete_alarm()
        elif choice == '5':
            save_alarms()
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    start_alarm_monitor()
    main_menu()
