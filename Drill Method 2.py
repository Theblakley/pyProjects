import os, time

for file in os.listdir("C:\\Users\\thebl\\OneDrive\\Desktop\\pyDrill"):
    if file.endswith(".txt"):
        x = (os.path.join("C:\\Users\\thebl\\OneDrive\\Desktop\\pyDrill", file))
        print((x), os.path.getmtime(x))
    
    
    
        
               
        
