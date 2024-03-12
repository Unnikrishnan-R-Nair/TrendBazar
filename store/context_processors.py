from django.db.models import Sum


def demo(request):

    return {'msg': 'Hello coder'}



def cart_count(request):

    count = 0

    if request.user.is_authenticated:

        data = request.user.cart.cartitems.filter(is_order_placed=False).values_list('quantity').aggregate(total=Sum('quantity'))

        count = data.get('total')

    return {'item_count': count}


