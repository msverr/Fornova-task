import json
from typing import Dict, List, Tuple, Union, Optional, Any


def load_data(file_path: str) -> Any:
    """
    Loads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Any: The data loaded from the file, typically a dictionary or list.
    """

    with open(file_path, "r") as file:
        return json.load(file)


def find_cheapest_room(shown_price: Dict[str, Union[str, float]]) -> Tuple[Optional[str], Optional[float]]:
    """
    Finds the room with the lowest price.

    Args:
        shown_price (dict): A dictionary where keys are room names and values are prices.

    Returns:
        Tuple[Optional[str], Optional[float]]: A tuple containing the name of the cheapest room 
                                                and its price, or None if no rooms are found.
    """

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
    """
    Splits a room name into the room's name and its types.

    Args:
        room_name (str): The full name of the room, including its type(s).

    Returns:
        Tuple[str, List[str]]: A tuple containing the room name and a list of room types.
    """

    rooms_data = room_name.split(" - ")
    room_name = rooms_data[0]
    room_types = []
    for room_type in rooms_data[1:]:
        room_types.extend(room_type.split("/"))

    return room_name.strip(), room_types


def calculate_total_prices(
    shown_price: Dict[str, Union[str, float]], taxes: float
) -> Dict[str, float]:
    """
    Calculates the total price for each room, including taxes.

    Args:
        shown_price (dict): A dictionary where keys are room names and values are prices.
        taxes (float): The tax amount to be added to each room's price.

    Returns:
        Dict[str, float]: A dictionary with room names as keys and their total prices (including taxes) as values.
    """

    total_taxes = sum(float(tax) for tax in taxes.values())
    total_prices = {
        room: round(float(price) + total_taxes, 2)
        for room, price in shown_price.items()
    }
    return total_prices


def generate_room_info(
    total_prices: Dict[str, float]
) -> List[Dict[str, Union[str, List[str], float]]]:
    """
    Formats detailed information about rooms, including their name, types, and total price.

    Args:
        total_prices (dict): A dictionary with room names as keys and their total prices as values.

    Returns:
        List[Dict[str, Union[str, List[str], float]]]: A list of dictionaries containing room details.
    """

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
    """
    Saves the output text and room information to a file.

    Args:
        file_path (str): The path to the file where the data should be saved.
        output_text (str): The text content to be saved in the file.
        room_info (list): A list of dictionaries containing room details.

    Returns:
        None
    """

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
