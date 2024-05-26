import numpy 
import matplotlib.pyplot as plt
n_dimension=2
moltiplication_matrix=np.random.random(size=(n_dimension,n_dimension))*10-5
moltiplication_matrix=(moltiplication_matrix+moltiplication_matrix.T)/2
transformation_matrix=np.random.randint(0,n_dimension,size=(n_dimension,n_dimension))
transformation_matrix=np.asarray(np.round((rules_trans+rules_trans.T)/2),dtype=int)
#they have to be simmetrical for commutative propriety if you want it 
print(moltiplication_matrix,"\n",transformation_matrix)
def mulpy(a,b):
    dot_matrix=np.dot(a,b.T)
    result=np.zeros(shape=(n_dimension,1))
    for i in range(n_dimension):
        for j in range(n_dimension):
            result[transformation_matrix[i,j]]+=moltiplication_matrix[i,j]*dot_matrix[i,j]
          
    return result
            


def mandelbrot(c, max_iter):
    z = np.zeros(shape=(n_dimension,1))
    for n in range(max_iter):
        g=z.reshape(-1)
        
        if np.absolute(g)[0] > 2:
            return n
        z= mulpy(z,z) 
        z+= c
    return max_iter

def generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter,z):
    mandelbrot_set = np.zeros((width, height))
    
    for x in range(width):
        for y in range(height):
            real = xmin + (xmax - xmin) * x / width
            imag = ymin + (ymax - ymin) * y / height
            c = np.array([[real],[imag]])
            mandelbrot_set[x, y] = mandelbrot(c, max_iter)
    return mandelbrot_set

def plot_mandelbrot(mandelbrot_set):
    plt.imshow(mandelbrot_set.T, cmap='hot', extent=(-2, 2, -2, 2))
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('Mandelbrot Set')
    plt.show()

# Set parameters
width = 200
height = 200

xmin, xmax = -1,1
ymin, ymax = -1, 1
max_iter = 100

# Generate and plot the Mandelbrot set

mandelbrot_set = generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter,0)
plot_mandelbrot(mandelbrot_set)

#[[-0.51551854 -0.82554248]
# [-0.82554248  0.83911271]] 
 #[[0 1]
 #[1 0]]
#[[-4.60841151  3.50889012]
 #[ 3.50889012  0.41863127]] 
 #[[0 1]
 #[1 0]]
