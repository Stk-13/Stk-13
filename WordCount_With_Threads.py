"""
Word Count With Thread Implementation
--> The program reads a text file and displays the frequency of each word while ignoring the case of the word.
--> It makes use of the 'threading' module to allow for multiple threads to process the word count problem in parallel.
"""

import threading

def word_count(text, word_count_dict):
    """
    Function to count the frequency of words in the text file.
    """
    for lines in text:
        words = lines.lower().split()  # Ignoring the case of words
        for word in words:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1


file_path = input("Enter the filename: ")
threads_num = int(input("Enter the number of threads: "))

word_count_dict = {}  
lock = threading.Lock()  # Lock for synchonization

with open(file_path, 'r') as f:
    text = f.readlines()

lines_per_thread = len(text) // threads_num  # Calculating the number of lines to be processed by each thread

threads = []  
for i in range(threads_num):
    start_pos = i * lines_per_thread  # Starting index of lines that the current thread will process
    end_pos = start_pos + lines_per_thread if i < threads_num - 1 else len(text)  # Ending index of lines that the current thread will process

    thread = threading.Thread(target=word_count, args=(text[start_pos:end_pos], word_count_dict))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join() 

print(word_count_dict) # Printing the frequency of each word