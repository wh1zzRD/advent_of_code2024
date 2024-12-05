from collections import defaultdict, deque


def topological_sort(pairs):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    nodes = set()

    for a, b in pairs:
        graph[a].append(b)
        indegree[b] += 1
        nodes.add(a)
        nodes.add(b)

    queue = deque([node for node in nodes if indegree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(nodes):
        raise ValueError("Cycle detected! Topological sorting is not possible.")

    return sorted_order


def check_single_page(pages, rules, page_num):
    for rule in rules:
        if rule[1] == pages[page_num]:
            for p in range(page_num + 1, len(pages)):
                if rule[0] == pages[p]:
                    return False

    return True


def reorder(book, rules):
    important_rules = []
    for rule in rules:
        if rule[0] in book and rule[1] in book:
            important_rules.append(rule)

    return important_rules


def main():
    rules = []
    books = []

    with open("task5_input.txt", "r") as file:
        parts = file.read().split("\n\n")

        for line in parts[0].strip().split("\n"):
            rules.append([int(x) for x in line.split("|")])

        for line in parts[1].strip().split("\n"):
            books.append([int(x) for x in line.split(",")])

    result = 0

    for book in books:
        for i in range(len(book)):
            if not check_single_page(book, rules, i):
                new = reorder(book, rules)
                top_sorted = topological_sort(new)
                print(top_sorted)
                result += top_sorted[len(top_sorted) // 2]
                break

    print(result)


if __name__ == '__main__':
    main()
