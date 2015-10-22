from __future__ import division
import pyopencl as cl
import numpy as np

# List our platforms
platforms = cl.get_platforms()
print 'The platforms detected are:'
print '---------------------------'
for platform in platforms:
    print platform.name, platform.vendor, 'version:', platform.version

# List devices in each platform
for platform in platforms:
    print 'The devices detected on platform', platform.name, 'are:'
    print '---------------------------'
    for device in platform.get_devices():
        print device.name, '[Type:', cl.device_type.to_string(device.type), ']'
        print 'Maximum clock Frequency:', device.max_clock_frequency, 'MHz'
        print 'Maximum allocable memory size:', int(device.max_mem_alloc_size / 1e6), 'MB'
        print 'Maximum work group size', device.max_work_group_size
        print '---------------------------'

# Create a context with all the devices
devices = platforms[0].get_devices()
context = cl.Context(devices)
print 'This context is associated with ', len(context.devices), 'devices'

# Create a queue for transferring data and launching computations.
# Turn on profiling to allow us to check event times.
queue = cl.CommandQueue(context, context.devices[0],
                        properties=cl.command_queue_properties.PROFILING_ENABLE)
print 'The queue is using the device:', queue.device.name


# Write a simple Z = X + Y vector addition kernel.
# This is bandwidth limited, not compute.
kernel_src = """
__kernel void
add_vectors(__global float* z,
            __global const float *x, __global const float *y,
            const unsigned int n) {
    unsigned int thread_id = get_global_id(0);

    // Make sure we stay in-bounds
    if (thread_id < n)
        z[thread_id] = x[thread_id] + y[thread_id];
}
"""

program = cl.Program(context, kernel_src).build(options='')

# Allocate arrays of 4-byte elements
N = 10000000
x = cl.Buffer(context, cl.mem_flags.READ_ONLY, N * 4)
y = cl.Buffer(context, cl.mem_flags.READ_ONLY, N * 4)
z = cl.Buffer(context, cl.mem_flags.READ_WRITE, N * 4)

# Allocate local copies for these arrays
host_x = np.random.uniform(0, 1, N).astype(np.float32)
host_y = np.random.uniform(0, 1, N).astype(np.float32)
host_z = np.empty(N).astype(np.float32)

# Send to the device, non-blocking
cl.enqueue_copy(queue, x, host_x, is_blocking=False)
cl.enqueue_copy(queue, y, host_y, is_blocking=False)

# Launch computation, run 3 times to "warm up" card, keep last result
global_size = host_x.shape
local_size = (32,)
for i in range(3):
    event_execute = program.add_vectors(queue, global_size, local_size,
                                        z, x, y, np.uint32(N))

# Copy back form device, blocking so we can check values (and to ensure
# computation completes)
event_copy = cl.enqueue_copy(queue, host_z, z, is_blocking=True)
assert np.allclose(host_z, host_x + host_y)

# profiling times come back in nanoseconds, dividing gives GB / sec
print 'The device memory bandwidth is', 3 * N * 4 / (event_execute.profile.end - event_execute.profile.start), 'GB/s'
print 'The host-device bandwidth is', N * 4 / (event_copy.profile.end - event_copy.profile.start), 'GB/s'
