from exams.aug2021.project.bakery import Bakery


def test_code():
    bake = Bakery("Rose")
    bake.add_food("Bread", "br1", 1)
    bake.add_food("Bread", "br2", 2)
    bake.add_food("Cake", "ca1", 1.2)
    print(bake.add_food("Cake", "ca2", 2.4))
    # bake.add_food("no mather", "br2", 2)  # raise exception

    bake.add_drink("Tea", "te", 200, "JS")
    print(bake.add_drink("Water", "we", 500, "VODA"))

    bake.add_table("InsideTable", 1, 2)
    bake.add_table("InsideTable", 3, 6)
    bake.add_table("OutsideTable", 52, 4)
    print(bake.add_table("OutsideTable", 54, 8))
    # bake.add_table("no mather", 3, 6)  # raise exception

    print(bake.reserve_table(2))
    print(bake.reserve_table(8))
    print(bake.reserve_table(8))

    print(bake.order_food(2, "br2", "ca3", "ca1"))
    print(bake.order_food(1, "br2", "ca3", "ca1"))
    print(bake.order_food(1, "br2", "ca1"))

    print(bake.order_drink(2, "br2", "ca3", "ca1"))
    print(bake.order_drink(1, "te", "we", "ca1"))
    print(bake.order_drink(1, "te", "we"))

    print(bake.order_drink(54, "te", "we"))

    print(bake.get_free_tables_info())
    print(bake.leave_table(1))
    print(bake.leave_table(2))
    print(bake.leave_table(54))

    print(bake.get_free_tables_info())
    print(bake.get_total_income())


if __name__ == '__main__':
    test_code()

# Added ca2 (Cake) to the food menu
# Added we (VODA) to the drink menu
# Added table number 54 in the bakery
# Table 1 has been reserved for 2 people
# Table 54 has been reserved for 8 people
# No available table for 8 people
# Could not find table 2
# Table 1 ordered:
#  - br2: 200.00g - 2.00lv
#  - ca1: 245.00g - 1.20lv
# Rose does not have in the menu:
# ca3
#
# Table 1 ordered:
#  - br2: 200.00g - 2.00lv
#  - ca1: 245.00g - 1.20lv
#
# Could not find table 2
# Table 1 ordered:
#  - te JS - 200.00ml - 2.50lv
#  - we VODA - 500.00ml - 1.50lv
# Rose does not have in the menu:
# ca1
#
# Table 1 ordered:
#  - te JS - 200.00ml - 2.50lv
#  - we VODA - 500.00ml - 1.50lv
#
# Table 54 ordered:
#  - te JS - 200.00ml - 2.50lv
#  - we VODA - 500.00ml - 1.50lv
#
# Table: 3
# Type: InsideTable
# Capacity: 6
# Table: 52
# Type: OutsideTable
# Capacity: 4
#
# Table: 1
# Bill: 14.40
# None
# Table: 54
# Bill: 4.00
# Table: 1
# Type: InsideTable
# Capacity: 2
# Table: 3
# Type: InsideTable
# Capacity: 6
# Table: 52
# Type: OutsideTable
# Capacity: 4
# Table: 54
# Type: OutsideTable
# Capacity: 8
#
# Total income: 18.40lv
