objects = [[] for _ in range(5)] # 시각적인 관점에서의 월드

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