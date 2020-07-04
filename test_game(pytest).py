import pytest
from game import Enemy  # from your created module import class Enemy
from game import Player  # from your created module import class Enemy

markers = [pytest.mark.enemySuite, pytest.mark.playerSuite]


class TestEnemyInit():
    @pytest.mark.enemySuite
    def test_enemy_init(self):
        e = Enemy('orc')
        assert e.name == 'orc'
        assert e.lives == 1

class TestEnemyDamage():
    @pytest.mark.enemySuite
    def test_enemy_takes_damage(self):
        e = Enemy('goblin')
        e.receive_damage(1)
        assert e.lives == 0

class TestPlayerMovement():
    def setup(self):
        self.player = Player('Link')

    @pytest.mark.enemySuite
    def test_move_north(self):
        self.player.reset_position()
        self.player.move_north()
        assert self.player.position_xy == (0, 1)

    @pytest.mark.enemySuite
    def test_move_east(self):
        self.player.reset_position()
        self.player.move_east()
        assert self.player.position_xy == (1, 0)

    @pytest.mark.enemySuite
    def test_pretty_position(self):
        self.player.move_south()
        self.player.move_south()
        self.player.move_west()
        self.player.move_west()
        assert self.player.pretty_position() == "Link went 2 steps south and 2 steps west"


class TestPlayerDamage():
    def setup(self):
        self.player = Player('hero')
        self.enemy = Enemy('wolf')

    @pytest.mark.enemySuite
    @pytest.mark.playerSuite
    def test_player_attack(self):
        self.player.attack_enemy(self.enemy)  # call the method after that =>
        # (if all steps of this sequence work as expected means test passed successfully)
        # game -> return enemy.receive_damage(self.attack) ->
        # -> self.lives=1 - self.attack(damage)=1 => self.lives = 0 -> return self.notify_is_dead() ->
        # -> (if not self.is_alive()) -> return self.lives>0 -> False => True ->
        # return f'{self.name} lost'
        assert self.enemy.lives == 0  # True
        assert self.enemy.is_alive() is False  # False
        assert self.enemy.notify_if_dead() == 'wolf lost!'  # True


