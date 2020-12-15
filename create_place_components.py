
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Object(object):
    pass

# Initialize script file for eagle
board_placement_file=open('./board_outline.scr','w')


g = Object()
g.bw=2 #in
g.bh=3 #in

g.r=1.5



# To draw a octogon, will turn the equation of a circle into 8 points
# first
num_sides=8
theta=360/num_sides*np.pi/180 # convert 360 to radians
all_points=['LINE 0 ']
xpoints=[]
ypoints=[]

plt.figure(1)
draw_theta=0

theta=np.linspace(0,360,9)*np.pi/180
for draw_theta in theta:

    x=np.round(g.r*np.cos(draw_theta)+g.r,4)
    y=np.round(g.r*np.sin(draw_theta)+g.r,4)
    string_xy=f'({x:.4f}in {y:.4f}in) '
    all_points.append(string_xy)
    xpoints.append(x)
    ypoints.append(y)
    plt.text(x,y,str(draw_theta))

plt.plot(xpoints,ypoints,marker='*',label=str(len(range(0,8))))

script_string=''
for item in all_points:
    script_string=script_string+item

script_string=script_string+';\n'
print(all_points)
board_placement_file.write('LAYER 20;\n')
#board_placement_file.write(f'LINE 0 (0 0) (0 {g.bh}in) ({g.bw}in {g.bh}in) ({g.bw}in 0) (0 0) ;\n')
board_placement_file.write(script_string)

g.hole_x=g.r-.2
g.holy_y=g.r

tap_4_40_free_fit=.1285 # in
tap_4_40_close_fit=.1160 # in

hole_od=0.5*(tap_4_40_close_fit+tap_4_40_free_fit)

hx1=g.r+g.hole_x
hy1=g.r

hx2=g.r
hy2=hx1

hx3=g.r-g.hole_x
hy3=g.r

hx4=g.r
hy4=hx3

hole_string=f'HOLE {hole_od:.6f}in '

holex_mat=[hx1,hx2,hx3,hx4]
holey_mat=[hy1,hy2,hy3,hy4]

for i,val in enumerate(holex_mat):
    x=val
    y=holey_mat[i]

    hole_string=hole_string+f' ({x:.6f}in {y:.6f}in)'

hole_string=hole_string+';\n'
board_placement_file.write(hole_string)
board_placement_file.close()
plt.legend()
plt.show()



