print('task 1 (print the number of words in a sentence')
print('---------------------------')

x='Egypt (Arabic: مصر Miṣr [mesˁr], Egyptian Arabic pronunciation: [mɑsˤr]), officially the Arab Republic of Egypt, is a transcontinental country spanning the northeast corner of Africa and the Sinai Peninsula in the southwest corner of Asia. It is bordered by the Mediterranean Sea to the north, the Gaza Strip of Palestine and Israel to the northeast, the Red Sea to the east, Sudan to the south, and Libya to the west. The Gulf of Aqaba in the northeast separates Egypt from Jordan and Saudi Arabia. Cairo is the capital and largest city of Egypt, while Alexandria, the second-largest city, is an important industrial and tourist hub at the Mediterranean coast.[14] At approximately 100 million inhabitants, Egypt is the 14th-most populated country in the world, and the third-most populated in Africa, behind Nigeria and Ethiopia'

print(x.count(''))


print('task -2(most occurer word')
print('----------------------------')

no_of_is=x.count('is')
no_of_are=x.count('are')
no_of_a=x.count('a')

print('total number of is :',no_of_is)
print('total number of are :',no_of_are)
print('total number of a :',no_of_a)
print('')

print('task-03 vowels to uppercase')
print('---------------------------')

vowels =x.replace('a','A'),x.replace('e','E'),x.replace('i','I'),x.replace('o','O'),x.replace('u','U')
print(vowels)
