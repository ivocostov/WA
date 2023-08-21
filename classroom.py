def convert_cm_to_meters(length_in_cm, width_in_cm):
    # Refactoring the working spot size from centimeters in meters
    length_in_meters = length_in_cm / 100
    width_in_meters = width_in_cm / 100

    return length_in_meters, width_in_meters


def calculate_the_amount_of_working_spots(room_length, working_spot_length, room_width, working_spot_width,
                                          corridor_width_in_meters):
    working_spots_rows = room_length // working_spot_length
    working_spots_columns = (room_width - corridor_width_in_meters) // working_spot_width

    return working_spots_rows, working_spots_columns


def calculate_working_spots(length, width):
    # By instruction limitation for area dimensions are: 3 <= classroom_length <= classroom_width <= 100,
    # but in my opinion it should be like this: 3 <= classroom_width <= classroom_length <= 100.
    # Otherwise, none of the given inputs in the task will return a result.
    if 3 <= width <= length <= 100:
        corridor_width_in_meters = 1
        working_spot_length_in_cm = 120
        working_spot_width_in_cm = 70
        working_spots_taken_by_door = 1
        working_spots_taken_by_desk = 2

        working_spot_length_in_meters, working_spot_width_in_meters = convert_cm_to_meters(working_spot_length_in_cm,
                                                                                           working_spot_width_in_cm)

        # Calculating working places rows and columns
        working_spots_rows, \
            working_spots_columns = calculate_the_amount_of_working_spots(length, working_spot_length_in_meters, width,
                                                                          working_spot_width_in_meters,
                                                                          corridor_width_in_meters)

        # Calculating the total number of working spots
        total_working_spots = working_spots_rows * working_spots_columns - working_spots_taken_by_door - working_spots_taken_by_desk

        return total_working_spots


classroom_length = float(input('Please enter Classroom length: '))
classroom_width = float(input('Please enter Classroom width: '))

print(int(calculate_working_spots(classroom_length, classroom_width)))
