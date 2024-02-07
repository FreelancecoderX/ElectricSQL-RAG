import json
from sseclient import SSEClient as EventSource
from typing import Any, Dict


class EventProcessor:
    def __init__(self, url: str):
        """
        Initialize the class with the given URL.

        Parameters:
            url (str): The URL to be assigned to the instance variable.

        Returns:
            None
        """
        self.url = url

    def process_events(self) -> None:
        """Process events from the URL."""
        for event in EventSource(self.url):
            self.process_event(event)

    def process_event(self, event: Any) -> None:
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
        self.append_change_to_file(change)

    def append_change_to_file(self, change: Dict) -> None:
        """Appends a change to the 'changes.json' file.

        Args:
            change (Dict): The change to be appended to the file.

        Returns:
            None
        """
        with open("output.json", "a") as f:
            json.dump(change, f)
            f.write(",\n")


if __name__ == "__main__":
    url = "https://stream.wikimedia.org/v2/stream/recentchange?format=json&limit=100"
    processor = EventProcessor(url)
    processor.process_events()
