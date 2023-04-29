from scipy.spatial import ConvexHull
import numpy as np



# Example input
our_planets = np.array([[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]])
zombie_planets = np.array([[2,2,2], [2,3,2], [3,2,2], [3,3,2], [3,2,3], [3,3,3]])

# Calculate convex hull and volume for each set of planets
our_hull = ConvexHull(our_planets)
our_volume = our_hull.volume
zombie_hull = ConvexHull(zombie_planets)
zombie_volume = zombie_hull.volume

# Calculate difference in volume
diff = our_volume - zombie_volume

# Find the planet from the zombie/Reaver set that, if captured, would give us the greatest increase in volume
best_capture = None
best_increase = 0
for z_planet in zombie_planets:
    # Calculate volume increase if we capture this planet
    new_our_planets = np.append(our_planets, [z_planet], axis=0)
    new_our_hull = ConvexHull(new_our_planets)
    new_our_volume = new_our_hull.volume
    increase = new_our_volume - our_volume
    
    # Check if this is the best capture so far
    if increase > best_increase:
        best_capture = z_planet
        best_increase = increase

# Find the planet from our set that, if captured by the zombie/Reavers, would give them the greatest increase in volume
worst_capture = None
worst_increase = 0
for o_planet in our_planets:
    # Calculate volume increase if the zombie/Reavers capture this planet
    new_zombie_planets = np.append(zombie_planets, [o_planet], axis=0)
    new_zombie_hull = ConvexHull(new_zombie_planets)
    new_zombie_volume = new_zombie_hull.volume
    increase = new_zombie_volume - zombie_volume
    
    # Check if this is the worst capture so far
    if increase > worst_increase:
        worst_capture = o_planet
        worst_increase = increase

# Print results
print(f"We control {diff:.1f} cubic light-years more than the zombie/Reavers.")
print(f"If we capture the planet at coordinates {best_capture} we will increase that to {our_volume+best_increase:.2f} cubic light-years.")
print(f"If instead they capture any of our planets at coordinates {worst_capture} they will have an advantage of {zombie_volume+worst_increase-our_volume:.3f} cubic light-years.")
