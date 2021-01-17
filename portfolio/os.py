import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path = os.path.join(BASE_DIR, '')
print(os.path.abspath(__file__))
print (path)