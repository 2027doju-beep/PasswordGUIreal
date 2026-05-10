import sqlite3
import Model

def admin_login(email, password):
    """Returns the user's role if login succeeds, otherwise None."""
    role = Model.lookupRole(email, password)
    return role

def change_user_role(admin_email, admin_password):
    """Lets a logged-in admin change another user's role."""
    role = admin_login(admin_email, admin_password)

    if role != "admin":
        print("Access denied. You must be an admin to change roles.")
        return

    print("\n--- Role Manager ---")
    target_email = input("Enter the email of the user to update: ").strip()
    print("Available roles: admin, user, employ")
    new_role = input("Enter new role: ").strip().lower()

    success = Model.updateRole(target_email, new_role)
    if success:
        print(f"✓ Role updated successfully.")
    else:
        print(f"✗ Update failed. Check the email and role.")

# --- Main ---
print("=== Admin Portal ===")
email = input("Your email: ").strip()
password = input("Your password: ").strip()

change_user_role(email, password)