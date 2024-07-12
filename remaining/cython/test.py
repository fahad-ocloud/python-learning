import main
import time

start_vanilla = time.time()
main.prime_finder_vanilla(10000)
end_vanilla = time.time()

start_cython = time.time()
main.prime_finder_cython(10000)
end_cython = time.time()

print(end_vanilla - start_vanilla)
print(end_cython - start_cython)