# All functions below are to be used in the PRINT.py file

def place_record(album):
    return

def rotate_record(album):
    return

def drop_needle(album):
    print("Now playing music in the restaurant: {} \n".format(album))

def orders(name, count):
    print("Total {} sold today: {} - WOOHOO!!".format(name, count))

def sales(name, price):
    print("Total {} sales today: ${} - YAY!!".format(name, price))


def draw_shape(name, char):
    if name == 'box':
        return BOX_SHAPE.replace('x', char)
    elif name == 'burger':
        return burger.replace(char, char)
    elif name == 'triangle':
        return TRIANGLE_SHAPE.replace('x', char)
    else:
        return QUESTION_SHAPE.replace('x', char)


BOX_SHAPE = """
xxx
x x
xxx
"""

TRIANGLE_SHAPE = """
  x 
 x x
xxxxx
"""


QUESTION_SHAPE = """
  x
 x x
x   x
   x
  x
  x

  x
"""


burger = """
        ████████████████████        
      ██                    ██      
    ██                        ██    
  ██                            ██  
  ██                            ██  
  ██                            ██  
██                                ██
████████████████████████████████████
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
  ████████████████████████████████  
██                                ██
  ██    ██    ██████    ██    ████  
  ██████  ████      ████  ████  ██  
  ██                            ██  
    ████████████████████████████    
    """




# ARTWORK COMMENTED OUT USING THE "#" SYMBOL

                    
                                                                                
#                                 ▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒                                
#                               ░░▒▒░░▒▒░░▒▒░░░░░░░░                              
#                             ▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                            
#                           ▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░                          
#                           ▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          
#                           ▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒                          
#                             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒                            
#                             ▓▓░░░░████░░░░░░░░░░░░░░                            
#                             ░░██▓▓▓▓▓▓▓▓████░░░░████                            
#                           ██▓▓░░░░░░░░░░░░░░░░░░░░██▓▓                          
#                           ████░░░░░░░░████████████████                          
#                           ▒▒▒▒██░░████████████████▒▒▒▒                          
#                           ▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒░░░░▒▒                          
#                             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                            





                                                                                
                                                                                
