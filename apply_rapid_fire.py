import json
import copy
import os
import shutil

DATA_PATH = 'extracted/assets/www/data.js'
BACKUP_PATH = 'extracted/assets/www/data.js.bak'

# Restore from pristine backup
shutil.copyfile(BACKUP_PATH, DATA_PATH)
print("Restored from backup.")

with open(DATA_PATH, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

project = data['project']
event_sheets = project[6]

peashooter_modified = 0
spread_modified = 0
plane_modified = 0

def check_spawned_obj(acts):
    spawned = set()
    for a in acts:
        # a is [inst_or_obj, act_id, behavior, uid, invert, params]
        if len(a) > 5 and isinstance(a[5], list):
            for p in a[5]:
                if isinstance(p, list) and len(p) == 2 and p[0] == 4: # object parameter
                    spawned.add(p[1])
    return spawned

def modify_event_tree(ev, sheet_name):
    global peashooter_modified, spread_modified, plane_modified
    
    conds = ev[5] if len(ev) > 5 and isinstance(ev[5], list) else []
    acts = ev[6] if len(ev) > 6 and isinstance(ev[6], list) else []
    subs = ev[7] if len(ev) > 7 and isinstance(ev[7], list) else []
    
    # Check if this event has timer condition [-1, 73, ...]
    for c in conds:
        if isinstance(c, list) and len(c) > 1 and c[0] == -1 and c[1] == 73:
            params = c[9]
            spawned = check_spawned_obj(acts)
            
            if 481 in spawned and sheet_name == 'cuphead_actions':
                # Spread
                params[0][1][1] = 0.008 # 12.5x faster
                new_acts = []
                for a in acts:
                    new_acts.append(a)
                for a in acts:
                    new_acts.append(copy.deepcopy(a))
                ev[6] = new_acts
                spread_modified += 1
                
            elif 18 in spawned:
                if sheet_name == 'cuphead_actions':
                    # Peashooter
                    params[0][1][1] = 0.01 # 12x faster
                    new_acts = []
                    for a in acts:
                        new_acts.append(a)
                    for a in acts:
                        new_acts.append(copy.deepcopy(a))
                    ev[6] = new_acts
                    peashooter_modified += 1
                elif sheet_name == 'cuphead_plane_actions':
                    # Plane peashooter
                    params[0][1][1] = 0.012 # 12.5x faster
                    new_acts = []
                    for a in acts:
                        new_acts.append(a)
                    for a in acts:
                        new_acts.append(copy.deepcopy(a))
                    ev[6] = new_acts
                    plane_modified += 1

    for sub in subs:
        modify_event_tree(sub, sheet_name)

for sheet in event_sheets:
    sheet_name = sheet[0]
    if sheet_name in ['cuphead_actions', 'cuphead_plane_actions']:
        for ev in sheet[1]:
            modify_event_tree(ev, sheet_name)

print("Modifications results:")
print(f"  Peashooter events modified: {peashooter_modified}")
print(f"  Spread events modified:     {spread_modified}")
print(f"  Plane events modified:      {plane_modified}")
print(f"  Total events modified:      {peashooter_modified + spread_modified + plane_modified}")

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':'))

print(f"Saved modified {DATA_PATH} ({os.path.getsize(DATA_PATH)} bytes)")
