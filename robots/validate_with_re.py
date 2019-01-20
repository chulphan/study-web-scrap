import re

value = '111341'

if not re.search(r'^[0-9,]+$', value):
    raise ValueError('Invalid PRice')
