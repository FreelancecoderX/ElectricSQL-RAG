import json
from sseclient import SSEClient as EventSource

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
for event in EventSource(url):
    if event.event == 'message':
        try:
            change = json.loads(event.data)
        except ValueError:
            pass
        else:
            # discard canary events
            if change['meta']['domain'] == 'canary':
                continue            
            print('{user} edited {title}'.format(**change))
            # append change to json file
            with  open("data.json", "a") as f:
                json.dump(change, f)