# import pyglet # type: ignore

# window = pyglet.window.Window(800, 600)

# # Create a rectangle
# rectangle = pyglet.shapes.Rectangle(20, 20, 20, 20, color=(0, 255, 0))

# # Function to print rectangle attributes
# def print_rectangle_attributes(rect):
#     print(f"x: {rect.x}, y: {rect.y}, width: {rect.width}, height: {rect.height}")

# # Print the rectangle's attributes
# print_rectangle_attributes(rectangle)

# rect = rectangle.x, rectangle.y, rectangle.width, rectangle.height
# print(rect)

# @window.event
# def on_draw():
#     window.clear()
#     rectangle.draw()


# pyglet.app.run()

print(400/32)

#make a box pattern of 24x24 with # at the edges and spaces in the middle and dosplay ot for a list of 24 elements with 24 elements each

for i in range(24):
    for j in range(24):
        if i == 0 or i == 23:
            print("#", end="")
        elif j == 0 or j == 23:
            print("#", end="")
        else:
            print(" ", end="")
    print()
    
    
########################
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
#                      #
########################

make this a list 

l = ["########################",
     "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "#                      #",
        "########################"]

