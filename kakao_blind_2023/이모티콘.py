from itertools import product
def discount_calculator(price, discount):
    return price * (100 - discount) // 100
def solution(users, emoticons):
    result = [0,0]
    discount_rates = [10,20,30,40]
    for discounts in product(discount_rates, repeat=len(emoticons)):
        plus_user = 0
        total_price = 0
        for user_discount, user_limit in users:
            total = 0
            for price, dc in zip(emoticons, discounts):
                if dc >= user_discount:
                    total += discount_calculator(price, dc)
            if total >= user_limit:
                plus_user += 1
            else:
                total_price += total
        if result[0] < plus_user or (result[0] == plus_user and result[1] < total_price):
            result = [plus_user, total_price]
    return result