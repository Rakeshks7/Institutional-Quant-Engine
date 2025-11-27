import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return x**2 + 10*np.sin(x)

def simulated_annealing(func, bounds, iterations=1000, temp=10.0, cooling=0.99):
    current_x = np.random.uniform(bounds[0], bounds[1])
    current_energy = func(current_x)
    
    best_x = current_x
    best_energy = current_energy
    
    path = []
    
    for i in range(iterations):
        step = np.random.uniform(-0.5, 0.5)
        new_x = np.clip(current_x + step, bounds[0], bounds[1])
        new_energy = func(new_x)
        
        if new_energy < current_energy:
            current_x = new_x
            current_energy = new_energy
        else:
            prob = np.exp((current_energy - new_energy) / temp)
            if np.random.rand() < prob:
                current_x = new_x
                current_energy = new_energy
        
        temp *= cooling
        
        if current_energy < best_energy:
            best_energy = current_energy
            best_x = current_x
            
        path.append(current_energy)

    return best_x, best_energy, path

best_solution, min_val, history = simulated_annealing(objective_function, [-10, 10])

print(f"--- QUANTUM-INSPIRED OPTIMIZATION ---")
print(f"Global Minimum Found at X = {best_solution:.4f}")
print(f"Minimum Energy (Risk) = {min_val:.4f}")

plt.plot(history)
plt.title('Annealing Process: Escaping Local Minima')
plt.ylabel('Energy (Risk)')
plt.xlabel('Iterations')
plt.show()

print("Tier 1 Insight: Classical Gradient Descent gets stuck.")
print("Annealing accepts 'bad' moves temporarily to find the true 'best' move.")