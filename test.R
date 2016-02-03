
options(echo=TRUE) # if you want see commands in output file
args <- commandArgs(trailingOnly = TRUE)
print(args)

# test if there is at least one argument: if not, return an error
if (length(args) < 2) {
  stop("At least two argument must be supplied (function_file iterations).\n", call.=FALSE)
}

# parse our functions
functions_file <- args[1]
iterations <- as.integer(args[2])
rm(args)

# read in functions
source(functions_file)

# and calculate pi
sim.pi(iterations)

# end of program
