import os
folder_path = "/Users/bagseonghyeon/Desktop/study/크롤링/lion/dataset"
for r,d,files in os.walk(folder_path):
    file_count = sum([len(files)])
print(file_count)