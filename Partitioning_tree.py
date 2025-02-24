import numpy as np
from matplotlib import pyplot as plt

"""
@Author: Julie Teerink
@Date: 17.02.25

"""


class Particle:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Cells:
    def __init__(self, particle_list, x_range: tuple, y_range: tuple):
        self.x_min, self.x_max = x_range
        self.y_min, self.y_max = y_range
        self.particle_list = particle_list
        self.children = None

    def partition(self):
        if len(self.particle_list) <= 8:
            print(f"smaller 8: {len(self.particle_list)}")
            return

        else:
            print(f"bigger 8 = {len(self.particle_list)}")
            x_length = self.x_max - self.x_min
            y_length = self.y_max - self.y_min

            if x_length >= y_length:
                partition_coord = self.x_max - x_length/2
                bins = [self.x_min, partition_coord, self.x_max]
                particle_axis = [particle.x for particle in self.particle_list]
                binned_particles_indices = np.digitize(particle_axis, bins)

                left_particles = np.extract(binned_particles_indices == 1, self.particle_list)

                right_particles = np.extract(binned_particles_indices == 2, self.particle_list)

                self.children = [Cells(x_range=(self.x_min, partition_coord), y_range=(self.y_min, self.y_max),
                                       particle_list=left_particles),
                                 Cells(x_range=(partition_coord, self.x_max), y_range=(self.y_min, self.y_max),
                                       particle_list=right_particles)]

            else:
                partition_coord = self.y_max - y_length / 2
                bins = [self.y_min, partition_coord, self.y_max]
                particle_axis = [p.y for p in self.particle_list]
                binned_particles_indices = np.digitize(particle_axis, bins)

                down_particles = np.extract(binned_particles_indices == 1, self.particle_list)

                up_particles = np.extract(binned_particles_indices == 2, self.particle_list)

                self.children = [Cells(x_range=(self.x_min, self.x_max), y_range=(self.y_min, partition_coord),
                                       particle_list=down_particles),
                                 Cells(x_range=(self.x_min, self.x_max), y_range=(partition_coord, self.y_max),
                                       particle_list=up_particles)]

            # Recursively partition children
            for child in self.children:
                child.partition()


    def plot(self, ax):
        ax.plot([self.x_min, self.x_max, self.x_max, self.x_min, self.x_min],
                [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min], 'k-')

        if self.children:
            for child in self.children:
                child.plot(ax)

particles_x = np.random.uniform(0,10, size=500)
particles_y = np.random.uniform(0, 10, size=500)

# making these Particle class instances will be useful later when the particles get more properties
particle_coords = [Particle(x, y) for x, y in zip(particles_x, particles_y)]

test = Cells(particle_coords, (0, 10), (0, 10))
test.partition()

fig, ax = plt.subplots(1,1, figsize=(10, 10))
ax.scatter(particles_x, particles_y, s=3)
test.plot(ax)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
plt.title('Randomly distributed points, partitioned')
plt.show()
#plt.savefig('Partitioning_result_graph.png')


