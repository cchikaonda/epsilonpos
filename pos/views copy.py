from django.shortcuts import render,redirect, get_object_or_404
from inventory.models import ItemCategory, Unit, Item
from pos.models import Customer, OrderItem, Order, Payment
from django.contrib import messages
from constance import config
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.core.exceptions import ObjectDoesNotExist
from accounts.forms import AddCustomerForm
from pos.forms import AddPaymentForm, CashPaymentForm, SearchForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.core import serializers
import json
from django.db.models import Count
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse

import qrcode
import qrcode.image.svg
from io import BytesIO
from django.db.models.query import *


def index(request):
    context = {}
    #generating QR Code
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
    return render(request, 'index.html', context=context)

@login_required
def pos_dashboard(request):
    customers = Customer.objects.all()
    form = AddCustomerForm()
    unpaid_orders = Order.objects.filter(ordered = False)

    context = {
        'home':'Home',
        'header':'Pos Dashboard',
        'customers':customers,
        'form':form,
        'unpaid_orders':unpaid_orders,
        }
    return render(request, 'pos_dashboard.html', context)

@login_required
def add_customer_to_order(request):
    # form = AddCustomerToOrderForm(request.POST or None)
    if request.method == "POST":
        try: 
            order_date = timezone.now()
            selected_customer = request.POST.get('customer_name')
            customer = Customer.objects.get(name=selected_customer)

            #check if there is already order for the customer
            check_order = Order.objects.get(customer = customer, ordered = False)

            if check_order:
                return redirect('/pos/personal_order_list/'+ str(check_order.id))
            else:
                messages.info(request, "You do not have an active order")
                return redirect("pos_dashboard")
        except ObjectDoesNotExist:
            order = Order.objects.create(user = request.user, order_date = order_date, customer=customer, active=True )
            order.save()
            return redirect('/pos/personal_order_list/'+ str(order.id))

@login_required
def add_new_customer_from_pos_dash(request):
    form = AddCustomerForm(request.POST or None)

    if request.method == "POST":
        try:
            if form.is_valid():
                form.save()
            messages.info(request, "New Customer is Added!")
            return redirect("pos_dashboard")
        except ObjectDoesNotExist:
            messages.info(request, "You do not have an active order")
            return redirect("pos_dashboard")
        return None

# def cash_payment(request):
#     form = CashPaymantForm(request.POST or None)
#     complete_payment(form)

@login_required
def add_payment(request):
    form = AddPaymentForm(request.POST or None)
    if request.method == "POST":
        order_id =request.session['opened_order']
        order = Order.objects.get(id = order_id, user = request.user, ordered=False)

        customer_id = request.POST.get('customer')
        # order = Order.objects.get(customer = customer_id, ordered = False, active=True )
        items_in_order = get_items_in_order(order)
        print(items_in_order)
        try:
            if form.is_valid():
                # print(request.POST)
                paid_amount = form.cleaned_data.get('paid_amount')
                payment_mode = request.POST.get('payment_mode') 
                
                payment = Payment()
                payment.payment_mode = payment_mode
                payment.paid_amount = paid_amount
            
                if str(payment_mode).lower() == str('Cash').lower():
                    reference = 'CASH'
                    payment.reference = reference
                else:
                    reference = form.cleaned_data.get('reference') 
                    payment.reference = reference
                
                print(payment_mode)
                print(paid_amount)
                print('customer_id')
                print(customer_id)
                
                order.paid_amount = payment
                payment.save()
                order.save()
            return redirect('/pos/personal_order_list/'+ str(order.id))
        except ObjectDoesNotExist:
            messages.info(request, "You do not have an active order")
            order = Order.objects.get(user = request.user, ordered = False, active=True )
            return redirect('/pos/personal_order_list/'+ str(order.id))
        return None

@login_required
def complete_order_only(order, request):
    order_id =request.session['opened_order']
    order = Order.objects.get(id = order_id, user = request.user, ordered=False)
    order.customer.total_orders +=1
    order.customer.save()
    order.order_total_cost = order.order_total_due()
    order_item = OrderItem.objects.filter(user = request.user, ordered = False, customer = order.customer)
    for order_item in order_item:
        order_item.ordered_item_price = order_item.price
        order_item.ordered_items_total = order_item.get_total_amount
        order_item.ordered = True
        order_item.save()
    order.ordered = True
    order.active = False
    order.vat_p = order.vat_rate
    order.vat_cost = order.get_vat_value
    order.save()


