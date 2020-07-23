class Point3D():

    def __init__(self, x, y, z):
        self.coord = [x, y, z]
    #1
    def __ne__(self, other):
        if (self.coord[0] != other.coord[0]) or (self.coord[1] != other.coord[1]) or (self.coord[2] != other.coord[2]):
            return True
        else:
            return False
    #2
    def __eq__(self, other):
        if (self.coord[0] == other.coord[0])&(self.coord[1] == other.coord[1])&(self.coord[2] == other.coord[2]):
            return True
        else:
            return False

    def distanse_to_zero(self):
        if isinstance(self, Point3D):
            kat = (self.coord[0]**2 + self.coord[1]**2)**0.5
            return (kat**2+self.coord[2]**2)**0.5
    #3
    def __gt__(self, other):
        if self.distanse_to_zero() > other.distanse_to_zero():
            return True
        else:
            return False

    #4
    def __lt__(self, other):
        if isinstance(other, Point3D):
            if self.distanse_to_zero() < other.distanse_to_zero():
                return True
            else:
                return False
    #5
    def __len__(self):
        return int(self.distanse_to_zero())

    #6
    def __le__(self, other):
        if isinstance(other, Point3D):
            if self.distanse_to_zero() <= other.distanse_to_zero():
                return True
            else:
                return False

    #7
    def __ge__(self, other):
        if self.distanse_to_zero() >= other.distanse_to_zero():
            return True
        else:
            return False

    #8
    def __str__(self):
        return f'Point: ({self.coord[0]},{self.coord[1]},{self.coord[2]})'
    #9
    def __add__(self, other):
        if isinstance(other, Point3D):
            x_ = self.coord[0]+other.coord[0]
            y_ = self.coord[1]+other.coord[1]
            z_ = self.coord[2]+other.coord[2]
            return Point3D(x_, y_, z_)
        elif isinstance(other, int):
            return Point3D(self.coord[0]+other, self.coord[1]+other, self.coord[2]+other)
    #10
    def __sub__(self, other):
        if isinstance(other, Point3D):
            x_ = self.coord[0] - other.coord[0]
            y_ = self.coord[1] - other.coord[1]
            z_ = self.coord[2] - other.coord[2]
            return Point3D(x_, y_, z_)
        elif isinstance(other, int):
            return Point3D(self.coord[0] - other, self.coord[1] - other, self.coord[2] - other)
    

if __name__ =='__main__':

    point1 = Point3D(1, 1, 1)
    point2 = Point3D(1, 1, 2)
    print("Первая точка не равна второй:", point1!=point2)
    print("Первая точка равна второй:",point1 == point2)
    print("Первая точка больше второй:",point1 > point2)
    print("Первая точка меньше второй:",point1 < point2)
    print("Первая точка меньше или равна второй:", point1 <= point2)
    print("Первая точка больше или равна второй:", point1 >= point2)
    print("Длинна вектора точки 1 ", len(point1))
    print("Длинна вектора точки 2 ", len(point2))
    print(point1)
    print(point2)
    print("Сложим две точки 1 и 2", point1 + point2)
    print("Вычтем из точки 2 - 1", point2 - point1)