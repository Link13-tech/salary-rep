import argparse
import sys
from parsers.csv_parser import parse_employee_data
from reports import Reports


def main():
    parser = argparse.ArgumentParser(description="Salary report generator")
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    parser.add_argument("--report", required=True, help="Report type to generate")
    args = parser.parse_args()

    all_employees = []
    for file_path in args.files:
        try:
            employees = parse_employee_data(file_path)
            all_employees.extend(employees)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        report = Reports().get_report(args.report)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    print(report.generate(all_employees))


if __name__ == "__main__":
    main()
