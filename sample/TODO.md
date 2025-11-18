# TODO: Implement Table to Show All Inserted Values

- [x] Add a new view function in views.py to fetch and display all contactMessage objects
- [x] Create a new template messages.html with a table showing all messages, including images if present
- [x] Add a new URL path in urls.py for the messages view
- [x] Optionally, add a navigation link in nav.html to access the messages page
- [x] Test the new messages page to ensure it displays all inserted values correctly
- [x] Verify image display if messages have images

# TODO: Add Editing and Deleting Views for contactMessages

- [x] Add edit_message view in views.py to handle editing a message
- [x] Add delete_message view in views.py to handle deleting a message
- [x] Create edit_message.html template for editing form
- [x] Create delete_message.html template for delete confirmation
- [x] Update messages.html to add Edit and Delete links/buttons for each message
- [x] Update urls.py to add edit/<int:id>/ and delete/<int:id>/ paths
- [x] Test editing and deleting functionality
