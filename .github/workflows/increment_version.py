import sys

def increment_version(version):
    # Split the version string into individual components
    components = version.split('.')

    # Convert each component to an integer
    components = [int(comp) for comp in components]

    # Increment the last component
    components[-1] += 1

    # Join the components back into a string
    new_version = '.'.join(str(comp) for comp in components)

    return new_version

current_version = sys.argv[1]
new_version = increment_version(current_version)
print(new_version)
