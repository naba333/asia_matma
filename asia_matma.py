import sys
import numpy
from numpy import random

max_mr = int(sys.argv[1])  # max multiplication result
urc = 100  # usable results counter

mult_arr = numpy.full((10, 10), 'free')

# fill true with result greater than max_mr and decrement urc
for x in range(10):
    for y in range(10):
        if max_mr < ((x + 1)*(y + 1)):
            urc -= 1
            mult_arr[x, y] = 'used'
print(mult_arr)

print(f'urc = {urc}\n\n')

# generate randomly exercises
multiply_exercises = list()

while urc > 0:
    el_nb = random.randint(urc)# print(f'random = {el_nb}')

    # find not used element
    x = 0
    y = 0
    current_element_counter = 0
    while current_element_counter < el_nb:
        if mult_arr[x, y] == 'free':
            current_element_counter += 1
            if current_element_counter == el_nb:
                break
        y += 1
        if y > 9:
            y = 0
            x += 1

    mult_arr[x, y] = "used"
    urc -= 1
    multiply_exercises.append(f'{x + 1} * {y + 1} = ___')

print(multiply_exercises)

# create html file
html_file_start_string = '''
<!DOCTYPE html>
<html>
<head>
	<title>Ćwiczenia z matematyki</title>
	<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
'''

html_file_end_string = '''
</body>
</html>
'''

# fill file with multiply exercises
html_pages_list = list()

mul_ex_nb = len(multiply_exercises)

line_nb = 1
col_nb = 1
start_new_page = True

# current page temporary string
cpts = ''

for i in range(mul_ex_nb):

    if start_new_page is True:
        start_new_page = False
        cpts = '\t<div class="page">\n'

    if line_nb == 1:
        cpts += '\t\t<div class="column">\n'

    cpts += f'\t\t\t<p>{multiply_exercises[i]}</p>\n'
    line_nb += 1

    # closing column
    if line_nb == 17:
        cpts += '\t\t</div>\n'
        line_nb = 1
        col_nb += 1
        # if last exercise
        if (i + 1) == mul_ex_nb:
            cpts += '\t</div>\n'
            html_pages_list.append(cpts)
            break

    # closing page
    if col_nb == 4:
        cpts += '\t</div>\n'
        html_pages_list.append(cpts)
        col_nb = 1
        start_new_page = True
        # if last exercise
        if (i + 1) == mul_ex_nb:
            break

    # if last exercise
    if (i + 1) == mul_ex_nb:
        cpts += '\t\t</div>\n'
        cpts += '\t</div>\n'
        html_pages_list.append(cpts)

for p in html_pages_list:
    print(p)

# save to file
file = open("matex.html","w+")
file.write(html_file_start_string)
for s in html_pages_list:
    file.write(s)
file.write(html_file_end_string)
file.close()