@login_required
def complete_order(request):
    order_id =request.session['opened_order']
    order = Order.objects.get(id = order_id, user = request.user, ordered=False)
    order.customer.total_orders +=1
    order.customer.save()
    order.order_total_cost = order.order_total_due()
    order_item = OrderItem.objects.filter(user = request.user, ordered = False, customer = order.customer)
    for order_item in order_item:
        order_item.ordered_item_price = order_item.price
        order_item.ordered_items_total = order_item.get_total_amount
        order_item.ordered = True
        order_item.save()
    order.ordered = True
    order.active = False
    order.vat_p = order.vat_rate
    order.vat_cost = order.get_vat_value
    order.save()
    del request.session['opened_order']
    return redirect("pos_dashboard")

@login_required
def customers_list(request):
    payment_options = AddPaymentForm()
    all_orders = Order.objects.all()
    unsettled_orders = Order.objects.filter(user=request.user, ordered = False)
    settled_orders = Order.objects.filter(user=request.user, ordered = True)
    Order_qs = Order.objects.filter(user=request.user, ordered= False, active= True)
    if Order_qs.exists():
        current_order = Order_qs[0]
        if current_order.active == True:
            current_order.active = False
            current_order.save()

    customers = Customer.objects.all()
    customers_count = customers.count()
    orders = Order.objects.all()
    orders_count = orders.count()
    settled_orders_count = settled_orders.count()
    unsettled_orders_count = unsettled_orders.count()
    all_orders_count = all_orders.count()
    context = {
        'customers':customers,
        'orders':orders,
        'config':config,
        'all_orders':all_orders,
        'settled_orders':settled_orders,
        'unsettled_orders':unsettled_orders,
        'customers_count':customers_count,
        'settled_orders_count':settled_orders_count,
        'unsettled_orders_count':unsettled_orders_count,
        'all_orders_count':all_orders_count,
        'header':'Bills',
        'home':'Home',
        'payment_options':payment_options,
    }
    return render(request, 'customers_list.html', context)

@login_required
def personal_order_list(request, id):
    payment_form = AddPaymentForm(initial={"payment_mode":['Cash', ], "paid_amount":['']})
    airtel_money_payment_form = AddPaymentForm(initial={"payment_mode":['Airtel Money', ], "paid_amount":['']})
    mpamba_payment_form = AddPaymentForm(initial={"payment_mode":['Mpamba', ], "paid_amount":['']})
    order = get_object_or_404(Order,id=id)

 
    request.session['opened_order'] = order.id
    all_order_related = Order.objects.prefetch_related('customer','items','user',).all()
    # print(all_order_related)
    unsettled_orders = Order.objects.filter(user=request.user, ordered = False)

    save_order(order, request)
    items_in_order = get_items_in_order(order)

    item_categories = ItemCategory.get_all_item_categories().annotate(item_in_category_count=Count('item'))

    items = None
    item_cat_id = request.GET.get('category')
    if item_cat_id:
        items = Item.get_all_items_by_category_id(item_cat_id)
        item_count = items.count()
    else:
        items = Item.get_all_items()
        item_count = items.count()
    all_items_count = Item.objects.count()
    category = ItemCategory.objects.filter(id=item_cat_id)


    query = request.GET.get("barcode", None)
    if query is not None:
        items = (items.filter(barcode__startswith  = query) | items.filter(item_name__startswith  = query))|items.filter(item_name__icontains = query)
    item_search_form = SearchForm()

    print(order.default_amount_paid())
    context = {
        'order':order,
        'item_categories':item_categories,
        'items':items,
        'item_count':item_count,
        'all_items_count':all_items_count,
        'config':config,
        'items_in_order':items_in_order,
        'home':'Home',
        'header':'Order Number:',
        'payment_form':payment_form,
        'airtel_money_payment_form':airtel_money_payment_form,
        'mpamba_payment_form':mpamba_payment_form,
        'category':category,
        'unsettled_orders':unsettled_orders,
        'item_search_form':item_search_form,

    }
    return render(request, 'personal_order_list.html',context )

@login_required
def save_order(order, request):
    order.order_total_cost = order.order_total_due()
    order.active = True
    order.save()
    return order

# def save_ordered_items(items):
#     for item in items.item:
#         item.ordered = True
#         item.save
#     return item

@login_required
def save_bill(request):
    order_id =request.session['opened_order']
    order = Order.objects.get(id = order_id, user = request.user, ordered=False)
    # Order_qs = Order.objects.filter(user=request.user, active= True)
    # order = Order_qs[0]


    # order_items = OrderItem.objects.filter(user = request.user, ordered = False, customer = order.customer.id)
    
    # for order_item in order_items:
    #     order_item.ordered = True
    #     order_item.save()

    order.active = False
    save_order(order, request)
    return redirect('pos_dashboard')

@login_required
def save_bill_and_print_receipt(request):
    order_id =request.session['opened_order']
    order = Order.objects.get(id = order_id, user = request.user, ordered=False)
    order.active = False
    save_order(order, request)
    return redirect('pos_dashboard')


