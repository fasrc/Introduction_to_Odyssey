# For this exercise we assume to draw random points inside the square on the [-1,1] unit, 
# and thus the value of Pi = 4(# random pts insid cirlce / # random pts in square)

sim.pi <- function(iterations = 1000) {
    # Generate two vectors for random points in unit circle
    x.pos <- runif(iterations, min=-1, max=1)
    y.pos <- runif(iterations, min=-1, max=1)
    # Test if draws are inside the unit circle
    draw.pos <- ifelse(x.pos^2 + y.pos^2 <= 1, TRUE, FALSE)
    draws.in <- length(which(draw.pos == TRUE))
    # Estimate Pi
    return(4*(draws.in/iterations))
}
