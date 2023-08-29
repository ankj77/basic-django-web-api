from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

import csv

used_coupon_list = []

unused_coupon_list = []


def fetch_coupon(request):
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
    return JsonResponse({
        'status': True,
        'message': "fetched one coupon",
        'data': {
            'coupon': latest_coupon,
            'total': len(used_coupon_list) + len(unused_coupon_list),
            'used': len(used_coupon_list),
            'unused': len(unused_coupon_list)
        }
    })


def load_csv():
    file_path = "./coupon.csv"  # Replace with the actual file path
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            coupon_name = row[0]
            coupon_status = row[1]
            print( coupon_name," -  ",coupon_status)
            if 'not' in coupon_status.lower():
                unused_coupon_list.append(coupon_name)
    print(" total unused_coupon_list coupon ", len(unused_coupon_list))
