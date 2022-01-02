from typing import NewType


def p1():
    input = open('input.txt', 'r')

    count = 0
    filelength = 0
    depth = int(input.readline().strip())
    filelength += 1
    print('first', depth)
    for line in input.readlines():
        depth_new = int(line.strip())
        if depth_new > depth:
            count += 1
        depth = depth_new
        print('depth', depth)
        filelength += 1

    print('increases', count)
    print('file length', )


def p1_2():
  input = open('input.txt', 'r')

  count = 0
  lines = input.readlines()
  lines = list(map(lambda x: x.strip(), lines))
  line_position = 0
  while True:
    print(lines[line_position])
    second_line_position = line_position + 1
    sum1 = 0
    for x in range(3):
      # print('x', x)
      sum1 += int(lines[line_position + x])
    print('sum1', sum1)

    sum2 = 0
    for x in range(3):
      sum2+=int(lines[second_line_position + x])
    print('sum2', sum2)
    
    if sum2 > sum1:
      count += 1
    line_position += 1
    # if line_position >= len(lines):
      # break
    if line_position + 3 >= len(lines):
      break
  print('increases', count)

def p2():
  input = open('input2.txt', 'r')
  lines = input.readlines()
  lines = list(map(lambda x: x.strip(), lines))
  depth = 0
  position = 0

  # print(lines)
  for line in lines:
    line_split = line.split()
    input_type = line_split[0]
    input_val = int(line_split[1])
    if input_type == 'forward':
      position+=input_val
    elif input_type == 'up':
      depth-=input_val
    elif input_type == 'down':
      depth+=input_val
    
    print(depth, position)
  print('final multiply', depth * position)

def p2_2():
  input = open('input2.txt', 'r')
  lines = input.readlines()
  lines = list(map(lambda x: x.strip(), lines))
  depth = 0
  position = 0
  aim = 0
  # print(lines)
  for line in lines:
    line_split = line.split()
    input_type = line_split[0]
    input_val = int(line_split[1])
    if input_type == 'forward':
      position += input_val
      depth += aim * input_val
    elif input_type == 'up':
      # depth-=input_val
      aim-=input_val
    elif input_type == 'down':
      # depth+=input_val
      aim+=input_val
    
    print(depth, position)
  print('final multiply', depth * position)

def p3():
  input = open('input3.txt', 'r')
  lines = input.readlines()
  
  print(lines)

##########
# p1()
# p1_2()
# p2()
# p2_2()
p3()