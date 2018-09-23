from stravalib import Client
import csv

client_id = '28806'
my_token = '5c7df309f008acb19be6df0f6dfba59d4b58804f'

client = Client(access_token=my_token)

activities = client.get_activities(limit=100)
rides = list(activities)

with open("activities.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    for ride in rides:
        date = str(ride.start_date_local)[:10]
        distance = str(ride.distance)[:-5]
        average_speed = str(ride.average_speed)
        kudos_count = str(ride.kudos_count)
        csv_writer.writerow([date, distance, average_speed, kudos_count])

# activity = client.get_activity(1801822008)

# print(activity.distance)
# print(activity.moving_time)
# print(activity.average_speed)
# print(activity.total_elevation_gain)