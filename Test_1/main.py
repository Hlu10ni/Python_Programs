# events = ["Coding Marathon", "Tech Talk", "Cultural Night", "Sports Day"]
# registrations = {"John Doe": ["Coding Marathon", "Tech Talk"], "Jane Smith": ["Cultural Night", "Sports Day"]}
#
# # Ask for the name
# userName = input("Enter your name: ")
# # Initialize userEvents list to populate it later
# userEvents = []
#
# # to keep it running until they are done choosing the events
# while True:
#     count = 1
#     print("Choose an event from the list below or 0 to stop choosing:")
#     # give the user the options and make it simple to choose by using numbers
#     for event in events:
#         print(f"{count}. {event}")
#         count+=1
#     # Show them the options
#     chosenEvent = input("Choose from 1-4 or 0 to stop: ")
#
#     # Conditional statements in a string or int is also fine
#     # Break if 0 or any type that will break the loop is fine
#     # As long as the user is able to choose multiple events
#     # Append or add the event to a list, ideally append is correct,
#     # But if they use other ways to add the items to the list is fine
#     if chosenEvent == "0":
#         break
#     elif chosenEvent == "1":
#         userEvents.append(events[0])
#     elif chosenEvent == "2":
#         userEvents.append(events[1])
#     elif chosenEvent == "3":
#         userEvents.append(events[2])
#     elif chosenEvent == "4":
#         userEvents.append(events[3])
#     else:
#         print(f"Invalid event")
#
# # Check if the user is already registered, if so update their events
# # Make sure there are no duplicates.
# if registrations.get(userName) == None:
#     # Update the registrations dictionary
#     registrations[userName] = userEvents
# else:
#     eventsChosenBefore = registrations.get(userEvents)  # This will return the existing value
#     # combine the userEvents with eventsChosenBefore
#     userEvents.extend(eventsChosenBefore)  # or newEventList = userEvent + eventsChosenBefore
#     # Create newUserEvent which will have no duplicates
#     newUserEvent = []
#     # Remove duplicate by iterating through all events
#     for event in userEvents:
#         if event in newUserEvent:
#             continue
#         else:
#             newUserEvent.append(event)
#
#     # Update the registrations dictionary
#     registrations[userName] = newUserEvent
#
# # Print the final updated registrations dictionary
# print(registrations)









