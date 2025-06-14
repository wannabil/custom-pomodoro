# ⏱️ Custom Pomodoro

A minimalist productivity timer that rewards you in **MYR (Malaysian Ringgit)** for every focused session you complete. Think of it like a habit builder that logs your earnings, keeps a running balance in your wallet, and plays an alarm when your session ends.

---

## 🔧 Features

- Custom session duration with tagging
- Auto-calculated reward per minute based on MYR 1700 monthly salary
- Tracks daily session count and earnings
- Sound alarm at the end of each session
- Saves session history and wallet balance
- Tag breakdown to track focus time per activity

---

## 🚀 Getting Started

### 1. Clone this repository and navigate to it:

```bash
git clone https://github.com/wannabil/custom-pomodoro.git
cd custom-pomodoro
```

### 2. Install dependencies

This app requires [ffplay](https://ffmpeg.org/ffplay.html) to play the alarm sound. Install `ffmpeg` if you haven’t:

```bash
# macOS (Homebrew)
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

### 3. Download the alarm sound

Go to [Mixkit Free Alarm Sounds](https://mixkit.co/free-sound-effects/alarm/) and download a sound of your choice. Rename it to `alarm.wav` and place it in the same folder as the Python script.

---

## 🧠 How It Works

Your reward is based on:

```python
BASE_SALARY = 1700  # MYR/month
```

It calculates how much you earn per **minute** assuming:

- 26 work days/month
- 8 hours/day

When you start a session:

1. You input how long you want to work (in minutes)
2. You enter a tag (e.g., `reading`, `coding`)
3. The timer begins and an alarm sounds at the end
4. Your reward is added to the wallet
5. The session is logged with a timestamp and tag

---

## 🖥️ Running the App

Run the script using Python 3:

```bash
python3 start-session.py
```

You'll be greeted with a dashboard like this:

```
👋 Welcome! Your wallet balance is: MYR 56.78

📊 DASHBOARD
💼 Wallet Balance: MYR 56.78
📅 Sessions Today: 3
💵 Earnings Today: MYR 7.82
🏷️ Tag Breakdown:
  - coding: 60 min
  - reading: 30 min
```

---

## 📁 Files

- `start-session.py` — main app
- `wallet.txt` — your current balance
- `session_log.txt` — log of all completed sessions
- `alarm.wav` — alarm sound (you need to download this)

---

## 📝 Example Log Entry

```
2025-06-14 11:00:00 - 25 min - MYR 3.40 - Balance: MYR 20.50 - Tag: coding
```
