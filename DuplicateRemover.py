from PIL import Image
import imagehash
import os
import numpy as np

class DuplicateRemover:

    extensions = ['png', 'jpg', 'jpeg', 'gif']

    def __init__(self, dirname, hash_size = 8):
        self.dirname = dirname
        self.hash_size = hash_size
        
    def find_duplicates(self, verbose=True):
        """
        Find and Delete Duplicates
        """
        
        fnames = os.listdir(self.dirname)
        hashes = {}
        duplicates = []
        if verbose:
            print("Finding Duplicates Now!\n")
        for image in fnames:
            if list(image.lower().split('.'))[-1] in self.extensions:
                with Image.open(os.path.join(self.dirname,image)) as img:
                    temp_hash = imagehash.average_hash(img, self.hash_size)
                    if temp_hash in hashes:
                        if verbose:
                            print("Duplicate {} \nfound for Image {}!\n".format(image,hashes[temp_hash]))
                        duplicates.append(image)
                    else:
                        hashes[temp_hash] = image
                   
        if len(duplicates) != 0:
            if verbose:
                a = input("Do you want to delete these {} Images? Press Y or N:  ".format(len(duplicates)))
            else:
                a = 'y'
            space_saved = 0
            if(a.strip().lower() == "y"):
                for duplicate in duplicates:
                    space_saved += os.path.getsize(os.path.join(self.dirname,duplicate))
                    
                    os.remove(os.path.join(self.dirname,duplicate))
                    if verbose:
                        print("{} Deleted Succesfully!".format(duplicate))
                
                if verbose:
                    print("\n\nYou saved {} mb of Space!".format(round(space_saved/1000000),2))
            else:
                if verbose:
                    print("Thank you for Using Duplicate Remover")
        else:
            if verbose:
                print("No Duplicates Found :(")
            
        
            
            
    def find_similar(self, location, similarity=80, verbose=True):
        fnames = os.listdir(self.dirname)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))
        
        with Image.open(location) as img:
            hash1 = imagehash.average_hash(img, self.hash_size).hash
        
        if verbose:
            print("Finding Similar Images to {} Now!\n".format(location))
        for image in fnames:
            if list(image.lower().split('.'))[-1] in self.extensions:
                with Image.open(os.path.join(self.dirname,image)) as img:
                    hash2 = imagehash.average_hash(img, self.hash_size).hash
                    
                    if np.count_nonzero(hash1 != hash2) <= diff_limit:
                        if verbose:
                            print("{} image found {}% similar to {}".format(image,similarity,location))
                    
                    
                    
                
        
            
