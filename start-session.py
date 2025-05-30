import time
import os
import subprocess
from datetime import datetime, date
from collections import defaultdict

# Constants
BASE_SALARY = 1700
WALLET_FILE = "wallet.txt"
SESSION_LOG_FILE = "session_log.txt"
ALARM_FILE = "alarm.wav"  # make sure this file exists in the same directory

def play_sound(file_path=ALARM_FILE):
    try:
        subprocess.Popen(
            ['ffplay', '-nodisp', '-autoexit', file_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print("🔇 Could not play sound:", e)

def reward_per_minute():
    result = BASE_SALARY / 26 / 8 / 60  # MYR per minute
    return round(result, 2)  # Round to 2 decimal places

def load_wallet():
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, "r") as f:
            try:
                return float(f.read())
            except ValueError:
                return 0.0
    return 0.0

def save_wallet(balance):
    with open(WALLET_FILE, "w") as f:
        f.write(str(balance))

def log_session(minutes, reward, balance, tag):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {minutes} min - MYR {reward:.2f} - Balance: MYR {balance:.2f} - Tag: {tag}\n"
    with open(SESSION_LOG_FILE, "a") as f:
        f.write(log_entry)

def get_wallet_balance():
    return round(wallet, 2)

def start_custom_timer(minutes, tag):
    global wallet
    reward = reward_per_minute() * minutes
    print(f"⏳ {minutes}-minute session on '{tag}' started... Stay focused!")
    time.sleep(minutes * 60)
    play_sound()
    wallet += reward
    save_wallet(wallet)
    log_session(minutes, reward, wallet, tag)
    print(f"✅ MYR {reward:.2f} awarded for '{tag}'.")
    print(f"💰 Wallet: MYR {get_wallet_balance()}")

def show_dashboard():
    today = date.today().strftime("%Y-%m-%d")
    sessions = 0
    earnings_today = 0.0
    tag_summary = defaultdict(int)

    if os.path.exists(SESSION_LOG_FILE):
        with open(SESSION_LOG_FILE, "r") as f:
            for line in f:
                if today in line:
                    sessions += 1
                    parts = line.split(" - ")
                    try:
                        earnings_today += float(parts[2].split()[1])
                        minutes = int(parts[1].split()[0])
                        tag = parts[5].replace("Tag: ", "").strip()
                        tag_summary[tag] += minutes
                    except (IndexError, ValueError):
                        pass

    print("\n📊 DASHBOARD")
    print(f"💼 Wallet Balance: MYR {get_wallet_balance()}")
    print(f"📅 Sessions Today: {sessions}")
    print(f"💵 Earnings Today: MYR {round(earnings_today, 2)}")
    print("🏷️ Tag Breakdown:")
    for tag, minutes in tag_summary.items():
        print(f"  - {tag}: {minutes} min")

# Load wallet on startup
wallet = load_wallet()

if __name__ == "__main__":
    print(f"👋 Welcome! Your wallet balance is: MYR {get_wallet_balance()}")
    while True:
        show_dashboard()
        user_input = input("\nEnter session duration in minutes (or 'q' to quit): ").strip().lower()
        if user_input == 'q':
            print(f"👋 Goodbye! Final wallet: MYR {get_wallet_balance()}")
            break
        if user_input.isdigit() and int(user_input) > 0:
            tag = input("🔖 Enter a tag for this session (e.g., 'reading', 'coding', 'writing'): ").strip().lower()
            if not tag:
                tag = "untagged"
            start_custom_timer(int(user_input), tag)
        else:
            print("❌ Please enter a valid positive number of minutes.")



