from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
engine = create_engine("sqlite:///flight_reservation.db")


#---------------- EXERCISE 1 ----------------
@app.route('/airports', methods=['GET'])
def airport_list():
    """
    Endpoint to retrieve a list of all airports available in the system.
    Returns a list of airports, each with its id, code, name, city, and country,
    sorted in ascending order by id.
    """
    # Define the SQL query to select airports information
    airport_query = text('''SELECT id, code, name, city, country FROM airports ORDER BY id ASC;''')
    try:
        # Attempt to connect to the database and execute the query
        with engine.connect() as connection:
            airports = connection.execute(airport_query)
            # Process the query results and format them into a list of dictionaries
            airport_data = [{
                "id": airport[0], 
                "code": airport[1], 
                "name": airport[2], 
                "city": airport[3], 
                "country": airport[4]
            } for airport in airports]
        # Return the list of airports as JSON
        return jsonify(airport_data)
    except SQLAlchemyError as e:
        # Handle any SQLAlchemy errors that occur during the database operation
        return jsonify({'error': 'Failed to retrieve airports due to a database error.'}), 500

#---------------- EXERCISE 2 ----------------
@app.route('/flights/search', methods=['GET'])
def search_flights():
    """
    Search for flights based on departure and arrival airport codes.
    Returns a list of matching flights including details like airline name, departure and arrival times, and price.
    """
    # Retrieve query parameters for departure and arrival airports
    departure_code = request.args.get('departure_airport')
    arrival_code = request.args.get('arrival_airport')

    # Validate input parameters to ensure they are provided
    if not departure_code or not arrival_code:
        return jsonify({"error": "Both departure and arrival airport codes are required."}), 400

    try:
        # Execute query to find matching flights
        with engine.connect() as connection:
            result = connection.execute(text(
                """
                SELECT flights.id, airlines.name AS airline_name, 
                (SELECT code FROM airports WHERE id = flights.departure_airport_id) AS departure_airport_code,
                (SELECT code FROM airports WHERE id = flights.arrival_airport_id) AS arrival_airport_code,
                flights.departure_datetime, flights.arrival_datetime, flights.price
                FROM flights
                JOIN airlines ON flights.airline_id = airlines.id
                JOIN airports AS departure_airports ON flights.departure_airport_id = departure_airports.id
                JOIN airports AS arrival_airports ON flights.arrival_airport_id = arrival_airports.id
                WHERE departure_airports.code = :departure_code AND arrival_airports.code = :arrival_code
                """),
                {'departure_code': departure_code, 'arrival_code': arrival_code}
            ).fetchall()

        # If no flights were found, return an appropriate message
        if not result:
            return jsonify({"error": "No flights found"}), 404
        
        # Prepare and return the flight data
        flights_data = [{
            "id": flight[0],
            "airline": flight[1],
            "departure_airport": flight[2],
            "arrival_airport": flight[3],
            "departure_datetime": flight[4],
            "arrival_datetime": flight[5],
            "price": flight[6]
        } for flight in result]

        return jsonify(flights_data)
    except Exception as e:
        return jsonify({"error": "An error occurred processing your request."}), 500

#---------------- EXERCISE 3 ----------------
@app.route('/flights/<flight_id>', methods=['GET'])
def get_flight(flight_id):
    """
    Retrieves detailed information about a specific flight by its ID.
    Returns airline, departure and arrival airport codes, departure and arrival times, and price.
    """
    # Validate flight_id to ensure it is a positive integer
    try:
        flight_id_int = int(flight_id)
        if flight_id_int <= 0:
            raise ValueError("Flight ID must be a positive integer.")
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400

    # Query to get the details of the specified flight
    flight_query = text("""
        SELECT 
            flights.id, 
            airlines.name AS airline_name, 
            departure_airports.code AS departure_airport_code, 
            arrival_airports.code AS arrival_airport_code, 
            flights.departure_datetime, 
            flights.arrival_datetime, 
            flights.price
        FROM flights
        JOIN airlines ON flights.airline_id = airlines.id
        JOIN airports departure_airports ON flights.departure_airport_id = departure_airports.id
        JOIN airports arrival_airports ON flights.arrival_airport_id = arrival_airports.id
        WHERE flights.id = :flight_id
    """)
    try:
        # Execute the query and fetch the flight details
        with engine.connect() as connection:
            flight = connection.execute(flight_query, {'flight_id': flight_id}).fetchone()
            if flight is None:
                return jsonify({'error': 'Flight not found'}), 404
            
            # Prepare and return the flight details
            flight_data = {
                "id": flight[0],
                "airline": flight[1],
                "departure": flight[2],
                "arrival": flight[3],
                "departure_datetime": flight[4],
                "arrival_datetime": flight[5],
                "price": flight[6]
            }
            
            return jsonify(flight_data) # this is used to return the details of the flight
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve flight details due to an unexpected error.'}), 500

