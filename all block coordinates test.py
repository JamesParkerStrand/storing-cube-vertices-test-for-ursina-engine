from ursina import *
import numpy as np

app = Ursina()

# initialize a new cube and its vertices
cubemodel = load_model("cube", use_deepcopy=True)

cube_verts = np.asarray(cubemodel.vertices)
###



# this is for storing all coordinates of blocks.
blocks = [[],[],[],[],[]]

# this is for saying what block it is.
blocksref = [[],[],[],[],[]]


#this is initialzing an array storing coordinates like to be able to index the blocks array by a y-axis, then all the x and z coordinates are then just scattered around
for x in range(5):
    for z in range(5):
        for y in range(5):
            blocks[y].append([x,y,z])
            blocksref[y].append(1)

# this is a test removing a single cube
blocksref[0][0] = 0

def displaycubes(blocks, blocksref):
    global cube_verts
    all_verts = np.asarray([])
    for i in range(len(blocks)):
        for j in range(len(blocks[0])):
            # renewing a new cube everytime
            new_cube = np.copy(cube_verts)

            if blocksref[i][j] == 1:

                new_cube[:, 0] += blocks[i][j][0]
                new_cube[:, 1] += blocks[i][j][1]
                new_cube[:, 2] += blocks[i][j][2]
                all_verts = np.append(all_verts, new_cube)

    # make sure all your vertices are wrapped into a shape of vertices that go [0,0,0] after saying all_verts[0]
    all_verts = all_verts.reshape((int(all_verts.shape[0] / 3),3))

    #initializing a mesh class to display the cube world
    mesh = Mesh(vertices=all_verts)

    #now displaying the cube world
    test = Entity(model=mesh)

displaycubes(blocks, blocksref)

EditorCamera()



app.run()
