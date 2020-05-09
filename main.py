from DuplicateRemover import DuplicateRemover
import time

dirname = "images"
dr = DuplicateRemover(dirname)
dr.find_duplicates()

time.sleep(2)
dr.find_similar("IMG-20110704-00007.jpg",70)