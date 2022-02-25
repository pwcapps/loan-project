# LoanStreet Backend Coding Quiz
## submission by Patrick Capps
### Basic Loan Server
I've built the server portion of the quiz using Node.js with the Express framework and using PostgreSQL to store loan data.

In order to run the application, Node.js and PostgreSQL should be installed and your database should include a table called loans with the following columns and associated data types. Unfortunately I did not get around to deploying this to a cloud provider.
- loan_id SERIAL
- amount NUMERIC(1000, 2)
- interest REAL
- length SHORTINT
- payment_amount NUMERIC(1000, 2)