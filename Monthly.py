import json
import os
from datetime import datetime

FILE = "budget_log.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def set_budget():
    amount = float(input("🔧 Set your daily budget (Rs.): "))
    data = load_data()
    data["budget"] = amount
    save_data(data)
    print(f"✅ Budget of Rs.{amount} set successfully.\n")

def log_spend():
    data = load_data()
    if "budget" not in data:
        print("⚠️ Set your daily budget first!\n")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    amount = float(input("Enter amount spent (Rs.): "))
    note = input("Enter note (e.g., snacks, bus fare): ")

    if "logs" not in data:
        data["logs"] = {}
    if today not in data["logs"]:
        data["logs"][today] = []

    data["logs"][today].append({"amount": amount, "note": note})
    save_data(data)

    print("📝 Expense recorded.\n")
    check_budget(data, today)

def check_budget(data=None, date=None):
    if not data:
        data = load_data()
    if "budget" not in data:
        print("⚠️ No budget set.\n")
        return

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    spent = 0
    print(f"\n📅 Spending for {date}:")
    if "logs" in data and date in data["logs"]:
        for idx, entry in enumerate(data["logs"][date], 1):
            print(f"  {idx}. Rs.{entry['amount']} - {entry['note']}")
            spent += entry["amount"]
    else:
        print("  No entries.")

    print(f"💰 Total Spent: Rs.{spent}")
    print(f"📊 Budget Limit: Rs.{data['budget']}")
    if spent > data["budget"]:
        print("⚠️ You have crossed your daily budget!\n")
    else:
        print(f"✅ Remaining: Rs.{data['budget'] - spent:.2f}\n")

def main():
    while True:
        print("------ Daily Budget Monitor ------")
        print("1. Set Daily Budget")
        print("2. Log Spending")
        print("3. View Today’s Spending")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            set_budget()
        elif choice == "2":
            log_spend()
        elif choice == "3":
            check_budget()
        elif choice == "4":
            print("Goodbye! Stay within budget 💸")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
