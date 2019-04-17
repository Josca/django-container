# Helper module to easily run 'python manage.py' from IDE.

import os

if __name__ == '__main__':
    os.environ['TEST'] = '1'                             # set env var to use sqlite db
    os.system('python ../manage.py makemigrations app')  # generate next migration to /app/migrations folder
    os.system('rm test.db')                              # remove tmp created database file
