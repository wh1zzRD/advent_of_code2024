def check_single_page(pages, rules, page_num):
    for rule in rules:
        if rule[1] == pages[page_num]:
            for p in range(page_num + 1, len(pages)):
                if rule[0] == pages[p]:
                    return False

    return True


def main():
    rules = []
    books = []

    # Read and process the file
    with open("task5_input.txt", "r") as file:
        # Split the file into two parts
        parts = file.read().split("\n\n")  # Assuming a blank line separates the two parts

        # Process the first part (pipe-separated pairs)
        for line in parts[0].strip().split("\n"):
            rules.append([int(x) for x in line.split("|")])

        # Process the second part (comma-separated lines)
        for line in parts[1].strip().split("\n"):
            books.append([int(x) for x in line.split(",")])

    # Print the results
    print("Pairs List:")
    print(rules)
    print("\nLines List:")
    print(books)

    result = 0

    for book in books:
        valid = True
        for i in range(len(book)):
            if not check_single_page(book, rules, i):
                valid = False
                break
        if valid:
            result += book[len(book) // 2]

    print(result)


if __name__ == '__main__':
    main()
