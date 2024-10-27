
with open('D:\\gitdemo\\Python Programs\\file.txt', 'r') as file:
    
    for line_number, line in enumerate(file, start=1):
        
        words = line.split()
        word_count = len(words)
        print(f"Line {line_number}: {word_count} words")

print("Word count for each line has been printed.")
