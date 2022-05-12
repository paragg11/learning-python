PRACTICING QUERIES

#### Insert the missing statement to get all the columns from the Customers table.

- SELECT * FROM Customers;

#### Write a statement that will select the City column from the Customers table.

- SELECT City FROM Customers;

#### Select all the different values from the Country column in the Customers table.

- SELECT DISTINCT Country FROM Customers;

#### Select all records where the City column has the value "Berlin".

- SELECT * FROM Customers WHERE City = 'Berlin';

#### Use the NOT keyword to select all records where City is NOT "Berlin".

- SELECT * FROM Customers WHERE NOT City = 'Berlin';

#### Select all records where the CustomerID column has the value 32.

- SELECT * FROM Customers WHERE CustomerID = 32; 

#### Select all records where the City column has the value 'Berlin' and the PostalCode column has the value 12209.

- SELECT * FROM Customers WHERE City = 'Berlin' AND PostalCode = 12209;

#### Select all records where the City column has the value 'Berlin' or 'London'.

- SELECT * FROM Customers WHERE City = 'Berlin' OR City = 'London';

#### Select all records from the Customers table, sort the result alphabetically by the column City.

- SELECT * FROM Customers ORDER BY City;

#### Select all records from the Customers table, sort the result reversed alphabetically by the column City.

- SELECT * FROM Customers ORDER BY City DESC;

#### Select all records from the Customers table, sort the result alphabetically, first by the column Country, then, by the column City.

- SELECT * FROM Customers ORDER BY Country, City;

#### Insert a new record in the Customers table.

- INSERT INTO Customers (CustomerName, Address, City, PostalCode, Country) VALUES ( 'Hekkan Burger', 'Gateveien 15', 'Sandnes', '4306', 'Norway');

#### Select all records from the Customers where the PostalCode column is empty.

- SELECT * FROM Customers WHERE PostalCode IS NULL;

#### Select all records from the Customers where the PostalCode column is NOT empty.

- SELECT * FROM Customers WHERE PostalCode IS NULL;

#### Update the City column of all records in the Customers table.

- UPDATE Customers SET City = 'Oslo';

#### Set the value of the City columns to 'Oslo', but only the ones where the Country column has the value "Norway".

- UPDATE Customers SET City = 'Oslo' WHERE Country = 'Norway';

#### Update the City value and the Country value.

- UPDATE Customers SET City = 'Oslo', Country = 'Norway' WHERE CustomerID = 32;