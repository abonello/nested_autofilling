# Experiment - Nested Autofilling
## Filling in second select element depending on selection in first select element
Note that the **Services** select element is not populated before you make a selection in the **Department** selector.  

This method uses jQuery to make an ajax call to Flask to get the relevant data and populate the servises selector once an option for the departments has been made by the user. We cannot rely on jinja to do this as jinja templating executes at the start of the page. At that time the user has not made any selection. The user has not even seen the page.