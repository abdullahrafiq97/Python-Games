import colorgram
colors = colorgram.extract('Spot Painting.jpg', 30)
all = []
for color in colors:
    r =  color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    t = (r, g, b)
    all.append(t)
print(all)