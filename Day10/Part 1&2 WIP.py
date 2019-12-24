import math

map1 = '.#..#\
.....\
#####\
....#\
...##'

map2 = '......#.#.\
#..#.#....\
..#######.\
.#.#.###..\
.#..#.....\
..#....#.#\
#..#....#.\
.##.#..###\
##...#..#.\
.#....####'

map3 = '#.#...#.#.\
.###....#.\
.#....#...\
##.#.#.#.#\
....#.#.#.\
.##..###.#\
..#...##..\
..##....##\
......#...\
.####.###.'

map4 = '.#..#..###\
####.###.#\
....###.#.\
..###.##.#\
##.##.#.#.\
....###..#\
..#.#..#.#\
#..#.#.###\
.##...##.#\
.....#.#..'

map5 = '.#..##.###...#######\
##.############..##.\
.#.######.########.#\
.###.#######.####.#.\
#####.##.#.##.###.##\
..#####..#.#########\
####################\
#.####....###.#.#.##\
##.#################\
#####.##.###..####..\
..######..##.#######\
####.##.####...##..#\
.#####..#.######.###\
##...#.##########...\
#.##########.#######\
.####.#.###.###.#.##\
....##.##.###..#####\
.#.#.###########.###\
#.#.#.#####.####.###\
###.##.####.##.#..##'

map6 = '...###.#########.####\
.######.###.###.##...\
####.########.#####.#\
########.####.##.###.\
####..#.####.#.#.##..\
#.################.##\
..######.##.##.#####.\
#.####.#####.###.#.##\
#####.#########.#####\
#####.##..##..#.#####\
##.######....########\
.#######.#.#########.\
.#.##.#.#.#.##.###.##\
######...####.#.#.###\
###############.#.###\
#.#####.##..###.##.#.\
##..##..###.#.#######\
#..#..########.#.##..\
#.#.######.##.##...##\
.#.##.#####.#..#####.\
#.#.##########..#.##.'

class Asteroid:
    def __init__(self, x, y, map_list: list):
        self.coor = (x, y)
        self.scan = 0
        self.detected = {}
        self.vaped = {}
        self.map_list = map_list

    def search(self):
        for j in range(len(self.map_list)):

            for i in range(len(self.map_list)):
                if self.map_list[j][i] == '#' and (i, j) != self.coor and (i, j) not in self.vaped:
                    #x_dir = i - self.coor[0]
                    #y_dir = j - self.coor[1]
                    x_dir = self.coor[0] - i
                    y_dir = self.coor[1] - j

                    # Keys are directions, values are locations
                    # Account for asteroids in order of closeness to location
                    if lcd(x_dir, y_dir) not in self.detected:
                        self.detected[lcd(x_dir, y_dir)] = (i, j)
                        self.scan += 1
                        
                    else:
                        curr = self.detected[lcd(x_dir, y_dir)]
                        #curr_dist = curr[0] + curr[1] - (self.coor[0] + self.coor[1])
                        curr_dist = dist(curr[0], curr[1], self.coor[0], self.coor[1])
                        
                        if dist(i, j, self.coor[0], self.coor[1]) < curr_dist:
                            self.detected[lcd(x_dir, y_dir)] = (i, j)

def map_gen(map):
    length = int(math.sqrt(len(map)))
    map_list = [[map[i * length + j] for j in range(length)] for i in range(length)]

    return map_list

def dist(x0, y0, x1, y1):
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

def gcf(a, b):
    if b == 0:
        return a
        
    return gcf(b, a % b)

def lcd(a, b):
    div = abs(gcf(a, b))  # Abs to avoid a negative / negative for positive

    return int(a/div), int(b/div) 

def best_most(map):
    map_list = map_gen(map)
    asteroids = []
    most_scanned = 0

    for y in range(len(map_list)):

        for x in range(len(map_list)):

            if map_list[y][x] == '#':
                asteroids.append(Asteroid(x, y, map_list))
                asteroids[-1].search()

                if asteroids[-1].scan > most_scanned:
                    most_scanned = asteroids[-1].scan
                    monitor = asteroids[-1]

    #for item in monitor.detected.values():
    #    print(item)

    print(monitor.coor)
    print(most_scanned)
    print('')

    return monitor

# To rotate clockwise, start with highest slope
# Therefore use large y and decrease in y
# Then increase x, and start with large y again
# Maybe use monitor location as new reference of (0, 0)
# Be weary of counting/including relative zero position coordinates
def vaporize(map):
    monitor = best_most(map)
    count = 0
    ast_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100, 199, 200, 201, 299]

    while monitor.detected != {}:
        angle = 359

        for item in monitor.detected:
            try:
                curr_angle = math.degrees(math.atan(item[1]/item[0]))
            except ZeroDivisionError:  # Accounts for 0 in x
                curr_angle = 0

            if curr_angle < angle:
                angle = curr_angle
                remove = item

        count += 1

        if count in ast_list:
            print('{} : {}'.format(count, monitor.detected[remove]))
            print(angle)
        del monitor.detected[remove]
    '''
    while count < 201:  # Change here
        #for item in monitor.detected.values():
        #    print(item)
        #print('')
        
        # Q1
        for i in range(monitor.coor[0], len(monitor.map_list)):

            # Begins at 0, top is 0, bottom is a higher number
            for j in range(0, monitor.coor[1]):
                print((i, j))
                x_dir = i - monitor.coor[0]
                y_dir = j - monitor.coor[1]

                if (i, j) in monitor.detected.values():
                    count += 1
                    monitor.vaped[(i, j)] = '*'
                    del monitor.detected[lcd(x_dir, y_dir)]

                    if count in ast_list:
                        print('{} : {}'.format(count, (i, j)))

        # Q2
        for j in range(monitor.coor[1], len(monitor.map_list)):
            
            # End of x-axis and back to monitor
            for i in range(len(monitor.map_list) - 1, monitor.coor[0], -1):
                x_dir = i - monitor.coor[0]
                y_dir = j - monitor.coor[1]

                if (i, j) in monitor.detected.values():
                    count += 1
                    monitor.vaped[(i, j)] = '*'
                    del monitor.detected[lcd(x_dir, y_dir)]

                    if count in ast_list:
                        print('{} : {}'.format(count, (i, j)))

        # Q3
        for i in range(monitor.coor[0], 0, -1):

            for j in range(len(monitor.map_list) - 1, monitor.coor[1], -1):
                x_dir = i - monitor.coor[0]
                y_dir = j - monitor.coor[1]

                if (i, j) in monitor.detected.values():
                    count += 1
                    monitor.vaped[(i, j)] = '*'
                    del monitor.detected[lcd(x_dir, y_dir)]

                    if count in ast_list:
                        print('{} : {}'.format(count, (i, j)))

        # Q4
        for j in range(monitor.coor[1], 0, -1):

            for i in range(0, monitor.coor[0]):
                x_dir = i - monitor.coor[0]
                y_dir = j - monitor.coor[1]

                if (i, j) in monitor.detected.values():
                    count += 1
                    monitor.vaped[(i, j)] = '*'
                    del monitor.detected[lcd(x_dir, y_dir)]

                    if count in ast_list:
                        print('{} : {}'.format(count, (i, j)))

        monitor.search()
        '''

vaporize(map5)