#                                ▓▓▓▓▓▓░░▓▓▓▓▓▓████▓▓▓▓▓▓▓▓████▓▓████                              
#                         ██▓▓██░░░░░░░░░░    ░░░░░░░░░░░░░░    ░░░░██████                        
#                     ████░░░░░░░░    ░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░░░▓▓██                    
#                   ██░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░    ░░░░░░░░░░██                  
#                 ██░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                
#               ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓              
#             ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██            
#             ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██            
#           ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██          
#           ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
#             ████████████████▓▓██████████████████████████████████████████████████████            
#           ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
#           ██▒▒▒▒▒▒████▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒██        
#         ▓▓▒▒▒▒▒▒██▓▓██▒▒▒▒██▓▓▒▒▓▓██▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▓▓          
#         ████████▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████          
#               ████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████░░░░░░██        
#             ██░░░░░░██▒▒██░░░░░░░░░░░░░░░░██████▒▒▒▒▒▒▒▒██████░░░░░░░░░░░░░░░░░░██████░░██      
#           ▓▓░░░░▓▓▓▓▒▒▓▓▒▒▓▓░░░░░░░░░░░░▓▓▒▒▒▒▒▒▓▓▒▒████▒▒▓▓▒▒▓▓░░░░░░░░░░░░░░▓▓▒▒▓▓▒▒▓▓██      
#           ██░░██▒▒▓▓██████████░░░░░░████▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒████░░░░░░░░▓▓▒▒▒▒▒▒▒▒██        
#           ██████████░░░░░░░░░░▓▓░░▓▓░░░░████████████▒▒▓▓████████░░░░██░░░░▓▓▓▓▓▓████████        
#         ▓▓░░██▒▒▒▒██░░░░░░░░░░░░▓▓░░░░██▒▒▒▒▒▒▓▓▒▒▒▒██░░░░░░░░░░░░░░░░████▒▒▓▓░░░░░░░░░░██      
#         ██░░██▒▒▓▓▒▒██░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░░░░░████▓▓▒▒▒▒▒▒████░░░░░░██      
#         ████▒▒▓▓▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓██░░░░████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██        
#             ██████████████░░░░████████████████████████████████████████████████████████          
#           ▓▓░░░░░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
#           ██░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
#       ▓▓▓▓░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░▓▓▓▓      
#   ▓▓██░░░░░░░░██▓▓▓▓██▓▓████▓▓██▓▓██░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒██▓▓██▓▓████▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░░░░░░░▓▓░░  
# ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
# ██████████▒▒██████████████████████████████████████████▓▓████████████████████████████████████████
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                            
                                                                                
                                                                     
#                                 ██▓▓████████████████████                                        
#                           ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒██████                                  
#                         ██░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                              
#                       ██░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒████                          
#                     ██░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                      
#                   ██░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒██                    
#                 ██░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                  
#                 ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██                
#             ████▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██                
#           ██▒▒░░▒▒▒▒▒▒██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░██              
#         ▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒████▓▓██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██              
#         ████▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██              
#             ██▒▒░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒████████░░░░░░░░░░░░░░░░░░░░░░░░██              
#           ▓▓▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒██▓▓██▓▓░░░░░░░░░░░░░░░░██▒▒▓▓▓▓        
#           ██▒▒░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░▒▒▒▒████░░░░░░░░░░██░░░░░░░░██      
#             ████████████████▒▒▒▒██████▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒██████████▒▒▒▒▒▒░░░░██      
#               ████▒▒▓▓▓▓▓▓▓▓████▓▓▓▓██▒▒▒▒▒▒▒▒████████▒▒▒▒░░░░██▒▒▒▒▒▒░░░░▒▒▒▒░░░░▒▒▒▒██        
#             ██▒▒██▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓██▒▒░░██▓▓██▒▒▒▒░░░░▒▒▒▒▒▒░░░░██          
#           ██▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▒▒██▒▒▒▒▓▓▓▓████▓▓▓▓██▒▒▒▒░░░░████▒▒░░░░░░██        
#           ██▒▒▒▒▒▒▒▒▒▒██▓▓▓▓██▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒░░▓▓▒▒▒▒████▒▒▓▓██        
#         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██      
#     ██████▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████  
#   ██▒▒▒▒▒▒████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
# ██▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██▒▒▒▒████▓▓▓▓▓▓████▒▒▒▒▒▒██████▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▓▓▒▒▒▒▒▒▒▒██
# ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▒▒▓▓▓▓▓▓██████▓▓▓▓▓▓▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒██████▓▓▓▓██  ██████▒▒██
#     ████▓▓██▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓████░░██      ██  
#           ██▒▒▒▒▒▒████░░░░████████▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓████░░░░██          
#           ████████▓▓██░░░░░░░░░░░░████████████████████████▓▓▓▓██████▓▓▓▓▓▓██░░██░░░░██          
#               ██▓▓▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██████░░░░██░░░░██          
#               ██▓▓▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░▒▒▒▒██░░██          
#                 ████████████░░░░░░░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████░░░░▒▒▒▒▒▒████            
#               ██▒▒▒▒▒▒░░░░░░██░░░░░░████░░░░██████████████████░░░░██░░░░▒▒▒▒▒▒▒▒██              
#               ██▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓░░██░░░░░░░░░░░░░░████░░░░░░░░░░▓▓░░▒▒▒▒▒▒▒▒▒▒██                
#               ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                
#                 ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                  
#                 ░░▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░                  
#                       ████▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▓▓                        
#                               ██████████████████████████████████                                




                                                                                        
                                                                                        
                                                                                        
#                             ▓▓██████████████████████████████                            
#                           ▓▓████░░░░░░  ░░░░░░░░░░░░    ░░████                          
#                         ▓▓████  ░░░░░░  ░░░░    ░░░░    ░░  ████                        
#                       ▓▓████    ░░░░  ░░░░░░    ░░  ░░░░░░    ████                      
#                       ▓▓██░░░░░░░░░░  ░░░░░░░░░░░░    ░░░░░░░░░░██                      
#                       ▓▓██    ░░░░░░░░░░░░    ░░░░░░░░░░░░    ░░██                      
#                       ▓▓██    ░░░░    ░░░░░░░░░░░░░░    ░░░░  ░░██                      
#                       ████░░░░░░░░    ░░░░░░░░░░░░      ░░░░░░░░████                    
#                     ▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    
#                     ▓▓████░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░░░░░████                    
#                         ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                      
#                         ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                      
#                         ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                      
#                     ▓▓██████░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██████                    
#                     ▓▓██                                          ██                    
#                     ▓▓██                                          ██                    
#                     ▓▓██      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓      ██                    
#                     ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                    
#                     ▓▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                    
#                       ▓▓▓▓████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████                      
#                           ▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                          
#                           ▓▓██████████████████████████████████                          
                                                                                        
                                                                                        




#           ██████████████████          
#       ████                  ████      
#     ██                          ██    
#   ██                              ██  
#   ██                              ██  
#   ██████████████████████████████████  
#     ██▒▒▒▒                  ▒▒▒▒██    
#   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
#   ██████████████████████████████████  
#     ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    



                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
#                                               ░░░░  ░░░░░░░░                                            
#                                         ░░░░░░░░░░░░░░░░░░░░░░░░                                        
#                                     ░░░░░░░░░░░░██░░░░░░░░░░██░░░░░░                                    
#                                   ░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░                                  
#                                 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                
#                               ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                              
#                               ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                              
#                               ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                              
#                               ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                              
#                               ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                              
#                             ██    ▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒░░░░  ██                            
#                           ██▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ██                          
#                         ██▒▒    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░██                        
#                         ██    ░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ██                        
#                         ██    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ██                        
#                         ██      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░    ██                        
#                         ██    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ██                        
#                           ██  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ██░░                        
#                                 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                
#                                             ██            ██                                            
#                                             ██            ██                                            
#                                             ██            ██                                            
#                                             ██            ██                                            
#                                             ██            ██                                            
#                                             ██            ██                                            
#                                             ████          ████                                          
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        