from constants import ASTEROID_MIN_RADIUS, VALUE_ASTEROID_KILL_1, VALUE_ASTEROID_KILL_2, VALUE_ASTEROID_KILL_3; VALUE_ASTEROID_KILL_2; VALUE_ASTEROID_KILL_3

def calc_points_from_kill(asteroid:"Asteroid")->int:
    kind = asteroid.radius // ASTEROID_MIN_RADIUS
    if kind == 1:
        return VALUE_ASTEROID_KILL_1
    elif kind == 2:
        return VALUE_ASTEROID_KILL_2
    else:
        return VALUE_ASTEROID_KILL_3
