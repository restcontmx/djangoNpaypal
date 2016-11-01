from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "restcontmx@gmail.com",
        "amount": "10.00",
        "item_name": "Carrera 5k",
        "invoice": "1ajksdnfqwemill997asbv",
        "notify_url": "https://paypal-test-gunt2raro.c9users.io/" + reverse('paypal-ipn'),
        "return_url": "https://paypal-test-gunt2raro.c9users.io/success-payment/",
        "cancel_return": "https://paypal-test-gunt2raro.c9users.io/cancel-payment/",
        "custom": "Payment for : Carrera 5k!",  # Custom command to correlate to some function later (optional),
        "currency_code" : "MXN"
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = { "form": form }
    return render( request, "paypal_test.html", context )

def show_me_the_money(sender, **kwargs):
    print( "Que pedou?" )
    ipn_obj = sender
    print( ipn_obj )
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the business field request. (The user could tamper
        # with those fields on payment form before send it to PayPal)
        if ipn_obj.receiver_email != "restcontmx@gmail.com":
            # Not a valid payment
            print( "Fucklt you!" )
            return

        # ALSO: for the same reason, you need to check the amount
        # received etc. are all what you expect.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Payment for : Carrera 5k!":
            #Users.objects.update(paid=True)
            print( "upgrade all users!" )
    else:
        print( "Payment not completed" )

valid_ipn_received.connect(show_me_the_money)