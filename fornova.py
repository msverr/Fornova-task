import json
from typing import Dict, List, Tuple, Union


def load_data(file_path: str) -> json:
    """Loading data from a JSON file."""

    with open(file_path, "r") as file:
        return json.load(file)


def find_cheapest_room(shown_price: Dict[str, Union[str, float]]) -> Tuple[str, float]:
    """Finding a room with the lowest price."""

    if not shown_price:
        return None, None

    cheapest_price = float("inf")
    cheapest_room = None

    for room, price in shown_price.items():
        price = float(price)
        if price < cheapest_price:
            cheapest_price = price
            cheapest_room = room

    return cheapest_room, cheapest_price


def parse_room_details(room_name: str) -> Tuple[str, List[str]]:
    """Splitting a room info into a room name and a room type."""

    rooms_data = room_name.split(" - ")
    room_name = rooms_data[0]
    room_types = []
    for room_type in rooms_data[1:]:
        room_types.extend(room_type.split("/"))

    return room_name.strip(), room_types


def calculate_total_prices(
    shown_price: Dict[str, Union[str, float]], taxes: float
) -> Dict[str, float]:
    """Calculating the total price for each room."""

    total_taxes = sum(float(tax) for tax in taxes.values())
    total_prices = {
        room: round(float(price) + total_taxes, 2)
        for room, price in shown_price.items()
    }
    return total_prices


def generate_room_info(
    total_prices: Dict[str, float]
) -> List[Dict[str, Union[str, List[str], float]]]:
    """Formatting information about rooms"""

    room_info = []

    for room, total_price in total_prices.items():
        room_name, room_types = parse_room_details(room)
        room_info.append(
            {
                "room_name": room_name,
                "room_types": room_types,
                "total_room_price": total_price,
            }
        )

    return room_info


def save_output(
    file_path: str,
    output_text: str,
    room_info: List[Dict[str, Union[str, List[str], float]]],
) -> None:
    """Saving result in a file"""

    with open(file_path, "w") as file:
        file.write(output_text)
        file.write("\n")
        json.dump(room_info, file, indent=4)


def main() -> None:
    data = load_data("Python-task.json")

    hotel = data["assignment_results"][0]

    cheapest_room, cheapest_price = find_cheapest_room(hotel["shown_price"])

    room_name, room_types = parse_room_details(cheapest_room)

    number_of_guests = hotel.get("number_of_guests", 0)

    output = (
        f"Cheapest room: {cheapest_room}\n"
        f"Price: {cheapest_price}\n"
        f"Room Name: {room_name}\n"
        f"Room Types: {room_types}\n"
        f"Number of Guests: {number_of_guests}\n"
    )

    taxes = json.loads(hotel.get("ext_data", {}).get("taxes", "[]"))
    total_prices = calculate_total_prices(hotel["shown_price"], taxes)
    room_info = generate_room_info(total_prices)

    output += "All rooms:"

    save_output("solution.txt", output, room_info)


if __name__ == "__main__":
    main()
