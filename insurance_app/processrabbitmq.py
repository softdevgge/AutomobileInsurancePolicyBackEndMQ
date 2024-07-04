from .models import User, Quote
import random
import hashlib
import json
from django.shortcuts import get_object_or_404, render
import random
import time

def calcule_quote(ch, method, properties, body):    
    jsonQuote= json.loads(body)  
    
    user_data = jsonQuote["quote_body"]["user"]
    user_p = get_object_or_404(User, username=user_data)   

    metadata_text_p = json.dumps(jsonQuote["quote_body"]["quote_data"])
    quote_id_p = json.dumps(jsonQuote["quote_id"])
    quote_type_p = 1 #means car
    quote_amount_p =  random.uniform(10.01, 50.05)
    time.sleep(random.randrange(5, 15));
    
    
    new_quote = Quote.objects.create(
        user= user_p,
        quote_code = quote_id_p,
        metadata_text = metadata_text_p,
        quote_type = quote_type_p       , 
        quote_amount =  quote_amount_p
    )    
    
    

