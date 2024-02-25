from datetime import datetime, timedelta

# Function to parse timestamp and convert to datetime object
def parse_timestamp(timestamp):
    return datetime.strptime(timestamp, "%a %d %b %Y %H:%M:%S %z")

# Function to calculate absolute difference in seconds between two timestamps
def time_difference_in_seconds(timestamp1, timestamp2):
    dt1 = parse_timestamp(timestamp1)
    dt2 = parse_timestamp(timestamp2)
    time_diff = abs(dt1 - dt2)
    return int(time_diff.total_seconds())

# Main function
if __name__ == "__main__":
    # Input the number of testcases
    num_testcases = int(input().strip())

    # Iterate through testcases
    for _ in range(num_testcases):
        # Input timestamps
        timestamp1 = input().strip()
        timestamp2 = input().strip()

        # Calculate difference in seconds and print
        difference_seconds = time_difference_in_seconds(timestamp1, timestamp2)
        print(difference_seconds)
