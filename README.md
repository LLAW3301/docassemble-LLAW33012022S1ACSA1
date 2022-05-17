# docassemble-LLAW33012022S1ACSA1
A docassemble extension.


---
objects:
  - event: Appointment
  - user: Individual
  - attendees: Individual
---
mandatory: true 
question: |
  Enter your AnglicareSA login.
fields:
  - Name: user.name.text
  - E-mail: user.email
    datatype: email
---
mandatory: true
question: |
  Would you like to invite any clients?
yesno: attendees.there_are_any
---
mandatory: true
question: |
  Enter client information.
fields:
  - Case Number: attendees.case
  - Name: attendees.name.text
  - E-mail: attendees.email
    datatype: email
---
mandatory: true
question: |
  Are there any more clients besides ${ attendees.name.text }?
yesno: attendees.there_is_another
---
mandatory: true
question: |
  Enter apppointment information.
fields:
  - Title: event.title
  - Location: event.location
    required: False
  - Start date: event.begin_date
    datatype: date
  - Start time: event.begin_time
    datatype: time
  - End date: event.end_date
    datatype: date
  - End time: event.end_time
    datatype: time
  - Description: event.description
    input type: area
    required: False
---
