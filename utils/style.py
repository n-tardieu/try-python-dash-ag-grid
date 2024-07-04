import random

def redToGreenScale(n_bins:int):
    res = []
    length = int(n_bins/2)
    if (length == n_bins/2):
        for i in range(0, length):
            res.append(f'rgb(255, {int(i*255/(length - 1))}, 0)')
        
        for i in range(length - 1, -1, -1):
            res.append(f'rgb({int(i*255/(length - 1))}, 255, 0)')
    
    else:
        for i in range(0, length):
            res.append(f'rgb(255, {int(i*255/(length))}, 0)')
        
        res.append('rgb(255, 255, 0)')

        for i in range(length - 1, -1, -1):
            res.append(f'rgb({int(i*255/(length))}, 255, 0)')

    return res

def greenToRedScale(n_bins:int):
    res = []
    length = int(n_bins/2)
    if (length == n_bins/2):
        for i in range(0, length):
            res.append(f'rgb({int(i*255/(length - 1))}, 255, 0)')
        
        for i in range(length - 1, -1, -1):
            res.append(f'rgb(255, {int(i*255/(length - 1))}, 0)')
    
    else:
        for i in range(0, length):
            res.append(f'rgb({int(i*255/(length))}, 255, 0)')
        
        res.append('rgb(255, 255, 0)')

        for i in range(length - 1, -1, -1):
            res.append(f'rgb(255, {int(i*255/(length))}, 0)')

    return res

def redToBlueScale(n_bins:int):
    res = []
    length = int(n_bins/2)
    if (length == n_bins/2):
        for i in range(0, length):
            res.append(f'rgb(255, 0, {int(i*255/(length - 1))})')
        
        for i in range(length - 1, -1, -1):
            res.append(f'rgb({int(i*255/(length - 1))}, 0, 255)')
    
    else:
        for i in range(0, length):
            res.append(f'rgb(255, 0, {int(i*255/(length))})')
        
        res.append('rgb(255, 0, 255)')

        for i in range(length - 1, -1, -1):
            res.append(f'rgb({int(i*255/(length))}, 0, 255)')

    return res

def blueToRedScale(n_bins:int):
    res = []
    length = int(n_bins/2)
    if (length == n_bins/2):
        for i in range(0, length):
            res.append(f'rgb({int(i*255/(length - 1))}, 0, 255)')
        
        for i in range(length - 1, -1, -1):
            res.append(f'rgb(255, 0, {int(i*255/(length - 1))})')
    
    else:
        for i in range(0, length):
            res.append(f'rgb({int(i*255/(length))}, 0, 255)')
        
        res.append('rgb(255, 0, 255)')

        for i in range(length - 1, -1, -1):
            res.append(f'rgb(255, 0, {int(i*255/(length))})')

    return res

def hex_to_rgb(hex):
  tmp = hex.lstrip('#')
  return 'rgb' + str(tuple(int(tmp[i:i+2], 16) for i in (0, 2, 4)))

def getRandomColor():
    return 'rgb('+ str(random.randint(0, 255)) + ',' + str(random.randint(0, 255)) + ',' + str(random.randint(0, 255)) + ')'

def getRandomColors(uniques:list[str]):
    res = {}
    for data in uniques:
        res[data] = getRandomColor()
    return res
