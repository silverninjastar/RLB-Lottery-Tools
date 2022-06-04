import hashlib
import math
import pyblake2
import json
import numpy as np

jackpot_fraction = 0.02
jackpot_probability = 0.1

vals = open("vals.json", "r", encoding="utf-8")
winnings = vals.read()
clean_winnings = json.loads(winnings)

jackpot = clean_winnings['jackpot']
total = clean_winnings['lottery']

with open("ratio.txt") as file_name:
    ratio = np.loadtxt(file_name, delimiter="\n")

target_block = b'2104518'
block_hash = b'000000000000000eb4e1776b5ee79fbaab9cb296540266ee42c169ef56f3f075'
secret = b'e92ee2f186b7b2cf7755d42023a329ba'

ratio = np.insert(ratio, 0, 0)

prizes = [
        {'prize_id': b'0', 'amount': jackpot},
        {'prize_id': b'1', 'amount': ratio[1] * total},
        {'prize_id': b'2', 'amount': ratio[2] * total},
        {'prize_id': b'3', 'amount': ratio[3] * total},
        {'prize_id': b'4', 'amount': ratio[4] * total},
        {'prize_id': b'5', 'amount': ratio[5] * total},
        {'prize_id': b'6', 'amount': ratio[6] * total},
        {'prize_id': b'7', 'amount': ratio[7] * total},
        {'prize_id': b'8', 'amount': ratio[8] * total},
        {'prize_id': b'9', 'amount': ratio[9] * total},
        {'prize_id': b'10', 'amount': ratio[10] * total},
        {'prize_id': b'11', 'amount': ratio[11] * total},
        {'prize_id': b'12', 'amount': ratio[12] * total},
        {'prize_id': b'13', 'amount': ratio[13] * total},
        {'prize_id': b'14', 'amount': ratio[14] * total},
        {'prize_id': b'15', 'amount': ratio[15] * total},
        {'prize_id': b'16', 'amount': ratio[16] * total},
        {'prize_id': b'17', 'amount': ratio[17] * total},
        {'prize_id': b'18', 'amount': ratio[18] * total},
        {'prize_id': b'19', 'amount': ratio[19] * total},
        {'prize_id': b'20', 'amount': ratio[20] * total},
        {'prize_id': b'21', 'amount': ratio[21] * total},
        {'prize_id': b'22', 'amount': ratio[22] * total},
        {'prize_id': b'23', 'amount': ratio[23] * total},
        {'prize_id': b'24', 'amount': ratio[24] * total},
        {'prize_id': b'25', 'amount': ratio[25] * total},
        {'prize_id': b'26', 'amount': ratio[26] * total},
        {'prize_id': b'27', 'amount': ratio[27] * total},
        {'prize_id': b'28', 'amount': ratio[28] * total},
        {'prize_id': b'29', 'amount': ratio[29] * total},
        {'prize_id': b'30', 'amount': ratio[30] * total},
        {'prize_id': b'31', 'amount': ratio[31] * total},
        {'prize_id': b'32', 'amount': ratio[32] * total},
        {'prize_id': b'33', 'amount': ratio[33] * total},
        {'prize_id': b'34', 'amount': ratio[34] * total},
        {'prize_id': b'35', 'amount': ratio[35] * total},
        {'prize_id': b'36', 'amount': ratio[36] * total},
        {'prize_id': b'37', 'amount': ratio[37] * total},
        {'prize_id': b'38', 'amount': ratio[38] * total},
        {'prize_id': b'39', 'amount': ratio[39] * total},
        {'prize_id': b'40', 'amount': ratio[40] * total},
        {'prize_id': b'41', 'amount': ratio[41] * total},
        {'prize_id': b'42', 'amount': ratio[42] * total},
        {'prize_id': b'43', 'amount': ratio[43] * total},
        {'prize_id': b'44', 'amount': ratio[44] * total},
        {'prize_id': b'45', 'amount': ratio[45] * total},
        {'prize_id': b'46', 'amount': ratio[46] * total},
        {'prize_id': b'47', 'amount': ratio[47] * total},
        {'prize_id': b'48', 'amount': ratio[48] * total},
        {'prize_id': b'49', 'amount': ratio[49] * total},
        {'prize_id': b'50', 'amount': ratio[50] * total},
        {'prize_id': b'51', 'amount': ratio[51] * total},
        {'prize_id': b'52', 'amount': ratio[52] * total},
        {'prize_id': b'53', 'amount': ratio[53] * total},
        {'prize_id': b'54', 'amount': ratio[54] * total},
        {'prize_id': b'55', 'amount': ratio[55] * total},
        {'prize_id': b'56', 'amount': ratio[56] * total},
        {'prize_id': b'57', 'amount': ratio[57] * total},
        {'prize_id': b'58', 'amount': ratio[58] * total},
        {'prize_id': b'59', 'amount': ratio[59] * total},
        {'prize_id': b'60', 'amount': ratio[60] * total},
        {'prize_id': b'61', 'amount': ratio[61] * total},
        {'prize_id': b'62', 'amount': ratio[62] * total},
        {'prize_id': b'63', 'amount': ratio[63] * total},
        {'prize_id': b'64', 'amount': ratio[64] * total},
        {'prize_id': b'65', 'amount': ratio[65] * total},
        {'prize_id': b'66', 'amount': ratio[66] * total},
        {'prize_id': b'67', 'amount': ratio[67] * total},
        {'prize_id': b'68', 'amount': ratio[68] * total},
        {'prize_id': b'69', 'amount': ratio[69] * total},
        {'prize_id': b'70', 'amount': ratio[70] * total},
        {'prize_id': b'71', 'amount': ratio[71] * total},
        {'prize_id': b'72', 'amount': ratio[72] * total},
        {'prize_id': b'73', 'amount': ratio[73] * total},
        {'prize_id': b'74', 'amount': ratio[74] * total},
        {'prize_id': b'75', 'amount': ratio[75] * total},
        {'prize_id': b'76', 'amount': ratio[76] * total},
        {'prize_id': b'77', 'amount': ratio[77] * total},
        {'prize_id': b'78', 'amount': ratio[78] * total},
        {'prize_id': b'79', 'amount': ratio[79] * total},
        {'prize_id': b'80', 'amount': ratio[80] * total},
        {'prize_id': b'81', 'amount': ratio[81] * total},
        {'prize_id': b'82', 'amount': ratio[82] * total},
        {'prize_id': b'83', 'amount': ratio[83] * total},
        {'prize_id': b'84', 'amount': ratio[84] * total},
        {'prize_id': b'85', 'amount': ratio[85] * total},
        {'prize_id': b'86', 'amount': ratio[86] * total},
        {'prize_id': b'87', 'amount': ratio[87] * total},
        {'prize_id': b'88', 'amount': ratio[88] * total},
        {'prize_id': b'89', 'amount': ratio[89] * total},
        {'prize_id': b'90', 'amount': ratio[90] * total},
        {'prize_id': b'91', 'amount': ratio[91] * total},
        {'prize_id': b'92', 'amount': ratio[92] * total},
        {'prize_id': b'93', 'amount': ratio[93] * total},
        {'prize_id': b'94', 'amount': ratio[94] * total},
        {'prize_id': b'95', 'amount': ratio[95] * total},
        {'prize_id': b'96', 'amount': ratio[96] * total},
        {'prize_id': b'97', 'amount': ratio[97] * total},
        {'prize_id': b'98', 'amount': ratio[98] * total},
        {'prize_id': b'99', 'amount': ratio[99] * total},
        {'prize_id': b'100', 'amount': ratio[100] * total}
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