@login_required
def get_items_in_order(order):
    items_in_order = OrderItem.objects.filter(order_id = order.get_code(), ordered=False, customer=order.customer)
    # items_in_order = order.items.all
    return items_in_order


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_id =request.session['opened_order']
    # Order_qs = Order.objects.filter(user=request.user, ordered= False, active=True)
    Order_qs = Order.objects.filter(id = order_id)
    if Order_qs.exists():
        order = Order_qs[0]
        customer = order.customer
        order_id_in_ordered_items = order.get_code()
        order_item, created = OrderItem.objects.get_or_create(order_id = order_id_in_ordered_items, item=item, user = request.user, ordered = False, customer=customer)
        #check if the order item is in the order
        if order.items.filter(item__slug = item.slug).exists():
            item.quantity_at_hand -=1
            order_item.quantity +=1
            order_item.customer = order.customer
            order_item.save()
            item.save()
        else:
            order_item.quantity = 1
            order.items.add(order_item)
            order_item.customer = order.customer
            order_item.order_id = order.get_code()
            order_item.save()
            item.quantity_at_hand -=1
            item.save()
    else:
        messages.info(request, "Item not in order")
    return redirect('/pos/personal_order_list/'+ str(order_id))

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_id =request.session['opened_order']
    # Order_qs = Order.objects.filter(user=request.user, ordered= False, active=True)
    Order_qs = Order.objects.filter(id = order_id)

    if Order_qs.exists():
        order = Order_qs[0]
        order = Order_qs[0]
        customer = order.customer
        # order_id = order.order_id
        order_id_in_ordered_items = order.get_code()
        #check if the order item is in the order
        if order.items.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(order_id = order_id_in_ordered_items, item = item, user = request.user, ordered = False, customer=customer)[0]
            order_item.ordered = True
            order.items.remove(order_item)
            item.quantity_at_hand += order_item.quantity
            order_item.delete()
            item.save()
            # order_item.save()
        else:
        # add a message saying the user doesnt have an order
            messages.info(request, "This Item is not in Cart!")
            return redirect ('/pos/personal_order_list/'+ str(order.id))
    else:
        messages.info(request, "Item not in order")
    # return redirect('/pos/personal_order_list/'+ str(order.id))
    return redirect('/pos/personal_order_list/'+ str(order_id))

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_id =request.session['opened_order']
    # Order_qs = Order.objects.filter(user=request.user, ordered= False, active=True)
    Order_qs = Order.objects.filter(id = order_id)
    if Order_qs.exists():
        order = Order_qs[0]
        customer = order.customer
        #check if the order item is in the order
        if order.items.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user = request.user, ordered = False, customer=customer)[0]
            if order_item.quantity >1:
                order_item.quantity -=1
                item.quantity_at_hand +=1
                order_item.save()
                item.save()
            else:
                order_item.delete()
                item.save()
            return redirect('/pos/personal_order_list/'+ str(order.id))
        else:
            return redirect('/pos/personal_order_list/'+ str(order.id))
    else:
        messages.info(request, "Item not in order")
    # return redirect('/pos/personal_order_list/'+ str(order.id))
    return redirect('/pos/personal_order_list/'+ str(order_id))

@login_required
def receipt(request):
    now = datetime.now()

    order_id =request.session['opened_order']
    order = Order.objects.get(id = order_id, user = request.user, ordered=False)

    q = {" Order Number: " + str(order_id), " Customer:" + str(order.customer) + " Cel: " + str(order.customer.phone_number)}

    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(q, image_factory=factory, box_size=5)
    stream = BytesIO()
    img.save(stream)
    svg = stream.getvalue().decode()

    complete_order_only(order, request)
    del request.session['opened_order']
    context = {
        'config':config,
        'order':order,
        'svg':svg,
        'now':now,
    }
    return render(request, 'receipt.html', context)

@login_required
def load_orders(request):
    unpaid_orders = Order.objects.filter(ordered=False)
    context = {
        'unpaid_orders':unpaid_orders,
    }
    return render(request, 'unpaid_orders.html', context)

# WE don't need csrf_token when using Ajax
@csrf_exempt
def load_orders(request):
   
    # Getting all unpaid_orders from Order model based on ordered False/True
    unpaid_orders = Order.objects.filter(ordered=False)

    # Only Passing Customer Name order Total Cost  Only
    list_data = []

    for unpaid_order in unpaid_orders:
        data_small={"id":unpaid_order.id, "customer":unpaid_order.customer +" "+unpaid_order.order_total_cost}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@login_required
def incident_list(request):
    incidents = Order.objects.all().order_by("-opened_at")[:10]
    return render(request, "incident-list.html", locals())

# View for the modal
@login_required
def view_order_items(request, id):
    order = get_object_or_404(Order, id=id)
    context = {
        'order':order
    }
    return render(request, 'view_order_items.html', context)
