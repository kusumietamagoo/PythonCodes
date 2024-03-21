import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []
        
        # Labels and Entry widgets
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)
        
        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, sticky="w")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="w")
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone_number:
            contact = Contact(name, phone_number, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact.name} - {contact.phone_number}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts found.")

    def search_contact(self):
        keyword = self.name_entry.get()
        if keyword:
            results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
            if results:
                contact_list = "\n".join([f"{contact.name} - {contact.phone_number}" for contact in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a name to search.")

def main():
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
