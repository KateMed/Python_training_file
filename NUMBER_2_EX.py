import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        # ?? ниже стоят 2 строки. Так, как я понимаю, должны выглядеть атрибуты
        photo_file_name = photo_file_name
        carrying = float(carrying)
        start, ext = os.path.splitext(photo_file_name)
        self.get_photo_file_ext = ext
        pass


class Car(CarBase):
    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying):
        car_type = 'car'
        passenger_seats_count = int(passenger_seats_count)
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, body_whl, carrying):
        car_type = 'truck'
        if body_whl == '':
            body_height, body_length, body_width = 0, 0, 0
        else:
            body_whl = body_whl.split('x')
            body_length = float(body_whl[0])
            body_height = float(body_whl[1])
            body_width = float(body_whl[2])

        self.get_body_volume = body_length*body_height*body_width
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        car_type = 'spec_machine'
        pass


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        data_read = [row[0] for row in reader]
        length = len(data_read)
        for i in range(length-1):
            data_read_inside = data_read[i].split('\t')
            if data_read_inside[0] == 'truck':
                del data_read_inside[2]
                car_list_local = Truck(data_read_inside[1], data_read_inside[2], data_read_inside[3],
                                        data_read_inside[4])
                car_list.append(car_list_local)
                print(car_list[i].get_body_volume)
            else:
                # data_read_inside = data_read[i].split('\t')
                # print()
                data_read_inside.remove('')
                if data_read_inside[0] == 'car':
                    #print(data_read_inside[4])
                    car_list_local = Car(data_read_inside[1], data_read_inside[2], data_read_inside[3],
                                         data_read_inside[4])
                    car_list.append(car_list_local)
                elif data_read_inside[0] == 'spec_mashine':
                    car_list_local = SpecMachine(data_read_inside[1], data_read_inside[2], data_read_inside[3],
                                              data_read_inside[4])
                    car_list.append(car_list_local)
            # print(car_list)
    return car_list

'''
tucky = Truck('brand','photo_file_name.jpg','carrying','')
print(tucky.get_body_volume)
'''
#car = Car('brand','2','carrying','9.6')

get_car_list('filemame.csv')