#---------------- EXERCISE 4 ----------------
@app.route('/flights', methods=['POST'])
def flights():
    """
    Endpoint to add a new flight to the system. It requires airline_id, departure_airport_id,
    arrival_airport_id, departure_datetime, arrival_datetime, and price.
    Checks for the flight's existence before creation to avoid duplicates.
    Returns the ID of the newly created flight.
    """
    try:
        # Extracting flight details
        flight_details = request.get_json()
        airline_id = int(flight_details['airline_id'])
        departure_airport_id = int(flight_details['departure_airport_id'])
        arrival_airport_id = int(flight_details['arrival_airport_id'])
        departure_datetime = flight_details['departure_datetime']
        arrival_datetime = flight_details['arrival_datetime']
        price = float(flight_details['price'])
        
        # Construct query to check for existing flight
        flight_existence_query = text("""
            SELECT COUNT(*) FROM flights 
            WHERE airline_id=:airline_id AND departure_airport_id=:departure_airport_id AND arrival_airport_id=:arrival_airport_id AND departure_datetime=:departure_datetime AND arrival_datetime=:arrival_datetime AND price=:price
        """)
        # Execute query to check for existing flight
        with engine.connect() as connection:
            result = connection.execute(flight_existence_query, {"airline_id": airline_id, "departure_airport_id": departure_airport_id, "arrival_airport_id": arrival_airport_id, "departure_datetime": departure_datetime, "arrival_datetime": arrival_datetime, "price": price}).scalar()
            if result > 0:
                # Flight exists, return error
                return jsonify({'error': 'Flight already exists'}), 409
        
        # Query to insert a new flight
        flight_creation_query = text("""
            INSERT INTO flights(airline_id, departure_airport_id, arrival_airport_id, departure_datetime, arrival_datetime, price)
            VALUES (:airline_id, :departure_airport_id, :arrival_airport_id, :departure_datetime, :arrival_datetime, :price);
        """)
        
        # Execute flight insertion
        connection.execute(flight_creation_query, {"airline_id": airline_id, "departure_airport_id": departure_airport_id, "arrival_airport_id": arrival_airport_id, "departure_datetime": departure_datetime, "arrival_datetime": arrival_datetime, "price": price})
        
        # Retrieve the ID of the newly created flight
        flight_id = connection.execute("SELECT last_insert_rowid()").scalar()

        return jsonify({'id': flight_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#---------------- EXERCISE 5 ----------------
@app.route("/reservations", methods = ["POST"])
def reservations():
    """
    Create a reservation for a flight.
    Validates input data for required fields: flight_id, passenger_name, passenger_email, and num_tickets.
    Checks if the requested flight exists and if the number of tickets is a positive integer.
    Inserts the reservation into the database and returns the reservation details.
    """
    try: 
        data = request.get_json()
        # Validate the input data first
        required_fields = ["flight_id", "passenger_name", "passenger_email", "num_tickets"]
        if not all(field in data and data[field] for field in required_fields):
            return jsonify({"error": "Missing required field(s)."}), 400

        try:
            flight_id = int(data["flight_id"])
            num_tickets = int(data["num_tickets"])
            if num_tickets <= 0:
                raise ValueError("Number of tickets must be a positive integer.")
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        flight_id = int(data["flight_id"])
        passenger_name = data["passenger_name"]
        passenger_email = data["passenger_email"]
        num_tickets_str = data["num_tickets"]

        # Check if num_tickets is a digit and a positive integer
        if not isinstance(num_tickets_str, int) or num_tickets_str <= 0:
            return jsonify({"error": "Number of tickets must be a positive integer."}), 400
        num_tickets = int(num_tickets_str)

        # Check if the flight exists
        with engine.connect() as connection:
            query_flightprice = text ("""
                SELECT price from flights WHERE id = :id
                                """)            
            flight_price_result = connection.execute(query_flightprice, {"id": flight_id}).fetchone()

            if flight_price_result:
                flight_price = flight_price_result[0]
                total_price = flight_price * num_tickets

                # Insert the reservation
                insert_reservation_query = text("""
                    INSERT INTO reservations (flight_id, passenger_name, passenger_email, num_tickets, total_price)
                    VALUES (:flight_id, :passenger_name, :passenger_email, :num_tickets, :total_price)
                    """)
                
                connection.execute(insert_reservation_query, {
                    "flight_id": flight_id, 
                    "passenger_name": passenger_name,
                    "passenger_email": passenger_email,
                    "num_tickets": num_tickets,
                    "total_price": total_price
                })

                # Retrieve and return the newly created reservation's ID
                reservation_query = text("""
                    SELECT * from reservations WHERE flight_id=:flight_id AND passenger_name=:passenger_name AND passenger_email=:passenger_email;
                    """)
                reservation_result = connection.execute(reservation_query, {
                    "flight_id": flight_id,
                    "passenger_name": passenger_name,
                    "passenger_email": passenger_email
                }).fetchone()

                if reservation_result:
                    # Convert the result to a dict to jsonify it
                    reservation_details = {
                    "id": int(reservation_result[0]),  # Assuming 'id' is the first column
                    "flight_id": int(reservation_result[1]),  # And so on, for the rest of the columns
                    "passenger_name": reservation_result[2],
                    "passenger_email": reservation_result[3],
                    "num_tickets": reservation_result[4],
                    "total_price": reservation_result[5]
                    }     
                    return jsonify(reservation_details), 201
                else:
                    return jsonify({"Error": "Reservation not found after creating."}), 404
            else:
                return jsonify({"Error": "Flight ID not found or invalid."}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

#---------------- EXERCISE 6 ----------------
@app.route('/reservations/<reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    """
    Retrieve details for a specific reservation.
    
    This endpoint returns the details of a reservation identified by its unique ID.
    It includes the reservation ID, flight ID, passenger name, email, number of tickets,
    and total price.
    
    :param reservation_id: ID of the reservation to retrieve.
    :return: JSON object with reservation details or an error message.
    """
    # Validate reservation_id as an integer to prevent SQL injections and ensure it's a valid ID.
    try:
        valid_reservation_id = int(reservation_id)
    except ValueError:
        # If reservation_id is not an integer, return an error message.
        return jsonify({"error": "Invalid reservation ID format. ID must be an integer."}), 400
    
    query = text(
        "SELECT id, flight_id, passenger_name, passenger_email, num_tickets, total_price "
        "FROM reservations "
        "WHERE id = :reservation_id"
    )
    try:
        with engine.connect() as connection:
            result = connection.execute(query, {'reservation_id': valid_reservation_id}).fetchone()
            
            if result is None:
                return jsonify({"error": "Reservation not found"}), 404

            reservation_data = {
                "id": result[0],
                "flight_id": result[1],
                "passenger_name": result[2],
                "passenger_email": result[3],
                "num_tickets": result[4],
                "total_price": result[5]
            }

            return jsonify(reservation_data)
    except Exception as e:
        return jsonify({"error": "Failed to retrieve reservation due to an unexpected error."}), 500

#---------------- EXTRA FEATURE 1 ----------------
@app.route('/airports/rate', methods=['POST'])
def rate_airport():
    """
    Endpoint to rate an airport. Accepts an airport code, a rating between 1 and 5, and a comment.
    Validates the input and inserts the rating into the airport_ratings table if valid.
    Returns a success message or an error message if the operation fails.
    """
    try:
        airport_code = str(request.json.get('airport_code'))
        rating = request.json.get('rating')
        comment = request.json.get('comment')

        # Validate the received data
        if not all([airport_code, rating, comment]):  
            return jsonify({'error': 'Missing required fields. Ensure airport_code, rating, and comment are provided.'}), 400
        if not isinstance(rating, (int, float)) or not 1 <= rating <= 5:
            return jsonify({'error': 'Invalid rating. Must be a number between 1 and 5.'}), 400

        # Insert the rating into the airport_ratings table
        with engine.connect() as connection:
            # Check if airport exists
            airport_exists_query = text("SELECT id FROM airports WHERE code = :airport_code")
            airport_exists_result = connection.execute(airport_exists_query, {'airport_code': airport_code}).fetchone()

            if airport_exists_result is None:
                return jsonify({'error': 'Invalid airport_code or no such airport exists in database.'}), 404
            
            airport_id = airport_exists_result[0]
            # If the airport exists, proceed to insert the rating
            insert_rating_query = text("""
                INSERT INTO airport_ratings (airport_id, rating, comment)
                VALUES (:airport_id, :rating, :comment)
            """)
            connection.execute(insert_rating_query, {'airport_id': airport_id, 'rating': rating, 'comment': comment})

        return jsonify({'message': 'Successfully added rating'}), 201
    except Exception as e:
        # In a real application, log the error for debugging purposes
        return jsonify({'error': 'Failed to add rating due to an unexpected error.'}), 500

# To check this endpoint, you can use the following curl command:
# Success case:
"""   
curl -X POST http://localhost:8080/airports/rate \
-H 'Content-Type: application/json' \
-d '{"airport_code": "JFK", "rating": 5, "comment": "Excellent airport"}'
"""
# Error case:
"""   
curl -X POST http://localhost:8080/airports/rate \
-H 'Content-Type: application/json' \
-d '{"airport_code": "ABC", "rating": 5, "comment": "Excellent airport"}'
"""
# ATTENTION: If you are getting the error "{"error":"Failed to add rating due to an unexpected error."}", it's likely that the table 
# airport_ratings is missing in your database. To create this table, execute the following SQL command using sqlite3:
"""CREATE TABLE IF NOT EXISTS airport_ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    airport_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT NOT NULL,
    FOREIGN KEY (airport_id) REFERENCES airports(id)
);
"""
# This cannot be done directly from this code. Open your terminal, run `sqlite3 flight_reservation.db` to access your database, paste the SQL command above, and then type `.exit` to exit sqlite3.

#---------------- EXTRA FEATURE 2 ----------------
@app.route('/airports/ratings/<airport_code>', methods=['GET'])
def get_airport_ratings(airport_code):
    """
    Retrieves all ratings for a specific airport identified by its code.
    Each rating entry includes the rating value and the comment.

    Parameters:
    - airport_code (str): The airport code to search for ratings.

    Returns:
    - A JSON response containing a list of all ratings for the specified airport
      including the score and comment. If the airport does not exist or an error
      occurs, an error message is returned.
    """
    try:
        # Validate airport code format to prevent unnecessary database queries
        if not airport_code.isalpha() or len(airport_code) > 4:
            return jsonify({'error': 'Invalid airport code format.'}), 40
        


        with engine.connect() as connection:
            # Check if the airport exists to provide more specific feedback
            airport_exists_query = text("SELECT id FROM airports WHERE code = :airport_code")
            try:
                airport_exists_result = connection.execute(airport_exists_query, {'airport_code': airport_code.upper()}).fetchone()
            except SQLAlchemyError as e:
                app.logger.error(f"Database error occurred: {str(e)}")
                return jsonify({'error': 'Database error occurred.'}), 500

            if airport_exists_result is None:
                return jsonify({'error': 'No such airport exists in the database.'}), 404

            airport_id = airport_exists_result[0]

            # Retrieve all ratings for the airport
            get_ratings_query = text("SELECT rating, comment FROM airport_ratings WHERE airport_id = :airport_id")
            try:
                ratings_result = connection.execute(get_ratings_query, {'airport_id': airport_id}).fetchall()
            except SQLAlchemyError as e:
                app.logger.error(f"Database error occurred: {str(e)}")
                return jsonify({'error': 'Database error occurred.'}), 500

            ratings_list = [{'rating': rating, 'comment': comment} for rating, comment in ratings_result]
            return jsonify(ratings_list), 200

    except Exception as e:
        app.logger.error(f"Unexpected error occurred: {str(e)}")
        return jsonify({'error': 'Failed to retrieve ratings due to an unexpected error.'}), 500

if __name__ == "__main__":
    app.run(port=8080)