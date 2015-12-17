# MuseumTracker
An attendance tracker for the Raupp Museum

This is a small app for logging the attendance of guests at the local histor museum I volunteer at. 
It was built to run on a Raspberry Pi with 7" touchscreen kit attached, to take in two different types of records.
Storage is here set to run in sqlite, but project will be set up in a mysql db running locally on the pi. 

The entire project is set to run locally, with later upgrates featuring "export database to csv".
Emailing csv, visual display to users, and analysis on guests and program success based on the entry fields.

Entry fields for both Walk ins and Group forms were requested by the museum, and are specific to this case.
Your mileage may vary. 

More documentation on the setup of the pi, tweaks, etc to come as the beta test product is installed.
A complete revamping of the HTML output through the templates is the next project, then a second App will be added 
to the framework to make calls on the data and actually output relevant graphs.

All specs on what kind of data is collected and how it's analyzed are provided by the museum.
