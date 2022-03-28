import math

input_cartoon_info = {
    "진격의거인": {"name": "진격의 거인", "genre": "판타지"},
    "원피스": {"name": "원피스", "genre": "소년만화"},
    "짱구": {"name": "짱구는 못말려", "genre": "코믹"},
    "괴짜가족": {"name": "괴짜 가족", "genre": "코믹"},
}

input_order_histories = [
    {
        "customer": "의정부고",
        "cartoon_consumption_histories":
            [
                {
                    "cartoon_id": "진격의거인", "view_count": 55
                },
                {
                    "cartoon_id": "원피스", "view_count": 40
                },
                {
                    "cartoon_id": "짱구", "view_count": 20
                },
                {
                    "cartoon_id": "괴짜가족", "view_count": 15
                }
            ]
    },
    {
        "customer": "의여고",
        "cartoon_consumption_histories":
            [
                {
                    "cartoon_id": "진격의거인", "view_count": 20
                },
                {
                    "cartoon_id": "원피스", "view_count": 10
                },
                {
                    "cartoon_id": "짱구", "view_count": 50
                },
                {
                    "cartoon_id": "괴짜가족", "view_count": 60
                }
            ]
    },
]


def get_result(order_histories, cartoon_info):
    result = ""

    for order_history in order_histories:
        result += f"{order_history['customer']} 주문 내역\n"
        total_amount = 0
        point = 0

        for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:
            amount = 0
            cartoon = cartoon_info[cartoon_consumption_history["cartoon_id"]]
            if cartoon["genre"] == "판타지":
                amount += 1000 * (cartoon_consumption_history["view_count"] - 30)
            elif cartoon["genre"] == "코믹":
                amount = 30000
                if cartoon_consumption_history["view_count"] > 20:
                    amount += 10000 + 500 * (cartoon_consumption_history["view_count"] - 20)
            else:
                amount = 4000 * cartoon_consumption_history["view_count"]
            point += max(cartoon_consumption_history["view_count"] - 30, 0)
            if cartoon["genre"] == "소년만화":
                point += math.floor(cartoon_consumption_history["view_count"] / 5)

            result += f"{cartoon['name']} : {amount}원 {cartoon_consumption_history['view_count']} 권 대여 \n"
            total_amount += amount

        result += f"총액 {total_amount}원 "
        result += f"적립 포인트 {point}점\n \n"
    return result


result = get_result(input_order_histories, input_cartoon_info)
objective_result = """의정부고 주문 내역
진격의 거인 : 25000원 55 권 대여 
원피스 : 160000원 40 권 대여 
짱구는 못말려 : 30000원 20 권 대여 
괴짜 가족 : 30000원 15 권 대여 
총액 245000원 적립 포인트 43점
 
의여고 주문 내역
진격의 거인 : -10000원 20 권 대여 
원피스 : 40000원 10 권 대여 
짱구는 못말려 : 55000원 50 권 대여 
괴짜 가족 : 60000원 60 권 대여 
총액 145000원 적립 포인트 52점"""
print(result)

assert objective_result in result
