from collections import namedtuple
from itertools import permutations
import random

dimension = namedtuple("Dimension", "length width")

def sort_by_decreasing_area(boxes):
    return sorted(boxes, key=lambda dim: dim.length * dim.width, reverse=True)

def can_stack(box1, box2):
    if box1.length < box2.length and box1.width < box2.width:
        return True
    elif box1.length < box2.width and box1.width < box2.length:
        return True

def box_stack_max_height(dimensions):
    out = []
    boxes = sort_by_decreasing_area(dimensions)
    num_boxes = len(boxes)
    H = [1 for rotation in boxes]
    R = [idx for idx in range(num_boxes)]
    for i in range(1, num_boxes):
        for j in range(0, i):
            if can_stack(boxes[i], boxes[j]):
                stacked_height = H[j] + 1
                if stacked_height > H[i]:
                    H[i] = stacked_height
                    R[i] = j
    max_height = max(H)
    start_index = H.index(max_height)
    while True:
        out.append(boxes[start_index])
        next_index = R[start_index]
        if next_index == start_index:
            break
        start_index = next_index
    print('Total of {0} boxes.'.format(len(out)))
    return out

def run():
    dims = []
    choice = input("Select input type('t' for text, 'm' for manual):")
    if choice == 't':
        loc = input("Enter location(just enter name if file is in the same location):")
        try: 
            sizes = open(loc,"r").read().split(' ')
            for size in sizes:
                try:
                    lw = size.split(',')
                    dims.append(dimension(float(lw[0]), float(lw[1])))
                except:
                    print("Wrong value type -> {0}".format(lw))
            return box_stack_max_height(dims)
        except:
            print("File access error.")
    elif choice == 'm':
        check = True
        print("Enter box dimensions with comma between numbers, enter 'f' to finish.")
        while check == True:
            inp = input("Enter box dimensions:")
            if inp == 'f':
                check = False
            else:
                try:
                    lw = inp.split(',')
                    dims.append(dimension(float(lw[0]), float(lw[1])))
                except:
                    print("Wrong value type.") 
        return box_stack_max_height(dims)
    else:
        print("Wrong selection type.")

def run_(inp,rcount = 0):
    dims = []
    if rcount == 0:
        try:
            lw = inp.split(',')
            dims.append(dimension(float(lw[0]), float(lw[1])))
        except:
            return "Wrong input."
        return box_stack_max_height(dims)
    else:
        for x in range(0,rcount):
            dims.append(dimension(random.randint(1,100), random.randint(1,100)))
        return box_stack_max_height(dims)

if __name__ == "__main__":
    o = run()
    try:
        for out in o:
            x,y = out
            print('({0:g},{1:g})'.format(x,y))
    except:
        pass
    k=input("Press any key to exit.")
