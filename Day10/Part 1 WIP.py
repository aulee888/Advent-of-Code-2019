map = '.#..#\
.....\
#####\
....#\
...##'

map_list = [[map[i * 5 + j] for j in range(5)] for i in range(5)]

class Asteroid:
    def __init__(self, x, y, map_list: list):
        self.coor = (x, y)
        self.scan = 0
        self.locations = {}
        self.locations[self.coor] = 'o'

    def search(self):
        for i in range(len(map_list)):

            for j in range(len(map_list)):
                if map_list[i][j] == '#' and (i, j) != self.coor:
                    x_dir = i - self.coor[0]
                    y_dir = j - self.coor[1]

                    if lcd(x_dir, y_dir) not in self.locations:
                        self.locations[lcd(x_dir, y_dir)] = '*'
                        self.scan += 1

def gcf(a, b):
    if b == 0:
        return a
        
    return gcf(b, a % b)

def lcd(a, b):
    div = gcf(a, b)

    return a/div, b/div  # Incorrect negative sorting affected by this line

def test(map_list):
    asteroids = []
    for x in range(len(map_list)):

        for y in range(len(map_list)):

            if map_list[x][y] == '#':
                asteroids.append(Asteroid(x, y, map_list))
                asteroids[-1].search()
                print(asteroids[-1].scan)

#test(map_list)

# Stuck with this problem, not correctly sorting between negatives
print(lcd(-1, 0))
print(lcd(1, 0))
print(lcd(0, -1))
print(lcd(0, 1))
