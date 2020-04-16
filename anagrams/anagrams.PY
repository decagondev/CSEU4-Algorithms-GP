# Given a text file words.txt, print out the largest set of anagrams

# read in the words from a file
f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

def first_pass_anagrams(words): 
    pass

def second_anagrams(words):
    pass

def anagrams(words):
    pass

# test the algorithms
import time
start = time.time()
print(first_pass_anagrams(words))
end = time.time()
print(f'1st pass solution time: {end - start} seconds\n')

start = time.time()
print(second_anagrams(words))
end = time.time()
print(f'2st pass solution time: {end - start} seconds\n')

start = time.time()
print(anagrams(words))
end = time.time()
print(f'3rd pass solution time: {end - start} seconds\n')