import hashlib
import math
import pyblake2
import json

jackpot_fraction = 0.02
jackpot_probability = 0.1

target_block = b'2104518'
block_hash = b'000000000000000eb4e1776b5ee79fbaab9cb296540266ee42c169ef56f3f075'
secret = b'e92ee2f186b7b2cf7755d42023a329ba'

prizes = [
        {'prize_id': b'0', 'amount': 800000.0},
        {'prize_id': b'1', 'amount': 1250.0},
        {'prize_id': b'2', 'amount': 150.0}
        ]

# the staked amounts are the integer number of RLB cents before applying multipliers
file1 = open("lottery_entries.json", "r",  encoding="utf-8") 
ugly_stakes = file1.read()
stakes = json.loads(ugly_stakes)

print('seed_hash for 1st stake:', hashlib.md5(b'seed123').hexdigest())
print('seed_hash for 2nd stake:', hashlib.md5(b'').hexdigest())
print('secret_hash:', pyblake2.blake2b(secret, digest_size=32).digest().hex())


def bytes_to_uniform_number(xs: bytes) -> float:
    hash = pyblake2.blake2b(xs, digest_size=32).digest()
    return int.from_bytes(hash[:8], byteorder='little', signed=False) / float(2**64 - 1)


jackpot_outcome = bytes_to_uniform_number(secret + block_hash)
prizes[0]['amount'] = math.floor(100.0 * prizes[0]['amount'] * min(1.0, jackpot_fraction * jackpot_probability / jackpot_outcome)) / 100.0
print('Jackpot amount:', prizes[0]['amount'])
jackpot_won = jackpot_outcome < jackpot_probability
print('Jackpot won:', jackpot_won)
if not jackpot_won:
    prizes.pop(0)

for stake in stakes:
    stake['staked'] = round(100.0 * (stake['staked'] / 100.0))

stakes.sort(key=lambda x: (x['seed'], x['user_id']))
for prize in prizes:
    if len(stakes) == 0:
        break
    total_staked = sum([x['staked'] for x in stakes])
    outcome = bytes_to_uniform_number(secret + block_hash + prize['prize_id'])
    outcome_stake = math.floor(outcome * total_staked)
    current_stake = 0
    for (i, stake) in enumerate(stakes):
        current_stake += stake['staked']
        if outcome_stake < current_stake:
            print(f"User {stake['user_id']} (is_team: {stake['team_users'] > 0}) won prize id {prize['prize_id'].decode('ascii')} for ${prize['amount']}")
            stakes[i]['team_users'] -= 5
            if stakes[i]['team_users'] < 1:
                stakes.pop(i)
            break