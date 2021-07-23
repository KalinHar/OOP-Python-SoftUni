from datetime import timedelta
from email_sender import send_email
from report_formatter import format_report
from report_generator import generate_report


def main():
    report = generate_report(duration=timedelta(seconds=2))
    formatted = format_report(report)
    print(formatted)
    send_email(formatted)


if __name__ == '__main__':
    main()
