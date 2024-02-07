# Event Streams

## EventProcessor Class

The `EventProcessor` class is responsible for processing events from a given URL and appending changes to a JSON file if valid. It contains the following methods:

## Methods

### \_\_init\_\_

Initialize the class with the given URL.

#### Parameters
- `url` (str): The URL to be assigned to the instance variable.

#### Returns
- None

### process_events

Process events from the URL.

#### Returns
- None

### process_event

Process a single SSE event and append change to a JSON file if valid.

#### Args
- `event` (Any): The event data.

#### Returns
- None

### append_change_to_file

Appends a change to the 'changes.json' file.

#### Args
- `change` (Dict): The change to be appended to the file.

#### Returns
- None

## Running the Script with Makefile

To run the script, use the following command:

```bash
make run
```
To clean up the build and distribution directories, use the following command:

```bash
make clean
```
