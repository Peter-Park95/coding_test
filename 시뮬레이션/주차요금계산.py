from math import ceil
def solution(fees, records):
    parking = []
    charge = {}
    result = []
    for record in records:
        time, car_num, status = record.split()
        if status == "IN":
            in_time = time.split(':')
            parking.append((int(in_time[0])*60+int(in_time[1]), car_num))
        elif status == "OUT":
            for in_time, p_num in parking:
                if p_num == car_num:
                    out_time = time.split(':')
                    parked_time = int(out_time[0])*60+int(out_time[1]) - in_time
                    charge[car_num] = charge.get(car_num, 0) + parked_time
                    parking.remove((in_time, p_num))
    for in_time, p_num in parking: #출차 안된 차 정산
        out_time = 1439 #23:59
        parked_time = out_time - in_time
        print(parked_time)
        charge[p_num] = charge.get(p_num, 0) + parked_time
    charge = dict(sorted(charge.items())) # 차번호 기준 내림차순으로 정렬렬
    for car_num, time in charge.items():
        if time <= fees[0]:
            result.append(fees[1])
        else:
            result.append(fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3])
    return result

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
            