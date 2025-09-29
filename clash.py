import random
import time

UNITS = {
    'Knight': {'cost': 3, 'hp': 6, 'damage': 2, 'symbol': 'K', 'target': 'ground'},
    'Archer': {'cost': 2, 'hp': 3, 'damage': 2, 'symbol': 'A', 'target': 'air_ground'},
    'Giant': {'cost': 5, 'hp': 10, 'damage': 4, 'symbol': 'G', 'target': 'building'},
}

LANES = ['left', 'center', 'right']
LANE_TO_COL = {'left': 0, 'center': 1, 'right': 2}
MAP_ROWS = 9  # 0 (player base) to 8 (AI base)

# Tower positions
PLAYER_TOWER_ROW = 0
AI_TOWER_ROW = MAP_ROWS - 1

class Unit:
    def __init__(self, name, lane, is_player):
        self.name = name
        self.lane = lane
        self.is_player = is_player
        self.hp = UNITS[name]['hp']
        self.damage = UNITS[name]['damage']
        # Use uppercase for player, lowercase for AI
        self.symbol = UNITS[name]['symbol'] if is_player else UNITS[name]['symbol'].lower()
        self.target = UNITS[name]['target']
        self.row = PLAYER_TOWER_ROW + 1 if is_player else AI_TOWER_ROW - 1
        self.col = LANE_TO_COL[lane]

    def advance(self):
        self.row += 1 if self.is_player else -1

class Tower:
    def __init__(self, name, hp, row, col, symbol):
        self.name = name
        self.hp = hp
        self.row = row
        self.col = col
        self.symbol = symbol

class Player:
    def __init__(self, is_player=True):
        row = PLAYER_TOWER_ROW if is_player else AI_TOWER_ROW
        self.mana = 5
        self.towers = {
            'left': Tower('Left Tower', 8, row, 0, 'PL' if is_player else 'AL'),
            'right': Tower('Right Tower', 8, row, 2, 'PR' if is_player else 'AR'),
            'king': Tower('King Tower', 15, row, 1, 'PK' if is_player else 'AK')
        }
        self.units = []
        self.is_player = is_player

    def available_units(self):
        return [u for u in UNITS if UNITS[u]['cost'] <= self.mana]

def print_board(player, ai):
    grid = [['   ' for _ in range(3)] for _ in range(MAP_ROWS)]
    # Place towers
    for t in player.towers.values():
        grid[t.row][t.col] = t.symbol
    for t in ai.towers.values():
        grid[t.row][t.col] = t.symbol
    # Place units (show max 2 per cell, stacked)
    unit_grid = [[[] for _ in range(3)] for _ in range(MAP_ROWS)]
    for u in player.units:
        if 0 <= u.row < MAP_ROWS:
            unit_grid[u.row][u.col].append(u.symbol)
    for u in ai.units:
        if 0 <= u.row < MAP_ROWS:
            unit_grid[u.row][u.col].append(u.symbol)
    for r in range(MAP_ROWS):
        for c in range(3):
            if unit_grid[r][c]:
                grid[r][c] = ''.join(unit_grid[r][c])[:2].ljust(3)
    # Print map
    print('\n    +-----+-----+-----+')
    for r in range(MAP_ROWS-1, -1, -1):
        row_str = f"{str(r).rjust(2)} |"
        for c in range(3):
            row_str += f" {grid[r][c]} |"
        print(row_str)
        print('    +-----+-----+-----+')
    print('     L     C     R  (lanes)')
    # Tower HP display
    print(f"\nYour Towers:  L:{player.towers.get('left',Tower('x',0,0,0,'')).hp}  "
          f"K:{player.towers.get('king',Tower('x',0,0,0,'')).hp}  "
          f"R:{player.towers.get('right',Tower('x',0,0,0,'')).hp}")
    print(f"AI Towers:    L:{ai.towers.get('left',Tower('x',0,0,0,'')).hp}  "
          f"K:{ai.towers.get('king',Tower('x',0,0,0,'')).hp}  "
          f"R:{ai.towers.get('right',Tower('x',0,0,0,'')).hp}\n")

