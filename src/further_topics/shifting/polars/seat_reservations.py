import polars as pl

# Create a DataFrame
seat_reservation_data = [
    (1, 1), (2, 0), (3, 1), (4, 1), (5, 1),
    (6, 0), (7, 1), (8, 1), (9, 0), (10, 1),
    (11, 0), (12, 1), (13, 0), (14, 1), (15, 1),
    (16, 1), (17, 1), (18, 1), (19, 0), (20, 1), (21, 1),
    (22, 1), (23, 0), (24, 0), (25, 1), (26, 1), (27, 1),
    (28, 0), (29, 1), (30, 1)
]
df_seat_reservation = pl.DataFrame(seat_reservation_data, schema=["seat_id", "is_free"])

# Step 1: Create free_seat_stat DataFrame
free_seat_stat = df_seat_reservation.filter(pl.col("is_free") == 1)
free_seat_stat = free_seat_stat.with_columns([
    pl.col("seat_id").shift(1).alias("prev_free"),
    pl.col("seat_id").shift(-1).alias("next_free")
])

# Step 2: Create consecutive_seats DataFrame
free_seat_stat = free_seat_stat.with_columns([
    (pl.col("seat_id") - pl.col("prev_free").fill_null(pl.col("seat_id")) - 1).alias("gap")
])
consecutive_seats = free_seat_stat.filter(
    (pl.col("seat_id") == pl.col("prev_free") + 1) |
    (pl.col("seat_id") == pl.col("next_free") - 1)
)

# Step 3: Create consecutive_seat_group_numbers DataFrame
consecutive_seats = consecutive_seats.with_columns([
    pl.col("gap").gt(0).cum_sum().alias("group_number")
])

# Step 4: Create group_sizes DataFrame
group_sizes = consecutive_seats.group_by("group_number").agg(pl.count().alias("group_size"))

# Step 5: Calculate the number of free seat groups by group_size
result = group_sizes.group_by("group_size").agg(pl.count().alias("nr_of_free_seatgroups"))

# Show the result
print(result.sort("group_size"))
