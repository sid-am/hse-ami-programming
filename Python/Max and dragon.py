spells_num = int(input())
mana_dict = dict()
min_mana = 101
for _ in range(spells_num):
    mana, dmg = map(int, input().split())
    min_mana = min(min_mana, mana)
    mana_dict[mana] = max(mana_dict.get(mana, 0), dmg)

dp = [0] * min_mana
hp = int(input())
mana_needed = min_mana
isAlive = True
while isAlive:
    dmg = 0
    for mana in mana_dict:
        if mana_needed >= mana:
            dmg = max(dmg, dp[mana_needed - mana] + mana_dict[mana])
            if dmg >= hp:
                print(mana_needed)
                isAlive = False
                break
    dp.append(dmg)
    mana_needed += 1
