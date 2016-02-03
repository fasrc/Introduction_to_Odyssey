#!/bin/bash
#
# add all other SBATCH directives here...
#

set -x

# add additional commands needed for Lmod and module loads here

host=`hostname`
date=`date`
echo "Job started at $date on node $host"

# add commands for analyses here
R CMD BATCH --quiet --no-restore --no-save '--args functions.R 10000000' ./test.R ./test.out

# end of program
exit 0;

