import arcade
nations_pop = open("nationsPop.txt", 'r')
nations_data = nations_pop.readlines()


myWindow = arcade.open_window(400, 400, "Project 4, By Yasmine Queen")
arcade.set_background_color(arcade.color.AFRICAN_VIOLET)

arcade.start_render()
# graph
arcade.draw_line(80, 400, 80, 80, arcade.color.BLACK)
arcade.draw_line(400, 80, 80, 80, arcade.color.BLACK)
scale = (400 - 80) / len(range(100, 1500, 100))
currentY = 80
# text
arcade.draw_text("Population of the largest pop Nations on Earth", 35, 10, arcade.color.BLACK, 12, 0, 'left', "Calibri")
# X-axis legend-unfinished
# I was supposed to turn nations_data into a list then strip the population numbers and the other numbers.
# then I was supposed to print the list to the x-axis. And I was also supposed to create blocks,
# to match the population number highest to lowest.
# arcade.draw_text(f"{nations_data}", 100, 100, arcade.color.BLACK, 12, 0, 'left', "Calibri")

# Draw the Y axis legend
for i in range(100, 1500, 100):
    currentLabel = arcade.Text(f"{i}M", 5, currentY, arcade.color.BLACK)
    currentLabel.draw()
    currentY += scale



arcade.finish_render()
arcade.run()
