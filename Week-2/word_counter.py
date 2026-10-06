def read_file():
    file = open("sample.txt", "r")
    content = file.read()
    file.close()
    return content


def count_words(content):
    words = content.split()
    return len(words)


def count_lines(content):
    lines = content.splitlines()
    return len(lines)


def count_characters(content):
    return len(content)


content = read_file()

print("#### The content in file is ####")
print(content)

word_count = count_words(content)
line_count = count_lines(content)
character_count = count_characters(content)

print("\nNumber of words:", word_count)
print("Number of lines:", line_count)
print("Number of characters:", character_count)