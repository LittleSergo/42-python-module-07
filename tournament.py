from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    opponent_1 = opponents[0][0].create_base()
    strategy_1 = opponents[0][1]
    opponent_2 = opponents[1][0].create_base()
    strategy_2 = opponents[1][1]
    print(f"* Battle *\n{opponent_1}\n vs.\n{opponent_2}\n now fight!")
    strategy_1.act(opponent_1)
    strategy_2.act(opponent_2)
    return None


def tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    oppon_num = len(opponents)
    print(f"*** Tournament ***\n{oppon_num} opponents involved")
    if oppon_num < 2:
        print("Not enough participants to compete!")
        return None
    try:
        for i in range(oppon_num):
            for j in range(i + 1, oppon_num):
                print()
                battle([opponents[i], opponents[j]])
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    transform_f = TransformCreatureFactory()
    norm_s = NormalStrategy()
    def_s = DefensiveStrategy()
    aggres_s = AggressiveStrategy()
    print("Tournament 0 (basic)\n [ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([(flame_f, norm_s), (heal_f, def_s)])
    print(
        "\nTournament 1 (error)\n"
        "[ (Flameling+Aggressive), (Healing+Defensive) ]"
    )
    tournament([(flame_f, aggres_s), (heal_f, def_s)])
    print(
        "\nTournament 2 (multiple)\n "
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )
    tournament([(aqua_f, norm_s), (heal_f, def_s), (transform_f, aggres_s)])
