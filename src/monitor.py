import os

LOG_FILE = "../logs/metrics_log.txt"
THRESHOLD_DROP = 0.05  # 5% allowed drop


def get_last_two_accuracies():
    if not os.path.exists(LOG_FILE):
        print("No metrics log found.")
        return None, None

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    if len(lines) < 2:
        print("Not enough logs to compare.")
        return None, None

    last = float(lines[-1].split("Accuracy: ")[1])
    previous = float(lines[-2].split("Accuracy: ")[1])

    return previous, last


def monitor_model():
    previous, current = get_last_two_accuracies()

    if previous is None:
        return

    print(f"Previous Accuracy: {previous}")
    print(f"Current Accuracy: {current}")

    drop = previous - current

    if drop > THRESHOLD_DROP:
        print("⚠ ALERT: Model performance dropped significantly!")
    else:
        print("✅ Model performance stable.")


if __name__ == "__main__":
    monitor_model()