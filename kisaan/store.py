from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass
class Farmer:
    id: int
    name: str
    village: str


@dataclass
class ServiceEntry:
    id: int
    farmer_id: int
    service_type: str
    unit_type: str
    quantity: float
    rate: float
    total: float
    entry_date: str


@dataclass
class Payment:
    id: int
    farmer_id: int
    amount: float
    method: str
    payment_date: str


class KisaanStore:
    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path

    def initialize(self) -> None:
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        with self.connection() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS farmers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    village TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS service_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    farmer_id INTEGER NOT NULL,
                    service_type TEXT NOT NULL,
                    unit_type TEXT NOT NULL,
                    quantity REAL NOT NULL,
                    rate REAL NOT NULL,
                    total REAL NOT NULL,
                    entry_date TEXT NOT NULL,
                    FOREIGN KEY (farmer_id) REFERENCES farmers (id)
                );

                CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    farmer_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    method TEXT NOT NULL,
                    payment_date TEXT NOT NULL,
                    FOREIGN KEY (farmer_id) REFERENCES farmers (id)
                );
                """
            )

            farmer_count = connection.execute("SELECT COUNT(*) FROM farmers").fetchone()[0]
            if farmer_count == 0:
                self.seed_data(connection)

    def seed_data(self, connection: sqlite3.Connection) -> None:
        farmers = [
            ("Ramesh", "Narsampet"),
            ("Laxmi", "Parkal"),
            ("Mahesh", "Atmakur"),
        ]
        connection.executemany(
            "INSERT INTO farmers (name, village) VALUES (?, ?)",
            farmers,
        )

        entries = [
            (1, "Ploughing", "acre", 4, 1500, 6000, "2026-03-22"),
            (2, "Harvester", "hour", 3, 2500, 7500, "2026-03-24"),
            (1, "Transport", "trip", 2, 1200, 2400, "2026-03-26"),
        ]
        connection.executemany(
            """
            INSERT INTO service_entries (
                farmer_id, service_type, unit_type, quantity, rate, total, entry_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            entries,
        )

        payments = [
            (1, 2000, "Cash", "2026-03-27"),
            (3, 1500, "UPI", "2026-03-25"),
        ]
        connection.executemany(
            "INSERT INTO payments (farmer_id, amount, method, payment_date) VALUES (?, ?, ?, ?)",
            payments,
        )

    def connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def get_farmers(self) -> list[Farmer]:
        with self.connection() as connection:
            rows = connection.execute(
                "SELECT id, name, village FROM farmers ORDER BY name"
            ).fetchall()
        return [Farmer(id=row["id"], name=row["name"], village=row["village"]) for row in rows]

    def get_entries(self) -> list[ServiceEntry]:
        with self.connection() as connection:
            rows = connection.execute(
                """
                SELECT id, farmer_id, service_type, unit_type, quantity, rate, total, entry_date
                FROM service_entries
                ORDER BY entry_date, id
                """
            ).fetchall()
        return [
            ServiceEntry(
                id=row["id"],
                farmer_id=row["farmer_id"],
                service_type=row["service_type"],
                unit_type=row["unit_type"],
                quantity=row["quantity"],
                rate=row["rate"],
                total=row["total"],
                entry_date=row["entry_date"],
            )
            for row in rows
        ]

    def get_payments(self) -> list[Payment]:
        with self.connection() as connection:
            rows = connection.execute(
                """
                SELECT id, farmer_id, amount, method, payment_date
                FROM payments
                ORDER BY payment_date, id
                """
            ).fetchall()
        return [
            Payment(
                id=row["id"],
                farmer_id=row["farmer_id"],
                amount=row["amount"],
                method=row["method"],
                payment_date=row["payment_date"],
            )
            for row in rows
        ]

    def add_farmer(self, name: str, village: str) -> None:
        with self.connection() as connection:
            connection.execute(
                "INSERT INTO farmers (name, village) VALUES (?, ?)",
                (name, village),
            )

    def update_farmer(self, farmer_id: int, name: str, village: str) -> None:
        with self.connection() as connection:
            connection.execute(
                "UPDATE farmers SET name = ?, village = ? WHERE id = ?",
                (name, village, farmer_id),
            )

    def add_entry(
        self,
        farmer_id: int,
        service_type: str,
        unit_type: str,
        quantity: float,
        rate: float,
        entry_date: str,
    ) -> None:
        total = quantity * rate
        with self.connection() as connection:
            connection.execute(
                """
                INSERT INTO service_entries (
                    farmer_id, service_type, unit_type, quantity, rate, total, entry_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (farmer_id, service_type, unit_type, quantity, rate, total, entry_date),
            )

    def add_payment(
        self,
        farmer_id: int,
        amount: float,
        method: str,
        payment_date: str,
    ) -> None:
        with self.connection() as connection:
            connection.execute(
                "INSERT INTO payments (farmer_id, amount, method, payment_date) VALUES (?, ?, ?, ?)",
                (farmer_id, amount, method, payment_date),
            )

    def farmer_totals(
        self,
        farmer_id: int,
        entries: list[ServiceEntry],
        payments: list[Payment],
    ) -> dict[str, float]:
        service_total = sum(entry.total for entry in entries if entry.farmer_id == farmer_id)
        payment_total = sum(payment.amount for payment in payments if payment.farmer_id == farmer_id)
        return {
            "service_total": service_total,
            "payment_total": payment_total,
            "outstanding": service_total - payment_total,
        }

    def build_dashboard(self) -> dict[str, object]:
        farmers = self.get_farmers()
        entries = self.get_entries()
        payments = self.get_payments()

        farmer_cards = []
        for farmer in farmers:
            totals = self.farmer_totals(farmer.id, entries, payments)
            recent_entries = [entry for entry in entries if entry.farmer_id == farmer.id][-3:]
            recent_entries.reverse()
            farmer_cards.append(
                {
                    "farmer": farmer,
                    "totals": totals,
                    "recent_entries": recent_entries,
                    "status": self.payment_status(totals),
                }
            )

        farmer_summary = sorted(
            farmer_cards,
            key=lambda item: item["totals"]["outstanding"],
            reverse=True,
        )

        activity = [
            {
                "type": "Service",
                "farmer_name": self.farmer_name(entry.farmer_id, farmers),
                "label": f"{entry.service_type} - {entry.quantity:g} {entry.unit_type}",
                "amount": entry.total,
                "activity_date": entry.entry_date,
            }
            for entry in entries
        ] + [
            {
                "type": "Payment",
                "farmer_name": self.farmer_name(payment.farmer_id, farmers),
                "label": f"{payment.method} settlement",
                "amount": payment.amount,
                "activity_date": payment.payment_date,
            }
            for payment in payments
        ]

        activity.sort(key=lambda item: item["activity_date"], reverse=True)

        total_service_value = sum(entry.total for entry in entries)
        total_paid_value = sum(payment.amount for payment in payments)

        return {
            "farmers": farmers,
            "farmer_cards": farmer_cards,
            "farmer_summary": farmer_summary,
            "activity": activity[:6],
            "totals": {
                "service_value": total_service_value,
                "paid_value": total_paid_value,
                "outstanding": total_service_value - total_paid_value,
            },
            "today": date.today().isoformat(),
        }

    def payment_status(self, totals: dict[str, float]) -> str:
        if totals["outstanding"] <= 0:
            return "Settled"
        if totals["payment_total"] > 0:
            return "Partially Paid"
        return "Pending"

    def farmer_name(self, farmer_id: int, farmers: list[Farmer]) -> str:
        farmer = next(farmer for farmer in farmers if farmer.id == farmer_id)
        return farmer.name


BASE_DIR = Path(__file__).resolve().parent.parent
store = KisaanStore(BASE_DIR / "data" / "kisaan.db")
