import json

with open('bullet_timers.json', 'r') as f:
    timers = json.load(f)

spread_timers = [t for t in timers if t['timer_val'] == 0.1 and t['sheet'] == 'cuphead_actions']
print(f"Total 0.1s timers in cuphead_actions in bullet_timers.json: {len(spread_timers)}")

for idx, t in enumerate(spread_timers):
    acts_str = json.dumps(t['acts'])
    has_481 = '481' in acts_str
    print(f"[{idx+1}] Path: {t['path']} | has_481: {has_481} | acts len: {len(t['acts'])}")
