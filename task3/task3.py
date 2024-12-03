import re


def mul_res(s):
    nums = s[4:-1]
    one, two = map(int, nums.split(","))
    return one * two


def main():
    with open("task3_input.txt", "r") as file:
        instructions = file.read()

        combined_pattern = (
            r"mul\(\d{1,3},\d{1,3}\)|"
            r"do\(\)|"
            r"don't\(\)"
        )

        # Find all matches
        matches = re.findall(combined_pattern, instructions)
        print(matches)

        result = 0
        i = 0
        do = True
        while i < len(matches):
            if matches[i] == "don't()":
                do = False
                i += 1
                continue
            elif matches[i] == "do()":
                do = True
                i += 1
                continue
            else:
                if do:
                    result += mul_res(matches[i])
                    i += 1
                    continue
            i += 1

        print(result)

if __name__ == '__main__':
    main()
