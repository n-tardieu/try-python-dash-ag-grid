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