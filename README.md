# Python Crash Course
***This is the Python crash course series where I revise the basic concepts of Python and make 4 mini projects.***

> **Concepts that I revise:**
  1) ***Variable, If-else, loops***
  2) ***Match Cases, Functions, exceptions***
  3) ***Lists, tuples, sets, dictionaries***
  4) ***OOPS, File IO***

> **Mini-Projects:**
  1) **RoboSpeaker Program:** *This is the basic program where text is converted into speech.*
     ```python
       import os
       if __name__ == "__main__":
       print("Welcome to the Robo Speaker 1.1")
        while(True):
            x = input("Enter what you want to say")
             if x == 'q':
                 break   
             command = f"say {x}"
             os.system(command)
      ```
  2) **Weather App:** This is an app in which I use Weather API to access the weather of the different cities.
     ```python
      import requests
      import json
      
      city = input("Enter the name of the city\n")
      
      url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
    
      r = requests.get(url)
      # to convert in string
      wDic = json.loads(r.text)
      w = wDic["current"]["temp_c"]
      print(w)
      ```
  3) **Image Resizer:** In this mini project user can resize the given image with the help of the cv2 module.
      ```python
            import cv2
            image = cv2.imread("ex.jpg") # reading the normal image
            scale_percent = 50 # scale percentage
            
            # If we want to make it a grayscale image
            # image = cv2.imread("ex.jpg",cv2.IMREAD_GRAYSCALE)
            
            # display the image
            # cv2.imshow("A girl reading the book", image)
            
            # new width and the new height
            new_width = int(image.shape[1] * scale_percent / 100)
            new_height = int(image.shape[0] * scale_percent / 100)
            
            # resizeing the image
            output = cv2.resize(image, (new_width, new_height))
            
            # save the new image with the given name
            cv2.imwrite("newImage.png", output)
            
            # wait for the user to press a key
            cv2.waitKey(0)
      ```
 4) **PDF Merger:** In this mini project, the user can merge the given PDFs with the help of the PyPDF2  module.
    ```python
       import PyPDF2

        # No of pdf files
        pdFiles = ["1.pdf", "2.pdf"]
        
        # With this we can merge the 
        merger = PyPDF2.PdfMerger()
        
        for filename in pdFiles:
            pdFile = open(filename,"rb")
            pdfReader = PyPDF2.PdfReader(pdFile)
            merger.append(pdfReader)
        
        pdFile.close()
        
        # write all the data to the given output
        merger.write("mergerd.file")
      ```
