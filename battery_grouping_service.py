import csv
import json
def get_battery_group(battery):
    if 60 <= battery <= 70:
        return "60-70"
    elif 71 <= battery <= 89:
        return "71-89"
    elif 90 <= battery <= 100:
        return "90-100"
    else:
        return "Others"

def main():
    input_file = "fleet_data.csv"
    output_file = "battery_grouped_vehicles.json"

    # to store vehicles
    grouped_vehicles = {}

    # Read CSV file
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            battery = int(row["battery_level"])
            group = get_battery_group(battery)  # Find battery group

            # If this group does not exist, create a list
            if group not in grouped_vehicles:
                grouped_vehicles[group] = []

            # Add vehicle details to the group
            vehicle = {
                "vehicle_id": row["vehicle_id"],
                "vehicle_type": row["vehicle_type"],
                "model": row["model"],
                "battery_level": battery,
                "status": row["status"]
            }
            grouped_vehicles[group].append(vehicle)
    # Sort  (Descending )
    for group in grouped_vehicles:
        grouped_vehicles[group] = sorted(
            grouped_vehicles[group],
            key=lambda v: v["battery_level"],
            reverse=True
        )
    # Write the grouped data to JSON file
    with open(output_file, "w") as file:
        json.dump(grouped_vehicles, file, indent=4)
    print("Battery grouping completed: ", output_file)

if __name__ == "__main__":
    main()
