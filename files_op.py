def read_file(file_name):
    with open(file_name, mode='r') as file:
        data = file.read()
        return data

    raise NotImplementedError()


def read_file_into_list(file_name):
    with open(file_name, mode='r') as file:
        data = file.readlines()
        return data
    raise NotImplementedError()


def write_first_line_to_file(file_contents, output_filename):
    split_lines = file_contents.split("\n")
    first_line = split_lines[0]

    with open(output_filename, mode='w') as file:
        file.write(first_line)

    return None

    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    with open(file_name, mode='r') as file:
        data = file.readlines()
        even_list = []
        for count, line in enumerate(data, start=1):
            if count % 2 == 0:
                even_list.append(line)

    return even_list

    raise NotImplementedError()


def read_file_in_reverse(file_name):

    with open(file_name, mode='r') as file:
        data = file.readlines()

        return data[::-1]

    raise NotImplementedError()


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
