def all_levels_safe(report, increasing):
    for i in range(len(report) - 1):
        if not two_levels_safe(report[i], report[i + 1], increasing):
            return False
    return True


def two_levels_safe(level1, level2, increasing):
    if increasing and (level2 == level1 + 1 or level2 == level1 + 2 or level2 == level1 + 3):
        return True
    if not increasing and (level2 == level1 - 1 or level2 == level1 - 2 or level2 == level1 - 3):
        return True
    return False


def main():
    reports = []

    # Open and read the file
    with open("task2_input.txt", "r") as file:
        for line in file:
            row = list(map(int, line.split()))
            reports.append(row)

    safe_reports = 0
    for report in reports:
        increasing = True
        if report[1] < report[0]:
            increasing = False

        if all_levels_safe(report, increasing):
            safe_reports += 1
        else:
            for i in range(len(report)):
                tmp_report = report.copy()
                tmp_report.pop(i)

                increasing = True
                if tmp_report[1] < tmp_report[0]:
                    increasing = False
                if all_levels_safe(tmp_report, increasing):
                    safe_reports += 1
                    break

    print(safe_reports)


if __name__ == '__main__':
    main()
