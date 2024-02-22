def fetch_lines(filename):
    with open(filename, 'r') as file:
        # Return all lines
        # lines = []
        # for line in file:
        #     lines.append(line)
        # return lines 

        # Store all and send when asked for (next)
        for line in file:
            yield line
    

lines = fetch_lines('sample.txt')
print(lines)
print(next(lines))
print(next(lines))
print(next(lines))