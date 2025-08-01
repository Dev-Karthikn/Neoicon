# def outer_function(message):
    
#     def inner_function():
#         print(f"The message is: {message}") 
        
#     inner_function() # Call the inner function

# # Call the outer function, which in turn calls the inner function
# outer_function("Hello from the enclosed scope!") 

x=20
def outerfn():
    name="kailash"
    def innerfn():
        global x
        x+=10
        print(f"Hello This is ",name,"and your age is ",x)
    innerfn()

outerfn()