def deploy_unit(player, lane, unit_name):
    if unit_name in UNITS and lane in LANES and player.mana >= UNITS[unit_name]['cost']:
        player.units.append(Unit(unit_name, lane, player.is_player))
        player.mana -= UNITS[unit_name]['cost']
        print(f"{'You' if player.is_player else 'AI'} deployed {unit_name} on {lane} lane.")
        return True
    else:
        print("Cannot deploy unit.")
        return False

def process_units(attacker, defender):
    units_to_remove = []
    for unit in list(attacker.units):
        unit.advance()
        # Out of bounds
        if not (0 <= unit.row < MAP_ROWS):
            units_to_remove.append(unit)
            continue
        # Enemy unit at same spot
        enemy_units = [u for u in defender.units if u.row == unit.row and u.col == unit.col]
        if enemy_units:
            enemy = enemy_units[0]
            enemy.hp -= unit.damage
            unit.hp -= enemy.damage
            print(f"{unit.symbol} fights {enemy.symbol} at ({unit.row},{unit.col})!")
            if enemy.hp <= 0:
                defender.units.remove(enemy)
                print(f"{enemy.symbol} defeated!")
            if unit.hp <= 0:
                units_to_remove.append(unit)
                print(f"{unit.symbol} defeated!")
            continue
        # Tower at this position
        for tname, tower in list(defender.towers.items()):
            if tower.row == unit.row and tower.col == unit.col:
                tower.hp -= unit.damage
                print(f"{unit.symbol} attacks {('your' if defender.is_player else 'AI')} {tower.name}!")
                if tower.hp <= 0:
                    print(f"{('Your' if defender.is_player else 'AI')} {tower.name} destroyed!")
                    del defender.towers[tname]
                units_to_remove.append(unit)
                break
    for unit in units_to_remove:
        if unit in attacker.units:
            attacker.units.remove(unit)

def ai_turn(ai, player):
    ai.mana = min(ai.mana + 2, 10)
    choices = ai.available_units()
    if choices and random.random() < 0.7:
        unit = random.choice(choices)
        lane = random.choice(LANES)
        deploy_unit(ai, lane, unit)

def player_turn(player):
    player.mana = min(player.mana + 2, 10)
    while True:
        available = player.available_units()
        if not available:
            print("No units affordable. Skipping turn.")
            return
        print(f"\nYour mana: {player.mana}")
        print("Units you can deploy:")
        for idx, unit in enumerate(available):
            u = UNITS[unit]
            print(f"{idx+1}. {unit} (cost:{u['cost']} HP:{u['hp']} dmg:{u['damage']})")
        print("0. Skip turn")
        try:
            choice = int(input("Choose unit number: "))
            if choice == 0:
                print("You skipped your turn.")
                return
            if 1 <= choice <= len(available):
                unit_name = available[choice-1]
                lane = input("Which lane? (left/center/right): ").strip().lower()
                if lane not in LANES:
                    print("Invalid lane. Try again.")
                    continue
                if deploy_unit(player, lane, unit_name):
                    return
                else:
                    print("Not enough mana or invalid choice. Try again.")
            else:
                print("Invalid choice. Try again.")
        except Exception:
            print("Invalid input. Try again.")

def game_over(player, ai):
    if 'king' not in player.towers or player.towers['king'].hp <= 0:
        print("\nYour king tower has fallen! AI wins!")
        return True
    if 'king' not in ai.towers or ai.towers['king'].hp <= 0:
        print("\nAI king tower has fallen! You win!")
        return True
    return False

def main():
    print("=== Clash Royale: Big Map Edition ===")
    player = Player(is_player=True)
    ai = Player(is_player=False)
    turn = 1
    while True:
        print(f"\n======== Turn {turn} ========")
        print_board(player, ai)
        if game_over(player, ai):
            break
        player_turn(player)
        ai_turn(ai, player)
        process_units(player, ai)
        process_units(ai, player)
        print_board(player, ai)
        if game_over(player, ai):
            break
        turn += 1
        time.sleep(1)

if __name__ == '__main__':
    main()