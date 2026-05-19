import re
from datetime import datetime
from pathlib import Path

INPUT_FILE = Path("sample_text.txt")
OUTPUT_FILE = Path("extracted_emails.txt")
REPORT_FILE = Path("automation_report.txt")


def create_sample_file():
    if not INPUT_FILE.exists():
        sample_data = """
Welcome to CodeAlpha Python Programming Internship.

For internship support, contact services@codealpha.tech.
For general queries, email services.codealpha@gmail.com.
Student email example: naman.phogat@example.com.
Project support: project.team@internship.org.

Thank you.
"""
        INPUT_FILE.write_text(sample_data.strip(), encoding="utf-8")


def read_file():
    try:
        return INPUT_FILE.read_text(encoding="utf-8")

    except FileNotFoundError:
        print("Input file not found.")
        return ""


def extract_emails(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    return sorted(set(emails))


def save_emails(emails):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        if emails:
            file.write("Extracted Email Addresses\n")
            file.write("=========================\n")

            for index, email in enumerate(emails, start=1):
                file.write(f"{index}. {email}\n")
        else:
            file.write("No email addresses found.\n")


def generate_report(emails):
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write("Task Automation Report\n")
        file.write("======================\n")
        file.write("Developer: Naman Phogat\n")
        file.write("Internship: CodeAlpha Python Programming Internship\n")
        file.write("Project: Email Extractor Automation\n")
        file.write(f"Generated On: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}\n\n")

        file.write(f"Input File: {INPUT_FILE}\n")
        file.write(f"Output File: {OUTPUT_FILE}\n")
        file.write(f"Total Emails Extracted: {len(emails)}\n\n")

        if emails:
            file.write("Emails Found:\n")
            for email in emails:
                file.write(f"- {email}\n")
        else:
            file.write("No email addresses were found in the input file.\n")


def display_emails(emails):
    print("\n========== Email Extraction Result ==========")

    if emails:
        print(f"Total Emails Found: {len(emails)}\n")

        for index, email in enumerate(emails, start=1):
            print(f"{index}. {email}")
    else:
        print("No email addresses found.")

    print("============================================")


def add_text_to_sample_file():
    print("\nEnter text to add into sample_text.txt")
    print("Type 'done' on a new line to stop.\n")

    lines = []

    while True:
        line = input()

        if line.lower().strip() == "done":
            break

        lines.append(line)

    if lines:
        with open(INPUT_FILE, "a", encoding="utf-8") as file:
            file.write("\n" + "\n".join(lines))

        print("\nText added successfully.")
    else:
        print("\nNo text added.")


def view_input_file():
    print("\n========== Input File Content ==========")
    print(read_file())
    print("========================================")


def run_email_extraction():
    text = read_file()
    emails = extract_emails(text)

    save_emails(emails)
    generate_report(emails)
    display_emails(emails)

    print(f"\nEmails saved in: {OUTPUT_FILE}")
    print(f"Report generated in: {REPORT_FILE}")


def show_menu():
    print("""
====================================================
        TASK AUTOMATION - EMAIL EXTRACTOR
====================================================
Developer : Naman Phogat
Internship: CodeAlpha Python Programming Internship
----------------------------------------------------
1. View Input File
2. Add Text to Input File
3. Extract Email Addresses
4. View Extracted Emails
5. Generate Fresh Report
6. Exit
====================================================
""")


def view_extracted_emails():
    if OUTPUT_FILE.exists():
        print("\n========== Extracted Emails File ==========")
        print(OUTPUT_FILE.read_text(encoding="utf-8"))
        print("===========================================")
    else:
        print("\nNo extracted email file found. Run extraction first.")


def main():
    create_sample_file()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_input_file()

        elif choice == "2":
            add_text_to_sample_file()

        elif choice == "3":
            run_email_extraction()

        elif choice == "4":
            view_extracted_emails()

        elif choice == "5":
            text = read_file()
            emails = extract_emails(text)
            generate_report(emails)
            print(f"\nFresh report generated successfully: {REPORT_FILE}")

        elif choice == "6":
            print("\nThank you for using Email Extractor Automation.")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")


if __name__ == "__main__":
    main()
