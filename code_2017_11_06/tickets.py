# -*- coding: utf-8 -*-
"""
Task from
http://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
"""


def sell_tickets_to_all_customers(*, people: list) -> str:
    """
    Can you sell a ticket to each person and give the change
    if you initially has no money and sells the tickets strictly
    in the order people follow in the line?
    Each customer bay only one ticket.
    Args:
        people: list of int - dollar banknotes (25, 50, 100)
    Return:
        "YES" if can sell to all customer else "NO"
    for example:
        can_sell_tickets_to_all_customers([25, 25, 50]) -> YES
        can_sell_tickets_to_all_customers([25, 50, 50]) -> NO
    """
    existing_banknotes_in_hand = []
    for person_bill in people:
        money = 25
        # no need to spend
        if person_bill == money:
            # you sell ticket
            existing_banknotes_in_hand.append(person_bill)
        else:
            # You have to spend the rest
            existing_banknotes_in_hand.sort(reverse=True)
            for iterate, bill in enumerate(existing_banknotes_in_hand):
                if bill <= person_bill - money:
                    money += bill
                    # spend the rest
                    existing_banknotes_in_hand[iterate] = 0
            if person_bill == money:
                # you sell ticket
                existing_banknotes_in_hand.append(person_bill)
            else:
                return "NO"
    return "YES"
