import hpx


# Set up the callback function
def add(a):
    print(a)
    hpx.exit(0)

# Register action
add_action = hpx.register_action(add, hpx.DEFAULT, hpx.ATTR_NONE, [hpx.INT])

# Initialize HPX runtime and run the action
hpx.init()
hpx.run(add_action, 5)
hpx.finalize()
