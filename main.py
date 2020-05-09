from DuplicateRemover import DuplicateRemover

dirname = "images"

# Remove Duplicates
dr = DuplicateRemover(dirname)
dr.find_duplicates()

# Find Similar Images
dr.find_similar("IMG-20110704-00007.jpg",70)