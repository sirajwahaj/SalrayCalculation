import csv
from datetime import datetime, timedelta

def calculate_overtime(start_time, end_time, break_time):
start_time = datetime.strptime(start_time, "%H:%M")
end_time = datetime.strptime(end_time, "%H:%M")
break_duration = timedelta(hours=int(break_time.split(':')[0]), minutes=int(break_time.split(':')[1]))

# Define overtime start and end times
overtime_start = datetime.strptime("23:30", "%H:%M").time()
overtime_end = datetime.strptime("5:30", "%H:%M").time()

# Calculate working hours excluding break time
total_working_hours = (end_time - start_time).seconds / 3600 # Convert seconds to hours
total_working_hours -= break_duration.total_seconds() / 3600 # Subtract break time in hours

# Calculate overtime hours based on overtime start and end times
if start_time.time() <= overtime_start and end_time.time()>= overtime_end:
    # Entire shift is overtime
    overtime_hours = total_working_hours
    elif end_time.time() <= overtime_end: # No overtime if the shift ends before the overtime period overtime_hours=0
        elif start_time.time()>= overtime_start:
        # No overtime if the shift starts after the overtime period
        overtime_hours = 0
        else:
        # Calculate overtime for the portion within the overtime period
        overlap_start = max(start_time.time(), overtime_start)
        overlap_end = min(end_time.time(), overtime_end)
        overtime_hours = (overlap_end.hour + overlap_end.minute / 60) - (overlap_start.hour + overlap_start.minute / 60)

        return total_working_hours, max(0, overtime_hours)

        # Read data from CSV file
        with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row if present
        for row in reader:
        day = row[0]
        date = int(row[1])
        start_time = row[2]
        end_time = row[3]
        break_time = row[5] # Assuming break time is in the sixth column (index 5)
        total_working_hours, overtime_hours = calculate_overtime(start_time, end_time, break_time)
        print(f"Day: {day}, Date: {date}")
        print(f"Start Time: {start_time}, End Time: {end_time}")
        print(f"Total working hours: {total_working_hours:.2f} hours")
        print(f"Overtime hours: {overtime_hours:.2f} hours")
        print("-" * 30)
