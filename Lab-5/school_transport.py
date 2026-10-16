
"""Manage school transport riders, routes, rosters, and collected fees."""

import sqlite3


def create_database():
    """Create and return an in-memory database for transport riders."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE riders (
            id INTEGER PRIMARY KEY,
            student TEXT,
            route TEXT,
            stop TEXT,
            fee INTEGER
        )
        """
    )
    return connection


def enroll_rider(connection, student, route, stop, fee):
    """Enroll a rider using parameterized SQL."""
    connection.execute(
        """
        INSERT INTO riders (student, route, stop, fee)
        VALUES (?, ?, ?, ?)
        """,
        (student, route, stop, fee),
    )
    connection.commit()


def route_roster(connection, route):
    """Return the student names registered on a route."""
    cursor = connection.execute(
        "SELECT student FROM riders WHERE route = ?",
        (route,),
    )
    return [row[0] for row in cursor.fetchall()]


def export_roster(connection, path, route):
    """Write a route's student roster to a text file."""
    with open(path, "w", encoding="utf-8") as output_file:
        for name in route_roster(connection, route):
            output_file.write(f"{name}\n")


def dispatch_alert(route):
    """Display a dispatch message without invoking a shell."""
    print(f"Dispatching bus {route}")


def fee_collected(connection, route):
    """Return the total fees collected for a route."""
    result = connection.execute(
        "SELECT SUM(fee) FROM riders WHERE route = ?",
        (route,),
    ).fetchone()
    return result[0] or 0


def main():
    """Run the school transport demonstration."""
    connection = create_database()

    try:
        enroll_rider(connection, "Tara", "R1", "Lake Road", 1800)
        enroll_rider(connection, "Kabir", "R1", "Mill Street", 1800)
        enroll_rider(connection, "Zoya", "R2", "Fort Gate", 2100)

        if fee_collected(connection, "R1") != 3600:
            raise ValueError("R1 fee total is incorrect")

        export_roster(connection, "route_r1.txt", "R1")
        dispatch_alert("R1")

        print(route_roster(connection, "R2"))
    finally:
        connection.close()


if __name__ == "__main__":
    main()
