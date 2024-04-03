# csv 파일 읽기

student_list = []
with open('D:\\python-bt0720-psh\\Python-bt0803-psh\\0803\\File_IO\\student.csv', 'rt', encoding = 'utf-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)
