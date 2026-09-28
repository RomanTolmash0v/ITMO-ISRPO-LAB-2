import math


def area(r):
    '''
    Возвращает площадь круга заданного радиуса
    
        Параметры:
            r (float): радиус круга
        
        Возвращаемое значение:
            circle_area (float): площадь круга заданного радиуса
    '''
    
    circle_area = math.pi * r * r
    return circle_area


def perimeter(r):
    '''
    Возвращает периметр круга заданного радиуса
    
        Параметры:
            r (float): радиус круга
        
        Возвращаемое значение:
            perimeter (float): периметр круга заданного радиуса
    '''
    perimeter = 2 * math.pi * r
    return perimeter

