def handle_numbers(n1, n2, n3):
    my_sum = 0
    for i in range(n1, n2 + 1):
        if i % n3 == 0:
            my_sum += 1
    return my_sum


def handle_string(value):
    result = {
        'letters': 0,
        'digits': 0
    }
    for symbol in value:
        if symbol.isalpha():
            result['letters'] += 1
        elif symbol.isdigit():
            result['digits'] += 1

    return result


def handle_list_of_tuples(input_list):
    return sorted(
        input_list,
        key=lambda record: (
            record[0],
            -int(record[1]),
            -int(record[2]),
            -int(record[3])
        ))


if __name__ == '__main__':
    print(handle_numbers(1, 10, 2))
    print(handle_string("Hello world! 123!"))

    example_list = [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98"),
    ]
    print(handle_list_of_tuples(example_list))
