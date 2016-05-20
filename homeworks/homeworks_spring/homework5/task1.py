import sqlite3


def unpaid(user_id):
    # import sqlite3  - if it is necessary within function
    with sqlite3.connect("data.sqlite") as con:
        cur = con.cursor()
        data = cur.execute("select users.name, orders.id, sum(price) from users "
                           "inner join orders on user_id = users.id "
                           "inner join GoodsInOrders on order_id = orders.id "
                           "inner join goods on goods.id = GoodsInOrders.good_id "
                           "where paid = 0 and users.id = ? "
                           "group by orders.id", [user_id]).fetchall()
    return data
