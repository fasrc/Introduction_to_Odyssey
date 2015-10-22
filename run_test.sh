#!/bin/bash
#
# add all other SBATCH directives here...
#
#SBATCH -p holyseasgpu
#SBATCH --gres=gpu


# add additional commands needed for Lmod and module loads here

module load pyopencl

# add commands for analyses here


# end of program
exit 0;

