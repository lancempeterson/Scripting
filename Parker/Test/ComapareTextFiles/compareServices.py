src = "C:/Users/Lance.Peterson/Desktop/Scripting/Parker"
dst = "C:/Users/Lance.Peterson/Desktop/Scripting/Parker/"

with open('CorrectServicesResult.txt', 'r') as file1:
    with open('CurrentServicesResult.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('ServicesResult.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)