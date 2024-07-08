import worker
from validators import string, int


class Catalog(worker.Worker):
    workers = []
    id = 0

