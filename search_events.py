import json

with open('extracted/assets/www/data.js', 'r', encoding='utf-8-sig', errors='ignore') as f:
    raw = f.read()

start = raw.find('[')
end = raw.rfind(']')
data = json.loads(raw[start:end+1])

event_sheets = data[6]
print(f"Total event sheets: {len(event_sheets)}")
for i, es in enumerate(event_sheets):
    name = es[0]
    # count events
    events = es[1]
    print(f"Sheet {i}: {name} ({len(events)} events)")

# Search for events referencing object index 18 (peashooter) or 481 (spread)
def search_obj_in_event(ev, target_idx, path=""):
    found = []
    ev_str = json.dumps(ev)
    # Check if target_idx appears as a number or in parameters
    if f"[{target_idx}," in ev_str or f",{target_idx}," in ev_str or f",{target_idx}]" in ev_str:
        found.append((path, ev))
    return found

print("\nSearching for events referencing object 18 (peashooter_bullet)...")
for es_idx, es in enumerate(event_sheets):
    sheet_name = es[0]
    for ev_idx, ev in enumerate(es[1]):
        matches = search_obj_in_event(ev, 18, f"{sheet_name}[{ev_idx}]")
        if matches:
            print(f"Found in {sheet_name} event {ev_idx}")

print("\nSearching for events referencing object 481 (spread_bullet)...")
for es_idx, es in enumerate(event_sheets):
    sheet_name = es[0]
    for ev_idx, ev in enumerate(es[1]):
        matches = search_obj_in_event(ev, 481, f"{sheet_name}[{ev_idx}]")
        if matches:
            print(f"Found in {sheet_name} event {ev_idx}")
