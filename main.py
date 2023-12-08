import json


def parsing():
    result = {}

    with open("TraderPlusPriceConfig.json", "r", encoding='utf-8') as file:
        json_read_data = json.load(file)

    for TraderCategories in json_read_data["TraderCategories"]:
        for Products in TraderCategories["Products"]:
            product = Products.split(",")

            if product[0] in result:
                result[product[0]].append(
                    {
                        "CategoryName": TraderCategories["CategoryName"],
                        "PurchasePrice": product[-2],
                        "SellingPrice": product[-1]
                    }
                )

            else:
                result[product[0]] = [
                    {
                        "CategoryName": TraderCategories["CategoryName"],
                        "PurchasePrice": product[-2],
                        "SellingPrice": product[-1]
                    }
                ]

    with open("result.json", "w", encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def return_data():
    with open("result.json", "r", encoding='utf-8') as file:
        json_return_data = json.load(file)

    with open("TraderPlusPriceConfig.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)

    for TraderCategories1 in json_data["TraderCategories"]:
        for products1 in TraderCategories1["Products"]:
            prod = products1.split(",")
            if prod[0] in json_return_data:
                for category in json_return_data[prod[0]]:
                    if TraderCategories1["CategoryName"] == category['CategoryName']:
                        prod[-1] = category["SellingPrice"]
                        prod[-2] = category["PurchasePrice"]
                        TraderCategories1["Products"][TraderCategories1["Products"].index(products1)] = ",".join(prod)

    with open("TotalResult.json", "w", encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # parsing()
    # input("Нажмите на любую клавишу для продолжения!")
    return_data()
