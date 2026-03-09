# log format [date] - [ip] - [status]
import os
import datetime

def analyze_logs(log_list, target_status="failed"):
    filtered_logs = [log for log in log_list if log["status"] == target_status]
    match_count = len(filtered_logs)
    target_ips = {log["ip"] for log in filtered_logs}
    event_dates = [log["date"] for log in filtered_logs]
    return match_count, target_ips, event_dates

if __name__ == "__main__":
    log_database = []
    while True:
        try:
            path = input("Please enter the file path (e.g., home/user/logs.txt):")
            with open(path, "r") as log_file:
                for line in log_file:
                    data = line.split(" - ")
                    log_entry = {
                        "date": datetime.datetime.strptime(data[0], "%Y-%m-%d %H:%M:%S"),
                        "ip": data[1],
                        "status": data[2].strip()
                    }
                    log_database.append(log_entry)
            break
        except FileNotFoundError:
            print("Critical Error: Log file not found!")

    failed_count, failed_ips, failed_dates = analyze_logs(log_list=log_database, target_status="failed")
    success_count, success_ips, success_dates = analyze_logs(log_list=log_database, target_status="success")

    success_date_range = f"{min(success_dates)} to {max(success_dates)}" if success_dates else "No dates found"
    failed_date_range = f"{min(failed_dates)} to {max(failed_dates)}" if failed_dates else "No dates found"

    while True:
        choice = input("Choose an option: (1)Successful Logs and IP's, "
                      "(2)Failed Logs and IP's, (3)All, (4)Save Report, (q)Quit: ")

        if choice == "1":
            print(f"Successful Log Count: {success_count}, Date Range: {success_date_range}")
            print(f"Successful IP's: {success_ips}")
        elif choice == "2":
            print(f"Failed Log Count: {failed_count}, Date Range: {failed_date_range}")
            print(f"Failed IP's: {failed_ips}")
        elif choice == "3":
            print(f"Successful IP's: {success_ips} | Successful Log Count: {success_count} "
                  f"| Successful Date Range: {success_date_range} "
                  f"| Failed Log Count: {failed_count} | Failed IP's: {failed_ips} "
                  f"| Failed Date Range: {failed_date_range}")
        elif choice == "4":
            with open("report.txt", "w") as report_file:
                report_file.write(f"Successful IP's: {success_ips} | Successful Log Count: {success_count} "
                  f"| Successful Date Range: {success_date_range} "
                  f"| Failed Log Count: {failed_count} | Failed IP's: {failed_ips} "
                  f"| Failed Date Range: {failed_date_range}")
            report_path = os.path.abspath("report.txt")
            print(f"Report saved: {report_path}")
        elif choice.lower() == "q":
            break
        else:
            print("Invalid selection, please try again.")