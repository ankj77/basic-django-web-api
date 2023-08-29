from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

import csv

used_coupon_list = []
unused_coupon_list = []
coupon_to_customer_id = dict()
file_path = "./coupon.csv"  # Replace with the actual file path


def update_csv():
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Voucher Code", "Status", "Customer_ID"])
        for used_coupon in used_coupon_list:
            row = [used_coupon, 'SENT', coupon_to_customer_id[used_coupon]]
            csv_writer.writerow(row)
        for unused_coupon in unused_coupon_list:
            row = [unused_coupon, 'NOT SENT', coupon_to_customer_id[unused_coupon]]
            csv_writer.writerow(row)


def fetch_coupon(request):
    customer_id = request.GET.get('customer_id')
    if customer_id is None:
        customer_id = ""
    if len(unused_coupon_list) == 0:
        return JsonResponse({
            'status': False,
            'message': "no coupon left",
            'data': {
                'coupon': 'NA',
                'total': len(used_coupon_list) + len(unused_coupon_list),
                'used': len(used_coupon_list),
                'unused': len(unused_coupon_list)
            }
        })
    latest_coupon = unused_coupon_list.pop(0)
    used_coupon_list.append(latest_coupon)
    coupon_to_customer_id[latest_coupon] = customer_id
    update_csv()
    return JsonResponse({
        'status': True,
        'message': "fetched one coupon",
        'data': {
            'coupon': latest_coupon,
            'customer_id': customer_id,
            'total': len(used_coupon_list) + len(unused_coupon_list),
            'used': len(used_coupon_list),
            'unused': len(unused_coupon_list)
        }
    })


def load_csv():
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            coupon_name = row[0]
            coupon_status = row[1]
            customer_id = row[2]
            print(coupon_name, " -  ", coupon_status)
            coupon_to_customer_id[coupon_name] = customer_id
            if 'not' in coupon_status.lower():
                unused_coupon_list.append(coupon_name)
            else:
                used_coupon_list.append(coupon_name)
    print(" total unused_coupon_list coupon ", len(unused_coupon_list))
