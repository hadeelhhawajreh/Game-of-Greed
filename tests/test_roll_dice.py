from game_of_greed.game_of_greed import GameLogic

def test_length():
    game_logic = GameLogic()
    actual = len(game_logic.roll_dice(5))
    expected = 5
    assert actual == expected

def test_value():
    game_logic = GameLogic()
    actual= game_logic.roll_dice(5)
    for i in actual:
        assert isinstance(i,int)
        assert 1<= i <=6