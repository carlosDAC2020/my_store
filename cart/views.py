from django.shortcuts import render, redirect

from .models import Invoice, Sale, timezone
from home.models  import Product


def my_cart(request):
    # traemos la ultima factura regiatrada 
    invoice_most_recently = Invoice.objects.filter(id_client=request.user).order_by("-date_invoice")[:5]
    invoices=[inv for inv in invoice_most_recently if inv.status_payment==True]
    # evaluamos si la ultima factura no se ha pagado
    if len(invoice_most_recently)>0 and invoice_most_recently[0].status_payment==False :

        sales_recently = Sale.objects.filter(id_invoice=invoice_most_recently[0].pk)
        
        return render(request,"cart.html",{
        "sales_recently":sales_recently,
        "invoice_most_recently":invoices
        })
    else:
        print(invoice_most_recently)
        mensaje=" Empty Cart "
        return render(request,"cart.html",{
        "mensaje":mensaje,
        "invoice_most_recently":invoices
    })




def add_sales(request,product_id):
    # traemos la ultima factura regiatrada 
    invoice_most_recently = Invoice.objects.filter(id_client=request.user.pk).order_by("-date_invoice")[:1]
    #invoice_most_recently = Invoice.objects.order_by("-date_invoice")[:1]
    # seleccionamos el producto a comprar
    product = Product.objects.get(pk=product_id)

    # en caso de que la ultima factura se haya registrado en los ultimos 30 minutos y su estado de pogo sea falso
    # se añadira la venta correspondiente a dicha factura 
    if len(invoice_most_recently)>0 and invoice_most_recently[0].invoice_most_recently():
        # craemos la venta y la asociamos  con la factura creada anteriormente 
        new_sale = Sale.objects.create(id_invoice=invoice_most_recently[0], id_product=product)
        new_sale.save()
    
    else:
        # creamos la factura
        new_invoice = Invoice.objects.create(date_invoice=timezone.now(), id_client=request.user)
        # guardamos la factura
        new_invoice.save()
        # añadimos la venta a una nueva factura
        new_sale = Sale.objects.create(id_invoice=new_invoice, id_product=product)
        new_sale.save()
    
    return redirect("sales:home")


def delete_sales(request, id_sale):
    sale=Sale.objects.get(pk=id_sale)
    if len(Sale.objects.filter(id_invoice=sale.id_invoice))>0:
        sale.delete()
        if len(Sale.objects.filter(id_invoice=sale.id_invoice))==0:
            inv=Invoice.objects.get(pk=sale.id_invoice.pk)
            inv.delete()
    return redirect("sales:shopping_cart")


