def daily_steps_tracker():
    steps = input("Enter the steps taken each day (separated by spaces): ")
    steps_list = list(map(int, steps.split()))
    highest_steps = max(steps_list)
    lowest_steps = min(steps_list)
    average_steps = sum(steps_list) / len(steps_list)
    sorted_steps = sorted(steps_list, reverse=True)
    print("")
    print(f"Highest Steps: {highest_steps}")
    print(f"Lowest Steps: {lowest_steps}")
    print(f"Average Steps: {average_steps:.2f}")
    print(f"Steps in Descending Order: {sorted_steps}")

daily_steps_tracker()