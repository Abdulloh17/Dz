with open('newfile.txt', 'w') as file:
    for i in range(5):
        s = input()
        file.write(s + ':' + ' ')

with open('newfile.txt', 'r', encoding='UTF-8') as file1:
    for line in file1:
        print(line)

