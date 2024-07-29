import pandas as pd
import numpy as np

# Create a DataFrame
seat_reservation_data = [
    (1, 1), (2, 0), (3, 1), (4, 1), (5, 1),
    (6, 0), (7, 1), (8, 1), (9, 0), (10, 1),
    (11, 0), (12, 1), (13, 0), (14, 1), (15, 1),
    (16, 1), (17, 1), (18, 1), (19, 0), (20, 1), (21, 1)
]
df_seat_reservation = pd.DataFrame(seat_reservation_data, columns=["seat_id", "is_free"])

# Step 1: Create free_seat_stat DataFrame
free_seat_stat = df_seat_reservation[df_seat_reservation["is_free"] == 1].copy()
free_seat_stat["prev_free"] = free_seat_stat["seat_id"].shift(1)
free_seat_stat["next_free"] = free_seat_stat["seat_id"].shift(-1)

# Step 2: Create consecutive_seats DataFrame
free_seat_stat["gap"] = free_seat_stat["seat_id"] - free_seat_stat["prev_free"].fillna(free_seat_stat["seat_id"]) - 1
consecutive_seats = free_seat_stat[
    (free_seat_stat["seat_id"] == free_seat_stat["prev_free"] + 1) |
    (free_seat_stat["seat_id"] == free_seat_stat["next_free"] - 1)
]

# Step 3: Create consecutive_seat_group_numbers DataFrame
consecutive_seats["group_number"] = (consecutive_seats["gap"] > 0).cumsum()

# Step 4: Create group_sizes DataFrame
group_sizes = consecutive_seats.groupby("group_number").size().reset_index(name="group_size")

# Step 5: Calculate the number of free seat groups by group_size
result = group_sizes.groupby("group_size").size().reset_index(name="nr_of_free_seatgroups")

# Show the result
print(result.sort_values("group_size"))
