import labtest1

cvs_list = [
    {"date" : "13.01.2022", "expense_item" : "rice", "price" : "13.5"},
    {"date" : "15.01.2022", "expense_item" : "butter", "price" : "3.5"},
    {"date" : "17.01.2022", "expense_item" : "sugar", "price" : "2.8"},
    {"date" : "19.01.2022", "expense_item" : "apples", "price" : "4.7"},
    {"date" : "20.01.2022", "expense_item" : "oranges", "price" : "3"},
    {"date" : "22.01.2022", "expense_item" : "potatos", "price" : "2.5"},
    {"date" : "30.01.2022", "expense_item" : "rice", "price" : "12"}
]

def test_calc_average_expenses():
    result = []
    avg_expense = labtest1.calc_average_expenses(cvs_list)

    assert (avg_expense == (13.5 + 3.5 + 2.8 + 4.7 + 3 + 2.5 + 12)/ len(cvs_list))



def test_calc_total_expenses():
    #csv_list=labtest1.load_csv_database()
    total_exp = labtest1.calc_total_expenses()

def test_is_price_range_valid():



def test_get_items_by_price_range():
    csv_list=labtest1.load_csv_database()


def test_sort_by_items():
    csv_list=labtest1.load_csv_database()



