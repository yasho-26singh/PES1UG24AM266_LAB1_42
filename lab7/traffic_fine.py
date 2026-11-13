"""Parse and validate traffic-ticket inputs."""


def _split_fields(value, separator, message, count=None):
    if not isinstance(value, str):
        raise ValueError(message)
    fields = [field.strip() for field in value.split(separator)]
    if (count is not None and len(fields) != count) or not all(fields):
        raise ValueError(message)
    return fields


def _parse_number(value, minimum, message):
    try:
        number = int(value)
    except ValueError:
        raise ValueError(message) from None
    if number < minimum:
        raise ValueError(message)
    return number


def parse_ticket_id(ticket_id):
    """Return the uppercased prefix, positive year, and nonnegative serial."""
    message = "Expected a ticket ID like TF-2024-0456."
    prefix, year, serial = _split_fields(ticket_id, "-", message, count=3)
    if not prefix.isalpha():
        raise ValueError(message)
    return prefix.upper(), _parse_number(year, 1, message), _parse_number(serial, 0, message)


def total_fines(amounts_csv):
    """Sum comma-separated nonnegative integers and cap the total at 10,000."""
    message = "Enter comma-separated nonnegative whole amounts, such as 500,1200,300."
    amounts = _split_fields(amounts_csv, ",", message)
    return min(sum(_parse_number(amount, 0, message) for amount in amounts), 10000)


def speed_excess(reading):
    """Return the signed percentage over the limit, rounded down."""
    message = "Enter a nonnegative speed and a positive limit, such as 72/60."
    speed_text, limit_text = _split_fields(reading, "/", message, count=2)
    speed = _parse_number(speed_text, 0, message)
    limit = _parse_number(limit_text, 1, message)
    return (speed - limit) * 100 // limit


def main():
    operations = (
        (parse_ticket_id, "Enter a ticket ID (e.g. TF-2024-0456): ",
         "Ticket Prefix, Year and Serial"),
        (total_fines, "Enter fine amounts as CSV (e.g. 500,1200,300): ",
         "Total Fines"),
        (speed_excess, "Enter speed/limit (e.g. 72/60): ", "Percent Over Limit"),
    )
    for operation, prompt, label in operations:
        print(f"\n==== Running {operation.__name__} ====")
        while True:
            try:
                value = input(prompt)
            except EOFError:
                print("\nInput ended.")
                return 1
            try:
                result = operation(value)
            except ValueError as error:
                print(f"Invalid input. {error}")
            else:
                print(f"{label}: {result}")
                break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
