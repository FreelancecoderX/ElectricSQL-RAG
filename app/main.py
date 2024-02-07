import json
from sseclient import SSEClient as EventSource
from typing import Any, Dict


def process_event(event: Any) -> None:
    """Process a single SSE event and append change to a JSON file if valid.

    Args:
        event (Any): The event data.

    Returns:
        None
    """
    if event.event != "message":
        return

    try:
        change = json.loads(event.data)
    except json.JSONDecodeError:
        return

    meta_domain = change.get("meta", {}).get("domain")
    if meta_domain == "canary":
        return

    print(f"{change['user']} edited {change['title']}")
    append_change_to_file(change)


def append_change_to_file(change: Dict) -> None:
    """Appends a change to the 'changes.json' file.

    Args:
    change (Dict): The change to be appended to the file.

    Returns:
    None
    """
    with open("output.json", "a") as f:
        json.dump(change, f)
        f.write(",\n")


def main(url: str) -> None:
    """
    Function to process events from the given URL.

    Parameters:
    url (str): The URL to fetch events from.
    """
    for event in EventSource(url):
        process_event(event)


if __name__ == "__main__":
    url = "https://stream.wikimedia.org/v2/stream/recentchange?format=json&limit=100"
    main(url)
