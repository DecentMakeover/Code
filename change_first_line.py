import os


for root,dirs,files in os.walk('/home/decentmakeover2/BBox-Label-Tool/Labels/002/'):
    for file in files:

        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r+b') as f:
                line = next(f) # grab first line
                old = '1'
                new = '0' 
                f.seek(0) 
                f.write(line.replace(old, new))


