"""
Main application for managing catalogues.
Handles user interaction and menu-based operation 
"""

from dto.catalogue_dto import catalogue
from util.validators import *
from service.catalogue_service import catalogueService

def menu() -> None:
    """
    Display the main menu and handle user input for catalogue operations.

    :return: None
    """

    service =catalogueService()
    

    while True:
        print("\n--- CATALOGUE MANAGEMENT SYSTEM ---")
        print("1) CREATE CATALOGUE")
        print("2) VIEW ALL CATALOGUE")
        print("3) VIEW CATALOGUE BY ID")
        print("4) DELETE CATALOGUE BY ID")
        print("5) UPDATE CATALOGUE BY ID")
        print("6) EXIT")

        choice = input("ENTER YOUR CHOICE: ").strip()

        if choice == "1":
            name = validate_alpha_string("Enter catalogue name: ")
            desc = validate_alpha_string("Enter description: ").strip()
            start = validate_date("Effective from (YYYY-MM-DD): ")
            end = validate_date("Effective to (YYYY-MM-DD): ")
            status = validate_status("Status (active/inactive/upcoming/expired): ")

            cat = catalogue(name, desc, start, end, status)
            if service.create_catalogue(cat):
                print("Catalogue created successfully.")
            else:
                print("Error occurred while creating catalogue.")

        elif choice == "2":
            catalogues = service.get_all_catalogues()
            if not catalogues:
                print("No catalogues found.")
            else:
                for cat in catalogues:
                    print(cat)

        elif choice == "3":
            cid = validate_int("Enter catalogue ID: ")
            cat = service.get_catalogue_by_id(cid)
            if cat:
                print(cat)
            else:
                print("Catalogue not found.")

        elif choice == "4":
            cid = validate_int("Enter catalogue ID to delete: ")
            if service.delete_catalogue_by_id(cid):
                print("Catalogue deleted successfully.")
            else:
                print("Failed to delete catalogue. Check if ID exists.")

        elif choice == "5":
            cid = validate_int("Enter catalogue ID to update: ")
            name = validate_alpha_string("New name: ", "Catalogue Name")
            desc = input("New description: ").strip()
            start = validate_date("New effective from date (YYYY-MM-DD): ")
            end = validate_date("New effective to date (YYYY-MM-DD): ")
            status = validate_status("Status (active/inactive/upcoming/expired): ")

            cat_update = catalogue(name, desc, start, end, status)
            if service.update_catalogue_by_id(cid, cat_update):
                print("Catalogue updated successfully.")
            else:
                print("Failed to update catalogue. Check if ID exists.")

        elif choice == "6":
            print("Exiting Catalogue Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()


    



    






