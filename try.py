>>> stand = ["Star Platinum", "Emperor", "The World", "Magician's Red", "Crazy Diamond", "The Fool"]
>>> del stand[1]
>>> print(stand)
['Star Platinum', 'The World', "Magician's Red", 'Crazy Diamond', 'The Fool']
>>> del stand[2:4]
>>> print(stand)
['Star Platinum', 'The World', 'The Fool']
>>> del stand
>>> print(stand)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'stand' is not defined

print(first_name*3)