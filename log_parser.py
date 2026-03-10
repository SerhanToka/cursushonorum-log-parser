# log format [yyyy-mm-dd hh:mm:ss] - [ip] - [status]
import os
import datetime
import re
from collections import Counter

def analyze_logs(log_list, target_status="failed"):
    filtered_logs = [log for log in log_list if log["status"] == target_status]
    match_count = len(filtered_logs)
    target_ips = [log["ip"] for log in filtered_logs]
    ip_frequency = Counter(target_ips)
    event_dates = [log["date"] for log in filtered_logs]
    return match_count, target_ips, ip_frequency, event_dates

if __name__ == "__main__":
    log_database = []
    while True:
        try:
            path = input("Please enter the file path (e.g., home/user/logs.txt): ")
            with open(path, "r") as log_file:
                for line in log_file:
                    log_pattern = r"([\d\- :]+) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ([a-zA-Z]+)"
                    match_result = re.search(log_pattern, line)

                    if match_result:
                        parsed_date = datetime.datetime.strptime(match_result.group(1), "%Y-%m-%d %H:%M:%S")
                        log_entry = {
                            "date": parsed_date,
                            "ip": match_result.group(2),
                            "status": match_result.group(3).lower()
                        }

                        log_database.append(log_entry)
            break
        except FileNotFoundError:
            print("Critical Error: Log file not found!")

    failed_count, failed_ips, failed_frequencies, failed_dates = analyze_logs(log_list=log_database, target_status="failed")
    success_count, success_ips, success_frequencies, success_dates = analyze_logs(log_list=log_database, target_status="success")

    success_date_range = f"{min(success_dates)} to {max(success_dates)}" if success_dates else "No dates found"
    failed_date_range = f"{min(failed_dates)} to {max(failed_dates)}" if failed_dates else "No dates found"

    while True:
        choice = input("Choose an option: (1)Successful Logs and IP's, "
                      "(2)Failed Logs and IP's, (3)All, (4)Save Report, (q)Quit: ")

        if choice == "1":
            print(f"Successful Log Count: {success_count}, Date Range: {success_date_range}")
            for ip, frequency in success_frequencies.items():
                print(f"{ip} -> {frequency} times")
        elif choice == "2":
            print(f"Failed Log Count: {failed_count}, Date Range: {failed_date_range}")
            for ip, frequency in failed_frequencies.items():
                print(f"{ip} -> {frequency} times")
        elif choice == "3":
            print(f"Successful Log Count: {success_count}, Date Range: {success_date_range}")
            for ip, frequency in success_frequencies.items():
                print(f"{ip} -> {frequency} times")
            print("~" * 20)
            print(f"Failed Log Count: {failed_count}, Date Range: {failed_date_range}")
            for ip, frequency in failed_frequencies.items():
                print(f"{ip} -> {frequency} times")
        elif choice == "4":
            with open("report.txt", "w") as report_file:
                report_file.write(f"Successful Log Count: {success_count}, Date Range: {success_date_range}\n")
                for ip, frequency in success_frequencies.items():
                    report_file.write(f"{ip} -> {frequency} times\n")

                report_file.write("~" * 20 + "\n")

                report_file.write(f"Failed Log Count: {failed_count}, Date Range: {failed_date_range}\n")
                for ip, frequency in failed_frequencies.items():
                    report_file.write(f"{ip} -> {frequency} times\n")

                report_path = os.path.abspath("report.txt")
                print(f"Report saved: {report_path}")
        elif choice.lower() == "q":
            break
        else:
            print("Invalid selection, please try again.")