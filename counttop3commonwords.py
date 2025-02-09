from collections import Counter
import  re

text = '''The quick brown fox jumps over the lazy dog.
I love reading books in the evening.
She went to the store to buy some groceries.
This is a simple test sentence for counting words.
We should walk in the park every Sunday afternoon.'''

words = re.findall('\w+',text)
count= Counter(words)

print(count.most_common(3))