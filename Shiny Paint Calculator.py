print("Welcome to Shiny Paint Company for indoor painting!")

def computeRoomArea(how_many_rooms_one, shape_of_room_one):
    how_many_rooms_one = str(input("How many Rooms do you want to paint: \n"))
    print("Thank you!")

    shape_of_room_one = str(input(" Room: 1 \n Select the shape of the room: \n 1 - Rectangular \n 2 - Square \n \
3 - Custom (more or less than 4 walls, all square or rectangles) \n"))
    length_of_room_one = float(input("Enter the length of the room in feet: \n"))
    width_of_room_one = float(input("Enter the width of the room in feet: \n"))
    height_of_room_one = float(input("Enter the height of the room in feet: \n"))

    def computeRectangleWallsArea(length_of_room_one, width_of_room_one, height_of_room_one):
        rectangle_walls_area = float((length_of_room_one * height_of_room_one) * 2) +\
        ((width_of_room_one * height_of_room_one) * 2)

    computeRectangleWallsArea(length_of_room_one, width_of_room_one, height_of_room_one)

    windows_and_doors_one = str(input("How many windows and doors does the room contain? \n"))
    w_and_d_length_one1 = float(input("Enter window/door length for window/door 1 in feet \n"))
    w_and_d_width_one1 = float(input("Enter window/door width for window/door 1 in feet \n"))
    w_and_d_length_one2 = float(input("Enter window/door length for window/door 2 in feet \n"))
    w_and_d_width_one2 = float(input("Enter window/door width for window/door 2 in feet \n"))

    def computeWindowsDoorsArea(w_and_d_length_one1, w_and_d_width_one1, w_and_d_length_one2, w_and_d_width_one2):
        rectangle_w_and_d_area = float((w_and_d_length_one1 * w_and_d_width_one1) +\
        (w_and_d_length_one2 * w_and_d_width_one2))

    computeWindowsDoorsArea(w_and_d_length_one1, w_and_d_width_one1, w_and_d_length_one2, w_and_d_width_one2)

    rectangle_walls_area = float((length_of_room_one * height_of_room_one) * 2) +\
    ((width_of_room_one * height_of_room_one) * 2)
    rectangle_w_and_d_area = float((w_and_d_length_one1 * w_and_d_width_one1) +\
    (w_and_d_length_one2 * w_and_d_width_one2))

    def calculateRectangleArea(rectangle_walls_area, rectangle_w_and_d_area):
        rectangle_paint_area = float(rectangle_walls_area - rectangle_w_and_d_area)
        rectangle_gallons = float(rectangle_paint_area / 350)
        rectangle_gallons_round = format(float(rectangle_paint_area / 350), '.2f')
        rectangle_cost = format(float(rectangle_gallons * 42), '.2f')
        print("For Room: 1, the area to be painted is " + str(rectangle_paint_area) + " square ft and will \
require " + str(rectangle_gallons_round) + " gallons to paint. This will cost the customer $" + str(rectangle_cost))

    calculateRectangleArea(rectangle_walls_area, rectangle_w_and_d_area)

    shape_of_room_two = str(input(" Room: 2 \n Select the shape of the room: \n 1 - Rectangular \n 2 - Square \n \
3 - Custom (more or less than 4 walls, all square or rectangles) \n"))

    length_of_room_two = float(input("Enter the length of one side of the room: \n"))

    def computeSquareWallsArea(length_of_room_two):
        square_walls_area = float((length_of_room_two * length_of_room_two) * 4)

    computeSquareWallsArea(length_of_room_two)

    windows_and_doors_two = str(input("How many windows and doors does the room contain? \n"))
    w_and_d_length_two1 = float(input("Enter window/door length for window/door 1 in feet \n"))
    w_and_d_width_two1 = float(input("Enter window/door width for window/door 1 in feet \n"))
    w_and_d_length_two2 = float(input("Enter window/door length for window/door 2 in feet \n"))
    w_and_d_width_two2 = float(input("Enter window/door width for window/door 2 in feet \n"))

    def computeWindowsDoorsArea(w_and_d_length_two1, w_and_d_width_two1, w_and_d_length_two2, w_and_d_width_two2):
        square_w_and_d_area = float((w_and_d_length_two1 * w_and_d_width_two1) +\
        (w_and_d_length_two2 * w_and_d_width_two2))

    computeWindowsDoorsArea(w_and_d_length_two1, w_and_d_width_two1, w_and_d_length_two2, w_and_d_width_two2)

    square_walls_area = float((length_of_room_two * length_of_room_two) * 4)
    square_w_and_d_area = float((w_and_d_length_two1 * w_and_d_width_two1) +\
    (w_and_d_length_two2 * w_and_d_width_two2))

    def computeSquareArea(square_walls_area, square_w_and_d_area):
        square_paint_area = float(square_walls_area - square_w_and_d_area)
        square_gallons = float(square_paint_area / 350)
        square_gallons_round = round(float(square_paint_area / 350), 2)
        square_cost = format(float(square_gallons * 42), '.2f')
        print("For Room: 2, the area to be painted is " + str(square_paint_area) + " square ft and will \
require " + str(square_gallons_round) + " to paint. This will cost the customer $" + str(square_cost))

    computeSquareArea(square_walls_area, square_w_and_d_area)

    shape_of_room_three = str(input(" Room: 3 \n Select the shape of the room: \n 1 - Rectangular \n 2 - Square \n \
3 - Custom (more or less than 4 walls, all square or rectangles) \n"))

    how_many_walls = str(input("How many walls are there in the room \n"))
    height_of_room_three1 = float(input("Enter the height of wall 1 in feet \n"))
    length_of_room_three1 = float(input("Enter the length of wall 1 in feet \n"))
    height_of_room_three2 = float(input("Enter the height of wall 2 in feet \n"))
    length_of_room_three2 = float(input("Enter the length of wall 2 in feet \n"))
    height_of_room_three3 = float(input("Enter the height of wall 3 in feet \n"))
    length_of_room_three3 = float(input("Enter the length of wall 3 in feet \n"))

    def computeCustomWallsArea(height_of_room_three1, length_of_room_three1, height_of_room_three2,
    length_of_room_three2, height_of_room_three3, length_of_room_three3):
        custom_walls_area = float((height_of_room_three1 * length_of_room_three1) + (height_of_room_three2 *
        length_of_room_three2) + (height_of_room_three3 * length_of_room_three3))

    computeCustomWallsArea(height_of_room_three1, length_of_room_three1, height_of_room_three2, length_of_room_three2,
    height_of_room_three3, length_of_room_three3)

    windows_and_doors_three = str(input("How many windows and doors does the room contain? \n"))
    w_and_d_length_three = float(input("Enter window/door length for window/door 1 in feet \n"))
    w_and_d_width_three = float(input("Enter window/door width for window/door 1 in feet \n"))

    def computeCustomDoorsArea(w_and_d_length_three, w_and_d_width_three):
        custom_w_and_d_area = float(w_and_d_length_three * w_and_d_width_three)

    computeCustomDoorsArea(w_and_d_length_three, w_and_d_width_three)

    custom_walls_area = float((height_of_room_three1 * length_of_room_three1) + (height_of_room_three2 *
    length_of_room_three2) + (height_of_room_three3 * length_of_room_three3))
    custom_w_and_d_area = float(w_and_d_length_three * w_and_d_width_three)

    def calculateCustomArea(custom_walls_area, custom_w_and_d_area):
        custom_paint_area = float(custom_walls_area - custom_w_and_d_area)
        custom_gallons = float(custom_paint_area / 350)
        custom_gallons_round = round(float(custom_paint_area / 350), 2)
        custom_cost = format(float(custom_gallons * 42), '.2f')
        print("For Room: 3, the area to be painted is " + str(custom_paint_area) + " square ft and will \
require " + str(custom_gallons_round) + " gallons to paint. This will cost the customer $" + str(custom_cost))

    calculateCustomArea(custom_walls_area, custom_w_and_d_area)

    rectangle_paint_area = rectangle_walls_area - rectangle_w_and_d_area
    rectangle_gallons = float(rectangle_paint_area / 350)
    rectangle_gallons_round = format(float(rectangle_paint_area / 350), '.2f')
    rectangle_cost = float(rectangle_gallons * 42)
    square_paint_area = square_walls_area - square_w_and_d_area
    square_gallons = float(square_paint_area / 350)
    square_gallons_round = round(float(square_paint_area / 350), 2)
    square_cost = float(square_gallons * 42)
    custom_paint_area = custom_walls_area - custom_w_and_d_area
    custom_gallons = float(custom_paint_area / 350)
    custom_gallons_round = round(float(custom_paint_area / 350), 2)
    custom_cost = float(custom_gallons * 42)

    def computeTotalArea(rectangle_paint_area, square_paint_area, custom_paint_area):
        Total_Area = str(rectangle_paint_area + square_paint_area + custom_paint_area)

    computeTotalArea(rectangle_paint_area, square_paint_area, custom_paint_area)

    def computeGallons(rectangle_gallons, square_gallons_round, custom_gallons_round):
        Total_Gallons = float(rectangle_gallons + square_gallons_round + custom_gallons_round)

    computeGallons(rectangle_gallons, square_gallons_round, custom_gallons_round)

    def computePaintPrice(rectangle_cost, square_cost, custom_cost):
        Total_Cost = rectangle_cost + square_cost + custom_cost

    Total_Area = format(rectangle_paint_area + square_paint_area + custom_paint_area, '.2f')
    Total_Gallons = round(float(rectangle_gallons + square_gallons_round + custom_gallons_round), 2)
    Total_Cost = format(float(rectangle_cost + square_cost + custom_cost), '.2f')

    print("Area to be painted is " + str(Total_Area) + " square ft and will require " + str(Total_Gallons) + " \
gallons to paint. This will cost the customer $" + str(Total_Cost))

    computePaintPrice(rectangle_cost, square_cost, custom_cost)

computeRoomArea(1, 1)
