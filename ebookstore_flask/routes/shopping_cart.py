from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from ebookstore_flask.utils.session import check_session, load_sessions
from ebookstore_flask.utils.credit_card import bin_number_checker
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.credit_card import Credit_card
from ebookstore_flask.models.shoppingCart_item import ShoppingCart_item
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models import db

shopping_cart = Blueprint('shopping_cart', __name__)

@shopping_cart.route('/cart', methods=['GET', 'POST'])
def index():
   if not check_session(): return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   user = (
      Member.query                      # SELECT * FROM "Member"
      .filter(Member.Email == email)    # WHERE "Email" = email
      .first()
   )
   products = (
      Product.query                                                       # SELECT * FROM "Product"
      .join(Item_line, Item_line.PID == Product.PID)                      # JOIN "Item_line" ON "Item_line"."PID" = "Product"."PID"
      .join(ShoppingCart_item, ShoppingCart_item.SCID == Item_line.SCID)  # JOIN "ShoppingCart_item" ON "ShoppingCart_item"."CMID" = "Item_line"."SCID"
      .filter(ShoppingCart_item.CMID == user.MID)                         # WHERE "ShoppingCart_item"."CMID" = user.MID
      .all()
   )
   cards = (
      Credit_card.query.with_entities(Credit_card.Number) # SELECT "Credit_card"."Number" FROM "Credit_card"
      .join(Member, Member.MID == Credit_card.CMID)       # JOIN "Member" ON "Member"."MID" = "Credit_card"."CMID"
      .filter(Member.Email == email)                      # WHERE "Member"."Email" = <email>;
      .all()
   )
   credit_cards = [card[0] for card in cards]
   for i in range(len(credit_cards)):
      bin_info = bin_number_checker(credit_cards[i][:6])
      credit_cards[i] = '**** **** **** ' + credit_cards[i][-4:]
      credit_cards[i] = {
         'Number': credit_cards[i],
         'Brand': bin_info.get('Brand', 'Unknown'),
         'Issuer': bin_info.get('Issuer', 'Unknown')
      }
   # if request.method == 'POST':
   #    if 
   return render_template(
      'user/shopping_cart.html',
      role=role,
      products=products,
      credit_cards=credit_cards
   )

@shopping_cart.route('/check_bin', methods=['POST'])
def check_bin():
   number = request.json.get('number')
   if not number: return jsonify({'error': 'No number provided'}), 400
   result = bin_number_checker(number[:6])
   return jsonify(result)