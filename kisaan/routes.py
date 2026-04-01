from __future__ import annotations

from flask import Blueprint, flash, redirect, render_template, request, url_for

from .store import store


main = Blueprint("main", __name__)


def parse_float(value: str) -> float:
    return float(value.strip())


def parse_text(value: str) -> str:
    return " ".join(value.strip().split())


@main.route("/")
def dashboard():
    return render_template("dashboard.html", data=store.build_dashboard())


@main.route("/farmers", methods=["POST"])
def add_farmer():
    name = parse_text(request.form["name"])
    village = parse_text(request.form["village"])
    if not name or not village:
        flash("Farmer name and village are required.")
        return redirect(url_for("main.dashboard", _anchor="farmers"))

    store.add_farmer(name=name, village=village)
    flash("Farmer added successfully.")
    return redirect(url_for("main.dashboard", _anchor="farmers"))


@main.route("/farmers/<int:farmer_id>", methods=["POST"])
def update_farmer(farmer_id: int):
    name = parse_text(request.form["name"])
    village = parse_text(request.form["village"])
    if not name or not village:
        flash("Farmer name and village cannot be empty.")
        return redirect(url_for("main.dashboard", _anchor="farmers"))

    store.update_farmer(farmer_id=farmer_id, name=name, village=village)
    flash("Farmer details updated.")
    return redirect(url_for("main.dashboard", _anchor="farmers"))


@main.route("/entries", methods=["POST"])
def add_entry():
    store.add_entry(
        farmer_id=int(request.form["farmer_id"]),
        service_type=request.form["service_type"],
        unit_type=request.form["unit_type"],
        quantity=parse_float(request.form["quantity"]),
        rate=parse_float(request.form["rate"]),
        entry_date=request.form["entry_date"],
    )
    flash("Service entry added to the ledger.")
    return redirect(url_for("main.dashboard", _anchor="entry"))


@main.route("/payments", methods=["POST"])
def add_payment():
    store.add_payment(
        farmer_id=int(request.form["farmer_id"]),
        amount=parse_float(request.form["amount"]),
        method=request.form["method"],
        payment_date=request.form["payment_date"],
    )
    flash("Payment recorded successfully.")
    return redirect(url_for("main.dashboard", _anchor="payments"))
