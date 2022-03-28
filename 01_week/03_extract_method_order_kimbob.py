def order_kimbob(cook, ingredients):
    if ingredients.is_empty():
        return None

    prepare_base_ingredients(cook, ingredients)
    kimbob = make_kimbob(cook, ingredients)
    return prepare_plating(cook, kimbob)



def prepare_plating(cook, kimbob):
    while kimbob.is_too_short():  # -> 플레이팅 준비하기
        cook.cut(kimbob)  # -> 플레이팅 준비하기
    plate = cook.put_on_a_plate(kimbob)  # -> 플레이팅 준비하기
    return plate


def make_kimbob(cook, ingredients):
    kimbob = cook.make_base_kimbob(ingredients.get_kim())  # -> 김밥 만들기
    cook.grap(kimbob)  # -> 김밥 만들기
    while kimbob.is_almost_full_with_rice():  # -> 김밥 만들기
        cook.spread_the_rice(kimbob)  # -> 김밥 만들기
    cook.add_ingredient(kimbob, ingredients.get_ham())  # -> 김밥 만들기
    cook.add_ingredient(kimbob, ingredients.get_carrot())  # -> 김밥 만들기
    cook.add_ingredient(kimbob, ingredients.get_cucumber())  # -> 김밥 만들기
    cook.add_ingredient(kimbob, ingredients.get_spinach())  # -> 김밥 만들기
    if ingredients.has_tuna() and ingredients.has_mayonnaise():  # -> 김밥 만들기
        cook.add_ingredient(kimbob, ingredients.get_tuna())  # -> 김밥 만들기
        cook.add_ingredient(kimbob, ingredients.get_mayonnaise())  # -> 김밥 만들기
    while kimbob.meet_each_ends():  # -> 김밥 만들기
        cook.hold_the_end(kimbob)  # -> 김밥 만들기
        cook.roll_up(kimbob)  # -> 김밥 만들기
        cook.hold_the_another_end(kimbob)  # -> 김밥 만들기
    cook.apply(kimbob, ingredients.get_sesame_oil())  # -> 김밥 만들기
    return kimbob


def prepare_base_ingredients(cook, ingredients):
    rice = ingredients.get_rice()  # -> 재료 준비하기
    sesame = ingredients.get_sesame()  # -> 재료 준비하기
    cook.season_to_taste(rice)  # -> 재료 준비하기
    cook.put_in(rice, sesame)  # -> 재료 준비하기
    cook.stir_in(rice)  # -> 재료 준비하기