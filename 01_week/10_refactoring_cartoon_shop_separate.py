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
    return get_output_data(get_order_data_list(cartoon_info, order_histories))


def get_order_data_list(cartoon_info, order_histories):
    order_data_list = []
    for order_history in order_histories:
        cartoon_consumption_histories = []
        for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:
            cartoon_consumption_histories.append({
                'cartoon_name': get_cartoon(cartoon_consumption_history, cartoon_info)['name'],
                'amount': calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info),
                                                  cartoon_consumption_history),
                'view_count': cartoon_consumption_history['view_count']
            })
        order_data_list.append({
            # 1. 각 주문 내역의 고객의 이름
            # 2. 각 주문 내역의 만화별 소비 이력의 만화 이름
            # 3. 각 주문 내역의 만화별 소비 이력의 총 비용
            # 4. 각 주문 내역의 만화별 소비 이력의 총 조회수
            # 5. 각 주문 내역의 총 만화 비용
            # 6. 각 주문 내역의 총 만화 포인트
            'customer': order_history['customer'],
            "cartoon_consumption_histories": cartoon_consumption_histories,
            'total_amount': calculate_total_amount_from_histories(cartoon_info, order_history),
            'point': calculate_point_from_history(cartoon_info, order_history)

        })
    return order_data_list


def get_output_data(order_data_list):
    result = ""
    for order_data in order_data_list:
        result += f"{order_data['customer']} 주문 내역\n"  # 출력 결과 추가하기
        for cartoon_consumption_history in order_data['cartoon_consumption_histories']:
            result += f"{cartoon_consumption_history['cartoon_name']} : {cartoon_consumption_history['amount']}원 {cartoon_consumption_history['view_count']} 권 대여 \n"  # 출력 결과 추가하기
        result += f"총액 {order_data['total_amount']}원 "  # 출력 결과 추가하기
        result += f"적립 포인트 {order_data['point']}점\n \n"  # 출력 결과 추가하기
    return result

def calculate_total_amount_from_histories(cartoon_info, order_history):
    total_amount = 0  # 총 비용 계산하기
    for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:  # 각 만화 소비 기록 별 for 문
        total_amount += calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info),
                                                cartoon_consumption_history)  # 총 비용 계산하기
    return total_amount


def calculate_point_from_history(cartoon_info, order_history):
    point = 0  # 포인트 계산하기
    for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:  # 각 만화 소비 기록 별 for 문
        point += calculate_point(cartoon_consumption_history, cartoon_info)
    return point


def calculate_point(cartoon_consumption_history, cartoon_info):
    point = 0
    point += max(cartoon_consumption_history["view_count"] - 30, 0)  # 포인트 계산하기
    if get_cartoon(cartoon_consumption_history, cartoon_info)["genre"] == "소년만화":
        point += math.floor(cartoon_consumption_history["view_count"] / 5)  # 포인트 계산하기
    return point


def get_cartoon(cartoon_consumption_history, cartoon_info):
    return cartoon_info[cartoon_consumption_history["cartoon_id"]]


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
