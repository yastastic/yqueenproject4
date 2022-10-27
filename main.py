import arcade
nations_pop = open("nationsPop.txt", 'r')
nations_data = nations_pop.readlines()

# window
myWindow = arcade.open_window(400, 400, "Project 4, By Yasmine Queen")
arcade.set_background_color(arcade.color.AFRICAN_VIOLET)

arcade.start_render()
# graph
arcade.draw_line(80, 400, 80, 80, arcade.color.BLACK)
arcade.draw_line(400, 80, 80, 80, arcade.color.BLACK)
scaleY = (380 - 80) / len(range(100, 1500, 100))
currentY = 80
# text
arcade.draw_text("Population of the largest pop Nations on Earth", 35, 10, arcade.color.BLACK, 12, 0, 'left', "Calibri")

# draw the Y axis legend
for i in range(100, 1500, 100):
    currentLabel = arcade.Text(f"{i}M", 5, currentY, arcade.color.BLACK)
    currentLabel.draw()
    currentY += scaleY

scaleX = (400 - 80) / (len(nations_data) + 1)
currentX = 80
# x-axis legend
for country in nations_data:
    nation_split = country.split(",")
    nation_name = nation_split[0]
    nation_pop = int(nation_split[1])
    nation_growth = float(nation_split[2].strip())
    nation_label = arcade.Text(nation_name, currentX, 70, arcade.color.BLACK, 10)
    nation_pop_normalized = nation_pop / 1_400_000_000
    color = None
    if nation_growth > 0:
        color = arcade.color.GREEN
    else:
        color = arcade.color.RED

    arcade.draw_xywh_rectangle_filled(currentX, 80, scaleX - 5, nation_pop_normalized * (380 - 80), color)
    currentX += scaleX
    nation_label.rotation = -45
    nation_label.draw()

arcade.finish_render()
arcade.run()
