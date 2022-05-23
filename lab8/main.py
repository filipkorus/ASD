from math import sqrt
import matplotlib.pyplot as plt

def pathfinder_naive(data):
	path_length = 0
	cities = []
	for i in range(len(data)):
		path_length += sqrt(
			(data[i % len(data)]['x'] - data[(i + 1) % len(data)]['x']) ** 2 +
			(data[i % len(data)]['y'] - data[(i + 1) % len(data)]['y']) ** 2
		)
		cities.append(data[i]['idx'])

	return path_length, cities

def get_closest_element_idx(src_idx, data):
	"""
	:returns: idx of the closest element to given source and its `data` list index
	"""
	list_idx = find_idx(src_idx, data)
	src_x, src_y = data[list_idx]['x'], data[list_idx]['y']
	min_distance = 1_000_000
	min_distance_idx = None
	for i in range(len(data)):
		if i == list_idx:
			continue
		distance = sqrt(
				(src_x - data[i]['x']) ** 2 + (src_y - data[i]['y']) ** 2
		)
		if distance < min_distance:
			min_distance = distance
			min_distance_idx = data[i]['idx']

	return min_distance_idx, find_idx(min_distance_idx, data)

def find_idx(idx, data):
	return next((index for (index, d) in enumerate(data) if d['idx'] == idx), None)

def generate_map(data, plot_title, plot_name, connections=None, caption_connection_order=True):
	plt.clf()  # clear plot
	if connections is not None:
		Xs, Ys = [], []
		for connection in connections:
			idx = find_idx(connection, data)
			Xs.append(data[idx]['x'])
			Ys.append(data[idx]['y'])

		if caption_connection_order:
			for connection in connections:
				idx = find_idx(connection, data)
				plt.plot(data[idx]['x'], data[idx]['y'], marker='o', markersize=5, color='b', linestyle='--')
				plt.annotate(str(data[idx]['idx']), (data[idx]['x'], data[idx]['y']), fontsize=8)

		plt.plot(Xs, Ys, marker='o', markersize=5, color='b', linestyle='--')

		# connect first and last points
		first_idx = find_idx(connections[0], data)
		last_idx = find_idx(connections[-1], data)
		point1 = [data[first_idx]['x'], data[first_idx]['y']]
		point2 = [data[last_idx]['x'], data[last_idx]['y']]
		x_values = [point1[0], point2[0]]
		y_values = [point1[1], point2[1]]
		plt.plot(x_values, y_values, color='b', linestyle="--")

		if caption_connection_order is False:
			i = 1
			for connection in connections:
				idx = find_idx(connection, data)
				plt.annotate(str(i), (data[idx]['x'], data[idx]['y']), fontsize=8)
				i += 1

		plt.title(plot_title)
		plt.ylabel('y')
		plt.xlabel('x')
		plt.savefig(plot_name, bbox_inches='tight')  # save plot to png file
		return

	for row in data:
		plt.plot(row['x'], row['y'], marker='o', markersize=5, linestyle='')
		plt.annotate(str(row['idx']), (row['x'], row['y']), fontsize=8)
		plt.title(plot_title)
		plt.ylabel('y')
		plt.xlabel('x')
		plt.savefig(plot_name, bbox_inches='tight')  # save plot to png file

def measure_path_length(connections, data):
	path_length = 0
	for i in range(len(connections)):
		idx = find_idx(connections[i % len(data)], data)
		idx2 = find_idx(connections[(i + 1) % len(data)], data)
		row = data[idx]
		row2 = data[idx2]
		path_length += sqrt(
			(row['x'] - row2['x']) ** 2 + (row['y'] - row2['y']) ** 2
		)
	return path_length

if __name__ == '__main__':
	# read file
	lines = open('TSP.txt').read().splitlines()
	data = []
	for line in lines:
		line = line.split('\t')
		data.append({
			'idx': int(line[0]),
			'x': float(line[1]),
			'y': float(line[2]),
		})

	generate_map(data, 'map of cities','cities.png')

	curr_idx = 93
	path = []
	tmp = data.copy()
	while len(tmp) > 0:
		prev_idx = curr_idx
		curr_idx, list_idx = get_closest_element_idx(curr_idx, tmp)
		path.append(prev_idx)
		tmp.pop(find_idx(prev_idx, tmp))

	naive_result = pathfinder_naive(data)
	print('naive distance =', naive_result[0])
	print('naive path:', naive_result[1])
	print('my algo distance =', measure_path_length(path, data))
	print('my algo path:', path)
	generate_map(data, 'my algorithm path', 'my_algo_path.png', connections=path, caption_connection_order=True)
	generate_map(data, 'naive algorithm path', 'naive_path.png', connections=naive_result[1], caption_connection_order=True)
