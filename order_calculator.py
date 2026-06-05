
def calculate_order(price, quantity, discount, delivery_type):
    """
    Рассчитывает итоговую стоимость заказа.
    
    :param price: Цена за единицу (float)
    :param quantity: Количество (int)
    :param discount: Скидка в % (float, 0-100)
    :param delivery_type: Тип доставки ('standard' или 'express')
    :return: Итоговая стоимость (float)
    """
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")
    if not (0 <= discount <= 100):
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100")
    
    base_cost = price * quantity
    cost_after_discount = base_cost * (1 - discount / 100)
    
    if cost_after_discount > 10000:
        delivery_cost = 0
    elif delivery_type == 'standard':
        delivery_cost = 300
    elif delivery_type == 'express':
        delivery_cost = 600
    else:
        raise ValueError("Неизвестный тип доставки")
        
    return cost_after_discount + delivery_cost
