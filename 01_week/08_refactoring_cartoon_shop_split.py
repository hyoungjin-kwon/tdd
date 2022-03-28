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
        result += f"{order_history['customer']} 주문 내역\n" # 출력 결과 추가하기
        total_amount = 0 # 총 비용 계산하기
        point = 0 # 포인트 계산하기

        for cartoon_consumption_history in order_history["cartoon_consumption_histories"]: # 각 만화 소비 기록 별 for 문

            cartoon = cartoon_info[cartoon_consumption_history["cartoon_id"]] # 만화 정보 가져오기
            amount = calculate_cost_of_comic(cartoon, cartoon_consumption_history)
            point += max(cartoon_consumption_history["view_count"] - 30, 0) # 포인트 계산하기
            if cartoon["genre"] == "소년만화":
                point += math.floor(cartoon_consumption_history["view_count"] / 5) # 포인트 계산하기

            result += f"{cartoon['name']} : {amount}원 {cartoon_consumption_history['view_count']} 권 대여 \n"  # 출력 결과 추가하기
            total_amount += amount # 총 비용 계산하기

        result += f"총액 {total_amount}원 " # 출력 결과 추가하기
        result += f"적립 포인트 {point}점\n \n" # 출력 결과 추가하기
    return result


def calculate_cost_of_comic(cartoon, cartoon_consumption_history):
    amount = 0  # 각 만화 별 비용 계산하기
    if cartoon["genre"] == "판타지":  # 장르 확인 -> 만화 비용 계산하기
        amount += 1000 * (cartoon_consumption_history["view_count"] - 30)
    elif cartoon["genre"] == "코믹":  # 장르 확인 -> 만화 비용 계산하기
        amount = 30000
        if cartoon_consumption_history["view_count"] > 20:
            amount += 10000 + 500 * (cartoon_consumption_history["view_count"] - 20)
    else:  # 장르 확인 -> 만화 비용 계산하기
        amount = 4000 * cartoon_consumption_history["view_count"]
    return amount


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
