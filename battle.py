from battle_results_db import *
from create_databases import *
from populate_initial_db import *
from populate_results_db import *


def create():
    create_databases()
    populate_results()
    populate_initial_stats()

def write():
    write_results()



write()




