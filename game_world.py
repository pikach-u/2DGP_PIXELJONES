objects = [[] for _ in range(5)] # 시각적인 관점에서의 월드
collision_pairs = {}

def add_object(o, depth=0):
    objects[depth].append(o)

def add_objects(object_list, depth=0):
    objects[depth] += object_list


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError("Cannot Delete None Existing Object")

def clear():
    for layer in objects:
        layer.clear()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_p()
    left_b, bottom_b, right_b, top_b = b.get_p()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def handle_collisions():
    collided_pairs = []
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    collided_pairs.append((group, a, b))
    for group, a, b in collided_pairs:
        a.handle_collision(group, b)
        b.handle_collision(group, a)
