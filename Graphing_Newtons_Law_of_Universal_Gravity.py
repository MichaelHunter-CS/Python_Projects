'''
The relationship between gravitational force and the distance between two bodies
'''

import matplotlib.pyplot as plt

# Drawing the graph
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in Newtons')
    plt.title('Gravitational force and distance')
    plt.show()

def generate_F_r():
    # Generate the values for r
    r = range(100, 1001, 50)
    # Empty the list to store the calculated values of F
    F = []

    # Constant of G
    G = 6.674*(10**-11)
    # Two masses
    m1 = 0.5
    m2 = 1.5

    # Calculate the force and add it to the list, F
    for dist in r:
        force = G*(m1*m2) / (dist**2)
        F.append(force)

    # Call the draw_graph function
    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()