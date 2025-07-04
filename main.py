import products
import store

def start(store_instance):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            print("------")
            active_products = store_instance.get_all_products()
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. {product.show()}")
            print("------")

        elif choice == "2":
            total = store_instance.get_total_quantity()
            print(f"\nTotal of {total} items in store")

        elif choice == "3":
            active_products = store_instance.get_all_products()
            print("------")
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. {product.show()}")
            print("------")

            shopping_list = []
            while True:
                product_input = input("Which product # do you want?  ").strip()
                if product_input == "":
                    break

                if not product_input.isdigit():
                    print("Please enter a valid product number.")
                    continue

                prod_index = int(product_input) - 1
                if prod_index < 0 or prod_index >= len(active_products):
                    print("Invalid product number.")
                    continue

                quantity_input = input("What amount do you want? ").strip()
                if not quantity_input.isdigit() or int(quantity_input) <= 0:
                    print("Please enter a valid positive quantity.")
                    continue

                quantity = int(quantity_input)
                shopping_list.append((active_products[prod_index], quantity))
                print("Product added to list!")

            if shopping_list:
                try:
                    total_price = store_instance.order(shopping_list)
                    print(f"Order completed! Total price: ${total_price}")
                except Exception as e:
                    print(f"Error processing order: {e}")

        elif choice == "4":
            print("Thank you for visiting Best Buy! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.")

if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    start(best_buy)
