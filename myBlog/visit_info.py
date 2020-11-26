from django.utils import timezone

from .models import UserIP, VisitNumber, DayNumber


# 自定义的函数，不是视图
def change_info(request, end_point):
    """
    # 修改网站访问量和访问 ip 等信息
    # 每一次访问，网站总访问次数加一
    """
    count_nums = VisitNumber.objects.filter(id=1)
    if count_nums:
        count_nums = count_nums[0]
        count_nums.count += 1
    else:
        count_nums = VisitNumber()
        count_nums.count = 1
    count_nums.save()

    # 记录访问 ip 和每个 ip 的次数
    # client_ip = ""
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取 ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的 ip
    else:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理 ip
    # print(client_ip)

    ip_exist = UserIP.objects.filter(ip=str(client_ip), end_point=end_point)
    if ip_exist:  # 判断是否存在该 ip
        uobj = ip_exist[0]
        uobj.count += 1
    else:
        uobj = UserIP.objects.create(ip=client_ip,end_point=end_point,count=1)
    uobj.save()

    # 增加今日访问次数
    date = timezone.now().date()
    today = DayNumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.count += 1
    else:
        temp = DayNumber()
        temp.dayTime = date
        temp.count = 1
    temp.save()