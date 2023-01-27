# Gatornetics_backend

This is the backend design / internal system / persistent state of the Gatornetics platform. Inside temp (OLD), you'll find a number of files that correspond to data collection, data transfer, and data manipulation. Aside from that, we have two main files labeled 'gatadata' and 'connection' where we pre-process our data before writing SQL quieries to upload data to Planetscale. As you can see from the csv files, we have generated temporary solutions to avoid timeout errors when working with either the MySQL connector or CFBD API. 
