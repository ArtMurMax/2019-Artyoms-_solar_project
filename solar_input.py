# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
	"""Cчитывает данные о космических объектах из файла, создаёт сами объекты
	и вызывает создание их графических образов

	Параметры:

	**input_filename** — имя входного файла
	"""

	objects = []
	with open(input_filename) as input_file:
		for line in input_file:
			if len(line.strip()) == 0 or line[0] == '#':
				continue  # пустые строки и строки-комментарии пропускаем
			object_type = line.split()[0].lower()
			if object_type == "star":
				obj = Star()
				parse_obj_parameters(line, obj)
				objects.append(obj)
			elif object_type == "planet":
				obj = Planet()
				parse_obj_parameters(line, obj)
				objects.append(obj)
			else:
				print("Unknown space object")

	return objects


def parse_obj_parameters(line, obj):
	"""Считывает данные о звезде из строки.
	Входная строка должна иметь слеюущий формат:
	Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

	Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
	Пример строки:
	Star 10 red 1000 1 2 3 4

	Параметры:

	**line** — строка с описание звезды.
	**star** — объект звезды.
	"""

	obj.R = float(line.split()[1])
	obj.color = line.split()[2]
	obj.m = float(line.split()[3])
	obj.x = float(line.split()[4])
	obj.y = float(line.split()[5])
	obj.Vx = float(line.split()[6])
	obj.Vy = float(line.split()[7])


def write_space_objects_data_to_file(output_filename, space_objects):
	"""Сохраняет данные о космических объектах в файл.
	Строки должны иметь следующий формат:
	Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
	Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

	Параметры:

	**output_filename** — имя входного файла
	**space_objects** — список объектов планет и звёзд
	"""
	with open(output_filename, 'w') as out_file:
		for obj in space_objects:
			print(out_file, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy)

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
	print("This module is not for direct call!")
