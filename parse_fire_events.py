import json

with open('cuphead_events_dump.json', 'r', encoding='utf-8') as f:
    dump = json.load(f)

# Inspect Event 27, 28, 29, 30
for ev_num in ['25', '26', '27', '28', '29', '30']:
    if ev_num in dump['events']:
        print(f"\n================ EVENT {ev_num} ================")
        ev = dump['events'][ev_num]
        print("Conditions count:", len(ev[5]))
        for c_idx, cond in enumerate(ev[5]):
            print(f"  Cond {c_idx}: {cond}")
        print("Actions count:", len(ev[6]))
        for a_idx, act in enumerate(ev[6]):
            print(f"  Act {a_idx}: {act}")
        if len(ev) > 7 and ev[7]:
            print(f"Sub-events count: {len(ev[7])}")
            for s_idx, sub in enumerate(ev[7]):
                print(f"  Sub {s_idx} conditions: {sub[5]}")
                print(f"  Sub {s_idx} actions: {sub[6]}")
                if len(sub) > 7 and sub[7]:
                    print(f"  Sub {s_idx} sub-sub-events: {len(sub[7])}")
