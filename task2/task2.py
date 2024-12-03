def main():
    reports = []

    # Open and read the file
    with open("task2_input.txt", "r") as file:
        for line in file:
            # Split the line into numbers and convert to float (or int if integers)
            row = list(map(int, line.split()))  # Change `float` to `int` if numbers are integers
            reports.append(row)

    safe_reports = 0
    for report in reports:
        increasing = True
        safe = True
        if report[1] < report[0]:
            increasing = False
        for i in range(len(report) - 1):
            if increasing:
                if not(report[i + 1] == report[i] + 1 or report[i + 1] == report[i] + 2 or report[i + 1] == report[i] + 3):
                    safe = False
                    break
            if not increasing:
                if not(report[i + 1] == report[i] - 1 or report[i + 1] == report[i] - 2 or report[i + 1] == report[i] - 3):
                    safe = False
                    break
        if safe:
            safe_reports += 1

    print(safe_reports)


if __name__ == '__main__':
    main()
