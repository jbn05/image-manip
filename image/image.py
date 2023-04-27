import os
from time import sleep
from PIL import Image, ImageFilter

# manipulation
os.mkdir('png_photos')#png
os.mkdir('size200_img')#new size
os.mkdir('size400_img')
os.mkdir('size600_img')
os.mkdir('rotated_img')#rotated
os.mkdir('black_white_img')#black and white
os.mkdir('blurred_img')#blurred 
os.mkdir('emboss_img')#emboss

# images
img1 = 'batman 1.jpeg'
img2 = 'flash 2.jpeg'
img3 = 'shazam 3.jpeg'
img4 = 'superman 4.jpeg'
img5 = 'cyborg 5.jpeg'
img6 = 'wonder woman 6.jpeg'
img7 = 'robin 7.jpeg'
img8 = 'raven 8.jpeg'
img9 = 'starfire 9.jpeg'
img10 = 'nightwing 10.jpeg'

# sizes
size_200 = (200,200)
size_400 = (400,400)
size_600 = (600,600)

#jpeg to png 
def transform(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)
                        i.save('png_photos/{}.png'.format(fn))
                        i.show()
# size change function
def size(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        if choice2 == "200":
                              i = Image.open(f)
                              fn, fext = os.path.splitext(f)
                              i.thumbnail(size_200)
                              i.save('size200_img/{}_200{}'.format(fn, fext))
                              i.show()
                        elif choice2 == "400":
                              i = Image.open(f)
                              fn, fext = os.path.splitext(f)
                              i.thumbnail(size_400)
                              i.save('size400_img/{}_400{}'.format(fn, fext))
                              i.show()
                        elif choice2 == "600":
                              i = Image.open(f)
                              fn, fext = os.path.splitext(f)
                              i.thumbnail(size_600)
                              i.save('size600_img/{}_600{}'.format(fn, fext))
                              i.show()
# rotate pics function               
def rotate(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)
                        y = int(input("Please type in desired length to rotate: "))
                        i.rotate(y).save('rotated_img/{}_rotated{}'.format(fn, fext))
                        i.show()
# black and white function
def color(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)
                        i.convert(mode='L').save('black_white_img/{}_black_and_white{}'.format(fn, fext))                                                   
# image blur
def blur(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)
                        b = int(input("Enter the amount of blur you want: "))
                        fn, fext = os.path.splitext(f)
                        i.filter(ImageFilter.GaussianBlur(b)).save('blurred_img/{}_blurred{}'.format(fn, fext))
# emboss filter
def emboss(x):
      for f in os.listdir('.'):
            if f.endswith('.jpeg'):
                  if x == f:
                        i = Image.open(f)  
                        fn, fext = os.path.splitext(f)              
                        i.filter(ImageFilter.EMBOSS()).save('emboss_img/{}_emboss{}'.format(fn, fext))

def empty():
      # empties folder
            for f in os.listdir('png_photos'):
                  os.remove('png_photos/'+f)  
            os.removedirs('png_photos')  
            # deletes size folder
            for f in os.listdir('size200_img'):
                  os.remove('size200_img/'+f)  
            os.removedirs('size200_img')    
            for f in os.listdir('size400_img'):
                  os.remove('size400_img/'+f)  
            os.removedirs('size400_img')     
            for f in os.listdir('size600_img'):
                  os.remove('size600_img/'+f)  
            os.removedirs('size600_img')
            # deletes rotated images 
            for f in os.listdir('rotated_img'):
                  os.remove('rotated_img/'+f)
            os.removedirs('rotated_img')
            # deletes black and white
            for f in os.listdir('black_white_img'):
                  os.remove('black_white_img/'+f)
            os.removedirs('black_white_img')
            # deletes blurred
            for f in os.listdir('blurred_img'):
                  os.remove('blurred_img/'+f)
            os.removedirs('blurred_img')
            # deletes emboss 
            for f in os.listdir('emboss_img'):
                  os.remove('emboss_img/'+f)
            os.removedirs('emboss_img')
                             
choice = input("""
      Hi! In here there are 10 random pictures of DC heroes! you can even do edits to them. Have fun!
      
      Type in a number from 1 to 10 to select a DC photo, or type in "quit" to exit. 
      """)

if choice.isdigit():
      if ("1" in choice) or ("2" in choice) or ("3" in choice) or ("4" in choice) or ("5" in choice) or ("6" in choice) or ("7" in choice) or ("8" in choice) or ("9" in choice) or ("10" in choice):
            choice1 = str(input("""
            Would you like to save the image as a png instead of jpeg? \n
            Yes or no
            """))
            if choice1 == "yes":
                  transform(locals()["img" + choice])
            
            choice2 = str(input("""
            You can also change the size of the picture by typing "200" for size 200, "400" for size 400, "600" for size 600
            """))
            if choice2 != "no":
                  size(locals()["img" + choice])
      
            choice3 = str(input("""
            Try rotating the picture! Yes or no
             """))     
            if choice3 == "yes":
                 rotate(locals()["img" + choice])
            
            choice4 = str(input("""
            Do you want your image black and white? Yes or no
            """))
            if choice4 == "yes":
                  color(locals()["img" + choice])
            
            choice5 = str(input("""
            You can also blur the picture! Yes or no

            """))
            if choice5 == "yes":
                  blur(locals()["img" + choice])
            
            choice6 = str(input("""
            Want to try the emboss filter? yes or no: 
            """))
            if choice6 == "yes":
                  emboss(locals()["img" + choice])
            
      final = input("""
      Would you like to quit?
              """)

      if final == "yes":
            sleep(0.5)
            # deletes png folder
            for f in os.listdir('png_photos'):
                  os.remove('png_photos/'+f)  
            os.removedirs('png_photos')  
            # deletes size folders
            for f in os.listdir('size200_img'):
                  os.remove('size200_img/'+f)  
            os.removedirs('size200_img')    
            for f in os.listdir('size400_img'):
                  os.remove('size400_img/'+f)  
            os.removedirs('size400_img')     
            for f in os.listdir('size600_img'):
                  os.remove('size600_img/'+f)  
            os.removedirs('size600_img')
            # deletes rotated images folder
            for f in os.listdir('rotated_img'):
                  os.remove('rotated_img/'+f)
            os.removedirs('rotated_img')
            # empties black and white folder
            for f in os.listdir('black_white_img'):
                  os.remove('black_white_img/'+f)
            os.removedirs('black_white_img')
            # empties blurred folder
            for f in os.listdir('blurred_img'):
                  os.remove('blurred_img/'+f)
            os.removedirs('blurred_img')
            # empties emboss folder
            for f in os.listdir('emboss_img'):
                  os.remove('emboss_img/'+f)
            os.removedirs('emboss_img')
            quit()
      
      elif final == "no":
            choice = input("Choose a new number between 1-10: ")
      
      else: 
            print("Sorry that isn't a valid number for a picture, please select a number between 1-10")
            choice = input()

elif choice == "quit":
      print("See you again!")
      sleep(0.5)
      empty
      quit()
      
else:
      print("That isn't one of the choices for a picture! Please insert a valid number, needs to be between 1-10.")
            
